#!/usr/bin/env python3
"""
Serwer HTTP dla strony Zmiana Klimatu
Otwórz w przeglądarce: http://localhost:8000
"""

from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
import webbrowser
from threading import Timer

# Ustaw katalog roboczy na katalog z main.py
os.chdir(os.path.dirname(os.path.abspath(__file__)))

PORT = 8000
HOST = "localhost"

class MyHTTPRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        """Dodaj nagłówki CORS i cache"""
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

    def log_message(self, format, *args):
        """Zmień format logów"""
        print(f"[{self.log_date_time_string()}] {format % args}")

def open_browser():
    """Otwórz przeglądarkę automatycznie"""
    webbrowser.open(f"http://{HOST}:{PORT}")

def run_server():
    """Uruchom serwer HTTP"""
    server_address = (HOST, PORT)
    httpd = HTTPServer(server_address, MyHTTPRequestHandler)
    
    print("=" * 60)
    print("🌍 Zmiana Klimatu - Serwer uruchomiony")
    print("=" * 60)
    print(f"📍 URL: http://{HOST}:{PORT}")
    print(f"📁 Katalog: {os.getcwd()}")
    print("\n✨ Naciśnij Ctrl+C aby zatrzymać serwer\n")
    
    # Otwórz przeglądarkę po 1 sekundzie
    Timer(1.0, open_browser).start()
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n🛑 Serwer zatrzymany")
        httpd.shutdown()

if __name__ == "__main__":
    run_server()