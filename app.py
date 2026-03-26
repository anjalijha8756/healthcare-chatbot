from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
from database import init_db, save_message, save_alert
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'healthcare_secret'
socketio = SocketIO(app, cors_allowed_origins="*")

# Initialize database on startup for production (Render)
init_db()

# Expanded symptom database with synonyms
SYMPTOM_DB = [
    {
        'keywords': ['high bp', 'high blood pressure', 'bp is high', 'hypertension', 'bp is 14', 'bp is 15', 'bp is 16', 'bp is 17', 'bp is 18', 'bp is 19'],
        'severity': 'Moderate', 'medicine': 'Amlodipine (Consult Doctor)', 'action': 'Rest and monitor BP'
    },
    {
        'keywords': ['low bp', 'low blood pressure', 'bp is low', 'bp drop', 'bp is 9', 'bp is 8', 'bp is 7'],
        'severity': 'Moderate', 'medicine': 'Fludrocortisone (Consult Doctor)', 'action': 'Drink fluids, increase salt intake'
    },
    {
        'keywords': ['bp ', 'blood pressure', 'bp is '], 
        'severity': 'Normal', 'medicine': 'Monitor BP, Consult Doctor', 'action': 'Check vitals regularly'
    },
    {
        'keywords': ['fever', 'temperature', 'hot', 'feeling hot', 'feverish'],
        'severity': 'Normal', 'medicine': 'Paracetamol', 'action': 'Rest, keep hydrated'
    },
    {
        'keywords': ['headache', 'head ache', 'migraine', 'head pain', 'head hurts', 'severe headache'],
        'severity': 'Normal', 'medicine': 'Ibuprofen or Aspirin', 'action': 'Rest in a quiet, dark room'
    },
    {
        'keywords': ['body pain', 'body ache', 'muscles hurt', 'joint pain', 'body hurts', 'muscle pain'],
        'severity': 'Normal', 'medicine': 'Acetaminophen', 'action': 'Rest and apply warm compress'
    },
    {
        'keywords': ['cold', 'cough', 'sneezing', 'runny nose', 'sore throat', 'suffering from cold', 'bad cold'],
        'severity': 'Normal', 'medicine': 'Antihistamine or Cough Syrup', 'action': 'Drink warm fluids, rest'
    },
    {
        'keywords': ['stomach ache', 'stomach pain', 'belly pain', 'nausea', 'vomiting', 'stomach hurts', 'stomachache'],
        'severity': 'Normal', 'medicine': 'Antacid or Anti-emetic (Consult Doctor)', 'action': 'Eat light food, stay hydrated'
    },
    {
        'keywords': ['sugar', 'diabetes', 'glucose', 'sugar is high'],
        'severity': 'Moderate', 'medicine': 'Insulin / Metformin (Consult Doctor)', 'action': 'Monitor blood glucose, avoid carbs'
    }
]

def analyze_symptoms(message):
    message_lower = message.lower()
    
    # Check for emergency keywords first
    emergency_keywords = ['chest pain', 'heart attack', 'stroke', 'emergency', 'fainted', "can't breathe", 'passed out', 'not breathing', 'severe chest']
    for keyword in emergency_keywords:
        if keyword in message_lower:
            return {'severity': 'Emergency', 'medicine': 'Emergency Care Needed', 'action': 'Call Ambulance Immediately! SOS Activated!'}
            
    # Check other symptoms
    detected_symptoms = []
    highest_severity = 'Normal'
    suggested_medicine = 'Consult doctor for proper diagnosis'
    suggested_action = 'Rest and observe'
    
    matched_any = False
    
    for item in SYMPTOM_DB:
        for kw in item['keywords']:
            # Use word boundary checks or direct inclusion
            if kw in message_lower:
                matched_any = True
                if item['keywords'][0] not in detected_symptoms:
                    detected_symptoms.append(item['keywords'][0]) # Add the primary name
                
                # Upgrade severity and medicine if necessary
                if item['severity'] == 'Emergency':
                    highest_severity = 'Emergency'
                    suggested_medicine = item['medicine']
                    suggested_action = item['action']
                elif item['severity'] == 'Moderate' and highest_severity != 'Emergency':
                    highest_severity = 'Moderate'
                    suggested_medicine = item['medicine']
                    suggested_action = item['action']
                elif highest_severity == 'Normal' and not matched_any:
                    # Only set it once unless a higher severity overrides it
                    suggested_medicine = item['medicine']
                    suggested_action = item['action']
                break # Only match one keyword per category
                
    if not matched_any:
        return None
        
    return {
        'symptoms': ', '.join(detected_symptoms),
        'severity': highest_severity,
        'medicine': suggested_medicine,
        'action': suggested_action
    }

@app.route('/')
def patient_view():
    return render_template('patient.html')

@app.route('/hospital')
def hospital_view():
    return render_template('hospital.html')

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('patient_message')
def handle_patient_message(data):
    msg = data.get('message', '')
    patient_id = data.get('patient_id', 'Patient-1')
    save_message(patient_id, msg)
    
    analysis = analyze_symptoms(msg)
    
    if analysis:
        # Save alert to DB
        is_sos = analysis['severity'] == 'Emergency'
        save_alert(patient_id, msg, analysis['severity'], analysis['medicine'], is_sos)
        
        response_data = {
            'patient_id': patient_id,
            'message': msg,
            'analysis': analysis,
            'is_sos': is_sos
        }
        
        # Send to hospital chatbot
        emit('hospital_alert', response_data, broadcast=True)
        
        # Reply to patient
        reply_msg = f"Your symptoms have been analyzed. Severity: {analysis['severity']}. Suggested Medicine: {analysis['medicine']}."
        if is_sos:
            reply_msg += " THIS IS AN EMERGENCY. SOS ALERT SENT TO HOSPITAL."
            
        emit('bot_reply', {'message': reply_msg, 'is_sos': is_sos})
    else:
        # Send to hospital as normal chat
        emit('hospital_message', {'patient_id': patient_id, 'message': msg}, broadcast=True)
        emit('bot_reply', {'message': "I have forwarded your message to the hospital staff. They will reply shortly.", 'is_sos': False})

@socketio.on('hospital_reply')
def handle_hospital_reply(data):
    msg = data.get('message', '')
    patient_id = data.get('patient_id', 'Patient-1')
    save_message('Hospital', msg)
    
    # Send reply specifically to patient
    emit('doctor_reply', {'message': msg}, broadcast=True)

@socketio.on('trigger_sos')
def handle_sos(data):
    patient_id = data.get('patient_id', 'Patient-1')
    location = data.get('location', 'Unknown')
    
    save_alert(patient_id, 'MANUAL SOS TRIGGERED', 'Emergency', 'Immediate dispatch and Doctor Alert!', True)
    
    sos_data = {
        'patient_id': patient_id,
        'location': location,
        'message': '🚨 MANUAL SOS BUTTON PRESSED! PATIENT NEEDS IMMEDIATE HELP!',
        'is_sos': True
    }
    emit('hospital_alert', sos_data, broadcast=True)
    emit('bot_reply', {'message': "🚨 SOS Alert Sent! Emergency notification dispatched to the hospital and ambulance simulation started.", 'is_sos': True})

if __name__ == '__main__':
    init_db()
    # Run server
    print("Starting Healthcare Chatbot Server...")
    print("Patient Interface: http://127.0.0.1:5000/")
    print("Hospital Interface: http://127.0.0.1:5000/hospital")
    socketio.run(app, debug=True, port=5000, allow_unsafe_werkzeug=True)
