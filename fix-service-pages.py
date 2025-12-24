#!/usr/bin/env python3
"""
Script to fix all service landing pages with:
- Proper accessibility (labels, ARIA, semantic HTML)
- SEO meta tags
- Security headers
- Focus indicators
- Input validation
- Honeypot spam protection
- Rate limiting
- Better error handling
"""

import re

# Service pages configuration
services = {
    'handyman-service.html': {
        'title': 'WZS Trading - Professional Handyman Services in the Vaal Triangle',
        'description': 'Trusted handyman services in the Vaal Triangle. Steel works, carports, electrical wiring, gate motor repairs, and emergency fixes.',
        'keywords': 'handyman Vaal Triangle, carport installation, gate motor repair, electrical wiring, WZS Trading',
        'business_name': 'WZS Trading',
        'service_type': 'Handyman',
        'cta': 'Get Free Quote'
    },
    'kroot-online.html': {
        'title': 'Kroot Online - Web Design & Digital Presence for Your Business',
        'description': 'Professional web design and digital presence services. Landing pages, business websites, SEO optimization, and branding in the Vaal Triangle.',
        'keywords': 'web design Vaal Triangle, landing pages, SEO optimization, digital presence, Kroot Online',
        'business_name': 'Kroot Online',
        'service_type': 'Kroot Online',
        'cta': 'Get Started'
    },
    'home-renovations.html': {
        'title': 'Borderline Renovations - Transform Your Home in the Vaal Triangle',
        'description': 'Quality home renovation services in the Vaal Triangle. Kitchen remodeling, bathroom upgrades, painting, flooring, and complete home transformations.',
        'keywords': 'home renovations Vaal Triangle, kitchen remodel, bathroom upgrade, Borderline Renovations',
        'business_name': 'Borderline Renovations',
        'service_type': 'Home Renovations',
        'cta': 'Get Free Quote'
    },
    'tall-guy-tree-service.html': {
        'title': 'Tall Guy Tree Service - Professional Tree Care in the Vaal Triangle',
        'description': 'Expert tree cutting, trimming, and removal services in the Vaal Triangle. Keep your property safe and beautiful with professional tree care.',
        'keywords': 'tree service Vaal Triangle, tree removal, tree cutting, tree trimming, Tall Guy Tree Service',
        'business_name': 'Tall Guy Tree Service',
        'service_type': 'Tree Service',
        'cta': 'Get Free Quote'
    },
    'vaal-skip-hire.html': {
        'title': 'Vaal Skip Hire - Hassle-Free Waste Removal & Skip Bin Services',
        'description': 'Convenient skip bin hire and waste removal services in the Vaal Triangle. Fast, reliable rubble removal for all project sizes.',
        'keywords': 'skip hire Vaal Triangle, waste removal, skip bin rental, rubble removal, Vaal Skip Hire',
        'business_name': 'Vaal Skip Hire',
        'service_type': 'Skip Hire',
        'cta': 'Request Service'
    }
}

def fix_service_page(filename, config):
    """Fix a single service page with all improvements"""

    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add SEO meta tags and security headers after title
    title_pattern = r'(<title>.*?</title>)\s*'
    meta_tags = f'''$1
    <meta name="description" content="{config['description']}">
    <meta name="keywords" content="{config['keywords']}">
    <meta http-equiv="X-Frame-Options" content="DENY">
    <meta http-equiv="X-Content-Type-Options" content="nosniff">
    <meta name="referrer" content="strict-origin-when-cross-origin">

    '''
    content = re.sub(title_pattern, meta_tags, content, count=1)

    # 2. Add focus indicators to CSS (after *{margin:0;padding:0;box-sizing:border-box})
    css_pattern = r'(\*\{margin:0;padding:0;box-sizing:border-box\})'
    focus_css = r'$1*:focus-visible{outline:3px solid var(--tuscan);outline-offset:2px}'
    content = re.sub(css_pattern, focus_css, content)

    # 3. Add skip link styles after focus indicators
    skip_styles = '.skip-link{position:absolute;top:-40px;left:0;background:var(--tuscan);color:var(--carbon);padding:8px;z-index:200;text-decoration:none;font-weight:600}.skip-link:focus{top:0}'
    content = content.replace('*:focus-visible{outline:3px solid var(--tuscan);outline-offset:2px}',
                            '*:focus-visible{outline:3px solid var(--tuscan);outline-offset:2px}' + skip_styles)

    # 4. Add skip link before <header>
    content = re.sub(r'</head>\s*<body>\s*<header>',
                    '</head>\\n<body>\\n    <a href="#main-content" class="skip-link">Skip to main content</a>\\n    <header>',
                    content)

    # 5. Wrap content in <main> tag
    content = re.sub(r'(</header>)\s*(<section class="hero">)',
                    '$1\\n\\n    <main id="main-content">\\n    $2',
                    content)

    # 6. Close <main> before modal
    content = re.sub(r'(</section>)\s*(<div id="successModal")',
                    '$1\\n    </main>\\n\\n    $2',
                    content)

    # 7. Fix form labels with proper IDs and attributes
    # Name field
    content = re.sub(
        r'<label>Your Name \*</label>\s*<input type="text" name="name" required>',
        f'<label for="{config["service_type"].lower().replace(" ", "-")}-name">Your Name <span aria-label="required">*</span></label>\\n                            <input type="text" id="{config["service_type"].lower().replace(" ", "-")}-name" name="name" autocomplete="name" minlength="2" maxlength="100" pattern="[A-Za-z\\s]+" required aria-required="true">',
        content
    )

    # Phone field
    content = re.sub(
        r'<label>Phone Number \*</label>\s*<input type="tel" name="phone" required>',
        f'<label for="{config["service_type"].lower().replace(" ", "-")}-phone">Phone Number <span aria-label="required">*</span></label>\\n                            <input type="tel" id="{config["service_type"].lower().replace(" ", "-")}-phone" name="phone" autocomplete="tel" pattern="[0-9\\s\\+\\-\\(\\)]{{10,15}}" placeholder="0821234567" required aria-required="true">',
        content
    )

    # Email field
    content = re.sub(
        r'<label>Email Address \*</label>\s*<input type="email" name="email" required>',
        f'<label for="{config["service_type"].lower().replace(" ", "-")}-email">Email Address <span aria-label="required">*</span></label>\\n                            <input type="email" id="{config["service_type"].lower().replace(" ", "-")}-email" name="email" autocomplete="email" maxlength="100" required aria-required="true">',
        content
    )

    # 8. Add trust signals and privacy notice before submit button
    trust_html = '''<p style="font-size:0.875rem;color:var(--graphite);margin-bottom:1.5rem">🔒 Your information is never shared • Response within 24 hours</p>
                        <div class="form-group" style="margin-bottom:1.5rem">
                            <label style="display:flex;align-items:center;font-size:0.875rem">
                                <input type="checkbox" required style="width:auto;margin-right:0.5rem" aria-required="true">
                                I consent to the collection of my personal data as per the <a href="privacy-policy.html" style="color:var(--tuscan);text-decoration:underline">Privacy Policy</a>
                            </label>
                        </div>
                        <div style="position:absolute;left:-5000px" aria-hidden="true">
                            <input type="text" name="honeypot" tabindex="-1" autocomplete="off">
                        </div>'''

    content = re.sub(r'(<button type="submit" class="btn-submit">)', trust_html + '\\n                        $1', content)

    # 9. Fix modal accessibility
    content = re.sub(
        r'<div id="successModal" class="modal">',
        '<div id="successModal" class="modal" role="dialog" aria-modal="true" aria-labelledby="modal-title">',
        content
    )

    content = re.sub(
        r'<div class="modal-icon">✅</div>\s*<h2>Thank You!</h2>',
        '<div class="modal-icon" aria-hidden="true">✅</div>\\n            <h2 id="modal-title">Thank You!</h2>',
        content
    )

    content = re.sub(
        r'<button class="modal-close-btn" onclick="closeModal\(\)">Close</button>',
        '<button class="modal-close-btn" onclick="closeModal()" aria-label="Close dialog">Close</button>',
        content
    )

    # 10. Replace entire JavaScript with improved version
    old_js_pattern = r'<script>.*?</script>'

    new_js = f'''<script>
        function closeModal() {{
            const modal = document.getElementById('successModal');
            modal.style.display = 'none';
            modal.setAttribute('aria-hidden', 'true');
        }}

        function openModal() {{
            const modal = document.getElementById('successModal');
            modal.style.display = 'block';
            modal.setAttribute('aria-hidden', 'false');
            const closeBtn = modal.querySelector('.modal-close-btn');
            if (closeBtn) closeBtn.focus();
        }}

        async function submitForm(e) {{
            e.preventDefault();
            const form = e.target;
            const btn = form.querySelector('.btn-submit');
            const fd = new FormData(form);

            // Honeypot check
            if (fd.get('honeypot')) {{
                return; // Bot detected, silently fail
            }}

            // Rate limiting
            const lastSubmit = localStorage.getItem('lastSubmitTime');
            if (lastSubmit && Date.now() - parseInt(lastSubmit) < 60000) {{
                alert('Please wait a moment before submitting again.');
                return;
            }}

            const name = fd.get('name');
            const phone = fd.get('phone');
            const email = fd.get('email');

            if (!name || !phone || !email) {{
                alert('Please complete all required fields');
                return;
            }}

            btn.disabled = true;
            btn.textContent = 'Sending...';

            const data = {{
                service: '{config["service_type"]}',
                name: name.trim(),
                phone: phone.trim(),
                email: email.trim(),
                source: '{config["business_name"]} Page',
                timestamp: new Date().toISOString()
            }};

            try {{
                await fetch('https://script.google.com/macros/s/AKfycbyO5Hqnx_LsPDhE-5nZHNidnH6jFbMipcK-aWw7AjvhXts08C--41x09Ftm3_pBqJn33Q/exec', {{
                    method: 'POST',
                    mode: 'no-cors',
                    headers: {{'Content-Type': 'application/json'}},
                    body: JSON.stringify(data)
                }});

                localStorage.setItem('lastSubmitTime', Date.now().toString());
                openModal();
                form.reset();
            }} catch (error) {{
                alert('Unable to submit form. Please try again later or contact us directly at info@kroot.co.za');
            }} finally {{
                btn.disabled = false;
                btn.textContent = '{config["cta"]}';
            }}
        }}

        // Modal click outside to close
        document.getElementById('successModal').addEventListener('click', function(e) {{
            if (e.target === this) closeModal();
        }});

        // Escape key to close modal
        document.addEventListener('keydown', function(e) {{
            if (e.key === 'Escape') {{
                const modal = document.getElementById('successModal');
                if (modal.style.display === 'block') closeModal();
            }}
        }});
    </script>'''

    content = re.sub(old_js_pattern, new_js, content, flags=re.DOTALL)

    # Write fixed content back
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✅ Fixed {filename}")

# Main execution
if __name__ == '__main__':
    for filename, config in services.items():
        try:
            fix_service_page(filename, config)
        except Exception as e:
            print(f"❌ Error fixing {filename}: {e}")

    print("\\n✅ All service pages fixed!")
