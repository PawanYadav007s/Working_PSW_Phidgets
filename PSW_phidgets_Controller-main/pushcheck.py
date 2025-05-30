import pyvisa
import time

# Initialize PyVISA with pyvisa-py backend
rm = pyvisa.ResourceManager('@py')
device = None  # Global variable for PSW device

def connect_device():
    global device
    try:
        available_ports = rm.list_resources()
        serial_ports = [port for port in available_ports if "ASRL" in port]

        if not serial_ports:
            return {"status": "Error", "message": "No COM ports found"}

        device_address = serial_ports[0]
        device = rm.open_resource(device_address)

        # Configure serial settings for PSW 30-36
        device.baud_rate = 9600
        device.data_bits = 8
        device.parity = pyvisa.constants.Parity.none
        device.stop_bits = pyvisa.constants.StopBits.one
        device.timeout = 2000

        # Test communication
        response = device.query("*IDN?")
        print(f"[CONNECTED] {response.strip()} on {device_address}")
        return {"status": "Connected", "message": f"{response.strip()}"}

    except pyvisa.VisaIOError as e:
        return {"status": "Error", "message": f"VISA Error: {e}"}
    except Exception as e:
        return {"status": "Error", "message": f"Unknown Error: {e}"}

def disconnect_device():
    global device
    if device:
        try:
            device.close()
            device = None
            print("[DISCONNECTED] Device disconnected.")
        except Exception as e:
            print(f"[ERROR] Failed to disconnect: {e}")
    else:
        print("[WARNING] No device to disconnect.")

def monitor_output_status():
    global device
    if not device:
        print("Device not connected.")
        return

    print("\n[INFO] Monitoring PSW output status... (press Ctrl+C to stop)")
    previous_state = None

    try:
        while True:
            try:
                state = device.query("OUTP?").strip()  # "1" for ON, "0" for OFF
                if state != previous_state:
                    print(f"[STATUS CHANGE] Output is {'ON' if state == '1' else 'OFF'}")
                    previous_state = state
            except Exception as e:
                print(f"[ERROR] Failed to query output status: {e}")
            time.sleep(1)  # Check every second

    except KeyboardInterrupt:
        print("\n[EXIT] Monitoring stopped by user.")

# Run test
if __name__ == "__main__":
    result = connect_device()
    if result["status"] == "Connected":
        monitor_output_status()
        disconnect_device()
    else:
        print(f"[ERROR] {result['message']}")
