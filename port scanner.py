import socket

target=input("Enter IP address:")

port=int(input("Enter port number:"))

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

result=sock.connect_ex((target,port))

if result == 0:

    print(f" port{port}is OPEN on {target}")

else:

    print(f" port {port} is CLOSED on {target}")

sock.close()
