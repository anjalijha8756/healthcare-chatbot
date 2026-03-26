const socket = io();

// UI Elements
const chatBox = document.getElementById('chat-box');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');
const sosBtn = document.getElementById('sos-btn');

// Generate a random patient ID for simulation
const patientId = 'PT-' + Math.floor(Math.random() * 10000);

function appendMessage(sender, text, isEmergency=false) {
    const div = document.createElement('div');
    div.classList.add('message');
    
    if (sender === 'user') {
        div.classList.add('user-message');
    } else {
        div.classList.add('bot-message');
        if (isEmergency) {
            div.classList.add('emergency-message');
        }
    }
    
    div.textContent = text;
    chatBox.appendChild(div);
    chatBox.scrollTop = chatBox.scrollHeight;
}

// Send message to server
function sendMessage() {
    const text = userInput.value.trim();
    if (!text) return;
    
    appendMessage('user', text);
    userInput.value = '';
    
    socket.emit('patient_message', {
        patient_id: patientId,
        message: text
    });
}

// Trigger SOS
function triggerSOS() {
    appendMessage('user', '🚨 SOS BUTTON PRESSED!');
    socket.emit('trigger_sos', {
        patient_id: patientId,
        location: 'Lat: 40.7128, Long: -74.0060' // dummy location
    });
}

// Event Listeners
sendBtn.addEventListener('click', sendMessage);
userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') sendMessage();
});
sosBtn.addEventListener('click', triggerSOS);

// Handle Bot Replies
socket.on('bot_reply', (data) => {
    appendMessage('bot', data.message, data.is_sos);
});

// Handle Doctor Reply (manual from dashboard)
socket.on('doctor_reply', (data) => {
    appendMessage('bot', "👨‍⚕️ Doctor says: " + data.message);
});
