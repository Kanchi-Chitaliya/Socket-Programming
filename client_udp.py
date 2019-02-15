from socket import *
import os
import sys
class Client():
    def __init__(self,serverName,serverPort):
        self.serverName = serverName
        self.serverPort = serverPort
        self.clientSocket = socket(AF_INET, SOCK_DGRAM)
        self.clientSocket.bind(('',15098))
        
    def create_socket(self):
        x= input("Please enter the command. The options presented to the users are:\n 1. put <file name>\n 2. list \n 3. get <file name>\n 4. rename <old_name> <new_name>\n 5. exit \n")
        self.clientSocket.sendto(x.encode(),(self.serverName,self.serverPort))
        x=x.split(" ")

        if x[0]=="put":
            self.put(x)
        elif x[0]=="list":
            self.create_list()
        elif x[0]=="get":
            self.get(x)
        elif x[0]=="Exit":
            self.exit()

    def put(self,x):
        if os.path.isfile(x[1]):
            
            k=os.path.getsize(x[1])
            y=str(k)
            self.clientSocket.sendto(y.encode(),(self.serverName,self.serverPort))
            i=0
            file1=open(x[1],"rb")
            while i<=k:
                msg=file1.read(buffer)
                self.clientSocket.sendto(msg,(self.serverName,self.serverPort))
                j,serverAddress=self.clientSocket.recvfrom(buffer)
                j=j.decode()
                while j=="NACK":
                    self.clientSocket.sendto(msg,(self.serverName,self.serverPort))
                    j,serverAddress=self.clientSocket.recvfrom(buffer)
                    j=j.decode()
                i=i+len(msg)
               
            file1.close()
        else:
            print("the file does not exist in the directory")
    def create_list(self):
        lt,serverAddress=self.clientSocket.recvfrom(buffer)
        lt=lt.decode()
        a=lt.split(" ")
        for items in a:
            print(items)
    
    def get(self,x):
        size,serverAddress=self.clientSocket.recvfrom(buffer)
        i=0
        data=open("Received_"+x[1],"wb")
        while i<=int(size):
            message,serverAddress= self.clientSocket.recvfrom(buffer)
            if len(message)>0:
                self.clientSocket.sendto("ACK".encode(),(self.serverName,self.serverPort))
                data.write(message)
                i=i+len(message)
            else:
                self.clientSocket.sendto("NACK".encode(),(self.serverName,self.serverPort))
        data.close()
    def change_name(self):
        message,serverAddress= self.clientSocket.recvfrom(buffer)
        message=message.decode()
        print(message)
    
            
    def exit(self):
        quit()
        
if __name__=='__main__':
    while(1):
        g=sys.argv[1]
        h=int(sys.argv[2])
        if h<5000:
            print("Invalid port Number")
            
        buffer=1024
        client=Client(g,h)
        client.create_socket()
        