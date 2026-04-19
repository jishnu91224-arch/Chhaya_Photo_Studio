import os
import re

files = [
    r'd:\SY\WD\PROJECT\Chhaya_Photo_Studio\frontend\dashboard.html',
    r'd:\SY\WD\PROJECT\Chhaya_Photo_Studio\frontend\contact.html',
    r'd:\SY\WD\PROJECT\Chhaya_Photo_Studio\frontend\pricing.html',
    r'd:\SY\WD\PROJECT\Chhaya_Photo_Studio\frontend\services.html'
]

new_footer = '''
<footer class="w-full py-20 px-8 bg-black border-t border-white/5 relative z-50">
    <div class="flex flex-col md:flex-row justify-between items-start gap-12 max-w-screen-2xl mx-auto">
        <div class="flex flex-col items-start transition-transform hover:-translate-y-1 duration-500">
            <span class="text-2xl font-serif font-bold text-yellow-600 tracking-tight leading-none lowercase">chhaya photo studio</span>
            <span class="text-[0.65rem] font-sans tracking-[0.3em] text-gray-400 uppercase mt-1 pl-1">Capture Your Moments</span>
            <p class="text-stone-500 text-xs tracking-widest uppercase mt-8">© 2024 Chhaya Photo Studio.<br/>All rights reserved.</p>
        </div>
        <div class="flex flex-col md:flex-row gap-12 md:gap-24 text-stone-500 font-sans text-sm tracking-widest leading-relaxed">
            <div class="flex flex-col gap-4">
                <span class="text-yellow-700 font-semibold uppercase mb-2 text-xs">Reach Out</span>
                <a href="mailto:jishnu1106@gmail.com" class="hover:text-yellow-600 transition-colors">jishnu1106@gmail.com</a>
                <a href="tel:9270059959" class="hover:text-yellow-600 transition-colors">+91 9270059959</a>
                <a href="tel:7410576273" class="hover:text-yellow-600 transition-colors">+91 7410576273</a>
            </div>
            <div class="flex flex-col gap-4">
                <span class="text-yellow-700 font-semibold uppercase mb-2 text-xs">Socials</span>
                <a href="https://instagram.com/chhaya_photos" target="_blank" class="hover:text-yellow-600 transition-colors">Insta: chhaya_photos</a>
            </div>
            <div class="flex flex-col gap-4 max-w-xs">
                <span class="text-yellow-700 font-semibold uppercase mb-2 text-xs">Visit Us</span>
                <p class="text-xs">Chhaya Photo Studio, Shop no.1,<br>Sonraj Complex, near Nalanda Hotel,<br>S.T. stand road, Islampur,<br>Maharashtra, India, 415409</p>
            </div>
        </div>
    </div>
</footer>
'''

nav_button_html = '''
<div class="flex items-center gap-3">
<button class="bg-gradient-to-br from-[#bca354] to-[#876600] text-yellow-50 px-8 py-3 rounded-md font-medium shadow-lg shadow-yellow-600/20 active:scale-95 transition-all" data-book-session-trigger="true">
    Book a Session
</button>
</div>
'''

for filepath in files:
    if os.path.exists(filepath):
        print(f"Modifying {filepath}")
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Replace Footer
        content = re.sub(r'<footer.*?</footer>', new_footer, content, flags=re.DOTALL)
        
        # Replace right side of nav
        nav_middle_pattern = r'(<div class="hidden md:flex items-center gap-10">.*?</div>).*?</nav>'
        if re.search(nav_middle_pattern, content, flags=re.DOTALL):
            content = re.sub(nav_middle_pattern, r'\1\n' + nav_button_html + '\n</nav>', content, flags=re.DOTALL)

        # Replace specific contact.html body details
        if 'contact.html' in filepath:
            content = content.replace('+91 87998 30109', '+91 9270059959')
            content = content.replace('@chhayastudio', 'chhaya_photos')
            content = content.replace('WhatsApp', 'Primary Touch')
            # Add secondary
            second_card = '''<div class="bg-surface-container-highest p-6 rounded-lg text-center mt-4 reveal-on-scroll">
<p class="text-xs font-label uppercase tracking-widest text-on-surface-variant mb-2">Secondary Contact</p>
<p class="font-medium">+91 7410576273</p>
</div>'''
            if 'Secondary Contact' not in content:
                content = content.replace('<div class="bg-surface-container-highest p-6 rounded-lg text-center">\n<p class="text-xs font-label uppercase tracking-widest text-on-surface-variant mb-2">Instagram</p>', 
                                          second_card + '\n<div class="bg-surface-container-highest p-6 rounded-lg text-center mt-4 reveal-on-scroll">\n<p class="text-xs font-label uppercase tracking-widest text-on-surface-variant mb-2">Instagram</p>')

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
