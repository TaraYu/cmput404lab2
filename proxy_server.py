#!/usr/bin/env python3
import socket
import time

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
        s.listen(2)
        
        #continuously listen for connections
        while True:
            conn, addr = s.accept()
            print("Connected by", addr)

            #recieve data, wait a bit, then send it back
            full_data = conn.recv(BUFFER_SIZE)
            print("send data  "+ full_data.decode()+" to google")
            remote_ip = socket.gethostbyname(host)
            #Get the address and port number of the target server
            target = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            target.connect((host, port))
            target.sendall(full_data)

            data = target.recv(BUFFER_SIZE)
            print("sending data "+ data.decode() +" to client")
            target.sendall(data)

            time.sleep(0.5)
            conn.sendall(full_data)

            target.close()
            conn.close()

if __name__ == "__main__":
    main()
