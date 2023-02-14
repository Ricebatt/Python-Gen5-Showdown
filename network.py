import socket

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = input("Enter your IPv4 (Can be found in your command prompt, type ipconfig): ")
        self.host = socket.gethostname()
        self.moveSelected = -1
        self.port = 5555
        self.teamString1 = ""
        self.teamString2 = ""
        self.addr = (self.server, self.port)
        self.id = self.connect()
        print(self.id)

    def getFirstTeamString(self):
        return self.teamString1

    def getSecondTeamString(self):
        return self.teamString2

    def getMove(self):
        return self.moveSelected

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(4096).decode()
        except:
            pass

    def send(self, data):
        try:
            print(data)
            self.client.send(str.encode(data))
            print("data received back: ")
            sendBack = self.client.recv(4096).decode()
            print(sendBack)
            return sendBack
        except socket.error as e:
            print(e)

'''
n = Network()
print(n.send("hello"))
print(n.send("working"))
'''