# Project Documentation: Healthcare Chatbot System

## 1. System Architecture overview
The system uses a Client-Server architecture with WebSockets for real-time, bi-directional communication.
- **Clients**: The Patient UI and the Hospital Dashboard.
- **Server**: A Python Flask application running `Flask-SocketIO`.
- **Database**: SQLite database persisting chat history and alert records.

## 2. Components

### A. Patient Chatbot (`templates/patient.html` & `static/patient.js`)
This is the interface for the patient. 
- It maintains an active WebSocket connection to the server.
- The user can type symptoms into a text box or click a dedicated SOS button.
- When an event occurs, it emits `patient_message` or `trigger_sos` over the socket.
- It listens for `bot_reply` and `doctor_reply` to show text back to the patient.

### B. Hospital Dashboard (`templates/hospital.html` & `static/hospital.js`)
This is the interface for doctors and hospital staff.
- Listens for `hospital_alert` and `hospital_message` events from the server.
- Dynamically creates UI "Alert Cards" when a patient sends a message.
- Uses browser notifications and the Web Audio API to play alert sounds during an Emergency/SOS.
- Contains reply boxes to emit `hospital_reply` directly back to specific patients.

### C. Backend Server (`app.py`)
The Python server is the "brain" connecting both bots.
- **Symptom Logic**: Checks incoming messages against a dictionary of keywords ('fever', 'chest pain', etc.). It maps these to severity ('Normal', 'Moderate', 'Emergency') and suggests medicines.
- **Event Routing**: Receives a `patient_message`, analyzes it, saves it to the SQLite `healthcare.db`, and broadcasts a `hospital_alert` to the Hospital Dashboard.
- **Emergency Processing**: If the analysis detects emergency keywords, or if `trigger_sos` is received, it flags `is_sos = True` to trigger the front-end alarm systems.

### D. Database (`database.py`)
- Standard SQLite3 database for zero-config local storage.
- Two tables: `messages` (for all chat logs) and `alerts` (for symptom reports and SOS triggers).
