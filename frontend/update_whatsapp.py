import os

files = [
    r'd:\SY\WD\PROJECT\Chhaya_Photo_Studio\frontend\dashboard.html',
    r'd:\SY\WD\PROJECT\Chhaya_Photo_Studio\frontend\contact.html',
    r'd:\SY\WD\PROJECT\Chhaya_Photo_Studio\frontend\pricing.html',
    r'd:\SY\WD\PROJECT\Chhaya_Photo_Studio\frontend\portfolio.html',
    r'd:\SY\WD\PROJECT\Chhaya_Photo_Studio\frontend\services.html'
]

for filepath in files:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update the JS constant
        content = content.replace('const WHATSAPP_NUMBER = "918799830109";', 'const WHATSAPP_NUMBER = "919270059959";')

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated WhatsApp in", filepath)
