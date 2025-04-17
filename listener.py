import socket

# create the listener
listener = socket.socket()
# bind it to localhost on port 4444
listener.bind(("0.0.0.0", 4444))
# listen for incoming connections
listener.listen(1)
print("[*] Waiting for connection...")

# accept the connection
conn, addr = listener.accept()
print(f"[*] Connection from {addr} has been established.")

while True:
    command = input("Shell> ")
    
    if command == "exit":
        break
    
    conn.send(command.encode())
    result = conn.recv(4096).decode()
    print(result)

conn.close()