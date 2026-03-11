import json

kitchens = [
    { "id": 1, "floor": "1er piso", "area": "14.70", "status": "Disponible", "uf": "35.28", "uf_m2": "2.40", "clp": "$1,401,614", "delay": "200ms" },
    { "id": 2, "floor": "1er piso", "area": "15.30", "status": "Disponible", "uf": "36.72", "uf_m2": "2.40", "clp": "$1,458,822", "delay": "300ms" },
    { "id": 3, "floor": "2do piso", "area": "24.36", "status": "Ocupada", "uf": "58.46", "uf_m2": "2.40", "clp": "$2,322,674", "delay": "400ms" },
    { "id": 4, "floor": "2do piso", "area": "14.00", "status": "Disponible", "uf": "32.20", "uf_m2": "2.30", "clp": "$1,279,251", "delay": "500ms" },
    { "id": 5, "floor": "2do piso", "area": "27.50", "status": "Reservada", "uf": "60.50", "uf_m2": "2.20", "clp": "$2,403,561", "delay": "600ms" }
]

def get_status_color(status):
    if status == "Disponible": return ("#10B981", "rgba(16, 185, 129, 0.1)", "rgba(16, 185, 129, 0.2)", "check-circle")
    if status == "Ocupada": return ("#E30613", "rgba(227, 6, 19, 0.1)", "rgba(227, 6, 19, 0.2)", "x-circle")
    if status == "Reservada": return ("#F59E0B", "rgba(245, 158, 11, 0.1)", "rgba(245, 158, 11, 0.2)", "clock")
    return ("#ffffff", "rgba(255, 255, 255, 0.1)", "rgba(255, 255, 255, 0.2)", "circle")

cards_html = []
for k in kitchens:
    color, bg, border, icon = get_status_color(k["status"])
    html = f"""
                <!-- Card Ñuñoa {k['id']} -->
                <div class="kitchen-card reveal" style="transition-delay: {k['delay']};">
                    <img src="./assets/modulo_las_condes.jpg" alt="Cocina Central Ñuñoa - Cocina {k['id']}" class="sr-only" style="display:none;">
                    <div class="kitchen-img" style="background-image: url('./assets/modulo_las_condes.jpg'); background-size: cover; background-position: center;">
                        <div class="badge-location"><i data-lucide="map-pin" style="width: 14px; height: 14px;"></i> Ñuñoa</div>
                    </div>
                    <div class="kitchen-info">
                        <h3>Cocina Central - Cocina {k['id']}</h3>
                        <p style="color: var(--text-secondary); font-size: 0.9375rem; margin-bottom: 16px;">Módulo profesional de alto estándar, ideal para operaciones de delivery.</p>
                        <div class="kitchen-specs" style="margin-bottom: 12px;">
                            <div class="spec-item"><i data-lucide="maximize" style="width: 16px; height: 16px;"></i> {k['area']} m²</div>
                            <div class="spec-item" style="color: {color}; border-color: {border}; background: {bg};">
                                <i data-lucide="{icon}" style="width: 16px; height: 16px; color: {color};"></i> {k['status']}
                            </div>
                        </div>
                        <ul style="margin-bottom: 24px; color: var(--text-secondary); font-size: 0.875rem; display: flex; flex-direction: column; gap: 8px;">
                            <li>• Planta: {k['floor']}</li>
                            <li>• Tipo: Caliente</li>
                        </ul>
                        <button class="btn btn-details" data-modal="modal-nunoa-{k['id']}">Ver detalles</button>
                    </div>
                </div>"""
    cards_html.append(html[1:]) # Strip first newline

cards_str = "\n".join(cards_html)

with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

start_idx = -1
end_idx = -1

for i, line in enumerate(lines):
    if '<!-- Card Ñuñoa 1 -->' in line and start_idx == -1:
        start_idx = i
    if '<!-- Features Section -->' in line:
        # The line right before <!-- Features Section --> is </section>, then </div>, then </div>
        # Find exactly where Card 5 ends.
        pass

# More robust strategy: we replace everything from start_idx up to the line right before the end of the grid.
# Actually, the quickest way is to just read the whole string and use regex, 
# or just find start_idx and end_idx.
for i, line in enumerate(lines):
    if '<!-- Card Ñuñoa 1 -->' in line and start_idx == -1:
        start_idx = i
    if '<!-- Card Ñuñoa 5 -->' in line:
        # Card 5 starts here. It's 18 lines long based on our previous template.
        pass

# Let's use string partitioning
with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

prefix = content.split('<!-- Card Ñuñoa 1 -->')[0]
suffix_split = content.split('<!-- Card Ñuñoa 5 -->')
suffix = suffix_split[1]

# Need to find the end of Card 5. Card 5 ends with </div></div> 
# We can just split by <!-- Features Section --> and reconstruct the end.

parts = content.split('<!-- Card Ñuñoa 1 -->')
first_half = parts[0]

second_half = parts[1]
# We want to remove everything up to the end of <!-- Card Ñuñoa 5 --> 's closing </div>.
import re
# The end of the cards is indicated by "</div>\n            </div>\n        </div>\n    </section>\n\n    <!-- Features Section -->"
end_marker = '            </div>\n        </div>\n    </section>\n\n    <!-- Features Section -->'
final_suffix = end_marker + second_half.split(end_marker)[1]

new_content = first_half + cards_str + "\n" + final_suffix

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_content)
    
print("Successfully replaced cards without pricing.")
