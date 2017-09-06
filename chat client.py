import socket
s = socket.socket()
host = socket.gethostname()
port = 15000

s.connect((host, port))
print ('Connected to', host)

while True:
    z = input("Enter something for the server: ")
    s.send(z)
    # Halts
    print ('[Waiting for response...]')
    print (s.recv(1024))