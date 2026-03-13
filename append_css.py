import os

css_to_append = """

/* SLIDE 5: Business Model */
.business-model {
    display: flex;
    justify-content: center;
    margin-top: 40px;
}
.business-card {
    background: linear-gradient(145deg, #1A1A1E, #111114);
    border: 1px solid rgba(227, 6, 19, 0.2);
    padding: 60px;
    border-radius: 24px;
    text-align: center;
    max-width: 600px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.5);
}
.business-icon {
    width: 64px; height: 64px;
    background: rgba(227, 6, 19, 0.1);
    color: var(--primary);
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    margin: 0 auto 30px;
}
.business-icon i {
    width: 32px; height: 32px;
}
.business-formula {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 20px;
    margin-bottom: 24px;
}
.business-formula .highlight {
    font-size: 1.5rem;
    font-weight: 700;
    color: white;
}
.business-formula .divider {
    color: var(--primary);
    font-size: 2rem;
    font-weight: 800;
}
.business-card p {
    color: var(--text-secondary);
    font-size: 1.1rem;
    line-height: 1.6;
    margin-bottom: 30px;
}
.commission-box {
    background: rgba(227, 6, 19, 0.1);
    border: 1px dashed rgba(227, 6, 19, 0.3);
    padding: 20px;
    border-radius: 12px;
    display: flex;
    flex-direction: column;
    gap: 8px;
}
.commission-box strong {
    font-size: 1.4rem;
    color: var(--primary);
}
.commission-box span {
    font-size: 0.9rem;
    color: var(--text-muted);
}

/* SLIDE 6: AI Agent */
.split-layout.reverse .split-content {
    order: 2;
}
.split-layout.reverse .split-image {
    order: 1;
}
.benefit-list {
    list-style: none;
    padding: 0; margin: 0;
    display: flex;
    flex-direction: column;
    gap: 16px;
}
.benefit-list li {
    display: flex;
    align-items: flex-start;
    gap: 12px;
    font-size: 1.1rem;
    color: var(--text-secondary);
    line-height: 1.5;
}
.benefit-list i {
    color: var(--primary);
    flex-shrink: 0;
    margin-top: 2px;
}

.chat-container {
    background-image: url('./assets/technology-integrated-everyday-life.jpg');
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 40px;
}
.chat-container::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(10, 10, 12, 0.85); /* Dark overlay */
}
.chat-mockup {
    position: relative;
    z-index: 2;
    width: 100%;
    max-width: 450px;
    background: rgba(20, 20, 25, 0.95);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 16px;
    padding: 30px 20px;
    box-shadow: 0 30px 60px rgba(0,0,0,0.6);
    display: flex;
    flex-direction: column;
    gap: 24px;
}
.chat-message {
    display: flex;
    flex-direction: column;
    max-width: 85%;
}
.chat-message.user {
    align-self: flex-end;
}
.chat-message.user p {
    background: rgba(255, 255, 255, 0.1);
    color: white;
    padding: 14px 18px;
    border-radius: 16px;
    border-bottom-right-radius: 4px;
    font-size: 0.95rem;
    line-height: 1.5;
    margin: 0;
}
.chat-message.ai {
    align-self: flex-start;
    flex-direction: row;
    gap: 12px;
    max-width: 95%;
}
.ai-avatar {
    width: 32px; height: 32px;
    border-radius: 8px;
    background: #000;
    display: flex; align-items: center; justify-content: center;
    flex-shrink: 0;
}
.ai-avatar img { width: 20px; }
.ai-bubble p {
    background: rgba(227, 6, 19, 0.1);
    border: 1px solid rgba(227, 6, 19, 0.2);
    color: white;
    padding: 14px 18px;
    border-radius: 16px;
    border-top-left-radius: 4px;
    font-size: 0.95rem;
    line-height: 1.5;
    margin: 0;
}
.ai-bubble strong { color: var(--primary); }

/* SLIDE 7: Benefits Grid */
.benefits-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 30px;
    margin-top: 60px;
}
.benefit-card {
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid rgba(255, 255, 255, 0.05);
    padding: 40px 30px;
    border-radius: 16px;
    text-align: left;
    transition: all 0.3s ease;
}
.benefit-card:hover {
    background: rgba(255, 255, 255, 0.05);
    border-color: rgba(227, 6, 19, 0.3);
    transform: translateY(-5px);
}
.benefit-card i {
    color: var(--primary);
    width: 36px; height: 36px;
    margin-bottom: 20px;
}
.benefit-card h4 {
    font-size: 1.3rem;
    color: white;
    margin-bottom: 12px;
}
.benefit-card p {
    color: var(--text-muted);
    font-size: 1rem;
    line-height: 1.6;
    margin: 0;
}

/* SLIDE 8: Closing CTA */
.slide-closing {
    background-image: url('./assets/life-style.jpg');
    background-size: cover;
    background-position: center;
}
.slide-closing .video-overlay {
    background: linear-gradient(to top, rgba(10, 10, 12, 1) 0%, rgba(10, 10, 12, 0.8) 100%);
}
.btn-outline:hover {
    background: rgba(255, 255, 255, 0.1);
}

@media (max-width: 992px) {
    .split-layout.reverse .split-content { order: 1; }
    .split-layout.reverse .split-image { order: 2; height: 400px; display: flex; } /* Show AI chat on mobile */
    .benefits-grid { grid-template-columns: 1fr; gap: 20px; margin-top: 30px; }
    .business-formula { flex-direction: column; gap: 10px; }
    .business-formula .divider { display: none; }
    .slide-closing .slide-title { font-size: 2.5rem !important; }
    .cta-buttons { flex-direction: column; }
    .chat-mockup { max-width: 100%; padding: 20px 15px; }
    .pitch-slide { height: auto; min-height: 100vh; padding: 100px 0; }
    .pitch-container { scroll-snap-type: none; overflow-y: auto; }
}
"""

with open('/Users/claudio/.gemini/antigravity/scratch/kitchen-hub/pitch-deck.css', 'a') as f:
    f.write(css_to_append)
