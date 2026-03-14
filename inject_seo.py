import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

default_descriptions = {
    'terminos-y-condiciones.html': 'Lee los términos y condiciones de uso de la plataforma Kitchen Hub y sus servicios de arriendo de cocinas para delivery.',
    'politica-de-privacidad.html': 'Conoce la política de privacidad de Kitchen Hub, donde explicamos cómo cuidamos y utilizamos tu información.',
    'publica-tu-cocina.html': '¿Tienes una dark kitchen disponible? Publica tu espacio comercial o cocina equipada en Kitchen Hub y conéctala con marcas gastronómicas de forma rápida.'
}

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Inject missing meta description
    if filename in default_descriptions and '<meta name="description"' not in content:
        desc = default_descriptions[filename]
        title_match = re.search(r'(<title>.*?</title>)', content, re.IGNORECASE | re.DOTALL)
        if title_match:
            meta_tag = f'\n    <meta name="description"\n        content="{desc}">'
            content = content[:title_match.end()] + meta_tag + content[title_match.end():]

    # 2. Extract title and desc for OG tags
    title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
    page_title = title_match.group(1).strip() if title_match else "Kitchen Hub"
    
    desc_match = re.search(r'<meta name="description"\s+content="([^"]*)"', content, re.IGNORECASE | re.DOTALL)
    if not desc_match:
        desc_match = re.search(r'<meta content="([^"]*)"\s+name="description"', content, re.IGNORECASE | re.DOTALL)
        
    page_desc = desc_match.group(1).strip() if desc_match else ""

    page_url = f"https://kitchenhub.cl/{filename}" if filename != 'index.html' else "https://kitchenhub.cl/"
    # For publica-tu-cocina, use a different hero if exists, otherwise normal hero
    og_image = "https://kitchenhub.cl/assets/hero.jpg"

    # 3. Inject OG tags
    if 'property="og:title"' not in content:
        og_tags = f'''
    <!-- Open Graph / Facebook / LinkedIn / WhatsApp -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="{page_url}">
    <meta property="og:title" content="{page_title}">
    <meta property="og:description" content="{page_desc}">
    <meta property="og:image" content="{og_image}">
    <meta property="og:site_name" content="Kitchen Hub">
'''
        head_end = content.find('</head>')
        if head_end != -1:
            content = content[:head_end] + og_tags + content[head_end:]
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {filename} with OG tags and descriptions.")

