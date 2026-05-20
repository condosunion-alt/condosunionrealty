#!/usr/bin/env python3
"""
给 hot-projects.html 和 new-launches.html 的项目卡片添加真实开发商宣传图
"""

import re
import os

# 项目名关键词 -> 图片文件的映射（智能匹配）
keyword_to_image = {
    # Ellis Lane
    "ellis": "ellis-lane.jpg",
    "poetry": "ellis-lane.jpg",
    "caledon": "ellis-lane.jpg",
    
    # Ivy Rouge
    "ivy": "ivy-rouge.gif",
    "rouge": "ivy-rouge.gif",
    "starlane": "ivy-rouge.gif",
    "oakville": "ivy-rouge.gif",
    
    # Winston
    "winston": "charbonnel.png",
    "baker": "charbonnel.png",
    "north york": "charbonnel.png",
    "chelsea": "charbonnel.png",
    
    # Taywood / Greenpark
    "taywood": "taywood-estates.webp",
    "greenpark": "greenpark-taywood.webp",
    "burlington": "greenpark-taywood.webp",
    
    # South Barrie / Remington
    "south barrie": "remington-valley.jpg",
    "remington": "remington-valley.jpg",
    "barrie": "remington-valley.jpg",
    
    # Pier House
    "pier house": "luma.png",
    "branthaven": "luma.png",
    "lakeview": "luma.png",
    "mississauga": "luma.png",
    
    # Towns on Bayview / Primont
    "bayview": "sienna-woods.png",
    "primont": "sienna-woods.png",
    "richmond hill": "sienna-woods.png",
    
    # Juniper Gate
    "juniper": "scenic-ridge.png",
    "gate": "scenic-ridge.png",
    
    # Concord Canada House
    "concord": "concord-canada-house.jpg",
    "canada house": "concord-canada-house.jpg",
    "prompton": "concord-canada-house.jpg",
    "downtown toronto": "concord-canada-house.jpg",
    
    # Exhale / In2ition
    "exhale": "the-willows.jpg",
    "in2ition": "the-willows.jpg",
    "long branch": "the-willows.jpg",
    
    # Carousel / Liberty
    "carousel": "carousel-thornhill.png",
    "thornhill": "carousel-thornhill.png",
    "liberty": "carousel-thornhill.png",
    
    # Simcoe Woods / Rosehaven
    "simcoe": "simcoe-woods.png",
    "rosehaven": "rosehaven-inventory.webp",
    "innisfil": "simcoe-woods.png",
    
    # Minto
    "minto": "great-gulf.jpg",
    "halfmoon": "great-gulf.jpg",
    
    # LSQ / RARE
    "lsq": "m-city-2.jpg",
    "rare": "m-city-2.jpg",
    "toronto": "m-city-2.jpg",
    
    # New Seaton / Towerhill / Aspen Ridge
    "new seaton": "seatonville.jpg",
    "seaton": "seatonville.jpg",
    "pickering": "seatonville.jpg",
    "towerhill": "seatonville.jpg",
    "aspen": "seatonville.jpg",
    
    # Appellation
    "appellation": "scenic-ridge-phase-3.png",
    "welland": "scenic-ridge-phase-3.png",
    
    # Station No.3 / Brookfield
    "station": "m-city.jpg",
    "brookfield": "m-city.jpg",
    "whitby": "m-city.jpg",
    
    # Anthem / Fusion / Metalworks / Guelph
    "anthem": "valley-woodbridge.jpg",
    "metalworks": "valley-woodbridge.jpg",
    "fusion": "valley-woodbridge.jpg",
    "guelph": "valley-woodbridge.jpg",
    
    # Carding House / Mattamy
    "carding": "great-gulf.jpg",
    "mattamy": "great-gulf.jpg",
    
    # UCE / The Grand / In2ition
    "uce": "luma.png",
    "grand": "luma.png",
    
    # 1989 Condominium / Latch
    "1989": "m-city-2.jpg",
    "latch": "m-city-2.jpg",
    "burlington": "greenpark-taywood.webp",
    
    # M City
    "m city": "m-city.jpg",
    "rogers": "m-city.jpg",
    "urban nation": "m-city.jpg",
    
    # Creekview Collective / Baker
    "creekview": "creekview-collective.jpg",
    "collective": "creekview-collective.jpg",
    
    # Cherry House / Baker
    "cherry house": "cherry-house.jpg",
    "downtown east": "cherry-house.jpg",
    
    # 250 Lawrence / Graywood
    "lawrence": "graywood-metroside.jpg",
    "graywood": "graywood-metroside.jpg",
    
    # Ivylea
    "ivylea": "ivy-rouge.gif",
    
    # Modtera
    "modtera": "artisan-towns-2.png",
    "artisan": "artisan-towns-2.png",
    
    # Chateau 9 / Flori / Charbonnel
    "chateau": "charbonnel.png",
    "flori": "charbonnel.png",
    "charbonnel": "charbonnel.png",
    
    # Metroside / Graywood
    "metroside": "graywood-metroside.jpg",
    
    # Seatonville
    "seatonville": "seatonville.jpg",
    "opus": "seatonville.jpg",
    
    # Skylands / Times Group
    "skylands": "skylands-townhome.png",
    "times": "skylands-townhome.png",
    
    # Gateway / Lindsay
    "gateway": "gateway-lindsay.jpg",
    "lindsay": "gateway-lindsay.jpg",
    
    # Double Kitchens
    "double": "red-oaks.png",
    "kitchens": "red-oaks.png",
    
    # Oakville Freehold
    "oakville": "ivy-rouge.gif",
    "freehold": "ivy-rouge.gif",
    
    # Angus Glen / Unionville
    "angus": "unionglen.png",
    "unionville": "unionglen.png",
    "unionglen": "unionglen.png",
    
    # Primont Richmond Hill
    "primont richmond": "sienna-woods.png",
    
    # East Preserve / Remington
    "east preserve": "remington-valley.jpg",
    
    # Bondhead Community / Bradford
    "bondhead": "bondhead-community.jpg",
    "bradford": "bondhead-community.jpg",
    
    # Mapleside Meadows / Uniq
    "mapleside": "mapleside-meadows.webp",
    "uniq": "mapleside-meadows.webp",
    "vaughan": "mapleside-meadows.webp",
    
    # Abeja District
    "abeja": "abeja-district.jpg",
    
    # Summit Blue Mountain / Primont
    "summit": "scenic-ridge.png",
    "blue mountain": "scenic-ridge.png",
    
    # The Willows
    "willows": "the-willows.jpg",
    
    # Camden Crossing
    "camden": "camden-crossing.gif",
    "crossing": "camden-crossing.gif",
}

def find_image_for_project(project_name, developer_info):
    """根据项目名和开发商信息查找匹配的图片"""
    search_text = f"{project_name} {developer_info}".lower()
    
    # 优先匹配最长的关键词
    best_match = None
    best_len = 0
    
    for keyword, img_file in keyword_to_image.items():
        if keyword in search_text:
            if len(keyword) > best_len:
                best_match = img_file
                best_len = len(keyword)
    
    return best_match

def add_images_to_html(html_file, output_file):
    """给 HTML 文件中的项目卡片添加图片"""
    
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 找到所有项目卡片（灵活匹配 class 中包含 card 的 div）
    # 使用更灵活的正则：匹配 <div class="...card..." ...>
    card_pattern = r'<div class="[^"]*card[^"]*"[^>]*>'
    card_matches = list(re.finditer(card_pattern, content))
    
    print(f"在 {html_file} 中找到 {len(card_matches)} 个卡片开头")
    
    if not card_matches:
        print("未找到卡片，跳过...")
        return
    
    # 分割内容为各个 card
    parts = []
    last_end = 0
    
    for i, match in enumerate(card_matches):
        # 添加卡片之前的内容
        parts.append(content[last_end:match.start()])
        # 添加卡片开头标签
        parts.append(match.group())
        last_end = match.end()
    
    # 添加最后一个卡片之后的内容
    parts.append(content[last_end:])
    
    # 现在 parts[0] 是文件开头，parts[1], parts[3], ... 是卡片开头
    # 需要重新组合并处理每个卡片的内容
    
    # 简化处理：直接在整个 content 中进行替换
    # 在每个卡片开头后添加图片
    
    new_content = card_splits[0]  # 前面的内容（head, header等）
    
    for i in range(1, len(card_splits), 2):
        card_start = card_splits[i]  # <div class="card">
        card_body = card_splits[i+1] if i+1 < len(card_splits) else ""
        
        # 提取项目名
        title_match = re.search(r'<div class="card-title">([^<]+)<small>([^<]+)</small>', card_body)
        
        if title_match:
            project_name = title_match.group(1).strip()
            developer_info = title_match.group(2).strip()
            
            # 查找匹配的图片
            img_file = find_image_for_project(project_name, developer_info)
            
            if img_file:
                # 检查图片文件是否存在
                img_path = f"images/projects/{img_file}"
                if os.path.exists(img_path):
                    # 在 card-body 前插入图片 div
                    img_div = '<div class="card-img" style="background-image:url(\'' + img_path + '\');background-size:cover;background-position:center;height:200px;"></div>\n      '
                    
                    # 在第一个 <div class="rank-badge"> 或 <div class="card-body"> 前插入图片
                    if '<div class="rank-badge"' in card_body:
                        # 在 rank-badge 前插入
                        card_body = card_body.replace('<div class="rank-badge"', img_div + '<div class="rank-badge"', 1)
                    elif '<div class="card-body">' in card_body:
                        # 在 card-body 前插入
                        card_body = card_body.replace('<div class="card-body">', img_div + '<div class="card-body">', 1)
                    
                    print(f"  ✓ {project_name} → {img_file}")
                else:
                    print(f"  ✗ 图片不存在: {img_path}")
            else:
                print(f"  ⚠ 未找到匹配图片: {project_name}")
        
        new_content += card_start + card_body
    
    # 写入输出文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"\n✓ 完成！输出文件: {output_file}\n")

if __name__ == "__main__":
    import shutil
    
    # 处理 hot-projects.html
    print("=" * 60)
    print("处理 hot-projects.html...")
    print("=" * 60 + "\n")
    add_images_to_html('hot-projects.html', 'hot-projects-with-images.html')
    
    # 处理 new-launches.html
    print("=" * 60)
    print("处理 new-launches.html...")
    print("=" * 60 + "\n")
    add_images_to_html('new-launches.html', 'new-launches-with-images.html')
    
    # 替换原文件
    print("替换原文件...")
    shutil.copy('hot-projects-with-images.html', 'hot-projects.html')
    shutil.copy('new-launches-with-images.html', 'new-launches.html')
    print("✓ 已替换 hot-projects.html")
    print("✓ 已替换 new-launches.html")
    
    # 删除临时文件
    os.remove('hot-projects-with-images.html')
    os.remove('new-launches-with-images.html')
    print("✓ 已删除临时文件")
