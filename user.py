from tkinter import *
import time
from network import Network

class User():
    def __init__(self):
        self.master = Tk()
        self.master.geometry("300x400")
        self.master.protocol("WM_DELETE_WINDOW", self.close)
        self.app = Canvas(self.master)

        label = Label(bg="orange")
        label.place(x=0, y=0, width=300, height=400)

        self.login = Text()
        self.login.place(x=0, y=0, width=100, height=25)

        self.password = Text()
        self.password.place(x=0, y=45, width=100, height=25)

        self.button1 = Button(text="Connect", command=self.on_press)
        self.button1.place(x=0, y=90, width=100, height=50)

        self.n = Network()
        self.counter = 0
        self.x = True

    def close(self):
        self.x = False

    def on_press(self):
        login = self.login.get("1.0", END).replace('\n', '')
        password = self.password.get("1.0", END).replace('\n', '')
        if password == "Admin" and login == "Admin":
            self.counter += 1

    def run(self):
        while self.x:
            self.app.update_idletasks()
            self.app.update()
            if not(self.counter % 2 == 0):
                data = self.n.send("data")
                #print(data)
            time.sleep(0.1)

if __name__ == "__main__":
    user = User()
    user.run()
