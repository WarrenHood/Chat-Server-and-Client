#!/usr/bin/python3
import socket
import sys
import threading


#Set the max number of clients in the chatroom
MAX_CLIENTS = 10



def help():
	print('''~TCP CHAT SERVER~

		usage: tcp_chat_server.py ip [port]''')
	sys.exit(0)



if len(sys.argv) < 2:
	help()
elif len(sys.argv) == 3:
	port = int(sys.argv[2])
	ip = sys.argv[1]
elif len(sys.argv) == 2:
	ip = sys.argv[1]
	port = 12345
else:
	print("Too many arguments")
	help()


clients = []
listener = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listener.bind((ip,port))
listener.listen(MAX_CLIENTS)


def send_to_all(msg):
	global listener
	global clients
	try:
		for c in clients:
			c.send(msg)
	except:
		pass


def recv_from_client(client):
	while 1:
		msg = client.recv(4096)
		if len(msg):
			print(msg.decode())
			send_to_all(msg)


while 1:
	client, addr = listener.accept()
	clients.append(client)
	print("Got new connection on",addr)
	client.send("You have successfuly connected to the chat server!".encode())
	threading.Thread(target=recv_from_client,args=(client,)).start()

