#!/usr/bin/env python
import socket
import sys
import collections
import time
import queue
import threading
from threading import Thread
added comment

# from SocketServer import ThreadingMixIn

class ClientThread(Thread):
    def __init__(self, socket, ip, port):
        Thread.__init__(self)
        self.socket = socket
        self.ip = ip
        self.port = port
        print("New thread started")

    def run(self):
        status = 0
        #userpresent = 0
        while True:
            self.socket.send(str(TIME_OUT).encode())
            data2 = "successful"
            #while userpresent == 0:
                #num = 0
            userdata = self.socket.recv(2048)
            userdata=userdata.decode()
            print(userdata)

            if not userdata: break

                #if userdata == 'veer' or 'harman':
                        #userpresent = 1
                        #print("i reached here")

            if data2 == "successful":
                self.socket.send(data2.encode())
                #passpresent = 0
                while status == 0:
                    #passdata = self.socket.recv(2048)
                    #if passdata=='veer' or 'harman':
                        #data2 = "successful"
                        #self.socket.send(data2.encode())
                        for p in offlineusers:
                            t = p.partition(" ")
                            if t[0] == userdata:
                                lock.acquire()
                                offlineusers.remove(p)
                                lock.release()
                        lock.acquire()
                        curusers.append(userdata)
                        lock.release()
                        print(userdata + " logged in")
                        status = 1  # 0 for offline , 1 for online , 2 for blocked
                        logtime = time.time()
                        fd = self.socket.fileno()
                        userfd = userdata + " " + str(fd)
                        lock.acquire()
                        userfdmap.append(userfd)
                        lock.release()






                        # print "[+] thread ready for "+ip+":"+str(port)
            while True:
                    self.socket.settimeout(TIME_OUT)
                    command = self.socket.recv(2048).decode()
                    if "send " in command:
                        content = command.partition(" ")
                        contentinner = content[2].partition(" ")
                        sendmsg = userdata + ": " + contentinner[2]

                        receiver = contentinner[0]
                        errorflag = 1

                        for z in userfdmap:
                            zi = z.partition(" ")
                            if zi[0] == receiver:
                                receiverfd = int(zi[2])
                                errorflag = 0
                                lock.acquire()
                                sendqueues[receiverfd].put(sendmsg)
                                lock.release()
                        replymsg = "message sent"
                        self.socket.send(replymsg.encode())

                    else:
                        error = "Invalid command. Please enter a proper one"
                        self.socket.send(error.encode())

        lock.acquire()
        curusers.remove(userdata)
        lock.release()
        offlinedata = userdata + " " + str(logtime)
        lock.acquire()
        offlineusers.append(offlinedata)
        lock.release()
        print(offlinedata, "removed")
        print("logged out")
        sys.exit()


class ClientThreadread(Thread):
    def __init__(self, sock):
        Thread.__init__(self)

        self.sock = sock

        print("New thread for chat relying started")

    def run(self):

        tcpsock2.listen(1)
        (conn2, addr) = tcpsock2.accept()
        welcomemsg = "hi"
        conn2.send(welcomemsg.encode())
        chat = "initial"
        #print("ind here is")
        print(self.sock.fileno())
        while True:
            for p in userfdmap:  # userfdmap contains mapping between usernames and their socket's file despcriptor which we use as index to access their respective queue
                if str(self.sock.fileno()) in p:
                    connectionpresent = 1
                else:
                    connectionpresent = 0  # We will use this to implement other features - no use as of now

            try:
                chat = sendqueues[self.sock.fileno()].get(False)

                print(chat)
                conn2.send(chat.encode())
            except queue.Empty:

                chat = "none"
                time.sleep(2)

            except KeyError:
                pass


lock = threading.Lock()
global command
command = " "

sendqueues = {}
TCP_IP = '127.0.0.1'
TCP_PORT = 5002  # int(sys.argv[1])
TCP_PORT2 = 50000
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response so we can put 20
TIME_OUT = 1800.0  # seconds   - For time_out    Block_time is 60 seconds
BLOCK_TIME = 60.0

curusers = []
offlineusers = []
blockusers = []
userlog = {}
userfdmap = []

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# host = socket.gethostname()
tcpsock.bind(('127.0.0.1', TCP_PORT))

tcpsock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock2.bind(('127.0.0.1', TCP_PORT2))

threads = []

while True:
    tcpsock.listen(6)
    print("Waiting for incoming connections...")
    (conn, (ip, port)) = tcpsock.accept()
    q = queue.Queue()
    lock.acquire()

    sendqueues[conn.fileno()] = q
    lock.release()

    print("new thread with ", conn.fileno())
    newthread = ClientThread(conn, ip, port)
    newthread.daemon = True
    newthread.start()
    newthread2 = ClientThreadread(conn)
    newthread2.daemon = True
    newthread2.start()

    threads.append(newthread)
    threads.append(newthread2)

for t in threads:
    t.join()
    print("eND")
