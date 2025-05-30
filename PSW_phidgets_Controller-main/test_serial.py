import serial
import time
import serial.tools.list_ports

def find_arduino_port():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        if 'Arduino' in port.description or 'CH340' in port.description or 'CP210x' in port.description:
            return port.device
    return None

def main():
    arduino_port = find_arduino_port()
    if arduino_port:
        print(f"Found Arduino on port: {arduino_port}")
        try:
            ser = serial.Serial(arduino_port, 9600, timeout=1)
            print("Connected to Arduino. Waiting for button presses...")
            while True:
                if ser.in_waiting > 0:
                    line = ser.readline().decode('utf-8').strip().lower()
                    if line == "start":
                        print("Start button pressed (received 'start' from Arduino)")
                    elif line == "stop":
                        print("Stop button pressed (received 'stop' from Arduino)")
                time.sleep(0.1)
        except serial.SerialException as e:
            print(f"Error communicating with Arduino: {e}")
        finally:
            if 'ser' in locals() and ser.is_open:
                ser.close()
                print("Serial port closed.")
    else:
        print("Could not find Arduino port.")

if __name__ == "__main__":
    main()




