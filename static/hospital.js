const socket = io();
const alertsContainer = document.getElementById('alerts-container');

// Audio setup for alert simulation
let audioContext;
function playAlertSound() {
    // Requires user interaction prior to playing sound in some browsers, but works well for demos
    try {
        if (!audioContext) audioContext = new (window.AudioContext || window.webkitAudioContext)();
        if(audioContext.state === 'suspended') { audioContext.resume(); }
        const oscillator = audioContext.createOscillator();
        oscillator.type = 'sine';
        oscillator.frequency.setValueAtTime(800, audioContext.currentTime); // 800 Hz
        oscillator.frequency.exponentialRampToValueAtTime(1200, audioContext.currentTime + 0.1);
        
        const gainNode = audioContext.createGain();
        gainNode.gain.setValueAtTime(0.1, audioContext.currentTime);
        gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.5);
        
        oscillator.connect(gainNode);
        gainNode.connect(audioContext.destination);
        
        oscillator.start();
        oscillator.stop(audioContext.currentTime + 0.5);
    } catch(e) {
        console.log("Audio not supported or played before interaction");
    }
}

function createAlertCard(data) {
    const card = document.createElement('div');
    card.classList.add('alert-card');
    
    let severityClass = 'normal';
    if (data.is_sos || (data.analysis && data.analysis.severity === 'Emergency')) {
        severityClass = 'emergency';
        card.classList.add('emergency');
        playAlertSound();
        if ("Notification" in window && Notification.permission === "granted") {
            new Notification(`🚨 Emergency Alert from ${data.patient_id}`, {
                body: data.message
            });
        }
    } else if (data.analysis && data.analysis.severity === 'Moderate') {
        severityClass = 'moderate';
        card.classList.add('moderate');
    }
    
    const severityText = data.analysis ? data.analysis.severity : (data.is_sos ? 'Emergency' : 'Normal');
    
    let html = `
        <div class="alert-header">
            <span>Patient: ${data.patient_id}</span>
            <span class="badge ${severityClass}">${severityText}</span>
        </div>
        <div class="alert-body">
            <p><span class="strong">Symptoms:</span> ${data.message}</p>
    `;
    
    if (data.analysis) {
        html += `
            <p><span class="strong">Suggested Med:</span> ${data.analysis.medicine}</p>
            <p><span class="strong">Action Plan:</span> ${data.analysis.action}</p>
        `;
    }
    
    if (data.location) {
        html += `<p><span class="strong">Location:</span> ${data.location}</p>`;
    }
    
    html += `
        </div>
        <div class="reply-section">
            <input type="text" id="reply-${data.patient_id}" placeholder="Reply to patient...">
            <button onclick="sendReply('${data.patient_id}')">Send</button>
        </div>
    `;
    
    card.innerHTML = html;
    
    // Insert at top
    alertsContainer.insertBefore(card, alertsContainer.firstChild);
}

window.sendReply = function(patientId) {
    const input = document.getElementById(`reply-${patientId}`);
    const text = input.value.trim();
    if (text) {
        socket.emit('hospital_reply', {
            patient_id: patientId,
            message: text
        });
        input.value = '';
        input.placeholder = 'Message sent...';
        setTimeout(() => { input.placeholder = 'Reply to patient...'; }, 2000);
    }
};

socket.on('hospital_alert', (data) => {
    createAlertCard(data);
});

socket.on('hospital_message', (data) => {
    createAlertCard(data);
});

// Request notification permission on load
document.addEventListener('DOMContentLoaded', () => {
    if ("Notification" in window && Notification.permission !== "denied") {
        Notification.requestPermission();
    }
});
