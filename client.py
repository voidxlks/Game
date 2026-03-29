import socket
import threading

HOST = "127.0.0.1"  # Change to your server IP later
PORT = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((HOST, PORT))
    print("Connected to server!")
except:
    print("Could not connect to server.")
    exit()

# Listen for messages from server
def receive():
    while True:
        try:
            message = client.recv(1024).decode("utf-8")
            if message:
                print(f"[SERVER]: {message}")
        except:
            print("Disconnected from server.")
            client.close()
            break

# Send messages to server
def send():
    while True:
        msg = input("")
        try:
            client.send(msg.encode("utf-8"))
        except:
            break

# Run both threads
receive_thread = threading.Thread(target=receive)
receive_thread.start()

send_thread = threading.Thread(target=send)
send_thread.start()
