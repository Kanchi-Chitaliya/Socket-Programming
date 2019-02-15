import socket
import os
import sys
class Server():
    def __init__(self,serverPort):
        self.serverPort = serverPort
        
    def create_socket(self):
        self.serverSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.serverSocket.bind(('', self.serverPort))
        print('The server  is ready')
        
            
    def put(self,s): 
        i=0 
        size,clientAddress=self.serverSocket.recvfrom(buffer)
        file1=open(s[1],"wb")
        size=size.decode()
        
        while i<int(size):
            message,clientAddress = self.serverSocket.recvfrom(buffer)
            if len(message)>0:
                self.serverSocket.sendto("ACK".encode(), clientAddress)
                file1.write(message)
                i=i+len(message)
            else:
                self.serverSocket.sendto("NACK".encode(),clientAddress)
                
        file1.close()
        print("File Written successfully")
    
    def create_list(self,clientAddress):
        f=os.listdir(os.getcwd())
        str=""
        for items in f:
            str=items+" "+str
        print(str)
        self.serverSocket.sendto(str.encode(),clientAddress)       
            
    def get(self,clientAddress,s):
        k=os.path.getsize(s[1])
        x=str(k)
        self.serverSocket.sendto(x.encode(),clientAddress)
        i=0
        file1=open(s[1],"rb")
        while i<=k:
            msg=file1.read(buffer)
            self.serverSocket.sendto(msg,clientAddress)
            j,clientAddress=self.serverSocket.recvfrom(buffer)
            j=j.decode()
            while j=="NACK":
                self.serverSocket.sendto(msg,clientAddress)
                j,clientAddress=self.serverSocket.recvfrom(buffer)
                j=j.decode()
            i=i+len(msg)
        file1.close()

    def change_name(self,clientAddress,s):
        k=os.listdir(os.getcwd())
        os.rename(s[1],s[2])

        if os.path.isfile(s[2]):
            self.serverSocket.sendto("file renamed".encode(),clientAddress)
    def exit(self):
        server.serverSocket.close()
        quit
        
if __name__=='__main__':
    k=int(sys.argv[1])
    if k<5000:
        print("Invalid Port number")
        
    buffer=1024
    server=Server(k)
    server.create_socket()
    s,clientAddress=server.serverSocket.recvfrom(buffer)
    s=s.decode()
    s=s.split(" ")
    if s[0]=="put":
        server.put(s)
    elif s[0]=="list":
        server.create_list(clientAddress)
    elif s[0]=="get":
        server.get(clientAddress,s)
    elif s[0]=="rename":
        server.change_name(clientAddress,s)
    elif s=="exit":
        server.exit() 
        