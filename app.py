import os
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # للسماح بالتواصل مع الـ Frontend/الموبايل

# 1. المسار الرئيسي (اختبار تشغيل السيرفر)
@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "status": "online",
        "message": "Gamer Streak API is running successfully!",
        "service": "PSN Tracker 24/7"
    }), 200

# 2. مسار فحص الحالة (Health Check)
@app.route('/api/status', methods=['GET'])
def get_status():
    return jsonify({
        "status": "active",
        "database": "connected",
        "psn_service": "ready"
    }), 200

# 3. مسار جلب بيانات الـ PSN والـ Streak
@app.route('/api/streak', methods=['GET'])
def get_streak():
    # هنا تقدر تضيف المنطق الخاص بك لجلب البيانات من Firestore / PSNAWP
    return jsonify({
        "user": "youssef",
        "online": True,
        "current_streak": 5,
        "last_seen": "Recently active"
    }), 200

if __name__ == '__main__':
    # الحصول على المنفذ تلقائياً من Railway
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
