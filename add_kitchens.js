const fs = require('fs');

const htmlContent = fs.readFileSync('index.html', 'utf8');

const kitchens = [
    {
        id: 1, floor: '1er piso', area: '14.70', status: 'Disponible',
        uf: '35.28', uf_m2: '2.40', clp: '$1,401,614', delay: '200ms'
    },
    {
        id: 2, floor: '1er piso', area: '15.30', status: 'Disponible',
        uf: '36.72', uf_m2: '2.40', clp: '$1,458,822', delay: '300ms'
    },
    {
        id: 3, floor: '2do piso', area: '24.36', status: 'Ocupada',
        uf: '58.46', uf_m2: '2.40', clp: '$2,322,674', delay: '400ms'
    },
    {
        id: 4, floor: '2do piso', area: '14.00', status: 'Disponible',
        uf: '32.20', uf_m2: '2.30', clp: '$1,279,251', delay: '500ms'
    },
    {
        id: 5, floor: '2do piso', area: '27.50', status: 'Reservada',
        uf: '60.50', uf_m2: '2.20', clp: '$2,403,561', delay: '600ms'
    }
];

const getStatusColor = (status) => {
    if (status === 'Disponible') return { color: '#10B981', bg: 'rgba(16, 185, 129, 0.1)', border: 'rgba(16, 185, 129, 0.2)', icon: 'check-circle' };
    if (status === 'Ocupada') return { color: '#E30613', bg: 'rgba(227, 6, 19, 0.1)', border: 'rgba(227, 6, 19, 0.2)', icon: 'x-circle' };
    if (status === 'Reservada') return { color: '#F59E0B', bg: 'rgba(245, 158, 11, 0.1)', border: 'rgba(245, 158, 11, 0.2)', icon: 'clock' };
};

const cardsHTML = kitchens.map(k => {
    const s = getStatusColor(k.status);
    return `
                <!-- Card Ñuñoa ${k.id} -->
                <div class="kitchen-card reveal" style="transition-delay: ${k.delay};">
                    <img src="https://images.unsplash.com/photo-1581622558667-3419a8dc5f83?q=80&w=800&auto=format&fit=crop" alt="Cocina Central Ñuñoa - Cocina ${k.id}" class="sr-only" style="display:none;">
                    <div class="kitchen-img" style="background-image: url('https://images.unsplash.com/photo-1581622558667-3419a8dc5f83?q=80&w=800&auto=format&fit=crop'); background-size: cover; background-position: center;">
                        <div class="badge-location"><i data-lucide="map-pin" style="width: 14px; height: 14px;"></i> Ñuñoa</div>
                    </div>
                    <div class="kitchen-info">
                        <h3>Cocina Central - Cocina ${k.id}</h3>
                        <p style="color: var(--text-secondary); font-size: 0.9375rem; margin-bottom: 16px;">Planta: ${k.floor} • Tipo: Caliente</p>
                        <div class="kitchen-specs" style="margin-bottom: 12px;">
                            <div class="spec-item"><i data-lucide="maximize" style="width: 16px; height: 16px;"></i> ${k.area} m²</div>
                            <div class="spec-item" style="color: ${s.color}; border-color: ${s.border}; background: ${s.bg};">
                                <i data-lucide="${s.icon}" style="width: 16px; height: 16px; color: ${s.color};"></i> ${k.status}
                            </div>
                        </div>
                        <div style="margin-bottom: 24px;">
                            <div style="font-size: 1.1rem; font-weight: 600; color: var(--primary);">${k.uf} UF <span style="font-size: 0.8rem; font-weight: 400; color: var(--text-secondary);">/ mes</span></div>
                            <div style="font-size: 0.85rem; color: var(--text-secondary);">Ref: ${k.clp} CLP • ${k.uf_m2} UF/m²</div>
                        </div>
                        <button class="btn btn-details" data-modal="modal-nunoa-${k.id}">Ver detalles</button>
                    </div>
                </div>`;
}).join('\\n');

const modalsHTML = kitchens.map(k => {
    const s = getStatusColor(k.status);
    return `
    <!-- Modal: Ñuñoa ${k.id} -->
    <div id="modal-nunoa-${k.id}" class="modal">
        <div class="modal-content">
            <span class="close-modal">&times;</span>
            <div class="modal-header">
                <h2>Cocina Central Ñuñoa - Cocina ${k.id}</h2>
                <p class="modal-subtitle">Cocina profesional equipada, ideal para operación de delivery.</p>
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
                            <span class="badge" style="color: ${s.color}; border-color: ${s.border}; background: ${s.bg};">${k.status}</span>
                        </div>
                    </div>
                </div>

                <div class="modal-section">
                    <h3><i data-lucide="layout-grid"></i> Características del módulo</h3>
                    <div class="modules-list">
                        <div class="module-card">
                            <h4>Cocina ${k.id}</h4>
                            <div class="module-specs">
                                <span><i data-lucide="layers"></i> ${k.floor}</span>
                                <span><i data-lucide="maximize"></i> Área: ${k.area} m²</span>
                                <span><i data-lucide="flame"></i> Tipo: Caliente</span>
                                <span class="badge" style="color: ${s.color}; border-color: ${s.border}; background: ${s.bg};">Estado: ${k.status}</span>
                            </div>
                        </div>
                    </div>
                    
                    <div style="margin-top: 24px; padding: 20px; background: rgba(0,0,0,0.2); border-radius: 12px; border: 1px solid var(--border-color);">
                        <h4 style="font-size: 1.1rem; color: var(--primary); margin-bottom: 8px;">Valores de Arriendo</h4>
                        <div style="display: flex; flex-direction: column; gap: 8px;">
                            <div style="display: flex; justify-content: space-between;">
                                <span style="color: var(--text-secondary);">Arriendo mensual</span>
                                <span style="font-weight: 600;">${k.uf} UF</span>
                            </div>
                            <div style="display: flex; justify-content: space-between;">
                                <span style="color: var(--text-secondary);">Valor por m²</span>
                                <span style="font-weight: 600;">${k.uf_m2} UF/m²</span>
                            </div>
                            <div style="display: flex; justify-content: space-between; border-top: 1px solid rgba(255,255,255,0.05); padding-top: 8px; margin-top: 4px;">
                                <span style="color: var(--text-secondary);">Referencia en Pesos</span>
                                <span style="font-weight: 600; color: #10B981;">${k.clp} CLP</span>
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
    </div>`;
}).join('\\n');

let newHtmlContent = htmlContent;

// Insert cards before the closing of kitchen-grid
const cardsSplit = '\\n            </div>\\n        </div>\\n    </section>\\n\\n    <!-- Features Section -->';
newHtmlContent = newHtmlContent.replace(cardsSplit, '\\n' + cardsHTML + cardsSplit);

// Insert modals before <!-- Modal: Publicar Espacio (Brokerage) -->
const modalsSplit = '<!-- Modal: Publicar Espacio (Brokerage) -->';
newHtmlContent = newHtmlContent.replace(modalsSplit, modalsHTML + '\\n    ' + modalsSplit);

fs.writeFileSync('index.html', newHtmlContent);
console.log('Successfully added kitchens to index.html');
