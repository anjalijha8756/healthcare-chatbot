# Presentation Outline (PPT Content)

## Slide 1: Title Slide
- **Project Title**: Bot-to-Bot Healthcare Communication System
- **Subtitle**: Patient Chatbot, Hospital Dashboard, and SOS Alerting
- **Presented By**: [Your Name/Team Name]

## Slide 2: Problem Statement
- **The Issue**: Delays in patient-to-hospital communication during emergencies can be fatal.
- **The Challenge**: Hospitals need an automated way to triage (sort) remote patients based on the severity of their symptoms immediately.
- **The Solution**: A real-time system where a patient talks to an AI bot, which analyzes symptoms and instantly alerts the hospital dashboard.

## Slide 3: Project Architecture
- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Python, Flask
- **Communication Protocol**: WebSockets (Socket.IO) for real-time speed.
- **Database**: SQLite for storing patient history and alerts.

## Slide 4: Key Features
1. Bot-to-Bot automatic communication.
2. NLP Keyword-based Symptom Detection.
3. Severity Prediction (Normal, Moderate, Emergency).
4. Automated Medicine & Action Suggestion.
5. One-Click SOS Emergency simulation.

## Slide 5: How it Works (Flow Diagram)
1. **Patient Input**: User types "chest pain" or clicks SOS.
2. **Server Processing**: Python backend detects emergency markers.
3. **Hospital Alerting**: Dashboard plays audio alarm and displays RED alert card.
4. **Doctor Reply**: Staff acknowledges alert and sends a message back to the patient bot.

## Slide 6: The AI Symptom Logic
- Explaining the Simple Dataset:
  - *Symptom*: Headache -> *Severity*: Normal -> *Meds*: Ibuprofen
  - *Symptom*: Low BP -> *Severity*: Moderate -> *Meds*: Fludrocortisone
  - *Symptom*: Stroke -> *Severity*: Emergency -> *Action*: Ambulance Dispatch!

## Slide 7: Demonstration (Live Demo)
- Displaying the Patient Chatbot side-by-side with the Hospital Dashboard.
- Showing a "Normal" message flow.
- Showing an "Emergency" flow.
- Pressing the "SOS" button to demonstrate audio alerts.

## Slide 8: Future Scope
- Integration of actual Machine Learning models for symptom accuracy.
- GPS Tracking for ambulance coordination.
- Mobile App development for broader patient access.

## Slide 9: Conclusion
- **Summary**: Real-time Bot-to-Bot architecture simplifies and accelerates emergency response.
- **Impact**: Provides a highly scalable, beginner-friendly layout for the future of remote telemedicine. 

## Slide 10: Q & A
- Thank you!
- Any Questions?
