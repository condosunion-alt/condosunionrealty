#!/bin/bash

cd pdf

echo "=== 重命名 PDF 文件 ==="
mv -v 1_Bonus-Incentives.pdf Bonus-Incentives.pdf
mv -v 2_Agent-Worksheet.pdf Agent-Worksheet.pdf
mv -v 3_Price-List.pdf Price-List.pdf
mv -v 6_Fast-Facts.pdf Fast-Facts.pdf
mv -v 7_Site-Plan.pdf Site-Plan.pdf
mv -v 9_Floorplans.pdf Floorplans.pdf

cd ../images

echo ""
echo "=== 重命名图片文件 ==="
mv -v 5_Amenities-Map.png Amenities-Map.png
mv -v 8_Rendering.png Rendering.png

echo ""
echo "=== 最终文件列表 ==="
echo "PDF 文件:"
ls -lh ../pdf/

echo ""
echo "图片文件:"
ls -lh .

