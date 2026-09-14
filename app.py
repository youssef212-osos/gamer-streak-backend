import os
import time
from flask import Flask, jsonify
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)
CORS(app)

# قراءة مفتاح Firebase من بيئة Render
firebase_json = os.environ.get("FIREBASE_KEY_JSON")
if firebase_json:
    import json
    cred_dict = json.loads(firebase_json)
    cred = credentials.Certificate(cred_dict)
    firebase_admin.initialize_app(cred)
else:
    # للعمل المحلي
    key_path = os.path.join(os.path.dirname(__file__), "key.json")
    if os.path.exists(key_path):
        cred = credentials.Certificate(key_path)
        firebase_admin.initialize_app(cred)

db = firestore.client()

@app.route('/')
def home():
    return jsonify({"status": "Gamer Streak Server is Running 24/7! 🔥"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)