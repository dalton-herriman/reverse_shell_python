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

try:
    while True:
        command = input("Shell> ")
    
        if command.strip().lower() == "exit":
            conn.sendall(b"exit")
            print("[!] Closing connection.")
            break
    
        conn.sendall(command.encode())
        result = conn.recv(4096).decode()
        print(result)
except (ConnectionResetError, BrokenPipeError):
    print("[!] Connection closed by the remote host.")

finally:
    conn.close()