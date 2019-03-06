import socket
import threading
import sys

def help():
	print('''~Tcp Chat Client~
			usage: tcp_chat.py ip [port]''')

if len(sys.argv) < 2 or len(sys.argv) > 3:
	help()
	sys.exit(0)
elif len(sys.argv) == 2:
	ip = sys.argv[1]
	port = 12345
else:
	ip = sys.argv[1]
	port = int(sys.argv[2])


username = input("Enter your name: ")


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client.connect((ip, port))


def klfnm():
	global client
	while 1:
		msg = client.recv(4096)
		msg = msg.decode()
		if len(msg):
			print(msg)


def keep_sending_msgs():
	global client
	global username
	while 1:
		msg = input()
		client.send((username+": "+msg).encode())


threading.Thread(target=klfnm).start()
threading.Thread(target=keep_sending_msgs).start()
