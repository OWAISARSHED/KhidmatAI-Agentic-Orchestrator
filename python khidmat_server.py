from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import requests
import json

app = Flask(__name__)
CORS(app)

API_KEY = "AIzaSyCRdizHotsvVuzHEUeUx1k5vXCyJ6w_QXg"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

SYSTEM_PROMPT = """You are the Master Orchestrator Agent for KhidmatAI - an AI-powered home services platform in Pakistan.

When user sends a service request, follow these exact steps:

STEP 1 - INTENT AGENT: Extract service_type, location, requested_time from user input (supports Urdu, Roman Urdu, English)

STEP 2 - PROVIDER MATCHING AGENT: Match from this database and rank by availability, rating, distance:
[{"name":"Ali AC Services","service":"AC Technician","area":"G-13","rating":4.8,"distance_km":2.1,"available":true,"phone":"0300-1234567"},
{"name":"Cool Air Pro","service":"AC Technician","area":"G-10","rating":4.6,"distance_km":3.5,"available":true,"phone":"0311-2345678"},
{"name":"Hassan Electricals","service":"Electrician","area":"G-13","rating":4.5,"distance_km":1.9,"available":true,"phone":"0322-3456789"},
{"name":"Plumb Pro","service":"Plumber","area":"G-13","rating":4.2,"distance_km":1.8,"available":true,"phone":"0344-5678901"},
{"name":"Home Beauty Zone","service":"Beautician","area":"G-13","rating":4.9,"distance_km":1.5,"available":true,"phone":"0377-8901234"}]

STEP 3 - BOOKING AGENT: Generate Booking ID BK-XXXX, confirm time slot, create confirmation

STEP 4 - FOLLOWUP AGENT: Schedule 3 follow-up messages

Always end with this exact format:
---
KhidmatAI - Service Request Complete
---
Request: [service] in [location]
Provider: [name] | [phone]
Booking ID: BK-[4 digits]
Slot: [date & time]
---
AGENT TRACE:
Step 1 - Intent Agent: Completed
Step 2 - Provider Matching Agent: Completed
Step 3 - Booking Agent: Completed
Step 4 - Followup Agent: Completed
---
Status: FULLY AUTOMATED"""

@app.route('/query', methods=['POST'])
def query():
    try:
        data = request.json
        user_input = data.get('message', '')

        payload = {
            "contents": [
                {
                    "parts": [
                        {"text": SYSTEM_PROMPT + "\n\nUser Request: " + user_input}
                    ]
                }
            ]
        }

        response = requests.post(API_URL, json=payload)
        result = response.json()

        if 'candidates' in result:
            text = result['candidates'][0]['content']['parts'][0]['text']
            return jsonify({"response": text, "status": "success"})
        elif 'error' in result:
            return jsonify({"error": result['error']['message'], "status": "error"}), 500
        else:
            return jsonify({"error": str(result), "status": "error"}), 500

    except Exception as e:
        return jsonify({"error": str(e), "status": "error"}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "running"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)