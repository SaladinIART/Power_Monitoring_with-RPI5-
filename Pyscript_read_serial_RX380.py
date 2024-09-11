import serial
import time

def read_mikro_rx380(port='/dev/ttyUSB0', baudrate=9600):
    ser = serial.Serial(port, baudrate, timeout=1)
    
    try:
        while True:
            # Send command to request data (replace with actual command)
            ser.write(b'GET_DATA\r\n')
            
            # Read response
            response = ser.readline().decode('utf-8').strip()
            
            if response:
                print(f"Received data: {response}")
                # Process and return the data as needed
                return response
            
            time.sleep(1)  # Adjust the polling interval as needed
    
    finally:
        ser.close()

if __name__ == "__main__":
    read_mikro_rx380()