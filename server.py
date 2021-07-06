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

info = {"number":0}

def read_log():
    file = open("Log.dat", 'r')
    lines = file.readlines()
    return lines

def write_log(text):
    file = open("Log.dat", "w")
    file.write(text)
    file.close()

def threaded_client(conn):
    conn.send(pickle.dumps('hi'))
    info["number"] += 1
    while True:
        try:
            data = conn.recv(2048)
            data = pickle.loads(data)

            if not data:
                print("Disconnected")
                break
            else:
                reply = 'Data received'

                if "write" in data:
                    write_log(data.replace("write ", ''))
                if 'read' in data:
                    reply = read_log()

                print("-------------------------")
                #print("Number of devices: ", info["number"])
                print("Received: ", data)
                print("Sending : ", reply)

                conn.sendall(pickle.dumps(info))
        except:
            break

    print("Lost connection")
    conn.close()
    info["number"] -= 1

connected_devices = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    connected_devices += 1
    start_new_thread(threaded_client, (conn,))