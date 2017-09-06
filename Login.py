import tkinter as tk
from tkinter import ttk



import Credentialsmatch as cm
import Client as Client
class login():
    def __init__(self):
        self.win=tk.Tk()
        self.win.title("Employee Portal")
        self.enterusername()
        self.enterpassword()
        self.loginbutton()

# entering username
    def enterusername(self):
        username=tk.StringVar()
        ttk.Label(self.win, text="Username").grid(column=0, row=0)
        self.username=ttk.Entry(self.win, width=20, textvariable=username)
        self.username.grid(column=1, row=0, sticky='W')

#function for password
    def enterpassword(self):
        password= tk.StringVar()
        ttk.Label(self.win, text="Password").grid(column=0, row=1)
        self.password = ttk.Entry(self.win, width=20, textvariable=password)
        self.password.grid(column=1, row=1, sticky='W')


# function that display login button
    def loginbutton(self):
        login=ttk.Button(self.win,text="Login", command=self.loginaction)
        login.grid(column=0, row=3, columnspan=2)

    def closesecond(self):
        self.chat.destroy()
        self.chat.quit()
        self.win.destroy()
        self.win.quit()
    def get(self):
        printlistbox=self.listbox.get('active')
        print(printlistbox)

# function that is caled when login button clicked
    def loginaction(self):
        recvpassword=self.password.get()
        recvusername=self.username.get()

        #function called from another module to match credentials
        x=cm.matchcredentials()

        # 1 returned if credentials match
        getreturn =x.matchingcredentials(recvusername,recvpassword)
        if getreturn:

            chatreceive=tk.StringVar()
            print(":login successfull")
            # the main window is closed
            self.win.state("withdrawn")
            # -----------------------------------------------------------------------------
            #another window opening showing the functions

            self.chat=tk.Toplevel(self.win)
            ttk.Label(self.chat, text="Chat").grid(column=0, row=0)
            chatreceive = ttk.Entry(self.chat, width=20, textvariable=chatreceive)
            chatreceive.grid(column=0, row=2)
            sendchat = ttk.Button(self.chat, text="Send")
            sendchat.grid(column=1, row=2)
            self.chat.protocol('WM_DELETE_WINDOW', self.closesecond)

            # -----------------------------------------------------------------------------
            # scroll bar code that is going to display

            loginscroll = tk.Scrollbar(self.chat)
            self.listbox = tk.Listbox(self.chat)
            self.listbox.grid(column=0,row=1)
            for i in range(100):
                self.listbox.insert(tk.END,i)
            self.listbox.config(yscrollcommand=loginscroll.set)
            loginscroll.config(command=self.listbox.yview)

            # ----------------------------------------------------------------------

            sendto = ttk.Button(self.chat, text="-->>", command=self.get)
            sendto.grid(column=1, row=1)
            client=Client.clientcode()
            client.clientcodemain(recvusername,recvpassword)




#function that quits the tkinter module
    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit()

log=login()
log.win.mainloop()

