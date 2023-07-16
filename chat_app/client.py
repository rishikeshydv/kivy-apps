import socket
import select
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = str(sys.argv[1])
port = int(sys.argv[2])
server.connect((ip, port))

while True:

	sockets_list = [sys.stdin, server]
	read, write, error = select.select(sockets_list,[],[])

	for socket in read:
		if socket == server:
			userMsg = socket.recv(2048)
		else:
			userMsg = sys.stdin.readline()
			server.send(userMsg)
			sys.stdout.write("<You>")
			sys.stdout.write(userMsg)
			sys.stdout.flush()
   
server.close()
