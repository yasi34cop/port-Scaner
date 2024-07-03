!/bin/python
import socket
from datetime import datetime

def scan_ports(target):
    try:
        # Resolve the target hostname to an IP address
        target_ip = socket.gethostbyname(target)

        # Print the scan start time
        print(f"Scanning target {target_ip} at {datetime.now()}")

        # Scan ports 1 to 65535
        for port in range(1, 65536):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target_ip, port))
            if result == 0:
                print(f"Port {port} is open")
            s.close()

    except socket.gaierror:
        print(f"Hostname could not be resolved. Exiting...")
        return
    except socket.error:
        print(f"Server not responding. Exiting...")
        return

if __name__ == "__main__":
    target = input("Enter the target host to scan: ")
    scan_ports(target)
