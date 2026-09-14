from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # السماح للواجهة بالاتصال بالسيرفر بدون حظر CORS

@app.route('/')
def home():
    return jsonify({"status": "Gamer Streak Server is Running 24/7!"})

@app.route('/api/streak', methods=['GET'])
def get_streak():
    # هنا كود جلب البيانات من Firestore و PSN الخاص بمشروعك
    # استبدل البيانات دي بالبيانات الحقيقية التي تجلبها من الداتابيز
    return jsonify({
        "current_streak": 0,
        "online": False
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
