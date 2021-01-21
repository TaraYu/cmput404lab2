#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
HOST = "localhost"
PORT = 8001
BUFFER_SIZE = 1024

def main():
    host = 'www.google.com'
    port = 80
    payload = 'GET / HTTP/1.0\r\nHost: '+host+'\r\n\r\n'
    buffer_size = 4096

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('127.0.0.1', 8001))
        s.sendall(payload.encode())
        s.shutdown(socket.SHUT_WR)

        full_data = s.recv(BUFFER_SIZE)
        print(full_data)
    except Exception as e:
        print(e)
    finally:
        s.close()

if __name__ == "__main__":
    main()