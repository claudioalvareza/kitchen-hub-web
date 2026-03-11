document.addEventListener('DOMContentLoaded', () => {
    // Google Analytics Event Tracking Helper
    const trackEvent = (eventName, eventParams = {}) => {
        if (typeof gtag === 'function') {
            gtag('event', eventName, eventParams);
        }
    };

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Navigation active state
    const sections = document.querySelectorAll('section');
    const navLinks = document.querySelectorAll('.nav-links a:not(.btn)');

    window.addEventListener('scroll', () => {
        let current = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            if (window.scrollY >= (sectionTop - 200)) {
                current = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href').includes(current)) {
                link.classList.add('active');
            }
        });
    });

    // Modal Logic
    const modals = document.querySelectorAll('.modal');
    const modalBtns = document.querySelectorAll('[data-modal]');
    const closeBtns = document.querySelectorAll('.close-modal');
    const closeModalActions = document.querySelectorAll('.close-modal-btn');

    // Open Modal
    modalBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            const modalId = btn.getAttribute('data-modal');
            trackEvent('view_item', { item_category: 'modal', item_id: modalId });
            const modal = document.getElementById(modalId);
            if (modal) {
                modal.style.display = 'block';
                // Small delay to allow display block to apply before adding class for transition
                setTimeout(() => {
                    modal.classList.add('show');
                }, 10);
                document.body.style.overflow = 'hidden'; // Prevent scrolling underneath
            }
        });
    });

    // Close Modal Function
    const closeModal = (modal) => {
        if (modal) {
            modal.classList.remove('show');
            setTimeout(() => {
                modal.style.display = 'none';
                document.body.style.overflow = 'auto'; // Re-enable scrolling
            }, 300); // Matches CSS transition duration
        }
    };

    // Close button (X) click
    closeBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const modal = btn.closest('.modal');
            closeModal(modal);
        });
    });

    // Action buttons inside modal click
    closeModalActions.forEach(btn => {
        btn.addEventListener('click', () => {
            const modal = btn.closest('.modal');
            closeModal(modal);
        });
    });

    // Click outside modal content to close
    window.addEventListener('click', (e) => {
        modals.forEach(modal => {
            if (e.target === modal) {
                closeModal(modal);
            }
        });
    });

    // Reveal animations on scroll
    const reveals = document.querySelectorAll('.reveal');

    const revealOnScroll = () => {
        const windowHeight = window.innerHeight;
        const revealPoint = 100;

        reveals.forEach(reveal => {
            const revealTop = reveal.getBoundingClientRect().top;
            if (revealTop < windowHeight - revealPoint) {
                reveal.classList.add('active');
            }
        });
    };

    window.addEventListener('scroll', revealOnScroll);
    revealOnScroll(); // Trigger on load

    // Sticky Navbar
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // Formspree Integration
    const setupFormspree = (formId) => {
        const form = document.getElementById(formId);
        if (form) {
            form.addEventListener('submit', async (e) => {
                e.preventDefault();
                const btn = form.querySelector('button[type="submit"]') || document.querySelector(`button[type="submit"][form="${formId}"]`);
                let originalText = '';

                if (btn) {
                    originalText = btn.textContent;
                    btn.textContent = 'Enviando...';
                    btn.disabled = true;
                }

                const formData = new FormData(form);

                try {
                    const response = await fetch("https://formspree.io/f/xjgawyjw", {
                        method: "POST",
                        body: formData,
                        headers: {
                            'Accept': 'application/json'
                        }
                    });

                    if (response.ok) {
                        trackEvent('form_submit_success', { form_id: formId });
                        if (btn) {
                            btn.textContent = '¡Mensaje Enviado!';
                            btn.style.background = 'var(--success-color, #10B981)';
                        }
                        form.reset();

                        setTimeout(() => {
                            if (btn) {
                                btn.textContent = originalText;
                                btn.style.background = '';
                                btn.disabled = false;
                            }

                            // Close modal if it's inside one
                            const modal = form.closest('.modal');
                            if (modal) {
                                closeModal(modal);
                            } else {
                                // For the publish form where button is outside the form, try finding the modal another way, or just close the open modal
                                const publishModal = document.getElementById('modal-publish');
                                if (publishModal && publishModal.classList.contains('show')) closeModal(publishModal);
                            }
                        }, 3000);
                    } else {
                        const errorData = await response.json();
                        console.error('Formspree Error payload:', errorData);
                        if (errorData.errors) {
                            console.error('Validation errors:', errorData.errors.map(err => err.message).join(', '));
                        }
                        throw new Error('Formspree returned an error');
                    }
                } catch (error) {
                    console.error("Error submitting form:", error);
                    if (btn) {
                        btn.textContent = 'Error al enviar';
                        btn.style.background = '#e30613';

                        setTimeout(() => {
                            btn.textContent = originalText;
                            btn.style.background = '';
                            btn.disabled = false;
                        }, 3000);
                    }
                }
            });
        }
    };

    setupFormspree('contactForm');
    setupFormspree('publishForm');

    // Custom AI Chat Widget Logic
    const N8N_WEBHOOK_URL = "https://claudioalvareza.app.n8n.cloud/webhook/a9a0d5f2-f15e-42ae-a9b2-3287d3f9ec47/chat";
    const toggleBtn = document.getElementById("kh-chat-toggle");
    const panel = document.getElementById("kh-chat-panel");
    const closeBtn = document.getElementById("kh-chat-close");
    const chatForm = document.getElementById("kh-chat-form");
    const chatInput = document.getElementById("kh-chat-input");
    const messages = document.getElementById("kh-chat-messages");
    const sendBtn = document.getElementById("kh-chat-send");
    const quickActions = document.querySelectorAll(".kh-quick-action");

    let sessionId = localStorage.getItem("kh_session_id");
    if (!sessionId) {
        sessionId = (window.crypto && crypto.randomUUID)
            ? crypto.randomUUID()
            : "kh-" + Date.now() + "-" + Math.random().toString(36).slice(2);
        localStorage.setItem("kh_session_id", sessionId);
    }

    function togglePanel(forceOpen = null) {
        if (!panel) return;
        const shouldOpen = forceOpen !== null ? forceOpen : panel.classList.contains("kh-hidden");
        panel.classList.toggle("kh-hidden", !shouldOpen);
        if (shouldOpen && chatInput) {
            setTimeout(() => chatInput.focus(), 50);
        }
    }

    function normalizeMessage(text) {
        return String(text)
            .replace(/\r\n/g, "\n")
            .replace(/\t/g, " ")
            .replace(/[ ]{2,}/g, " ")
            .replace(/\n{3,}/g, "\n\n")
            .trim();
    }

    function appendMessage(text, sender = "bot", isHtml = false) {
        const wrapper = document.createElement("div");
        wrapper.className = `kh-msg kh-msg-${sender}`;

        const bubble = document.createElement("div");
        bubble.className = "kh-msg-bubble";

        if (isHtml) {
            bubble.innerHTML = text;
        } else {
            bubble.textContent = normalizeMessage(text);
        }

        wrapper.appendChild(bubble);
        messages.appendChild(wrapper);
        messages.scrollTop = messages.scrollHeight;
        return wrapper;
    }

    // Initialize welcome message if empty
    if (messages && messages.children.length === 0) {
        const welcomeMessage = `Hola, soy el asistente virtual de Kitchen Hub. 👨‍🍳\n\nPuedo ayudarte a encontrar una dark kitchen para tu marca.\n\n¿En qué comuna o zona te gustaría operar? 📍`;
        appendMessage(welcomeMessage, "bot");
    }

    function addTyping() {
        const typingNode = appendMessage(
            '<span class="kh-typing"><span></span><span></span><span></span></span>',
            "bot",
            true
        );
        typingNode.dataset.typing = "true";
        return typingNode;
    }

    function removeTyping() {
        const typing = messages.querySelector('[data-typing="true"]');
        if (typing) typing.remove();
    }

    function extractBotText(payload) {
        if (!payload) return "No pude procesar la respuesta.";
        if (typeof payload === "string") return payload;

        // Prioritize specific fields based on webhook structure
        if (payload.clean_response) return payload.clean_response;
        if (payload.response) return payload.response;
        if (payload.output) return payload.output;
        if (payload.message) return payload.message;
        if (payload.reply) return payload.reply;
        if (payload.text) return payload.text;

        if (Array.isArray(payload) && payload.length > 0) {
            return extractBotText(payload[0]);
        }

        if (payload.data) {
            return extractBotText(payload.data);
        }

        return "No pude procesar la respuesta (Formato no reconocido).";
    }

    async function sendMessage(message) {
        appendMessage(message, "user");
        sendBtn.disabled = true;
        chatInput.disabled = true;

        addTyping();

        try {
            const response = await fetch(N8N_WEBHOOK_URL, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    message: message,
                    sessionId: sessionId,
                    source: "kitchenhub-web",
                    timestamp: new Date().toISOString()
                })
            });

            const contentType = response.headers.get("content-type") || "";

            if (!response.ok) {
                throw new Error(`HTTP ${response.status}`);
            }

            let payload;
            if (contentType.includes("application/json")) {
                payload = await response.json();
            } else {
                payload = await response.text();
            }

            removeTyping();
            let botText = extractBotText(payload);

            // Normalize before HTML replacements
            botText = normalizeMessage(botText);

            // Convert markdown bold to HTML
            botText = botText.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');

            appendMessage(botText, "bot", true);
        } catch (error) {
            removeTyping();
            appendMessage(
                "Hubo un problema al conectar con el asistente. Intenta nuevamente en unos segundos.",
                "bot"
            );
            console.error("Kitchen Hub chat error:", error);
        } finally {
            sendBtn.disabled = false;
            chatInput.disabled = false;
            chatInput.focus();
            messages.scrollTop = messages.scrollHeight;
        }
    }

    if (toggleBtn) toggleBtn.addEventListener("click", () => togglePanel());
    if (closeBtn) closeBtn.addEventListener("click", () => togglePanel(false));

    if (chatForm) {
        chatForm.addEventListener("submit", async (e) => {
            e.preventDefault();
            const message = chatInput.value.trim();
            if (!message) return;
            chatInput.value = "";
            await sendMessage(message);
        });
    }

    quickActions.forEach((btn) => {
        btn.addEventListener("click", async () => {
            const message = btn.dataset.message;
            trackEvent('chat_quick_action', { action_text: message });
            await sendMessage(message);
        });
    });

    // Trigger buttons from website
    const chatTriggerBtns = document.querySelectorAll('.chat-trigger-btn');
    chatTriggerBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            trackEvent('chat_open', { source: 'trigger_button' });
            // Close any open modals
            const openModal = btn.closest('.modal');
            if (openModal) {
                closeModal(openModal);
            }
            togglePanel(true);
        });
    });

    // Scroll trigger (below hero section)
    let chatOpenedOnce = false;
    const heroSection = document.querySelector('.hero');
    if (heroSection) {
        window.addEventListener('scroll', () => {
            if (!chatOpenedOnce && window.scrollY > heroSection.offsetHeight) {
                trackEvent('chat_auto_open', { trigger: 'scroll' });
                togglePanel(true);
                chatOpenedOnce = true;
            }
        });
    }
});
