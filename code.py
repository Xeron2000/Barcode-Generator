import argparse
import barcode
from barcode.writer import ImageWriter
import re
import os

def generate_barcode(text, output_dir):
    # 选择条形码格式（如 'code128'）
    barcode_format = barcode.get_barcode_class('code128')

    # 处理文件名，去掉不适合文件名的字符
    safe_filename = re.sub(r'[^\w\-\.]', '_', text)

    # 检查输出文件夹是否存在，如果不存在则创建
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 创建条形码并保存到指定文件夹下
    barcode_instance = barcode_format(text, writer=ImageWriter())
    output_file = os.path.join(output_dir, safe_filename)  # 拼接文件路径
    barcode_instance.save(output_file)
    print(f"条形码已保存为 {output_file}.png")

def batch_generate_barcodes(base_text, start, end):
    # 文件夹名为基础文字部分
    output_dir = base_text

    # 批量生成条形码
    for i in range(start, end + 1):
        text = f"{base_text}{i}"
        generate_barcode(text, output_dir)

def main():
    # 设置命令行参数解析
    parser = argparse.ArgumentParser(description="批量生成条形码并存储在指定文件夹下")
    parser.add_argument("base_text", help="生成条形码的基础文字部分")
    parser.add_argument("start", type=int, help="数字起始值")
    parser.add_argument("end", type=int, help="数字结束值")

    # 解析命令行参数
    args = parser.parse_args()

    # 调用批量生成条形码函数
    batch_generate_barcodes(args.base_text, args.start, args.end)

if __name__ == "__main__":
    main()
