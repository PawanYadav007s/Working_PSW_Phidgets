import serial
import serial.tools.list_ports
import time
import threading
import requests

# 🔍 Find Arduino Port using VID/PID or Description
def find_arduino_port():
    arduino_vids = ["2341", "1A86", "10C4"]  # Add more VIDs if needed
    ports = serial.tools.list_ports.comports()

    print("Checking available ports...")
    for port in ports:
        vid = format(port.vid, "04X") if port.vid else ""
        pid = format(port.pid, "04X") if port.pid else ""
        desc = port.description.lower()

        print(f"Checking port: {port.device} | VID: {vid} | PID: {pid} | Desc: {desc}")

        if vid in arduino_vids or "arduino" in desc or "ch340" in desc:
            print(f"[INFO] Arduino detected on {port.device}")
            return port.device

    print("[ERROR] Arduino not found.")
    return None

# 🔄 Listen to Arduino for button press command
def listen_for_start_signal(flask_url="http://127.0.0.1:5000/start_loop"):
    port = find_arduino_port()
    if not port:
        print("[ERROR] No Arduino found.")
        return

    try:
        ser = serial.Serial(port, 9600, timeout=1)
        print(f"[READY] Listening on {port}...")

        while True:
            line = ser.readline().decode().strip()
            if line:
                print(f"[RECEIVED] {line}")
                if line.lower() == "start":
                    print("[ACTION] Sending POST to /start_loop")
                    try:
                        response = requests.post(flask_url)
                        print(f"[RESPONSE] {response.status_code} - {response.text}")
                    except Exception as e:
                        print(f"[ERROR] Failed to send POST: {e}")
            time.sleep(0.1)

    except serial.SerialException as e:
        print(f"[ERROR] Could not open serial port: {e}")

# 🧵 Start in background (if needed)
def run_in_thread():
    thread = threading.Thread(target=listen_for_start_signal)
    thread.daemon = True
    thread.start()
    print("[INFO] Background listener started.")

if __name__ == "__main__":
    run_in_thread()

    # Keep the main program running to listen for the Arduino signal
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("[INFO] Program interrupted by user.")
