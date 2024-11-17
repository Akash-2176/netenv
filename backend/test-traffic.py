import socket

suspicious_ports = [22, 23, 80, 443]

for port in suspicious_ports:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)  # Set timeout to avoid long waits
            result = sock.connect_ex(("localhost", port))
            if result == 0:
                print(f"Connected to port {port}")
            else:
                print(f"Port {port} is closed or unreachable")
    except Exception as e:
        print(f"Failed to connect to port {port}: {e}")
