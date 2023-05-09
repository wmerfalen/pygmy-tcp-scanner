import socket
import sys

for host in sys.argv[1:]:
    print(host,"scanning")
    for port in range(1,65535):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.550)
            s.connect((host,port))
            s.close()
            print(host,"open",port)
        except ConnectionRefusedError:
            s.close()
        except Exception:
            s.close()
    print(host,"done")

