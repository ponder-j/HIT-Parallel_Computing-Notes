#!/usr/bin/env python3
"""
合并当前目录下的所有PDF文件
"""

import os
import glob
from pypdf import PdfReader, PdfWriter

def merge_pdfs():
    # 获取当前目录下所有PDF文件
    pdf_files = glob.glob("*.pdf")

    # 过滤掉可能已存在的合并后的文件
    pdf_files = [f for f in pdf_files if not f.startswith("merged_")]

    # 按文件名排序（这样CH0, CH1, CH2...会按顺序排列）
    pdf_files.sort()

    if not pdf_files:
        print("未找到PDF文件")
        return

    print(f"找到 {len(pdf_files)} 个PDF文件:")
    for i, pdf in enumerate(pdf_files, 1):
        print(f"  {i}. {pdf}")

    # 创建PDF写入器
    writer = PdfWriter()

    # 逐个添加PDF文件
    print("\n开始合并...")
    for pdf_file in pdf_files:
        try:
            print(f"  添加: {pdf_file}")
            reader = PdfReader(pdf_file)
            for page in reader.pages:
                writer.add_page(page)
        except Exception as e:
            print(f"  错误: 无法添加 {pdf_file} - {e}")

    # 输出合并后的文件
    output_filename = "merged_parallel_computing_notes.pdf"
    print(f"\n保存到: {output_filename}")
    with open(output_filename, "wb") as output_file:
        writer.write(output_file)

    print("\n✓ PDF合并完成!")

    # 显示文件大小
    size = os.path.getsize(output_filename)
    size_mb = size / (1024 * 1024)
    print(f"文件大小: {size_mb:.2f} MB")

if __name__ == "__main__":
    merge_pdfs()
