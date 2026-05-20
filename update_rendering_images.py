#!/usr/bin/env python3
"""
更新白金项目页面的渲染图：用真实图片替换 SVG 占位图
正确映射项目名 -> 图片文件
"""

import re
import os
import shutil

# 项目名 -> 图片文件的准确映射
image_mapping = {
    "Urban Towns - Oshawa North": "unionglen.png",
    "The Conservancy - Barrhaven": "the-willows.jpg",
    "New Seaton - Pickering": "seatonville.jpg",
    "Triple Crown Estates": "ellis-lane.jpg",  # 需要确认
    "Aura - Lakeview Village": "luma.png",
    "Glenway Townhomes": "graywood-metroside.jpg",
    "WestHaven - Whitby": "rosehaven-inventory.webp",
    "King Terraces - King City": "scenic-ridge.png",  # 需要确认
    "Gold Park Homes - Vaughan": "great-gulf.jpg",
    "LIVE/WORK Townhome - Port Credit": "sienna-woods.png",
    "Midhurst Valley - Near Barrie": "scenic-ridge-phase-3.png",
    "Eclipse - Downtown Toronto": "m-city.jpg",  # 需要确认
    "The Bentley Residences": "concord-canada-house.jpg",  # 需要确认
    "Vaughan Metropolitan": "m-city-2.jpg",
    "Parkside Towns - Aurora": "abeja-district.jpg",
    "Richmond Green Estates": "remington-valley.jpg",
    "Water's Edge - Oshawa": "red-oaks.png",
    "The Ivy - Mississauga": "ivy-rouge.gif",
    "Union Station Condos": "concord-canada-house.jpg",
    "Maple Ridge - Maple": "mapleside-meadows.webp",
    "Burlington Heights": "greenpark-taywood.webp",  # 需要确认
    "Scarborough Junction": "camden-crossing.gif",  # 需要确认
    "Forest Hill Residences": "charbonnel.png",  # 需要确认
    "Yorkville Plaza": "m-city.jpg",  # 需要确认
}

def update_html_images(html_file, output_file):
    """更新 HTML 文件中的项目渲染图"""
    
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 找到所有带 base64 SVG 的图片标签
    # 模式：<img src="data:image/svg+xml;base64,..." style="..." alt="..."/>
    pattern = r'<img src="data:image/svg\+xml;base64,[^"]*" style="[^"]*" alt="([^"]*)"/>'
    
    def replace_img(match):
        alt_text = match.group(1)
        print(f"处理项目: {alt_text}")
        
        # 查找对应的图片文件
        img_file = image_mapping.get(alt_text)
        
        if img_file:
            # 检查文件是否存在
            img_path = f"images/projects/{img_file}"
            if os.path.exists(img_path):
                print(f"  ✓ 找到图片: {img_file}")
                return f'<img src="{img_path}" style="width:100%;height:220px;object-fit:cover;border-radius:0;" alt="{alt_text}"/>'
            else:
                print(f"  ✗ 图片文件不存在: {img_path}")
                return match.group(0)  # 保持原样
        else:
            print(f"  ⚠ 没有映射到图片: {alt_text}")
            return match.group(0)  # 保持原样
    
    # 替换所有匹配的图片
    updated_content = re.sub(pattern, replace_img, content)
    
    # 写入输出文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print(f"\n✓ 更新完成！输出文件: {output_file}")

if __name__ == "__main__":
    html_file = "platinum-projects.html"
    output_file = "platinum-projects-updated.html"
    
    if not os.path.exists(html_file):
        print(f"错误: 找不到文件 {html_file}")
        exit(1)
    
    print(f"开始更新 {html_file} 中的渲染图...")
    print(f"输出文件: {output_file}\n")
    
    update_html_images(html_file, output_file)
    
    # 用更新后的文件替换原文件
    print(f"\n替换原文件...")
    shutil.copy(output_file, html_file)
    print(f"✓ 已替换原文件: {html_file}")
    
    # 删除临时文件
    if os.path.exists(output_file):
        os.remove(output_file)
        print(f"✓ 已删除临时文件: {output_file}")
