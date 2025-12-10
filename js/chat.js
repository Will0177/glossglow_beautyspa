// Live Chat Widget Functionality
document.addEventListener('DOMContentLoaded', function() {
    const chatToggle = document.getElementById('chat-toggle');
    const chatWidget = document.getElementById('live-chat-widget');
    const chatClose = document.getElementById('chat-close');
    const chatMessages = document.getElementById('chat-messages');
    const chatInput = document.getElementById('chat-input');
    const chatSend = document.getElementById('chat-send');

    let messageIndex = 0;
    const botMessages = [
        "Hello! 👋 How can we help you today?",
        "Are you interested in our services?",
        "We'll reply in under 2 minutes.",
        "Would you like a free consultation?"
    ];

    // Open/Close chat
    if (chatToggle) {
        chatToggle.addEventListener('click', function() {
            chatWidget.classList.toggle('open');
            if (chatWidget.classList.contains('open') && messageIndex === 0) {
                setTimeout(() => {
                    addBotMessage(botMessages[0]);
                    messageIndex = 1;
                }, 500);
            }
        });
    }

    if (chatClose) {
        chatClose.addEventListener('click', function() {
            chatWidget.classList.remove('open');
        });
    }

    // Send message
    function sendMessage() {
        const message = chatInput.value.trim();
        if (message) {
            addUserMessage(message);
            chatInput.value = '';
            
            // Auto-reply after 1 second
            setTimeout(() => {
                if (messageIndex < botMessages.length) {
                    addBotMessage(botMessages[messageIndex]);
                    messageIndex++;
                } else {
                    addBotMessage("Thank you for your interest! Please fill out our contact form or call us directly for more information.");
                }
            }, 1000);
        }
    }

    if (chatSend) {
        chatSend.addEventListener('click', sendMessage);
    }

    if (chatInput) {
        chatInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                sendMessage();
            }
        });
    }

    function addBotMessage(text) {
        const messageDiv = document.createElement('div');
        messageDiv.className = 'chat-message bot';
        messageDiv.textContent = text;
        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    function addUserMessage(text) {
        const messageDiv = document.createElement('div');
        messageDiv.className = 'chat-message user';
        messageDiv.textContent = text;
        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
});

