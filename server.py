import socket
from _thread import *
import pickle

server = "Your IP address"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

def threaded_client(conn, device):
    conn.send(pickle.dumps('hi'))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            data = pickle.loads(data)

            if not data:
                print("Disconnected")
                break
            else:
                reply = 'Data received'
                print("-------------------------")
                print("Device number: ", device)
                print("Received: ", data)
                print("Sending : ", reply)

                conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    conn.close()

connected_devices = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    connected_devices += 1
    start_new_thread(threaded_client, (conn, connected_devices))