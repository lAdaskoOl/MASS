import socket
import pickle
from time import sleep

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "Your IP address"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.pos = self.connect()

    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048))
        except:
            pass

    def send(self, data):
        print(self.pos)
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)

if __name__ == "__main__":
    #a = np.array([[3, 3, 3], [2, 1, 3], [1, 2, 5]])
    #date = datetime.datetime.now()

    #d = [date, a]
    n = Network()
    while(True):
        information = n. send('Hello')
        print(information)
        sleep(1)