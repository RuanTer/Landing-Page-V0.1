# Service Page Template - Usage Guide

## 📄 Template File

**File:** `service-page-template.html`

This is your master template for all service landing pages. Copy this file and replace the placeholder text with your business information.

---

## 🚀 Quick Start - Creating a New Service Page

### Step 1: Copy the Template

```bash
cp service-page-template.html your-business-name.html
```

Or manually copy the file and rename it.

### Step 2: Replace ALL Placeholder Text

Search and replace the following placeholders (use Ctrl+H in most text editors):

#### **Required Replacements:**

| Placeholder | Replace With | Example |
|------------|--------------|---------|
| `BUSINESS_NAME` | Your business name | `WZS Trading` |
| `SERVICE_TYPE` | Type of service | `Professional Handyman Services` |
| `BUSINESS_CATEGORY` | Business category | `Handyman Services` |
| `META_DESCRIPTION` | SEO description (155 chars max) | `Trusted handyman services in the Vaal Triangle. Steel works, carports, electrical wiring...` |
| `META_KEYWORDS` | SEO keywords | `handyman Vaal Triangle, carport installation, gate motor repair` |
| `HERO_DESCRIPTION` | Main hero text | `Trusted professional handyman services in the Vaal Triangle area.` |

#### **Service Cards (4 per page):**

For each of the 4 service cards, replace:

**Card 1:**
- `SERVICE1_IMAGE` → Image filename (e.g., `carport-installation`)
- `SERVICE1_ALT` → Alt text (e.g., `Carport installation service`)
- `SERVICE1_TITLE` → Card title (e.g., `Carport Installation`)
- `SERVICE1_DESCRIPTION` → Description (e.g., `Professional steel works and roofing installation of carports.`)

**Card 2, 3, 4:** Repeat same pattern with SERVICE2_, SERVICE3_, SERVICE4_

#### **Form Configuration:**

- `FORM_ENDPOINT_URL` → Your Google Apps Script URL
- `SERVICE_NAME` → Service identifier (e.g., `Handyman`, `Tree Service`)

#### **Optional (When Ready to Activate):**

- `GA_TRACKING_ID` → Your Google Analytics tracking ID (e.g., `G-XXXXXXXXXX`)
- `WHATSAPP_NUMBER` → Your WhatsApp Business number (format: `27821234567`)

---

## 📱 Features Included

### ✅ Mobile-First Design
- 1 column on mobile (< 640px)
- 2 columns on tablet (640px - 1023px)
- 4 columns on desktop (1024px+)

### ✅ Google Analytics Ready
- Commented out by default
- Uncomment lines 20-29 when ready
- Replace `GA_TRACKING_ID` with your tracking ID
- Tracks form submissions automatically

### ✅ WhatsApp Business Integration
- Floating button (bottom right)
- Hidden by default
- To activate: Add class `active` to the `whatsapp-float` link (line 245)
- Replace `WHATSAPP_NUMBER` with your number

### ✅ Security & UX Features
- Honeypot spam protection
- 60-second rate limiting
- Form validation
- WCAG 2.1 AA accessibility
- Privacy consent checkbox
- Success modal
- Keyboard navigation

---

## 🎨 Complete Example: WZS Trading Handyman Service

Here's how to fill out the template for a handyman service:

```html
<!-- Line 6 -->
<title>WZS Trading - Professional Handyman Services in the Vaal Triangle</title>

<!-- Line 9 -->
<meta name="description" content="Trusted handyman services in the Vaal Triangle. Steel works, carports, electrical wiring, gate motor repairs, and emergency fixes.">

<!-- Line 12 -->
<meta name="keywords" content="handyman Vaal Triangle, carport installation, gate motor repair, electrical wiring, WZS Trading">

<!-- Line 80 -->
<div class="business-name">WZS Trading</div>

<!-- Line 88 -->
<span class="business-category">Handyman Services</span>

<!-- Line 91 -->
<h1>WZS Trading</h1>

<!-- Line 94 -->
<p>Trusted professional handyman services in the Vaal Triangle area.</p>

<!-- Service Cards (lines 105-144) -->
Card 1: Carport Installation
Card 2: Electrical Wiring
Card 3: Gate Motor Repair
Card 4: Emergency Repairs

<!-- Line 287-290 -->
const FORM_CONFIG = {
    endpoint: 'https://script.google.com/macros/s/YOUR_SCRIPT_ID/exec',
    serviceName: 'Handyman',
    source: 'WZS Trading Page'
};
```

---

## 🖼️ Image Requirements

### Service Card Images
- **Location:** `/images/services/`
- **Size:** Any size (will be cropped to 128px height)
- **Format:** JPG or PNG
- **Naming:** Use descriptive names (e.g., `carport-installation.jpg`)

### Business Card Image (for index.html)
- **Location:** `/images/business-cards/`
- **Size:** 800x600px minimum
- **Format:** JPG
- **Naming:** Use business name (e.g., `wzs-trading.jpg`)

---

## 🔧 Activating Google Analytics

1. Get your Google Analytics tracking ID (format: `G-XXXXXXXXXX` or `UA-XXXXXXXXX-X`)

2. In your service page, find lines 20-29:

```html
<!-- Google Analytics - REPLACE: GA_TRACKING_ID with your actual tracking ID -->
<!-- Remove comments below when ready to activate -->
<!--
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_TRACKING_ID"></script>
<script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'GA_TRACKING_ID');
</script>
-->
```

3. Remove the `<!--` and `-->` comment markers

4. Replace both instances of `GA_TRACKING_ID` with your actual ID

**Final result:**
```html
<script async src="https://www.googletagmanager.com/gtag/js?id=G-ABC123XYZ"></script>
<script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-ABC123XYZ');
</script>
```

---

## 📱 Activating WhatsApp Business

1. Get your WhatsApp Business number

2. Format it correctly: Remove spaces, hyphens, and add country code
   - South Africa: `27821234567` (replace 082 with 2782)
   - Example: `0821234567` → `27821234567`

3. Find line 245 in your service page:

```html
<a href="https://wa.me/WHATSAPP_NUMBER?text=Hi!%20I'm%20interested%20in%20your%20services"
   class="whatsapp-float"
```

4. Replace `WHATSAPP_NUMBER` with your formatted number

5. Add `active` class to show the button:

```html
<a href="https://wa.me/27821234567?text=Hi!%20I'm%20interested%20in%20your%20services"
   class="whatsapp-float active"
```

---

## 📋 Checklist for New Service Page

- [ ] Copy `service-page-template.html`
- [ ] Rename to `your-business-name.html`
- [ ] Replace `BUSINESS_NAME` (all instances)
- [ ] Replace `SERVICE_TYPE`
- [ ] Replace `BUSINESS_CATEGORY`
- [ ] Replace `META_DESCRIPTION`
- [ ] Replace `META_KEYWORDS`
- [ ] Replace `HERO_DESCRIPTION`
- [ ] Replace all SERVICE1_ placeholders
- [ ] Replace all SERVICE2_ placeholders
- [ ] Replace all SERVICE3_ placeholders
- [ ] Replace all SERVICE4_ placeholders
- [ ] Replace `FORM_ENDPOINT_URL`
- [ ] Replace `SERVICE_NAME` (2 places)
- [ ] Add 4 images to `/images/services/`
- [ ] Add 1 image to `/images/business-cards/`
- [ ] (Optional) Activate Google Analytics
- [ ] (Optional) Activate WhatsApp Business
- [ ] Test the page on mobile device
- [ ] Test form submission
- [ ] Add to index.html directory

---

## 🏠 Adding to Index Page

After creating your service page, add a card to `index.html`:

```html
<!-- Your New Business -->
<div class="business-card">
    <div class="card-content">
        <div>
            <span class="business-category">YOUR_CATEGORY</span>
            <div class="card-text">
                <h3>YOUR_HEADLINE</h3>
                <p>YOUR_DESCRIPTION</p>
            </div>
        </div>
        <a href="your-business-name.html" class="btn-card">Get Quote</a>
    </div>
    <div class="card-image">
        <img src="images/business-cards/your-business.jpg" alt="Your Business Name">
    </div>
</div>
```

---

## 🎯 Tips for Best Results

1. **Keep descriptions concise** - Service cards have limited space
2. **Use action-oriented titles** - "Get X" instead of "We offer X"
3. **High-quality images** - Professional photos convert better
4. **Test on mobile first** - Most users will be on phones
5. **Monitor Analytics** - See which services get most interest
6. **Update WhatsApp message** - Customize the pre-filled text
7. **Consistent naming** - Use same format for all service pages

---

## 🆘 Troubleshooting

**Images not showing?**
- Check file path is correct
- Ensure images are in `/images/services/` folder
- Check file extension matches (.jpg not .jpeg)

**Form not submitting?**
- Verify `FORM_ENDPOINT_URL` is correct
- Check browser console for errors (F12)
- Test with valid email address

**Mobile layout broken?**
- Clear browser cache (Ctrl + F5)
- Test in different browser
- Check no custom CSS conflicts

**WhatsApp not working?**
- Verify number format (country code + number)
- Check link has `active` class
- Test on mobile device

---

## 📞 Support

For issues or questions:
- Email: info@kroot.co.za
- Review template comments for inline guidance
- Check browser console (F12) for errors

---

**Version:** 1.0
**Last Updated:** 2025-01-29
**Compatible with:** All modern browsers, mobile-first design
