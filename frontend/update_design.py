import os
import re

dashboard_path = r'd:\SY\WD\PROJECT\Chhaya_Photo_Studio\frontend\dashboard.html'
site_css_path = r'd:\SY\WD\PROJECT\Chhaya_Photo_Studio\frontend\site.css'

# 1. Update dashboard.html
if os.path.exists(dashboard_path):
    with open(dashboard_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove Female, Male, and Kids categories
    pattern = r'<!-- FEMALE MODEL CATEGORIES -->.*?<!-- ECOMMERCE CATEGORIES \(Vertical!\) -->'
    new_content = re.sub(pattern, '<!-- ECOMMERCE CATEGORIES (Vertical!) -->', content, flags=re.DOTALL)
    
    if new_content != content:
        with open(dashboard_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Updated dashboard.html")
    else:
        print("Categories not found or already removed in dashboard.html")

# 2. Update site.css
if os.path.exists(site_css_path):
    with open(site_css_path, 'r', encoding='utf-8') as f:
        css = f.read()
    
    # Update the parallax-frame class
    new_frame_css = '''
.parallax-frame {
    position: absolute;
    /* Primary color from the theme (#bca354) with subtle opacity */
    border-style: solid;
    border-color: rgba(188, 163, 84, 0.7);
    box-shadow: 0 0 20px rgba(188, 163, 84, 0.15), inset 0 0 15px rgba(188, 163, 84, 0.1);
    box-sizing: border-box;
    /* Hardware acceleration for smooth animation */
    will-change: transform, opacity;
    /* Ensure no background fills the frame */
    background: transparent;
}

/* New element type: Solid geometric dots */
.parallax-dot {
    position: absolute;
    background-color: rgba(188, 163, 84, 0.5);
    box-shadow: 0 0 10px rgba(188, 163, 84, 0.3);
    border-radius: 50%;
    will-change: transform, opacity;
}
'''
    # We replace the existing .parallax-frame block
    css = re.sub(r'\.parallax-frame \{.*?\n\}', new_frame_css.strip(), css, flags=re.DOTALL)
    
    with open(site_css_path, 'w', encoding='utf-8') as f:
        f.write(css)
    print("Updated site.css")

