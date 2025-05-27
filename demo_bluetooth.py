'''import pygatt

# Specify the Bluetooth address of the device you want to connect to
device_address = "20:2B:20:D4:4E:1E"

# Create a GATT connection
adapter = pygatt.GATTToolBackend()
adapter.start()
device = adapter.connect(device_address)

# Perform Bluetooth operations
# Example: Read a characteristic
value = device.char_read("0000xxxx-0000-1000-8000-00805f9b34fb")  # Replace with your characteristic UUID

# Print the read value
print(f"Read value: {value}")

# Disconnect from the device
adapter.stop()

import pygatt

Create a GATTToolBackend instance
adapter = pygatt.GATTToolBackend()

adapter = pygatt.BGAPIBackend()


try:
    # Start the adapter
    adapter.start()

    # Discover nearby BLE devices
    devices = adapter.scan()

    # Print the discovered devices
    for device in devices:
        print(f"Device: {device['address']} - {device['name']}")
finally:
    # Stop the adapter when done
    adapter.stop()


import socket

def send_command_to_speaker(command):
    # Implement the logic to send the command to the Bluetooth speaker here
    # This could involve sending specific data or instructions depending on your speaker's requirements
    pass

ser = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

try:
    ser.bind(("20:2B:20:D4:4E:1E", 4))
    ser.listen(1)
    print("Waiting for connection...")

    client, addr = server.accept()
    print(f"Accepted connection from {addr}")

    while True:
        data = client.recv(1024)
        if not data:
            break

        received_command = data.decode('utf-8')
        print(f"Received command: {received_command}")

        # Process the received command and send corresponding instructions to the speaker
        if received_command == "play":
            send_command_to_speaker("play")
        elif received_command == "pause":
            send_command_to_speaker("pause")
        elif received_command == "volume_up":
            send_command_to_speaker("volume_up")
        elif received_command == "volume_down":
            send_command_to_speaker("volume_down")

except Exception as e:
    print(f"Error: {e}")

finally:
    print("Disconnected")
    client.close()
    server.close()'''




import pygatt

def discover_devices(device_name):
    adapter = pygatt.GATTToolBackend()
    adapter.start()

    try:
        devices = adapter.scan()
        for device in devices:
            if device_name in device["name"]:
                return device["address"]
    finally:
        adapter.stop()

def connect_and_play(device_name):
    device_address = discover_devices(device_name)

    if device_address:
        print(f"Connecting to {device_name} at address {device_address}...")
        adapter = pygatt.GATTToolBackend()
        device = adapter.connect(device_address)

        # Your code to interact with the Bluetooth speaker goes here
        # For example, you might send commands to play music or control volume

        device.disconnect()
        print(f"Disconnected from {device_name}.")
    else:
        print(f"Device with name '{device_name}' not found.")

if __name__ == "__main__":
    device_name = "Stone 750"  # Replace with the name of your Bluetooth speaker
    connect_and_play(device_name)





































