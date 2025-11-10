import socket
domain=input("Enter domain name:")
ip=socket.gethostbyname(domain)
print("IP Address of",domain,"is",ip)
