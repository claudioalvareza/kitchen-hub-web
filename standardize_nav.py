import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# The old dropdown pattern to look for
old_dropdown_regex = r'<div class="dropdown-content">\s*<a href="#cocinas-para-delivery">Ver todas</a>\s*<a href="dark-kitchen-vitacura\.html">Dark Kitchens en Vitacura</a>\s*<a href="dark-kitchen-nunoa\.html">Dark Kitchens en Ñuñoa</a>\s*</div>'

# The new dropdown content
new_dropdown_html = '''<div class="dropdown-content">
                        <a href="dark-kitchen-santiago.html">Dark Kitchens en Santiago</a>
                        <a href="dark-kitchen-vitacura.html">Dark Kitchens en Vitacura</a>
                        <a href="dark-kitchen-nunoa.html">Dark Kitchens en Ñuñoa</a>
                    </div>'''

# We also need to fix dark-kitchen-santiago.html which already has it right mostly, 
# But just to be sure we'll do a more robust replace or just replace all 
# '<div class="dropdown-content">...</div>' blocks entirely.

dropdown_pattern = re.compile(r'<div class="dropdown-content">.*?</div>', re.DOTALL)

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = dropdown_pattern.sub(new_dropdown_html, content)
    
    if new_content != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
        
    # Also standardize the footer links where we have "Ver cocinas en..."
    footer_pattern = re.compile(r'<div class="footer-links" style="margin-top: 24px;">\s*<a href="terminos-y-condiciones\.html">Términos y condiciones</a>\s*<a href="politica-de-privacidad\.html">Políticas de privacidad</a>\s*<a href="index\.html">Página Principal</a>\s*<a href="dark-kitchen-vitacura\.html">Cocinas en Vitacura</a>\s*<a href="dark-kitchen-nunoa\.html">Cocinas en Ñuñoa</a>\s*</div>', re.DOTALL)
    
    new_footer = '''<div class="footer-links" style="margin-top: 24px;">
                        <a href="terminos-y-condiciones.html">Términos y condiciones</a>
                        <a href="politica-de-privacidad.html">Políticas de privacidad</a>
                        <a href="index.html">Página Principal</a>
                        <a href="dark-kitchen-santiago.html">Dark Kitchens en Santiago</a>
                        <a href="dark-kitchen-vitacura.html">Cocinas en Vitacura</a>
                        <a href="dark-kitchen-nunoa.html">Cocinas en Ñuñoa</a>
                    </div>'''
                    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    new_content_footer = footer_pattern.sub(new_footer, content)
    
    if new_content_footer != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content_footer)
        print(f"Updated footer in {filename}")

