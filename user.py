import sys
from tkinter import *
import time
from network import Network

class User():
    def __init__(self):
        self.master = Tk()
        self.master.title("MASS")
        self.master.geometry("230x400")
        self.master.resizable(False, False)
        self.master.protocol("WM_DELETE_WINDOW", self.close)
        self.app = Canvas(self.master)

        label = Label(bg="orange")
        label.place(x=0, y=0, width=300, height=400)

        label_login = Label(text="Login: ", bg="orange")
        label_login.place(x=10, y=10, width=100, height=25)

        password_login = Label(text="Password: ", bg="orange")
        password_login.place(x=10, y=55, width=100, height=25)

        self.login = Text()
        self.login.place(x=110, y=10, width=100, height=25)

        self.password = Text()
        self.password.place(x=110, y=55, width=100, height=25)

        self.button1 = Button(text='Connect', command=self.connect)
        self.button1.place(x=10, y=120, width=100, height=50)

        self.button2 = Button(text='Get image', command=self.image_get)
        self.button2.place(x=120, y=120, width=100, height=50)

        self.info = Label(text="Not connected", bg="grey", fg="red")
        self.info.place(x=10, y=200, width=210, height=180)

        self.n = Network()
        self.counter = 0
        self.x = True
        self.image = False

    def close(self):
        self.x = False

    def image_get(self):
        self.image = True

    def connect(self):
        login = self.login.get("1.0", END).replace('\n', '')
        password = self.password.get("1.0", END).replace('\n', '')
        if password == "Admin" and login == "Admin":
            self.counter += 1

    def disconnect(self):
        self.counter = 0

    def run(self):
        while self.x:
            self.app.update_idletasks()
            self.app.update()
            if self.counter % 2 == 0:
                self.button1['text'] = 'Connect'
                self.info['text'] = "Not connected"
            else:
                self.button1['text'] = 'Disconnect'
                data = self.n.send("data")
                self.info['text'] = data
                #print(data)
                if self.image:
                    self.n.get_image()
                    self.image = False
                    # Connection will be closed after the image s sent,
                    # therefore connection has to be established again
                    self.n = Network()
            time.sleep(0.1)

if __name__ == "__main__":
    user = User()
    user.run()