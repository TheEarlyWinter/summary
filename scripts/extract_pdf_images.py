#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
extract_pdf_images.py - 从实验 PDF 报告（液相色谱 HPLC、气质联用 GC-MS、核磁 NMR、TLC 点板图等）中提取图片或渲染图谱页面
"""

import sys
import os
import fitz  # PyMuPDF
from PIL import Image
import io
import argparse

def extract_images_from_pdf(pdf_path: str, output_dir: str, render_pages: bool = True, min_width: int = 100, min_height: int = 100):
    """
    从 PDF 文件中提取图片。
    如果 PDF 内部包含嵌入位图（Raster Images），提取位图；
    如果 PDF 是矢量图谱或报告页，或者需要整页图谱，则将页面高分辨率渲染（300 DPI）为图片。
    """
    os.makedirs(output_dir, exist_ok=True)
    doc = fitz.open(pdf_path)
    extracted_files = []
    
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    
    # 1. 尝试提取嵌入图片
    img_idx = 1
    for page_num in range(len(doc)):
        page = doc[page_num]
        image_list = page.get_images(full=True)
        
        for img_info in image_list:
            xref = img_info[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            width = base_image["width"]
            height = base_image["height"]
            
            # 过滤极小的装饰性图标
            if width >= min_width and height >= min_height:
                img_filename = f"{base_name}_p{page_num+1}_img{img_idx}.{image_ext}"
                img_filepath = os.path.join(output_dir, img_filename)
                with open(img_filepath, "wb") as f:
                    f.write(image_bytes)
                extracted_files.append({
                    "path": os.path.abspath(img_filepath),
                    "page": page_num + 1,
                    "type": "extracted_image",
                    "width": width,
                    "height": height
                })
                img_idx += 1

    # 2. 如果没有提取到位图，或者用户需要整页渲染（如 HPLC 标准工作站报告单）
    if render_pages or len(extracted_files) == 0:
        for page_num in range(len(doc)):
            page = doc[page_num]
            # 300 DPI 渲染以保证图谱波形与文字清晰
            zoom = 300 / 72  # 72 is standard PDF dpi
            mat = fitz.Matrix(zoom, zoom)
            pix = page.get_pixmap(matrix=mat, alpha=False)
            
            page_filename = f"{base_name}_page_{page_num+1}.png"
            page_filepath = os.path.join(output_dir, page_filename)
            pix.save(page_filepath)
            
            extracted_files.append({
                "path": os.path.abspath(page_filepath),
                "page": page_num + 1,
                "type": "rendered_page",
                "width": pix.width,
                "height": pix.height
            })
            
    doc.close()
    return extracted_files

def main():
    parser = argparse.ArgumentParser(description="Extract images or render pages from experiment report PDF.")
    parser.add_argument("--pdf", "-p", required=True, help="Path to input PDF file.")
    parser.add_argument("--output-dir", "-o", required=True, help="Directory to save extracted images.")
    parser.add_argument("--render-pages", action="store_true", default=True, help="Also render full pages as high-res images.")
    args = parser.parse_args()
    
    if not os.path.exists(args.pdf):
        print(f"Error: PDF file '{args.pdf}' not found.", file=sys.stderr)
        sys.exit(1)
        
    results = extract_images_from_pdf(args.pdf, args.output_dir, render_pages=args.render_pages)
    print(f"Extracted {len(results)} images/pages to {args.output_dir}:")
    for item in results:
        print(f"  - [{item['type']}] {item['path']} ({item['width']}x{item['height']})")

if __name__ == "__main__":
    main()
