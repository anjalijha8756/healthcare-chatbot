# Project Report

**Project Title**: Bot-to-Bot Healthcare Communication System
**Domain**: Artificial Intelligence & Web Technologies
**Technology Stack**: Python, Flask, WebSockets, HTML, CSS, JavaScript, SQLite

## Abstract
In critical healthcare scenarios, communication delays between a patient and the hospital can lead to severe consequences. This project proposes a real-time, bot-to-bot communication system where a Patient Chatbot gathers initial symptoms and immediately transmits them to a Hospital Dashboard. An integrated symptom-analysis algorithm classifies the severity of the condition and suggests preliminary remedies. Additionally, an SOS feature ensures immediate simulated medical dispatch for critical emergencies.

## 1. Introduction
With the growing need for remote healthcare, intelligent monitoring systems are highly relevant. This project bridges the gap by providing a seamless, real-time communication pipeline between a patient at home and hospital staff. The system is designed to be beginner-friendly, operating entirely locally without the need for paid external APIs.

## 2. Objectives
1. Build a real-time bot-to-bot messaging system.
2. Implement an automated symptom analyzer to classify health conditions (Normal, Moderate, Emergency).
3. Provide an intuitive Dashboard for hospital staff to monitor patients.
4. Integrate a manual SOS alert button for immediate attention.

## 3. Methodology
- **Frontend**: Developed using standard HTML5 and CSS3 for a responsive and clean User Interface. JavaScript is used to manage real-time DOM manipulations.
- **Backend**: Uses Python with the Flask framework to serve HTTP requests. Socket.IO is heavily utilized to upgrade standard HTTP to WebSockets, ensuring zero-latency data transfer between the Patient UI and the Hospital Dashboard.
- **Database**: SQLite is used for lightweight, file-based data storage, effectively logging all patient communications and alerts.

## 4. Key Features
- **Real-Time Data Transmission**: Instant message delivery using WebSockets.
- **Auto-Triage**: The server automatically analyzes the English text of symptoms, checking for keywords like "heart attack" or "fever", and categorizes them.
- **Visual & Audio Alerts**: The hospital dashboard blinks red and plays an audio alarm if an Emergency condition or SOS is triggered.

## 5. Implementation details
### 5.1 Symptom Dataset
The project utilizes a hard-coded dictionary mapping symptoms to treatments:
- *Fever* -> Paracetamol (Normal)
- *High Blood Pressure* -> Amlodipine (Moderate)
- *Chest Pain* -> Emergency Care Needed (Emergency)

### 5.2 Bot-to-Bot Mechanism
When the patient sends a message, the JavaScript client emits a Socket.IO event to the Server. The Server performs the NLP keyword analysis, saves the result to the database, and re-emits a targeted event specifically to all connected Hospital clients. 

## 6. Future Improvements
1. **Machine Learning**: Replace the keyword-based dictionary with a trained NLP model (like BERT or standard Naive Bayes) for highly accurate symptom classification.
2. **Authentication**: Add Login systems for Doctors and Patients to secure the data.
3. **GPS Tracking**: Integrate real HTML5 Geolocation API to send exact coordinates when the SOS button is pressed.
4. **Mobile App**: Port the Patient Web App into a React Native or Flutter mobile application.

## 7. Conclusion
The Bot-to-Bot Healthcare Communication system successfully demonstrates how simple technologies like Python, WebSockets, and Vanilla Web Stack can be combined to build a powerful, life-saving prototype. The real-time triage feature proves highly effective in monitoring remote patients and prioritizing critical care.
