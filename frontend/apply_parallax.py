import os

html_files = [
    r'd:\SY\WD\PROJECT\Chhaya_Photo_Studio\frontend\dashboard.html',
    r'd:\SY\WD\PROJECT\Chhaya_Photo_Studio\frontend\contact.html',
    r'd:\SY\WD\PROJECT\Chhaya_Photo_Studio\frontend\pricing.html',
    r'd:\SY\WD\PROJECT\Chhaya_Photo_Studio\frontend\services.html'
]

js_tag = '\n<script src="assets/js/parallax.js"></script>'

for filepath in html_files:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Add JS before </body>
        if 'parallax.js' not in content:
            content = content.replace('</body>', js_tag + '\n</body>')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")
