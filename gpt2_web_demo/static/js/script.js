document.addEventListener('DOMContentLoaded', function() {
    const morphChat = document.getElementById('morph-chat');
    const bpeChat = document.getElementById('bpe-chat');
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-button');
    const clearButton = document.getElementById('clear-button');
    const loadingIndicator = document.getElementById('loading');
    
    sendButton.addEventListener('click', sendMessage);
    
    userInput.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });
    
    clearButton.addEventListener('click', function() {
        morphChat.innerHTML = '';
        bpeChat.innerHTML = '';
    });
    
    function sendMessage() {
        const message = userInput.value.trim();
        if (!message) return;
        
        // Add user message to both chats
        addMessage(morphChat, 'user', message);
        addMessage(bpeChat, 'user', message);
        userInput.value = '';
        
        // Show loading indicator
        loadingIndicator.style.display = 'block';
        
        // Send request to server
        fetch('/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ prompt: message })
        })
        .then(response => response.json())
        .then(data => {
            addMessage(morphChat, 'bot', data.morph);
            addMessage(bpeChat, 'bot', data.bpe);
        })
        .catch(error => {
            addMessage(morphChat, 'bot', `Error: ${error.message}`);
            addMessage(bpeChat, 'bot', `Error: ${error.message}`);
        })
        .finally(() => {
            loadingIndicator.style.display = 'none';
            // Scroll both chats to bottom
            morphChat.scrollTop = morphChat.scrollHeight;
            bpeChat.scrollTop = bpeChat.scrollHeight;
        });
    }
    
    function addMessage(container, sender, text) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message');
        
        if (sender === 'user') {
            messageDiv.innerHTML = `
                <div class="user-message">${text}</div>
            `;
        } else {
            messageDiv.innerHTML = `
                <div class="bot-message">${text}</div>
            `;
        }
        
        container.appendChild(messageDiv);
        container.scrollTop = container.scrollHeight;
    }
});