# Quick Fix Guide - Remaining 2 Pages

I've already fixed:
- ✅ directory.html
- ✅ handyman-service.html

You need to fix:
- ⏳ kroot-online.html (I'm doing this now)
- ⏳ home-renovations.html (I'm doing this now)
- 🔧 tall-guy-tree-service.html (YOU do this)
- 🔧 vaal-skip-hire.html (YOU do this)

---

## For tall-guy-tree-service.html

### Step 1: Add meta tags after line 6 (after `<title>`)
```html
<meta name="description" content="Expert tree cutting, trimming, and removal services in the Vaal Triangle. Keep your property safe and beautiful with professional tree care.">
<meta name="keywords" content="tree service Vaal Triangle, tree removal, tree cutting, tree trimming, Tall Guy Tree Service">
<meta http-equiv="X-Frame-Options" content="DENY">
<meta http-equiv="X-Content-Type-Options" content="nosniff">
<meta name="referrer" content="strict-origin-when-cross-origin">
```

### Step 2: Replace line 9 CSS start
Find: `*{margin:0;padding:0;box-sizing:border-box}:root{`

Replace with:
`*{margin:0;padding:0;box-sizing:border-box}*:focus-visible{outline:3px solid var(--tuscan);outline-offset:2px}.skip-link{position:absolute;top:-40px;left:0;background:var(--tuscan);color:var(--carbon);padding:8px;z-index:200;text-decoration:none;font-weight:600}.skip-link:focus{top:0}:root{`

### Step 3: Add skip link after `<body>`
Add this line right after `</head>` and `<body>`:
```html
<a href="#main-content" class="skip-link">Skip to main content</a>
```

### Step 4: Add `<main>` wrapper
After `</header>` add: `<main id="main-content">`
Before `<div id="successModal"` add: `</main>`

### Step 5: Replace the form section (around lines 63-81)
```html
<div class="form-container">
    <h3>Request a Quote</h3>
    <p class="form-subtitle">Fill out the form and we'll contact you shortly</p>
    <p style="font-size:0.875rem;color:var(--graphite);margin-bottom:1.5rem">🔒 Your information is never shared • Response within 24 hours</p>

    <form onsubmit="submitForm(event)">
        <div class="form-group">
            <label for="tree-name">Your Name <span aria-label="required">*</span></label>
            <input type="text" id="tree-name" name="name" autocomplete="name" minlength="2" maxlength="100" pattern="[A-Za-z\s]+" required aria-required="true">
        </div>
        <div class="form-group">
            <label for="tree-phone">Phone Number <span aria-label="required">*</span></label>
            <input type="tel" id="tree-phone" name="phone" autocomplete="tel" pattern="[0-9\s\+\-\(\)]{10,15}" placeholder="0821234567" required aria-required="true">
        </div>
        <div class="form-group">
            <label for="tree-email">Email Address <span aria-label="required">*</span></label>
            <input type="email" id="tree-email" name="email" autocomplete="email" maxlength="100" required aria-required="true">
        </div>
        <div class="form-group" style="margin-bottom:1.5rem">
            <label style="display:flex;align-items:center;font-size:0.875rem">
                <input type="checkbox" required style="width:auto;margin-right:0.5rem" aria-required="true">
                I consent to the collection of my personal data as per the <a href="privacy-policy.html" style="color:var(--tuscan);text-decoration:underline">Privacy Policy</a>
            </label>
        </div>
        <div style="position:absolute;left:-5000px" aria-hidden="true">
            <input type="text" name="honeypot" tabindex="-1" autocomplete="off">
        </div>
        <button type="submit" class="btn-submit">Get Free Quote</button>
    </form>
</div>
```

### Step 6: Fix modal (around line 87)
Find: `<div id="successModal" class="modal">`
Replace with: `<div id="successModal" class="modal" role="dialog" aria-modal="true" aria-labelledby="modal-title">`

Find: `<div class="modal-icon">✅</div>`
Replace with: `<div class="modal-icon" aria-hidden="true">✅</div>`

Find: `<h2>Thank You!</h2>`
Replace with: `<h2 id="modal-title">Thank You!</h2>`

Find: `<button class="modal-close-btn" onclick="closeModal()">Close</button>`
Replace with: `<button class="modal-close-btn" onclick="closeModal()" aria-label="Close dialog">Close</button>`

### Step 7: Replace entire `<script>` section (last 2 lines of file)

Replace the one-line minified script with:
```javascript
<script>
    function closeModal() {
        const modal = document.getElementById('successModal');
        modal.style.display = 'none';
        modal.setAttribute('aria-hidden', 'true');
    }

    function openModal() {
        const modal = document.getElementById('successModal');
        modal.style.display = 'block';
        modal.setAttribute('aria-hidden', 'false');
        const closeBtn = modal.querySelector('.modal-close-btn');
        if (closeBtn) closeBtn.focus();
    }

    async function submitForm(e) {
        e.preventDefault();
        const form = e.target;
        const btn = form.querySelector('.btn-submit');
        const fd = new FormData(form);

        if (fd.get('honeypot')) return;

        const lastSubmit = localStorage.getItem('lastSubmitTime');
        if (lastSubmit && Date.now() - parseInt(lastSubmit) < 60000) {
            alert('Please wait a moment before submitting again.');
            return;
        }

        const name = fd.get('name');
        const phone = fd.get('phone');
        const email = fd.get('email');

        if (!name || !phone || !email) {
            alert('Please complete all required fields');
            return;
        }

        btn.disabled = true;
        btn.textContent = 'Sending...';

        const data = {
            service: 'Tree Service',
            name: name.trim(),
            phone: phone.trim(),
            email: email.trim(),
            source: 'Tall Guy Tree Service Page',
            timestamp: new Date().toISOString()
        };

        try {
            await fetch('https://script.google.com/macros/s/AKfycbyO5Hqnx_LsPDhE-5nZHNidnH6jFbMipcK-aWw7AjvhXts08C--41x09Ftm3_pBqJn33Q/exec', {
                method: 'POST',
                mode: 'no-cors',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(data)
            });

            localStorage.setItem('lastSubmitTime', Date.now().toString());
            openModal();
            form.reset();
        } catch (error) {
            alert('Unable to submit form. Please try again later or contact us directly at info@kroot.co.za');
        } finally {
            btn.disabled = false;
            btn.textContent = 'Get Free Quote';
        }
    }

    document.getElementById('successModal').addEventListener('click', function(e) {
        if (e.target === this) closeModal();
    });

    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            const modal = document.getElementById('successModal');
            if (modal.style.display === 'block') closeModal();
        }
    });
</script>
```

---

## For vaal-skip-hire.html

### Follow the EXACT same steps as tall-guy above, but use these values:

**Meta tags:**
```html
<meta name="description" content="Convenient skip bin hire and waste removal services in the Vaal Triangle. Fast, reliable rubble removal for all project sizes.">
<meta name="keywords" content="skip hire Vaal Triangle, waste removal, skip bin rental, rubble removal, Vaal Skip Hire">
```

**Form IDs:** Use `skip-name`, `skip-phone`, `skip-email` instead of `tree-`

**JavaScript data values:**
```javascript
service: 'Skip Hire',
source: 'Vaal Skip Hire Page',
btn.textContent = 'Request Service';  // Instead of 'Get Free Quote'
```

---

## ✅ Checklist After Fixing

For each page, verify:
- [ ] Meta tags added in `<head>`
- [ ] Skip link appears (press Tab on page load)
- [ ] Focus indicators visible (Tab through form)
- [ ] Form labels properly associated (click label focuses input)
- [ ] Privacy checkbox present
- [ ] Honeypot field hidden
- [ ] Submit button says correct text
- [ ] Modal opens on submit
- [ ] ESC key closes modal
- [ ] Click outside modal closes it

---

## Testing Your Fixes

1. Open the page in browser
2. Press Tab - you should see a yellow "Skip to main content" link
3. Tab through the form - yellow outlines should appear
4. Try submitting without filling - validation should work
5. Fill form and submit - modal should appear
6. Press ESC - modal should close
7. Submit again within 60 seconds - should get rate limit message

---

## If You Get Stuck

The handyman-service.html file is now a perfect template. You can:
1. Open handyman-service.html
2. Copy the structure
3. Replace business-specific content
4. Save as the other filename

That's the easiest way!