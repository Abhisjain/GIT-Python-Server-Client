#!/usr/bin/env python
import socket
import sys
import collections
import time
import queue
import threading
from threading import Thread


# from SocketServer import ThreadingMixIn

class ClientThread(Thread):
    def __init__(self, socket, ip, port):
        Thread.__init__(self)
        self.socket = socket
        self.ip = ip
        self.port = port

    def run(self):
        while True:
            self.socket.send(str(TIME_OUT).encode())
            command=self.socket.recv(2048)


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
                conn2.send(chat)
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
TCP_PORT2 = 5001
BUFFER_SIZE = 20  # Normally 1024, but we want fast response
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
