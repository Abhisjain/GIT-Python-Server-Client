#!/usr/bin/env python
import sys
import socket
import time
import threading
from threading import Thread
import tkinter as tk
from tkinter import ttk
import queue
import Credentialsmatch as cm
# from SocketServer import ThreadingMixIn

class ServerThread(Thread):
    def __init__(self, socket):
        Thread.__init__(self)
        self.socket = socket

    def run(self):
        print("send")

        while True:
            #starttime = time.time()
            #command = input(" Enter command: ")
            command=q.get()
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


TCP_IP = '54.152.237.120'  # sys.argv[1]
TCP_PORT = 5002  # int(sys.argv[2])
TCP_PORT2 = 50000
BUFFER_SIZE = 1024
threads = []
q = queue.Queue()
global log
log = 0
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect((TCP_IP, TCP_PORT))
TIME_OUT = s.recv(BUFFER_SIZE)  # Server exchanges tmeout details with client at the start of every socket
count = [1, 2, 3]
status = 0
class clientchatwindows():

    def code(self,usernamein):
        self.deleteofflineuser=usernamein
        print("runfunction")
        self.clientwin = tk.Tk()
        self.clientwin.title("Chat")

        # self.clientwin.mainloop()
        # chatwindowgui = windows()
        print("self.clientwin")

        print("afterchatreeive")

        chatreceive = tk.StringVar()
        print("aftertkstringintvar")
        ttk.Label(self.clientwin, text="Chat").grid(column=0, row=0)
        self.chatreceive = ttk.Entry(self.clientwin, width=20, textvariable=chatreceive)
        self.chatreceive.grid(column=0, row=2)
        sendchat = ttk.Button(self.clientwin, text="Send", command=self.gettext)  # button calls the sendchat function
        sendchat.grid(column=1, row=2)
        self.clientwin.protocol('WM_DELETE_WINDOW', self.closesecond)

        # -----------------------------------------------------------------------------
        # scroll bar code that is going to display

        loginscroll = tk.Scrollbar(self.clientwin)
        self.listbox = tk.Listbox(self.clientwin)
        self.listbox.grid(column=0, row=1)
        # function that adds users who are online
        getonlineusers=cm.matchcredentials()
        v=getonlineusers.getonlineusers()  # function return list of users who are online
        for i in v:
            print(i[0])
            self.listbox.insert(tk.END, i)
        self.listbox.config(yscrollcommand=loginscroll.set)
        loginscroll.config(command=self.listbox.yview)
        sendto=tk.StringVar()

        self.sendtowindow=ttk.Entry(self.clientwin, textvariable=sendto) # entry widget getting the name to send chat to
        self.sendtowindow.grid(column=2, row=1)

        # ----------------------------------------------------------------------

        sendto = ttk.Button(self.clientwin, text="-->>", command=self.get)
        sendto.grid(column=1, row=1)
        #   print "New thread started for write"
        print("mainloop")
        self.clientwin.mainloop()
        self.clientwin.protocol('WM_DELETE_WINDOW', self.closesecond)
    def closesecond(self):

        CLOSEWINDOW=cm.matchcredentials()
        CLOSEWINDOW.deleteofflineusers(self.deleteofflineuser)     # self.deleteofflineuser is passed in this class when stating this client gui thread
        self.clientwin.destroy()
        self.clientwin.quit()
    def get(self):
        printlistbox = self.listbox.get('active')
        self.sendtowindow.insert(0,printlistbox)
        print(printlistbox)
    def gettext(self):
        gettextchatreceive=self.chatreceive.get()
        getsendtowindow=self.sendtowindow.get()

        q.put(gettextchatreceive)  # putting data in queue to send data to the threading sending to server
        #print(gettextchatreceive)
    def _quit(self):
        self.clientwin.quit()
        self.clientwin.destroy()
        exit()


class clientcode():                                         # t
    def clientcodemain(self,usernamein,passwordin):    #username and password received from Login after the credentials matched by credentialsmatch
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
                    newmethod = clientchatwindows()
                    t = Thread(target=newmethod.code(username))
                    t.start()
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
