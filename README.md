# Bot-to-Bot Healthcare Communication System

Welcome to the Bot-to-Bot Healthcare Communication System! This is a complete, beginner-friendly system where a Patient Chatbot communicates automatically with a Hospital Chatbot Dashboard.

## 🌟 Project Features
- **Auto-communication**: Patient chatbot directly talks to the Hospital dashboard.
- **Symptom Detection**: AI-based text analysis of patient input.
- **Severity Prediction**: Categorizes symptoms into Normal, Moderate, or Emergency.
- **Medicine Suggestion**: Automatically suggests medication and action plans based on symptoms.
- **SOS Alert System**: A dedicated emergency button that simulates ambulance signaling and alerts the doctor.

---

## 💻 Tech Stack
- Frontend: HTML, CSS, JavaScript
- Backend: Python (Flask, Flask-SocketIO)
- Database: SQLite
- Communication: WebSockets (Socket.IO)

---

## 🚀 How to Run the Project (Step-by-Step)

### Step 1: Install Python
Ensure you have Python installed on your computer. You can download it from [python.org](https://www.python.org/).

### Step 2: Open Terminal / Command Prompt
Navigate to this project folder (`e:/bot/healthcare_chatbot`).

### Step 3: Install Required Libraries
Run the following command to install Flask and SocketIO:
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
Start the backend server by running:
```bash
python app.py
```

### Step 5: Open the Chatbots
Once the server is running, open your web browser. You will need two tabs (or two different devices) to see the communication in action!
1. **Patient Chatbot**: Go to `http://127.0.0.1:5000/`
2. **Hospital Dashboard**: Go to `http://127.0.0.1:5000/hospital`

---

## 🏥 How to Test the System
1. **Normal Chat**: Type "I have a fever" in the Patient bot. Watch it instantly appear on the Hospital Dashboard with the categorization 'Normal'.
2. **Emergency Chat**: Type "I am having chest pain" in the Patient bot. Watch the Hospital Dashboard trigger an emergency red alert!
3. **SOS Button**: Click the 'SOS Emergency' button. Hear the alert sound in the Hospital Dashboard and see the immediate dispatch notification!
4. **Doctor Reply**: In the Hospital Dashboard, type a reply in the input box on any patient's card and click send. See the response appear in the Patient Chatbot.
