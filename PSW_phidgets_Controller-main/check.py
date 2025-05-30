import pyvisa

# Initialize PyVISA with pyvisa-py backend
rm = pyvisa.ResourceManager('@py')  # Use '@py' for pyvisa-py backend
device = None  # Global variable to hold the connected device

def connect_device():
    global device
    try:
        # List all available VISA resources
        available_ports = rm.list_resources()
        serial_ports = [port for port in available_ports if "ASRL" in port]  # Filter serial ports (COM ports)

        if not serial_ports:
            return {"status": "Error", "message": "No COM ports found"}

        # Pick the first available serial port
        device_address = serial_ports[0]
        device = rm.open_resource(device_address)

        # PSW 30-36 default serial settings
        device.baud_rate = 9600
        device.data_bits = 8
        device.parity = pyvisa.constants.Parity.none
        device.stop_bits = pyvisa.constants.StopBits.one
        device.timeout = 2000  # Timeout in ms

        # Query device identity
        response = device.query("*IDN?")
        return {"status": "Connected", "message": f"Connected to {response} on {device_address}"}
    
    except pyvisa.VisaIOError as e:
        return {"status": "Error", "message": f"VISA Communication Error: {str(e)}"}
    
    except Exception as e:
        return {"status": "Error", "message": f"Unknown Error: {str(e)}"}

def disconnect_device():
    global device
    if device:
        try:
            device.close()
            device = None
            return {"status": "Disconnected", "message": "Device disconnected successfully"}
        except pyvisa.VisaIOError as e:
            return {"status": "Error", "message": f"VISA Communication Error: {str(e)}"}
        except Exception as e:
            return {"status": "Error", "message": f"Unknown Error: {str(e)}"}
    return {"status": "Error", "message": "No device connected"}

# For testing standalone
if __name__ == "__main__":
    result = connect_device()
    print(result)
