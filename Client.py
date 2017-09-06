#!/usr/bin/env python
import sys
import socket
import time
import threading
from threading import Thread


# from SocketServer import ThreadingMixIn

class ServerThread(Thread):
    def __init__(self, socket):
        Thread.__init__(self)
        self.socket = socket

        #   print "New thread started for write"

    def run(self):
        print("send")
        while True:
            #starttime = time.time()
            command = input(" Enter command: ")
            self.socket.send(command.encode())
            ack = self.socket.recv(BUFFER_SIZE)
            print(ack.decode())

class ServerThreadread(Thread):
    def __init__(self, socket):
        Thread.__init__(self)
        self.socket = socket

        #  print "New thread started for chat display"

    def run(self):
        s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s2.connect((TCP_IP, TCP_PORT2))
        welcomemsg = s2.recv(BUFFER_SIZE)
        chat = "initial"
        print(welcomemsg.decode())
        while True:
            chat = s2.recv(BUFFER_SIZE)
            print(chat.decode())
            time.sleep(5)


TCP_IP = '127.0.0.1'  # sys.argv[1]
TCP_PORT = 5002  # int(sys.argv[2])
TCP_PORT2 = 50000
BUFFER_SIZE = 1024
threads = []
global log
log = 0
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
TIME_OUT = s.recv(BUFFER_SIZE)  # Server exchanges tmeout details with client at the start of every socket
count = [1, 2, 3]
status = 0
class clientcode():                                         # t
    def clientcodemain(self,usernamein,passwordin):
        #status = 0
        #while status == 0:
            number = 0
            username = usernamein
            #username = input("Enter username: ")
            s.send(username.encode())
            #password = passwordin
            #password = input("Enter password: ")
            #s.send(password.encode())
            #passwordcheck = s.recv(BUFFER_SIZE)
            #passwordcheck=passwordcheck.decode()
            #if (passwordcheck == "invalid password"):
                #status = 0
                #number = number + 1
                #if number == 3:
                    #status = 2
                    #break

                #else:
                    #print(" Invalid password , enter details again ")
                    #continue
            #else:
                #status = 1

        #if ( status == 1 ):
            try:
                    newthread = ServerThread(s)
                    newthread.daemon = True
                    newthread2 = ServerThreadread(s)
                    newthread2.daemon = True
                    newthread.start()
                    newthread2.start()
                    threads.append(newthread)
                    threads.append(newthread2)
                    while True:
                        for t in threads:
                            t.join(600)
                            if not t.isAlive():
                                break
                        break


            except KeyboardInterrupt:
                    command = "logout"
                    s.send(command.encode())
                    sys.exit()
