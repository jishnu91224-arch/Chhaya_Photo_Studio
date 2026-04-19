import os
import re

html_files = [
    r'd:\SY\WD\PROJECT\Chhaya_Photo_Studio\frontend\dashboard.html',
    r'd:\SY\WD\PROJECT\Chhaya_Photo_Studio\frontend\services.html',
    r'd:\SY\WD\PROJECT\Chhaya_Photo_Studio\frontend\pricing.html',
    r'd:\SY\WD\PROJECT\Chhaya_Photo_Studio\frontend\contact.html'
]

site_css_path = r'd:\SY\WD\PROJECT\Chhaya_Photo_Studio\frontend\site.css'
js_path = r'd:\SY\WD\PROJECT\Chhaya_Photo_Studio\frontend\assets\js\parallax.js'

images = [
    "assets/SHRI0750.JPG.jpeg",
    "assets/SHRI0813.JPG.jpeg",
    "assets/SHRI0833.JPG.jpeg",
    "assets/SHRI0915.JPG.jpeg",
    "assets/SHRI8382.JPG.jpeg",
    "assets/SHRI8868.JPG.jpeg",
    "assets/SHRI9240.JPG.jpeg",
    "assets/SHRI9268.JPG.jpeg",
    "assets/SM_P5318.JPG.jpeg",
    "assets/SM_P5378.JPG.jpeg",
    "assets/SM_P9808.JPG.jpeg",
    "assets/SM_P9822.JPG.jpeg",
    "assets/SM_P9832.JPG.jpeg"
]
img_idx = 0

map_iframe = '''
<div class="mt-6 w-full overflow-hidden rounded-lg border border-white/10 shadow-lg" style="height: 250px;">
    <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d30528.857321591873!2d74.24647!3d17.04231!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bc17480a424e4d3%3A0xc63b1fb25b52db77!2sIslampur%2C%20Maharashtra!5e0!3m2!1sen!2sin!4v1713500000000!5m2!1sen!2sin" width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
</div>
'''

for filepath in html_files:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. Global Theme Update
        # Replace hex colors
        content = content.replace('#bca354', '#D4AF37')
        content = content.replace('#a89048', '#B5952F')
        content = content.replace('#876600', '#B5952F')

        # 2. Image Replacement
        def img_repl(match):
            global img_idx
            src_attr = match.group(1)
            # Find the actual src value
            if 'src="' in match.group(0):
                new_img = match.group(0).replace(src_attr, images[img_idx])
            else:
                new_img = match.group(0) # fallback
            img_idx = (img_idx + 1) % len(images)
            
            # Ensure it has object-cover w-full h-full
            if 'class="' in new_img:
                if 'object-cover' not in new_img:
                    new_img = new_img.replace('class="', 'class="object-cover w-full h-full ')
            else:
                new_img = new_img.replace('<img ', '<img class="object-cover w-full h-full" ')
            return new_img

        content = re.sub(r'<img[^>]*src="([^"]+)"[^>]*>', img_repl, content)

        # 3. Add Business Legacy Text (Dashboard only)
        if 'dashboard.html' in filepath:
            legacy_text = '''
            <div class="mt-16 w-full max-w-4xl mx-auto bg-gradient-to-r from-transparent via-[#D4AF37]/20 to-transparent py-6 px-8 border-y border-[#D4AF37]/30 text-center reveal-on-scroll">
                <p class="font-headline text-xl md:text-2xl text-[#D4AF37] italic font-medium tracking-wide drop-shadow-md">
                    "This is the first photography studio in Islampur city with over 80 years of legacy. It is one of the oldest and most trusted shops in the city."
                </p>
            </div>
            '''
            if '80 years of legacy' not in content:
                content = content.replace('</section>', legacy_text + '\n</section>', 1)
            
            # 4. Feature Offer Text Visibility
            feature_offer_pattern = r'(<h3 class="[^"]*text-white[^"]*">)(Featured Offers For You)(</h3>)'
            if 'Featured Offers For You' in content:
                # Wrap it with an overlay and text shadow
                content = re.sub(r'<div class="mb-10 pl-5 border-l-\[6px\] border-\[#D4AF37\]">', 
                                 r'<div class="mb-10 p-6 border-l-[6px] border-[#D4AF37] bg-black/40 backdrop-blur-sm rounded-r-lg shadow-2xl">', content)
                content = content.replace('text-stone-400 mt-3', 'text-[#D4AF37] mt-3 drop-shadow-md')
                content = re.sub(feature_offer_pattern, r'<h3 class="text-4xl md:text-5xl font-headline font-extrabold uppercase tracking-tight text-white drop-shadow-lg">Featured Offers For You</h3>', content)

            # 5. Add "Explore" Button in Pricing Section
            explore_btn = '''<a href="services.html" class="mt-8 inline-block rounded-md bg-gradient-to-br from-[#D4AF37] to-[#B5952F] px-10 py-3 text-base font-bold text-white shadow-xl shadow-[#D4AF37]/25 transition-all hover:scale-105 hover:brightness-110 active:scale-95 text-center uppercase tracking-widest">Explore</a>'''
            if '<a class="font-headline italic text-primary border-b' in content:
                content = re.sub(r'<a class="font-headline italic text-primary border-b.*?>Explore Packages</a>', explore_btn, content)

        # 6. Move Pricing & Services to Top (Services only)
        if 'services.html' in filepath:
            pricing_section_pattern = r'(<!-- Pricing & Services Section -->\s*<section class="reveal-on-scroll mt-32">.*?</section>)'
            match = re.search(pricing_section_pattern, content, flags=re.DOTALL)
            if match and '<!-- Pricing & Services Section -->' in content:
                pricing_html = match.group(1)
                content = content.replace(pricing_html, '')
                # Insert right after <main class="...">
                content = re.sub(r'(<main[^>]*>)', r'\1\n' + pricing_html + '\n<div class="mt-24"></div>\n', content, count=1)

        # 7. Map Integration
        if 'contact.html' in filepath:
            if 'google.com/maps/embed' not in content:
                # Add to contact info area
                content = content.replace('<!-- Contact Information -->', '<!-- Contact Information -->\n' + map_iframe)
        
        if 'google.com/maps/embed' not in content:
             # Add to footer
             content = re.sub(r'(<div class="flex max-w-xs flex-col gap-3">.*?</div>)', r'\1\n' + map_iframe.replace('mt-6', 'mt-4').replace('250px', '150px'), content, flags=re.DOTALL)


        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")

# Also update site.css and parallax.js to #D4AF37
if os.path.exists(site_css_path):
    with open(site_css_path, 'r', encoding='utf-8') as f:
        css = f.read()
    css = css.replace('188, 163, 84', '212, 175, 55') # rgb for #D4AF37
    with open(site_css_path, 'w', encoding='utf-8') as f:
        f.write(css)

print("Updates completed successfully.")
