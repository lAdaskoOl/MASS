import socket
from _thread import *
import pickle
import os

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
    file = open("Log.dat", "a")
    file.write(text+"\n")
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

                if data == 'send':
                    #get image from the folder
                    dir = 'images/'
                    files = os.listdir(dir)

                    #read image and send it
                    f = open(dir+files[0], 'rb')
                    l = f.read(1024)
                    while (l):
                        print('Sending...')
                        conn.send(l)
                        l = f.read(1024)
                    f.close()
                    conn.close()

                print("-------------------------")
                #print("Number of devices: ", info["number"])
                print("Received: ", data)
                print("Sending : ", reply)

                #conn.sendall(pickle.dumps(info))
                conn.sendall(pickle.dumps(reply))
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