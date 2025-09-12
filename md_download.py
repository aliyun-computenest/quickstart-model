#!/usr/bin/env python3
"""
Markdown图片下载器 - 简化版
自动从当前目录下的所有MD文件中识别图片链接，下载到与MD文件相同的目录下并替换引用
保持原始文件内容不变
支持Python 3.10+
"""

import os
import re
import requests
import hashlib
import time
from pathlib import Path
from urllib.parse import urlparse, unquote
from typing import List, Tuple, Set, Dict
import logging
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('md_image_downloader.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class MarkdownImageDownloader:
    def __init__(self,
                 images_subdir: str = "images",
                 timeout: int = 30,
                 max_retries: int = 3,
                 delay_between_downloads: float = 1.0):
        """
        初始化下载器

        Args:
            images_subdir: 图片子目录名称（在每个MD文件目录下创建）
            timeout: 下载超时时间（秒）
            max_retries: 最大重试次数
            delay_between_downloads: 下载间隔时间（秒）
        """
        self.images_subdir = images_subdir
        self.timeout = timeout
        self.max_retries = max_retries
        self.delay_between_downloads = delay_between_downloads
        self.downloaded_urls: Dict[str, str] = {}  # url -> local_path 映射

        # 支持的图片格式
        self.image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.svg', '.ico', '.tiff', '.tif'}

        # 创建会话并配置重试策略
        self.session = requests.Session()
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

        # 更完整的请求头
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'image',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Site': 'cross-site',
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache'
        })

    def find_markdown_files(self, directory: str = ".") -> List[Path]:
        """查找目录下所有的Markdown文件"""
        md_files = []
        for file_path in Path(directory).rglob("*.md"):
            if file_path.is_file():
                md_files.append(file_path)

        logger.info(f"找到 {len(md_files)} 个Markdown文件")
        return md_files

    def extract_image_urls(self, content: str) -> List[Tuple[str, str, str]]:
        """
        从Markdown内容中提取图片URL

        Returns:
            List of (original_match, alt_text, url)
        """
        image_urls = []

        # Markdown格式: ![alt](url)
        markdown_pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
        for match in re.finditer(markdown_pattern, content):
            original_match = match.group(0)
            alt_text = match.group(1)
            url = match.group(2).strip()

            if self.is_remote_image_url(url):
                image_urls.append((original_match, alt_text, url))

        # HTML img标签格式
        html_patterns = [
            r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>',
            r'<img[^>]+src=([^\s>]+)[^>]*>'
        ]

        for pattern in html_patterns:
            for match in re.finditer(pattern, content, re.IGNORECASE):
                original_match = match.group(0)
                url = match.group(1).strip().strip('"\'')

                if self.is_remote_image_url(url):
                    # 尝试从img标签中提取alt属性
                    alt_match = re.search(r'alt=["\']([^"\']*)["\']', original_match, re.IGNORECASE)
                    alt_text = alt_match.group(1) if alt_match else ""

                    image_urls.append((original_match, alt_text, url))

        return image_urls

    def is_remote_image_url(self, url: str) -> bool:
        """判断是否为远程图片URL"""
        if not url:
            return False

        # 跳过本地路径
        if not url.startswith(('http://', 'https://')):
            return False

        # 检查是否为图片URL（通过扩展名或常见图片服务）
        parsed_url = urlparse(url.lower())
        path = parsed_url.path

        # 检查文件扩展名
        if any(path.endswith(ext) for ext in self.image_extensions):
            return True

        # 检查常见图片服务域名
        image_domains = [
            'imgur.com', 'i.imgur.com',
            'github.com', 'raw.githubusercontent.com',
            'cdn.', 'img.', 'image.',
            'unsplash.com', 'pixabay.com',
            'pexels.com', 'freepik.com',
            'githubusercontent.com'
        ]

        if any(domain in parsed_url.netloc for domain in image_domains):
            return True

        return False

    def get_file_extension_from_url(self, url: str, content_type: str = None) -> str:
        """从URL或Content-Type获取文件扩展名"""
        # 首先尝试从URL获取扩展名
        parsed_url = urlparse(url)
        path = unquote(parsed_url.path)
        _, ext = os.path.splitext(path)

        if ext.lower() in self.image_extensions:
            return ext.lower()

        # 如果URL没有扩展名，尝试从Content-Type推断
        if content_type:
            content_type = content_type.lower().split(';')[0].strip()
            ext_map = {
                'image/jpeg': '.jpg',
                'image/jpg': '.jpg',
                'image/png': '.png',
                'image/gif': '.gif',
                'image/bmp': '.bmp',
                'image/webp': '.webp',
                'image/svg+xml': '.svg',
                'image/x-icon': '.ico',
                'image/tiff': '.tiff',
                'image/tif': '.tif',
                'text/xml': '.svg',
                'application/xml': '.svg'
            }
            return ext_map.get(content_type, '.jpg')

        return '.jpg'  # 默认扩展名

    def generate_filename(self, url: str, alt_text: str = "", content_type: str = None) -> str:
        """生成本地文件名"""
        # 获取扩展名
        ext = self.get_file_extension_from_url(url, content_type)

        # 生成基于URL的哈希值作为文件名
        url_hash = hashlib.md5(url.encode('utf-8')).hexdigest()[:12]

        # 如果有alt文本，尝试使用它作为文件名的一部分
        if alt_text:
            # 清理alt文本，只保留字母数字和中文
            clean_alt = re.sub(r'[^\w\u4e00-\u9fff]', '_', alt_text)[:30]
            clean_alt = re.sub(r'_+', '_', clean_alt).strip('_')
            if clean_alt:
                filename = f"{clean_alt}_{url_hash}{ext}"
            else:
                filename = f"image_{url_hash}{ext}"
        else:
            filename = f"image_{url_hash}{ext}"

        return filename

    def get_image_dir_for_md(self, md_file_path: Path) -> Path:
        """获取MD文件对应的图片目录"""
        return md_file_path.parent / self.images_subdir

    def download_image(self, url: str, target_path: Path) -> bool:
        """下载图片到指定路径 - 保持原始内容不变"""
        # 检查是否已经下载过这个URL到相同位置
        if url in self.downloaded_urls and Path(self.downloaded_urls[url]).exists():
            logger.info(f"图片已下载过，跳过: {url}")
            return True

        # 创建目标目录
        target_path.parent.mkdir(parents=True, exist_ok=True)

        # 如果文件已存在，跳过下载
        if target_path.exists():
            logger.info(f"文件已存在，跳过下载: {target_path}")
            self.downloaded_urls[url] = str(target_path)
            return True

        for attempt in range(self.max_retries):
            try:
                logger.info(f"正在下载 ({attempt + 1}/{self.max_retries}): {url}")
                logger.info(f"保存到: {target_path}")

                # 使用会话发送请求
                response = self.session.get(
                    url,
                    timeout=self.timeout,
                    allow_redirects=True
                )
                response.raise_for_status()

                # 获取内容类型
                content_type = response.headers.get('content-type', '').lower().split(';')[0].strip()
                logger.debug(f"Content-Type: {content_type}")

                # 检查响应状态
                if response.status_code != 200:
                    logger.error(f"HTTP状态码错误: {response.status_code}")
                    continue

                # 检查内容长度
                content_length = len(response.content)
                if content_length == 0:
                    logger.error(f"下载内容为空: {url}")
                    continue

                # 根据实际内容类型调整文件扩展名
                correct_ext = self.get_file_extension_from_url(url, content_type)
                if not target_path.name.endswith(correct_ext):
                    # 更新目标路径的扩展名
                    new_target_path = target_path.with_suffix(correct_ext)
                    if new_target_path != target_path:
                        logger.info(f"根据Content-Type调整文件扩展名: {target_path.name} -> {new_target_path.name}")
                        target_path = new_target_path

                # 直接保存原始响应内容，不做任何处理
                with open(target_path, 'wb') as f:
                    f.write(response.content)

                # 验证保存的文件
                if target_path.exists() and target_path.stat().st_size > 0:
                    file_size = target_path.stat().st_size
                    logger.info(f"下载成功: {target_path.name} ({file_size} bytes)")

                    # 简单验证：检查文件大小是否合理
                    if file_size < 50:  # 小于50字节可能是错误页面
                        logger.warning(f"文件大小异常小，可能下载失败: {file_size} bytes")
                        # 读取文件内容检查是否是错误信息
                        try:
                            with open(target_path, 'r', encoding='utf-8', errors='ignore') as f:
                                content_preview = f.read(200)
                            if any(error_text in content_preview.lower() for error_text in
                                   ['404', 'not found', 'error', 'forbidden', 'access denied']):
                                logger.error(f"下载的是错误页面，删除文件: {target_path}")
                                target_path.unlink()
                                continue
                        except:
                            pass

                    self.downloaded_urls[url] = str(target_path)

                    # 下载间隔
                    if self.delay_between_downloads > 0:
                        time.sleep(self.delay_between_downloads)

                    return True
                else:
                    logger.error(f"文件保存失败: {target_path}")
                    continue

            except requests.exceptions.RequestException as e:
                logger.warning(f"下载失败 (尝试 {attempt + 1}/{self.max_retries}): {url} - {str(e)}")
                if attempt < self.max_retries - 1:
                    time.sleep(2 ** attempt)  # 指数退避

            except Exception as e:
                logger.error(f"下载时发生未知错误: {url} - {str(e)}")
                break

        return False

    def process_markdown_file(self, file_path: Path) -> bool:
        """处理单个Markdown文件"""
        logger.info(f"处理文件: {file_path}")

        try:
            # 读取文件内容
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # 提取图片URL
            image_urls = self.extract_image_urls(content)

            if not image_urls:
                logger.info(f"文件中没有找到远程图片链接: {file_path}")
                return True

            logger.info(f"找到 {len(image_urls)} 个图片链接")

            # 获取该MD文件对应的图片目录
            images_dir = self.get_image_dir_for_md(file_path)

            # 记录替换信息
            replacements = []
            modified_content = content

            # 下载图片并记录替换信息
            for original_match, alt_text, url in image_urls:
                # 先尝试获取内容类型来生成正确的文件名
                try:
                    head_response = self.session.head(url, timeout=10, allow_redirects=True)
                    content_type = head_response.headers.get('content-type', '')
                except:
                    content_type = None

                filename = self.generate_filename(url, alt_text, content_type)
                target_path = images_dir / filename

                if self.download_image(url, target_path):
                    # 使用实际保存的文件名（可能因为扩展名调整而改变）
                    actual_filename = target_path.name
                    relative_path = f"{self.images_subdir}/{actual_filename}"

                    # 根据原始格式生成新的引用
                    if original_match.startswith('!['):
                        # Markdown格式
                        new_reference = f"![{alt_text}]({relative_path})"
                    else:
                        # HTML格式，保持原有属性但替换src
                        new_reference = re.sub(
                            r'src=["\']?[^"\'>\s]+["\']?',
                            f'src="{relative_path}"',
                            original_match,
                            flags=re.IGNORECASE
                        )

                    replacements.append((original_match, new_reference, url))
                else:
                    logger.error(f"下载失败，跳过替换: {url}")

            # 执行替换
            if replacements:
                for original, new_ref, url in replacements:
                    modified_content = modified_content.replace(original, new_ref)
                    logger.info(f"替换: {url} -> {new_ref}")

                # 备份原文件
                backup_path = file_path.with_suffix(f"{file_path.suffix}.backup")
                if not backup_path.exists():
                    with open(backup_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    logger.info(f"创建备份文件: {backup_path}")

                # 写入修改后的内容
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(modified_content)

                logger.info(f"文件处理完成: {file_path} (替换了 {len(replacements)} 个图片链接)")
                logger.info(f"图片保存在: {images_dir}")

            return True

        except Exception as e:
            logger.error(f"处理文件时发生错误 {file_path}: {str(e)}")
            return False

    def run(self, directory: str = ".") -> None:
        """运行主程序"""
        logger.info("开始处理Markdown文件中的图片链接...")

        # 查找所有Markdown文件
        md_files = self.find_markdown_files(directory)

        if not md_files:
            logger.info("没有找到Markdown文件")
            return

        # 处理每个文件
        success_count = 0

        for md_file in md_files:
            if self.process_markdown_file(md_file):
                success_count += 1

        logger.info(f"处理完成! 成功处理 {success_count}/{len(md_files)} 个文件")
        logger.info(f"总共下载了 {len(self.downloaded_urls)} 个图片")

        # 显示每个目录的图片统计
        dir_stats = {}
        for url, local_path in self.downloaded_urls.items():
            dir_name = Path(local_path).parent
            if dir_name not in dir_stats:
                dir_stats[dir_name] = 0
            dir_stats[dir_name] += 1

        logger.info("各目录图片统计:")
        for dir_path, count in dir_stats.items():
            logger.info(f"  {dir_path}: {count} 个图片")

    def __del__(self):
        """清理资源"""
        if hasattr(self, 'session'):
            self.session.close()


def main():
    """主函数"""
    # 配置参数
    config = {
        'images_subdir': 'images',            # 图片子目录名称
        'timeout': 30,                        # 下载超时时间
        'max_retries': 3,                     # 最大重试次数
        'delay_between_downloads': 1.0,       # 下载间隔时间
    }

    print("🎨 Markdown图片下载器 - 简化版")
    print("=" * 50)
    print(f"📁 图片将保存到每个MD文件目录下的 '{config['images_subdir']}' 子目录中")
    print(f"⏱️  下载超时: {config['timeout']}秒")
    print(f"🔄 最大重试: {config['max_retries']}次")
    print(f"⏳ 下载间隔: {config['delay_between_downloads']}秒")
    print("🔧 简化策略:")
    print("   - 保持原始文件内容不变")
    print("   - 不进行任何内容处理或验证")
    print("   - 直接保存响应内容")
    print("=" * 50)

    # 创建下载器实例
    downloader = MarkdownImageDownloader(**config)

    # 运行处理
    try:
        downloader.run()
        print("\n✅ 所有任务完成!")
    except KeyboardInterrupt:
        logger.info("用户中断操作")
        print("\n⚠️  操作被用户中断")
    except Exception as e:
        logger.error(f"程序运行时发生错误: {str(e)}")
        print(f"\n❌ 程序出错: {str(e)}")


if __name__ == "__main__":
    main()
