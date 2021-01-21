#!/usr/bin/env python3
import socket
import time
from multiprocessing import Process

#define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def main():
    host = "www.google.com"
    #the defualt port of http
    port = 80
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
        #QUESTION 3
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #bind socket to address
        s.bind((HOST, PORT))
        #set to listening mode
        s.listen(1)
        
        #continuously listen for connections
        while True:
            conn, addr = s.accept()
            print("Connected by", addr)
            #recieve data, wait a bit, then send it back
            remote_ip = socket.gethostbyname(host)
            #Get the address and port number of the target server
            target = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            target.connect((host, port))
            p = Process(target=handle_echo, args = (addr,conn,target))
            p.daemon = True
            p.start()
            print("Started process ",p)

            conn.close()


def handle_echo(addr, conn, target):
    full_data = conn.recv(BUFFER_SIZE)
    print("send data  "+ full_data.decode()+" to google")

    target.sendall(full_data)
    target.shutdown(socket.SHUT_WR)
    data = target.recv(BUFFER_SIZE)
    print("sending data "+ data.decode() +" to client")
    conn.send(data)

if __name__ == "__main__":
    main()
