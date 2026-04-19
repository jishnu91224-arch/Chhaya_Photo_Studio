import os
import re

html_files = [
    r'd:\SY\WD\PROJECT\Chhaya_Photo_Studio\frontend\dashboard.html',
    r'd:\SY\WD\PROJECT\Chhaya_Photo_Studio\frontend\services.html',
    r'd:\SY\WD\PROJECT\Chhaya_Photo_Studio\frontend\pricing.html',
    r'd:\SY\WD\PROJECT\Chhaya_Photo_Studio\frontend\contact.html'
]

# 1. Contact Page Cleanup
contact_path = r'd:\SY\WD\PROJECT\Chhaya_Photo_Studio\frontend\contact.html'
if os.path.exists(contact_path):
    with open(contact_path, 'r', encoding='utf-8') as f:
        contact_html = f.read()
    
    # Remove "Visit Our Studio" overlay
    overlay_pattern = r'<!-- Custom Map Pin Overlay -->.*?</div>\s*</div>\s*</div>'
    contact_html = re.sub(overlay_pattern, '', contact_html, flags=re.DOTALL)
    
    # Also clean up theme colors in contact
    contact_html = contact_html.replace('text-yellow-600', 'text-[#D4AF37]')
    contact_html = contact_html.replace('text-yellow-700', 'text-[#D4AF37]')
    contact_html = contact_html.replace('border-yellow-700', 'border-[#D4AF37]')
    
    with open(contact_path, 'w', encoding='utf-8') as f:
        f.write(contact_html)
    print("Updated contact.html")

# 2, 4, 5. Dashboard Fixes
dashboard_path = r'd:\SY\WD\PROJECT\Chhaya_Photo_Studio\frontend\dashboard.html'
if os.path.exists(dashboard_path):
    with open(dashboard_path, 'r', encoding='utf-8') as f:
        dash_html = f.read()

    # Theme colors
    dash_html = dash_html.replace('text-yellow-600', 'text-[#D4AF37]')
    dash_html = dash_html.replace('text-yellow-700', 'text-[#D4AF37]')
    dash_html = dash_html.replace('border-yellow-700', 'border-[#D4AF37]')
    dash_html = dash_html.replace('text-stone-400', 'text-white/70')
    dash_html = dash_html.replace('text-stone-600', 'text-white/90')

    # Remove unwanted headline (eCommerce Products Categories)
    headline_pattern = r'<div class="mb-10 p-6 border-l-\[6px\].*?</div>'
    dash_html = re.sub(headline_pattern, '', dash_html, flags=re.DOTALL, count=1)

    # Remove text below images in eCommerce section
    text_below_img_pattern = r'<div class="text-center w-full">\s*<h4[^>]*>.*?</h4>\s*</div>'
    dash_html = re.sub(text_below_img_pattern, '', dash_html)

    # Improve Top Section
    # Add subtle animation and better visual hierarchy
    hero_pattern = r'(<section class="reveal-on-scroll py-24 md:py-32 flex flex-col items-center text-center">)(.*?)(</section>)'
    
    new_hero = r'''\1
    <div class="relative z-10 bg-black/20 backdrop-blur-md p-8 md:p-16 rounded-2xl border border-[#D4AF37]/20 shadow-2xl">
        <span class="font-label text-[#D4AF37] tracking-[0.4em] uppercase text-sm mb-6 block drop-shadow-md">The Art of Preservation</span>
        <h1 class="font-headline text-5xl md:text-7xl text-white max-w-4xl leading-[1.2] mb-8 drop-shadow-lg font-bold">
            Capturing the <span class="italic text-[#D4AF37]">essence</span> of your most cherished chapters.
        </h1>
        <div class="w-16 h-px bg-[#D4AF37] mx-auto mb-8"></div>
        <p class="font-body text-white/90 max-w-2xl text-xl leading-relaxed mx-auto font-light">
            We believe photography is more than a service; it is a curation of heritage. Each session is approached with architectural precision and a storyteller’s heart.
        </p>
    </div>
\3'''
    dash_html = re.sub(hero_pattern, new_hero, dash_html, flags=re.DOTALL)

    with open(dashboard_path, 'w', encoding='utf-8') as f:
        f.write(dash_html)
    print("Updated dashboard.html")

# 6, 7. Services Fixes
services_path = r'd:\SY\WD\PROJECT\Chhaya_Photo_Studio\frontend\services.html'
if os.path.exists(services_path):
    with open(services_path, 'r', encoding='utf-8') as f:
        serv_html = f.read()

    # Theme colors
    serv_html = serv_html.replace('text-yellow-600', 'text-[#D4AF37]')
    serv_html = serv_html.replace('text-yellow-700', 'text-[#D4AF37]')
    serv_html = serv_html.replace('border-yellow-700', 'border-[#D4AF37]')

    # 6. Performance fix for Pricing & Services section
    # Remove 'reveal-on-scroll' from inside the pricing section to prevent heavy recalculations
    pricing_start = serv_html.find('<!-- Pricing & Services Section -->')
    if pricing_start != -1:
        # Just remove all 'reveal-on-scroll' from the file (or specifically pricing area)
        # Actually, let's remove hover transition translate-y and reveal-on-scroll from cards
        serv_html = serv_html.replace('reveal-on-scroll', '') # Remove all scroll reveals to make it lightning fast
        serv_html = serv_html.replace('hover:-translate-y-1 transition-transform duration-300', '')
    
    # 7. Remove "Maternity and Infancy" box
    # Look for the grid card containing "Maternity &amp; Infancy" or "Maternity & Infancy"
    maternity_pattern = r'<!-- Grid Card 3 -->.*?</div>\s*</div>\s*</div>'
    serv_html = re.sub(maternity_pattern, '', serv_html, flags=re.DOTALL)

    # Fix the grid from 12 cols to fit the remaining 2 cards evenly if needed.
    # The grid has:
    # Card 1 (Large): md:col-span-8
    # Card 2 (Vertical): md:col-span-4
    # Card 3 (Maternity): was md:col-span-4
    # Card 4 (Wide): md:col-span-8
    # If Card 3 is removed, Card 4 (span 8) will wrap to the next line. 
    # To fix layout gap, let's change Card 4 to md:col-span-12
    serv_html = serv_html.replace('<!-- Wide Service Card 4 -->\n<div class="md:col-span-8', '<!-- Wide Service Card 4 -->\n<div class="md:col-span-12')

    with open(services_path, 'w', encoding='utf-8') as f:
        f.write(serv_html)
    print("Updated services.html")

# Update pricing.html for theme consistency
pricing_path = r'd:\SY\WD\PROJECT\Chhaya_Photo_Studio\frontend\pricing.html'
if os.path.exists(pricing_path):
    with open(pricing_path, 'r', encoding='utf-8') as f:
        price_html = f.read()
    price_html = price_html.replace('text-yellow-600', 'text-[#D4AF37]')
    price_html = price_html.replace('text-yellow-700', 'text-[#D4AF37]')
    price_html = price_html.replace('border-yellow-700', 'border-[#D4AF37]')
    with open(pricing_path, 'w', encoding='utf-8') as f:
        f.write(price_html)
    print("Updated pricing.html")

print("Fixes applied successfully.")
