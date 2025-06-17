import os
from jinja2 import Environment, FileSystemLoader


def render_j2_files(directory):
    # 设置 Jinja2 环境
    env = Environment(loader=FileSystemLoader("."))

    # 遍历目录中的所有文件
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.j2'):
                # 获取完整的文件路径
                file_path = os.path.join(root, filename)

                template = env.get_template(file_path)

                # 渲染模板（这里假设不需要传入额外的变量，如果需要，可以在 render() 中添加）
                output = template.render()

                # 生成输出文件名（去掉 .j2 后缀）
                output_filename = os.path.splitext(filename)[0]
                output_path = os.path.join(root, output_filename)

                # 写入输出文件
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(output)

                print(f"Generated {output_path}")


if __name__ == "__main__":
    # 指定要处理的目录
    directory_to_process = './docs'  # 你可以更改这个路径为你想要处理的目录

    # 调用函数处理目录
    render_j2_files(directory_to_process)
