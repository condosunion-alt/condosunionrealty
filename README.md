# Condos Union Realty - Platinum Projects Portal

## 🏢 Website Structure

```
condosunionrealty-site/
├── index.html              # Homepage
├── platinum-projects.html  # 50 Platinum Projects grid
├── project-detail.html    # Project detail page (login required)
├── portal.html            # Broker & Client login/register
├── contact.html           # Contact page
├── about.html             # About page
├── css/                   # Stylesheets
├── js/                    # JavaScript
├── images/                # Images
└── data/
    └── projects.json       # 50 projects database
```

## 🔐 Access Control

- **portal.html** - Login/Register system
  - Broker Registration (with brokerage name)
  - Client/Investor Registration
  - Stores accounts in localStorage (demo mode)
  - Auto-login after registration

- **project-detail.html** - Protected page
  - Requires login (checks localStorage `cur_loggedin`)
  - Shows full project details, features, pricing
  - Access denied message with login link if not authenticated

- **platinum-projects.html** - Public browsing
  - Shows all 50 projects in card grid
  - Each card links to `project-detail.html?id=xxx`
  - Buttons say "View Details →" (redirects to login if not logged in)

## 📊 Projects Database (data/projects.json)

Each project has:
- `id` - URL-friendly identifier
- `name` - Project name
- `developer` - Developer name
- `location` - City, ON
- `price` - Display price
- `priceValue` - Numeric value for sorting
- `status` - "Platinum Launch" | "VIP Registration" | "Now Selling" | "Platinum"
- `type` - "Townhome" | "Condominium" | "Luxury Detached Homes" etc.
- `bedrooms`, `bathrooms`, `sqft`
- `completionDate` - Expected completion year
- `depositStructure` - Deposit payment structure
- `maintenanceFee` - Monthly maintenance fee
- `description` - Project description
- `features` - Array of feature strings
- `vipAccess` - Boolean: requires VIP/broker access
- `renderImage` - (Reserved for future real render images)
- `brokerPortalUrl` - (Reserved for developer broker portal links)

## 🚀 How to Add Real Render Images

1. Get the real render image URL or file
2. Update `data/projects.json`:
   ```json
   "renderImage": "https://condosunionrealty.com/images/projects/urban-towns-oshawa.jpg"
   ```
3. Or base64 encode and use data URL:
   ```json
   "renderImage": "data:image/jpeg;base64,/9j/4AAQ..."
   ```

## 🔗 How to Add Broker Portal Links

Once you receive broker portal URLs from developers:
1. Update `data/projects.json`:
   ```json
   "brokerPortalUrl": "https://broker.developer.com/register/condosunion"
   ```
2. The project detail page will show a "Register for VIP Access" button linking to this URL

## 🚀 GitHub Pages Deployment

- Repository: `condosunion-alt/condosunionrealty`
- Branch: `main`
- Custom domain: `condosunionrealty.com`
- Auto-deploys on push to main

## 📝 Next Steps

1. **Add real render images** - Replace SVG placeholders with actual project renderings
2. **Add broker portal URLs** - When you receive them from developers
3. **Add floor plans** - PDF or image floor plans for each project
4. **Upgrade to real backend** - Replace localStorage with real database (Supabase/Firebase)
5. **Add email notifications** - Notify Mike when brokers/clients register
