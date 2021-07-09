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
        #print(self.pos)
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)

'''
    The following is ment for testing the network connection
'''
if __name__ == "__main__":
    n = Network()
    while(True):
        information = n. send('write Face detected 120983209')
        sleep(1)