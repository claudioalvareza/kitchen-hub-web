import json

html_content = ""
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

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

modals_html = []
for k in kitchens:
    color, bg, border, icon = get_status_color(k["status"])
    html = f"""
    <!-- Modal: Ñuñoa {k['id']} -->
    <div id="modal-nunoa-{k['id']}" class="modal">
        <div class="modal-content">
            <span class="close-modal">&times;</span>
            <div class="modal-header">
                <h2>Cocina Central Ñuñoa - Cocina {k['id']}</h2>
                <p class="modal-subtitle">Cocina profesional equipada en José Luis Araneda 20, ideal para operación de delivery.</p>
            </div>

            <div class="modal-body">
                <div class="modal-section">
                    <h3><i data-lucide="info"></i> Información general</h3>
                    <div class="info-grid">
                        <div class="info-item">
                            <span class="info-label">Dirección</span>
                            <span class="info-value">José Luis Araneda 20, Ñuñoa</span>
                        </div>
                        <div class="info-item">
                            <span class="info-label">Operador</span>
                            <span class="info-value">Cocina Central</span>
                        </div>
                        <div class="info-item">
                            <span class="info-label">Horario de funcionamiento</span>
                            <span class="info-value">09:00 a 23:00</span>
                        </div>
                        <div class="info-item">
                            <span class="info-label">Estado</span>
                            <span class="badge" style="color: {color}; border-color: {border}; background: {bg};">{k['status']}</span>
                        </div>
                    </div>
                </div>

                <div class="modal-section">
                    <h3><i data-lucide="layout-grid"></i> Características del módulo</h3>
                    <div class="modules-list">
                        <div class="module-card">
                            <h4>Cocina {k['id']}</h4>
                            <div class="module-specs">
                                <span><i data-lucide="layers"></i> {k['floor']}</span>
                                <span><i data-lucide="maximize"></i> Área: {k['area']} m²</span>
                                <span><i data-lucide="flame"></i> Tipo: Caliente</span>
                                <span class="badge" style="color: {color}; border-color: {border}; background: {bg};">Estado: {k['status']}</span>
                            </div>
                        </div>
                    </div>
                    
                    <div style="margin-top: 24px; padding: 20px; background: rgba(0,0,0,0.2); border-radius: 12px; border: 1px solid var(--border-color);">
                        <h4 style="font-size: 1.1rem; color: var(--primary); margin-bottom: 8px;">Valores de Arriendo</h4>
                        <div style="display: flex; flex-direction: column; gap: 8px;">
                            <div style="display: flex; justify-content: space-between;">
                                <span style="color: var(--text-secondary);">Arriendo mensual</span>
                                <span style="font-weight: 600;">{k['uf']} UF</span>
                            </div>
                            <div style="display: flex; justify-content: space-between;">
                                <span style="color: var(--text-secondary);">Valor por m²</span>
                                <span style="font-weight: 600;">{k['uf_m2']} UF/m²</span>
                            </div>
                            <div style="display: flex; justify-content: space-between; border-top: 1px solid rgba(255,255,255,0.05); padding-top: 8px; margin-top: 4px;">
                                <span style="color: var(--text-secondary);">Referencia en Pesos</span>
                                <span style="font-weight: 600; color: #10B981;">{k['clp']} CLP</span>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="modal-section">
                    <h3><i data-lucide="package"></i> Infraestructura y servicios incluidos</h3>
                    <ul class="features-list">
                        <li><i data-lucide="check"></i> Electricidad monofásica y trifásica</li>
                        <li><i data-lucide="check"></i> Sistema de extracción de aire</li>
                        <li><i data-lucide="check"></i> Campana de acero inoxidable</li>
                        <li><i data-lucide="check"></i> Trampa de grasa</li>
                        <li><i data-lucide="check"></i> Lavamanos</li>
                        <li><i data-lucide="check"></i> Lavafondos</li>
                        <li><i data-lucide="check"></i> Punto de red</li>
                        <li><i data-lucide="check"></i> Citofonía</li>
                    </ul>
                </div>

                <div class="modal-grid-2">
                    <div class="modal-section">
                        <h3><i data-lucide="users"></i> Operación</h3>
                        <ul class="features-list">
                            <li><i data-lucide="check"></i> Zona de Check Out</li>
                            <li><i data-lucide="check"></i> Runner</li>
                            <li><i data-lucide="check"></i> Personal dedicado</li>
                        </ul>
                    </div>
                    <div class="modal-section">
                        <h3><i data-lucide="shield-check"></i> Seguridad</h3>
                        <ul class="features-list">
                            <li><i data-lucide="check"></i> Sistema de alarma</li>
                            <li><i data-lucide="check"></i> Cámaras de seguridad</li>
                        </ul>
                    </div>
                </div>

                <div class="modal-section">
                    <h3><i data-lucide="wrench"></i> Mantención</h3>
                    <ul class="features-list">
                        <li><i data-lucide="check"></i> Limpieza de baños</li>
                        <li><i data-lucide="check"></i> Limpieza de zonas comunes</li>
                        <li><i data-lucide="check"></i> Fumigación y control de plagas mensual</li>
                    </ul>
                </div>
            </div>

            <div class="modal-footer">
                <a href="#" class="btn btn-secondary close-modal-btn chat-trigger-btn">Solicitar información</a>
                <a href="#contacto" class="btn btn-primary close-modal-btn">Agendar visita</a>
            </div>
        </div>
    </div>"""
    modals_html.append(html)

cards_str = "\\n".join(cards_html)
modals_str = "\\n".join(modals_html)

# Insert cards before the closing of kitchen-grid
cards_split = '\\n            </div>\\n        </div>\\n    </section>\\n\\n    <!-- Features Section -->'
html_content = html_content.replace(cards_split, '\\n' + cards_str + cards_split)

# Insert modals before <!-- Modal: Publicar Espacio (Brokerage) -->
modals_split = '<!-- Modal: Publicar Espacio (Brokerage) -->'
html_content = html_content.replace(modals_split, modals_str + '\\n    ' + modals_split)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)
print("Successfully generated and included all cards and modals.")
