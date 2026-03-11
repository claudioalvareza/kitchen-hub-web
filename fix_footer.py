def fix_html():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. REMOVE REMNANT OF MODAL 3
    # Find start of modal 4
    m4_idx = content.find('<div id="modal-nunoa-4" class="modal">')
    # Find the nearest "</div>\n\n    <div class="modal-section">" before m4_idx that leads to Cocina 3
    
    # Let's find Cocina 3
    c3_idx = content.find('<h4>Cocina 3</h4>')
    if c3_idx != -1 and m4_idx != -1:
        # Before c3_idx, find the start of its floating modal-section
        start_cut = content.rfind('    <div class="modal-section">', 0, c3_idx)
        # We also need to remove the literal `\n` that might be right before it if it exists.
        # But `start_cut` is good enough.
        content = content[:start_cut] + content[m4_idx:]

    # 2. REMOVE REMNANT OF MODAL 5
    # Find the start of the next section after modal 5 remnant. That's the Chat widget.
    chat_idx = content.find('<!-- Kitchen Hub AI Agent Widget -->')
    c5_idx = content.find('<h4>Cocina 5</h4>')
    if c5_idx != -1 and chat_idx != -1:
        start_cut_5 = content.rfind('    <div class="modal-section">', 0, c5_idx)
        content = content[:start_cut_5] + content[chat_idx:]

    # 3. REORDER KITCHEN CARDS
    # We want Ñuñoa cards (1, 2, 4) to be BEFORE Vitacura and Las Condes.
    # So the order should be: Ñuñoa 1, Ñuñoa 2, Ñuñoa 4, Vitacura 1, Las Condes 1.
    
    # Let's extract them.
    # Vitacura: starts at `<!-- Card 1: Vitacura -->` and ends before `<!-- Card 2: Las Condes -->`
    vita_start = content.find('                <!-- Card 1: Vitacura -->')
    las_condes_start = content.find('                <!-- Card 2: Las Condes -->')
    nunoa1_start = content.find('                <!-- Card Ñuñoa 1 -->')
    # Nunoa ends where the grid ends: `            </div>\n        </div>\n    </section>`
    grid_end = content.find('            </div>\n        </div>\n    </section>', nunoa1_start)

    if vita_start != -1 and las_condes_start != -1 and nunoa1_start != -1 and grid_end != -1:
        card_vita = content[vita_start:las_condes_start]
        card_lascondes = content[las_condes_start:nunoa1_start]
        cards_nunoa = content[nunoa1_start:grid_end]
        
        # Reconstruct the grid
        new_grid_content = cards_nunoa + card_vita + card_lascondes
        
        # Replace in content
        content = content[:vita_start] + new_grid_content + content[grid_end:]

    # Fix the literal '\n' bug at line 1076 or so that was caused by JS join('\\n') or similar string replace
    content = content.replace('</div>\\n\n', '</div>\n')

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    fix_html()
    print("Fixed!")
