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
                        <p style="color: var(--text-secondary); font-size: 0.9375rem; margin-bottom: 16px;">Planta: {k['floor']} • Tipo: Caliente</p>
                        <div class="kitchen-specs" style="margin-bottom: 12px;">
                            <div class="spec-item"><i data-lucide="maximize" style="width: 16px; height: 16px;"></i> {k['area']} m²</div>
                            <div class="spec-item" style="color: {color}; border-color: {border}; background: {bg};">
                                <i data-lucide="{icon}" style="width: 16px; height: 16px; color: {color};"></i> {k['status']}
                            </div>
                        </div>
                        <div style="margin-bottom: 24px;">
                            <div style="font-size: 1.1rem; font-weight: 600; color: var(--primary);">{k['uf']} UF <span style="font-size: 0.8rem; font-weight: 400; color: var(--text-secondary);">/ mes</span></div>
                            <div style="font-size: 0.85rem; color: var(--text-secondary);">Ref: {k['clp']} CLP • {k['uf_m2']} UF/m²</div>
                        </div>
                        <button class="btn btn-details" data-modal="modal-nunoa-{k['id']}">Ver detalles</button>
                    </div>
                </div>"""
    cards_html.append(html)

cards_str = "\n".join(cards_html)

with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

# find exact line index
import sys
idx = -1
for i, line in enumerate(lines):
    if '<!-- Features Section -->' in line:
        idx = i
        break

if idx == -1:
    print("Could not find section target")
    sys.exit(1)

# walk back to find the closing tags of the grid
# we expect 
# 246:             </div>
# 247:         </div>
# 248:     </section>
# 249: 
# 250:     <!-- Features Section -->
# Since they are on their own lines, we insert cards_str before the </div> that closes kitchen-grid
# So that is at idx - 4

target_idx = idx - 4
print(f"Index to insert: {target_idx}, line content: {lines[target_idx]}")

lines.insert(target_idx, cards_str + "\n")

with open("index.html", "w", encoding="utf-8") as f:
    f.writelines(lines)
    
print("Success")
