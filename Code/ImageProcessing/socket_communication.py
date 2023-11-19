import socket

HOST = "192.168.12.84"
PORT = 2222

# str = "p[1.1, 2.2, 3.3, 4.4, 5.5, 6.6]"

def postolist(str):
    str = str.replace("p", "", 1)
    str = str.replace("[", "", 1)
    str = str.replace("]", "", 1)
    print(str)
    lst = str.split(",")
    for i in range(len(lst)):
        lst[i] = float(lst[i])
    return lst

def readPos(Client):
    dataFromClient = Client.recv(1024)
    decoded_data = dataFromClient.decode()
    return postolist(decoded_data)

def sendPos(p, Client):
    dataInput = p
    Client.send(str(dataInput).encode())
    return 0

def sendJoint(p, Client):
    dataInput = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    dataInput[p[0]] = p[1]
    Client.send(str(dataInput).encode())
    return 0

def sendConf(Server):
    # Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket started")
    # Server.bind((HOST, PORT))
    print("Socket bound")
    # Server.listen()
    print("Server listening")
    Client, addr = Server.accept()
    print(f"Socket accepted, client {Client}:{addr} connected")
    dataInput = "1"
    Client.send(str(dataInput).encode())
    return 0

def readAck(Client):
    print("Awaiting ack")
    dataFromClient = Client.recv(1024)
    decoded_data = dataFromClient.decode()
    print("Receved ack")
    return decoded_data