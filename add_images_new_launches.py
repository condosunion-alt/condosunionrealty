#!/usr/bin/env python3
"""
简化版：给 new-launches.html 添加项目图片
直接在每个卡片的 rank-badge 或 card-body 前插入图片
"""

import re
import os

# 项目名关键词 -> 图片文件的映射
keyword_to_image = {
    "1989": "m-city-2.jpg",
    "latch": "m-city-2.jpg",
    "m city": "m-city.jpg",
    "rogers": "m-city.jpg",
    "pickering": "seatonville.jpg",
    "concord": "concord-canada-house.jpg",
    "station": "m-city.jpg",
    "brookfield": "m-city.jpg",
    "whitby": "m-city.jpg",
    "anthem": "valley-woodbridge.jpg",
    "metalworks": "valley-woodbridge.jpg",
    "fusion": "valley-woodbridge.jpg",
    "lsq": "m-city-2.jpg",
    "rare": "m-city-2.jpg",
    "uce": "luma.png",
    "grand": "luma.png",
    "exhale": "the-willows.jpg",
    "in2ition": "the-willows.jpg",
    "creekview": "creekview-collective.jpg",
    "cherry": "cherry-house.jpg",
    "lawrence": "graywood-metroside.jpg",
    "graywood": "graywood-metroside.jpg",
    "ivylea": "ivy-rouge.gif",
    "modtera": "artisan-towns-2.png",
    "artisan": "artisan-towns-2.png",
    "chateau": "charbonnel.png",
    "flori": "charbonnel.png",
    "charbonnel": "charbonnel.png",
    "winston": "charbonnel.png",
    "baker": "charbonnel.png",
    "ivy rouge": "ivy-rouge.gif",
    "starlane": "ivy-rouge.gif",
    "taywood": "taywood-estates.webp",
    "greenpark": "greenpark-taywood.webp",
    "carousel": "carousel-thornhill.png",
    "thornhill": "carousel-thornhill.png",
    "liberty": "carousel-thornhill.png",
    "bayview": "sienna-woods.png",
    "primont": "sienna-woods.png",
    "appellation": "scenic-ridge-phase-3.png",
    "welland": "scenic-ridge-phase-3.png",
    "pier house": "luma.png",
    "branthaven": "luma.png",
    "carding": "great-gulf.jpg",
    "mattamy": "great-gulf.jpg",
    "metroside": "graywood-metroside.jpg",
    "seatonville": "seatonville.jpg",
    "opus": "seatonville.jpg",
    "seaton": "seatonville.jpg",
    "skylands": "skylands-townhome.png",
    "times": "skylands-townhome.png",
    "gateway": "gateway-lindsay.jpg",
    "lindsay": "gateway-lindsay.jpg",
    "double": "red-oaks.png",
    "oakville": "ivy-rouge.gif",
    "angus": "unionglen.png",
    "unionville": "unionglen.png",
    "unionglen": "unionglen.png",
    "mapleside": "mapleside-meadows.webp",
    "uniq": "mapleside-meadows.webp",
    "abeja": "abeja-district.jpg",
    "summit": "scenic-ridge.png",
    "blue mountain": "scenic-ridge.png",
    "willows": "the-willows.jpg",
    "camden": "camden-crossing.gif",
    "simcoe": "simcoe-woods.png",
    "rosehaven": "rosehaven-inventory.webp",
    "minto": "great-gulf.jpg",
    "ellis": "ellis-lane.jpg",
    "poetry": "ellis-lane.jpg",
    "caledon": "ellis-lane.jpg",
    "remington": "remington-valley.jpg",
    "barrie": "remington-valley.jpg",
    "juniper": "scenic-ridge.png",
    "gate": "scenic-ridge.png",
    "east preserve": "remington-valley.jpg",
    "bondhead": "bondhead-community.jpg",
    "bradford": "bondhead-community.jpg",
    "south barrie": "remington-valley.jpg",
}

def find_image_for_project(project_name):
    """根据项目名查找匹配的图片"""
    search_text = project_name.lower()
    
    # 优先匹配最长的关键词
    best_match = None
    best_len = 0
    
    for keyword, img_file in keyword_to_image.items():
        if keyword in search_text:
            if len(keyword) > best_len:
                best_match = img_file
                best_len = len(keyword)
    
    return best_match

def add_images_to_new_launches():
    """给 new-launches.html 添加图片"""
    
    with open('new-launches.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 提取所有项目名
    projects = re.findall(r'<div class="card-title">([^<]+)<small>([^<]+)</small>', content)
    
    print(f"在 new-launches.html 中找到 {len(projects)} 个项目\n")
    
    # 为每个项目添加图片
    updated_content = content
    
    for project_name, developer in projects:
        project_name = project_name.strip()
        developer = developer.strip()
        
        img_file = find_image_for_project(project_name + " " + developer)
        
        if img_file:
            img_path = f"images/projects/{img_file}"
            if os.path.exists(img_path):
                # 在 card-title 前插入图片 div
                img_div = f'<div class="card-img" style="background-image:url(\\'{img_path}\\');background-size:cover;background-position:center;height:200px;"></div>\n        '
                
                # 在 <div class="card-title"> 前插入图片
                old_pattern = f'<div class="card-title">{project_name}<small>{developer}</small>'
                if old_pattern in updated_content:
                    new_pattern = img_div + old_pattern
                    updated_content = updated_content.replace(old_pattern, new_pattern, 1)
                    print(f"  ✓ {project_name} → {img_file}")
                else:
                    print(f"  ⚠ 未找到匹配的文本: {project_name}")
            else:
                print(f"  ✗ 图片不存在: {img_path}")
        else:
            print(f"  ⚠ 未找到匹配图片: {project_name}")
    
    # 写入文件
    with open('new-launches.html', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print(f"\n✓ 完成！已更新 new-launches.html")

if __name__ == "__main__":
    print("=" * 60)
    print("处理 new-launches.html...")
    print("=" * 60 + "\n")
    
    add_images_to_new_launches()
