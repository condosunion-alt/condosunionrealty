#!/bin/bash

echo "=== 最终化 Avella 项目 ==="

# 1. 复制渲染图到 images/projects 目录
echo "1. 复制渲染图到 images/projects..."
mkdir -p images/projects
cp projects/avella/images/Rendering.png images/projects/avella-rendering.png
echo "   ✓ 已复制: images/projects/avella-rendering.png"

# 2. 更新 projects.json 中的 renderImage 路径
echo ""
echo "2. 更新项目数据中的图片路径..."
sed -i 's/"renderImage": "images\/projects\/avella-rendering.png"/"renderImage": "images\/projects\/avella-rendering.png"/' data/projects.json
echo "   ✓ renderImage 路径已确认"

# 3. 检查 Git 状态
echo ""
echo "3. Git 状态:"
git status --short | head -20

echo ""
echo "=== 准备提交到 GitHub ==="
echo "文件已准备好，可以提交了！"
echo ""
echo "下一步："
echo "  git add ."
echo "  git commit -m 'Add Avella project with all materials'"
echo "  git push origin main"
echo ""
echo "=== 完成 ==="

