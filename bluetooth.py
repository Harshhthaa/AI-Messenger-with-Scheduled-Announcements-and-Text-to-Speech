import bluetooth

def connect_to_speaker(device_address, class_name):
    if class_name == "DS A":
        port = 1  # Default port for Bluetooth audio devices

        try:
            socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            socket.connect((device_address, port))
            print(f"Connected to {device_address}")
            
            # Print some content specific to "DS A"
            print("Content for DS A: ...")
            
            return socket
        except Exception as e:
            print(f"Error connecting to {device_address}: {e}")
            return None
    else:
        print(f"Unknown class name: {class_name}")
        return None

# Replace these with the actual Bluetooth addresses of your speakers
speaker1_address = "xx:xx:xx:xx:xx:xx"
speaker2_address = "yy:yy:yy:yy:yy:yy"

class_name_1 = "DS A"
class_name_2 = "DS B"

speaker1_socket = connect_to_speaker(speaker1_address, class_name_1)
speaker2_socket = connect_to_speaker(speaker2_address, class_name_2)
