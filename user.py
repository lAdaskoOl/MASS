from tkinter import *
import time
import sys

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

        self.counter = 0
        self.x = True

    def close(self):
        self.x = False

    def on_press(self):
        text = self.login.get("1.0", END).replace('\n', '')
        print(text)

    def run(self):
        while self.x:
            self.app.update_idletasks()
            self.app.update()

            time.sleep(0.1)

if __name__ == "__main__":
    user = User()
    user.run()
