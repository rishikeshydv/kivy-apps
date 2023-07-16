import socket
import select
import sys
from _thread import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ip = str(sys.argv[1])
port = int(sys.argv[2])
server.bind((ip, port))
server.listen(3000)

clientList = []

def clientthread(conn, addr):

	conn.send("You are successfully connected to the chatroom")

	while True:
        
            userMsg = conn.recv(2048)
            if userMsg:
                
                message_to_send = "<" + addr[0] + "> " + userMsg
                broadcastMsg(message_to_send, conn)

            else:
                removeConnection(conn)

def broadcastMsg(userMsg, connection):
	for clients in clientList:
		if clients!=connection:
			try:
				clients.send(userMsg)
			except:
				clients.close()
				removeConnection(clients)


def removeConnection(connection):
	if connection in clientList:
		clientList.removeConnection(connection)

while True:

	conn, addr = server.accept()
	clientList.append(conn)
	start_new_thread(clientthread,(conn,addr))	

conn.close()
server.close()
