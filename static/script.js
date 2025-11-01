const chatToggle = document.getElementById('chatToggle');
const chatBox = document.getElementById('chatBox');
const sendBtn = document.getElementById('sendBtn');
const userInput = document.getElementById('userInput');
const chatLog = document.getElementById('chatLog');

chatToggle.onclick = () => {
    chatBox.style.display = chatBox.style.display === 'none' ? 'block' : 'none';
};

sendBtn.onclick = async () => {
    const message = userInput.value.trim();
    if (!message) return;

    addMessage('You', message);
    userInput.value = '';

    const response = await fetch('/chatbot/chat/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message }),
    });

    const data = await response.json();
    addMessage('Bot', data.response);
};

function addMessage(sender, text) {
    const msg = document.createElement('div');
    msg.textContent = `${sender}: ${text}`;
    chatLog.appendChild(msg);
    chatLog.scrollTop = chatLog.scrollHeight;
}
