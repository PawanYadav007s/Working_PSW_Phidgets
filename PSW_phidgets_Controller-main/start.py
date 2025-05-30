import webview
import time
import threading
import app  # This runs your Flask app in the background

def run_flask():
    app.app.run(port=5001, threaded=True)

if __name__ == "__main__":
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()
    time.sleep(1)  # Optional: wait a moment to let Flask start
    webview.create_window("Mahindra PSW Controller", "http://localhost:5001", width=1200, height=800)
    webview.start()
