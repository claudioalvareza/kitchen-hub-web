import re
import sys

def process_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    # REMOVE CARD 3
    card3_pattern = re.compile(r'\s*<!-- Card Ñuñoa 3 -->\s*<div class="kitchen-card reveal".*?</div>\s*</div>', re.DOTALL)
    content = card3_pattern.sub('', content)

    # REMOVE CARD 5
    card5_pattern = re.compile(r'\s*<!-- Card Ñuñoa 5 -->\s*<div class="kitchen-card reveal".*?</div>\s*</div>', re.DOTALL)
    content = card5_pattern.sub('', content)

    # REMOVE MODAL 3
    modal3_pattern = re.compile(r'\s*<!-- Modal: Ñuñoa 3 -->\s*<div id="modal-nunoa-3" class="modal">.*?</div>\s*</div>\s*</div>', re.DOTALL)
    content = modal3_pattern.sub('', content)

    # REMOVE MODAL 5
    modal5_pattern = re.compile(r'\s*<!-- Modal: Ñuñoa 5 -->\s*<div id="modal-nunoa-5" class="modal">.*?</div>\s*</div>\s*</div>', re.DOTALL)
    content = modal5_pattern.sub('', content)

    # UPDATE IMAGES FOR CARDS 1, 2, 4
    # The cards currently use ./assets/modulo_las_condes.jpg twice (one for img src, one for background-image)
    
    # CARD 1
    def replacer_card1(match):
        text = match.group(0)
        return text.replace('./assets/modulo_las_condes.jpg', './assets/modulos/cocina_central_1.jpg')
    content = re.sub(r'<!-- Card Ñuñoa 1 -->\s*<div class="kitchen-card reveal".*?</div>\s*</div>', replacer_card1, content, flags=re.DOTALL)

    # CARD 2
    def replacer_card2(match):
        text = match.group(0)
        return text.replace('./assets/modulo_las_condes.jpg', './assets/modulos/cocina_central_2.jpg')
    content = re.sub(r'<!-- Card Ñuñoa 2 -->\s*<div class="kitchen-card reveal".*?</div>\s*</div>', replacer_card2, content, flags=re.DOTALL)

    # CARD 4
    def replacer_card4(match):
        text = match.group(0)
        return text.replace('./assets/modulo_las_condes.jpg', './assets/modulos/cocina_central_4.png')
    content = re.sub(r'<!-- Card Ñuñoa 4 -->\s*<div class="kitchen-card reveal".*?</div>\s*</div>', replacer_card4, content, flags=re.DOTALL)

    # Replace URL encoding in filenames because they have spaces which is bad practice on web. We should rename them in bash but the browser will URL encode them automatically. Alternatively, let's fix spaces with %20 just in case.
    # Actually, Chrome handles spaces in src/background-image, but just to be totally safe it's better to rename files. We'll rename later or the browser will handle it.

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

process_file("index.html")
print("HTML successfully modified.")
