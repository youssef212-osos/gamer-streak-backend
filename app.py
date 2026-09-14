import os
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # تفعيل CORS للربط مع الـ Frontend/PWA بدون حظر

@app.route('/')
def home():
    return jsonify({
        "status": "Gamer Streak Backend is Active & Running!",
        "version": "1.0.0"
    })

@app.route('/api/streak', methods=['GET'])
def get_streak():
    # كود تجريبي لإرجاع بيانات الـ Streak والـ PSN
    # يمكنك ربط الداتابيز (Firestore) أو الـ PSN API هنا مباشرة
    return jsonify({
        "current_streak": 1,
        "online": True,
        "username": "PSN_User",
        "last_updated": "Today"
    })

if __name__ == '__main__':
    # جلب المنفذ تلقائياً من بيئة التشغيل على Railway
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
