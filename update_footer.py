import os

# The replacement HTML for the footer
footer_html = """    <!-- Footer -->
    <footer>
        <div class="container">
            <div class="footer-content" style="align-items: flex-start; flex-direction: column; gap: 40px;">
                <div style="display: flex; justify-content: space-between; width: 100%; align-items: flex-start; flex-wrap: wrap; gap: 24px;">
                    <img src="./assets/logo_kitchen_lab.png" alt="Kitchen Hub Logo" class="logo-img" style="height: 100px;">
                    <div class="footer-links" style="margin-top: 24px;">
                        <a href="terminos-y-condiciones.html">Términos y condiciones</a>
                        <a href="politica-de-privacidad.html">Políticas de privacidad</a>
                        <a href="index.html">Página Principal</a>
                        <a href="dark-kitchen-vitacura.html">Cocinas en Vitacura</a>
                        <a href="dark-kitchen-nunoa.html">Cocinas en Ñuñoa</a>
                    </div>
                </div>
                <p style="color: var(--text-secondary); font-size: 0.95rem; line-height: 1.6; max-width: 100%; margin-bottom: 0; font-weight: 400; font-family: var(--font-body);">
                    Kitchen Hub es una plataforma especializada en dark kitchens que conecta operadores de cocinas
                    profesionales con marcas gastronómicas que buscan espacios listos para delivery. Nuestro marketplace
                    permite descubrir cocinas ocultas disponibles, evaluar sus características y encontrar rápidamente una
                    cocina adecuada para lanzar o expandir un negocio gastronómico enfocado en delivery.
                </p>
            </div>
            <div class="footer-bottom">
                &copy; 2026 Kitchen Hub Tech. Todos los derechos reservados.
            </div>
        </div>
    </footer>
"""

files = [
    '/Users/claudio/.gemini/antigravity/scratch/kitchen-hub/index.html',
    '/Users/claudio/.gemini/antigravity/scratch/kitchen-hub/dark-kitchen-vitacura.html',
    '/Users/claudio/.gemini/antigravity/scratch/kitchen-hub/dark-kitchen-nunoa.html'
]

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Find the start and end of the footer
    start_tag = '<!-- Footer -->'
    end_tag = '</footer>'
    
    start_idx = content.find(start_tag)
    end_idx = content.find(end_tag)
    
    if start_idx != -1 and end_idx != -1:
        new_content = content[:start_idx] + footer_html + content[end_idx + len(end_tag) + 1:]
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
    else:
        print(f"Footer not found in {filepath}")
