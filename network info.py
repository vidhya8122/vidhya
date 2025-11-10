import socket, uuid, platform

print("===NETWORK INFO REPORT ===")

print("Hostname:",socket.gethostname())

print("Local IP:",socket.gethostbyname(socket.gethostname()))

print("Platform:",platform.system(),platform.release())

print("MAC Address:",':'.join(['{:02x}'.format((uuid.getnode()>>elements) & 0xff)

               for elements in range(0,8*6,8)][::-1]))
