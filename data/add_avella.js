const fs = require('fs');

// Avella 项目信息
const avellaProject = {
  "id": "avella-aurora",
  "name": "Avella",
  "developer": "Treasure Hill",
  "location": "Aurora, ON",
  "price": "Register for VIP Pricing",
  "priceValue": 0,
  "status": "Platinum Launch",
  "type": "2-Car Garage Homes",
  "bedrooms": "Up to 5 Bedrooms",
  "bathrooms": "2.5-4 Bathrooms",
  "sqft": "2500-4000 sqft (est.)",
  "completionDate": "2028-2029",
  "depositStructure": "TBD - Contact for details",
  "maintenanceFee": "N/A - Freehold",
  "renderImage": "images/projects/avella-rendering.png",
  "floorPlans": [
    {
      "name": "Floor Plans",
      "file": "projects/avella/pdf/Floorplans.pdf"
    }
  ],
  "brokerPortalUrl": "https://broker.treasurehill.com/community/avella",
  "description": "Luxury 2-car garage homes in Aurora with up to 5 bedrooms. Premium location in York Region with easy access to Hwy 404 and GO Transit.",
  "features": [
    "2-Car Garage Standard",
    "Up to 5 Bedrooms",
    "Premium Aurora Location",
    "Close to Hwy 404",
    "GO Transit Access",
    "York Region Schools",
    "Luxury Finishes Throughout",
    "Treasure Hill Quality"
  ],
  "vipAccess": true,
  "brokerCommission": "Contact for details",
  "documents": [
    {
      "name": "Price List",
      "file": "projects/avella/pdf/Price-List.pdf",
      "type": "pdf"
    },
    {
      "name": "Floor Plans",
      "file": "projects/avella/pdf/Floorplans.pdf",
      "type": "pdf"
    },
    {
      "name": "Site Plan",
      "file": "projects/avella/pdf/Site-Plan.pdf",
      "type": "pdf"
    },
    {
      "name": "Fast Facts",
      "file": "projects/avella/pdf/Fast-Facts.pdf",
      "type": "pdf"
    },
    {
      "name": "Bonus Incentives",
      "file": "projects/avella/pdf/Bonus-Incentives.pdf",
      "type": "pdf"
    },
    {
      "name": "Agent Worksheet",
      "file": "projects/avella/pdf/Agent-Worksheet.pdf",
      "type": "pdf"
    },
    {
      "name": "Amenities Map",
      "file": "projects/avella/images/Amenities-Map.png",
      "type": "image"
    },
    {
      "name": "Rendering",
      "file": "projects/avella/images/Rendering.png",
      "type": "image"
    }
  ]
};

// 读取现有项目
let projects = [];
try {
  const data = fs.readFileSync('projects.json', 'utf8');
  projects = JSON.parse(data);
  console.log(`✓ 已读取现有项目: ${projects.length} 个`);
} catch (err) {
  console.log('⚠  projects.json 不存在或为空，创建新数组');
  projects = [];
}

// 检查是否已存在 Avella 项目
const existingIndex = projects.findIndex(p => p.id === 'avella-aurora');
if (existingIndex >= 0) {
  console.log('⚠ Avella 项目已存在，将更新...');
  projects[existingIndex] = avellaProject;
} else {
  console.log('✓ 添加新项目: Avella');
  projects.push(avellaProject);
}

// 保存到文件
fs.writeFileSync('projects.json', JSON.stringify(projects, null, 2));
console.log(`✓ 已保存 ${projects.length} 个项目到 projects.json`);

// 同时更新 projects_updated.json
try {
  fs.writeFileSync('projects_updated.json', JSON.stringify(projects, null, 2));
  console.log('✓ 已更新 projects_updated.json');
} catch (err) {
  console.log('⚠  无法更新 projects_updated.json');
}

console.log('');
console.log('=== Avella 项目已添加 ===');
console.log('项目 ID: avella-aurora');
console.log('项目名称: Avella');
console.log('位置: Aurora, ON');
console.log('类型: 2-Car Garage Homes');
console.log('状态: Platinum Launch');
