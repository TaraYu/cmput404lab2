#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
from multiprocessing import Pool

HOST = "localhost"
PORT = 8001
BUFFER_SIZE = 1024

def proxyClient(address):
    host = 'www.google.com'
    port = 80
    payload = 'GET / HTTP/1.0\r\nHost: '+host+'\r\n\r\n'
    buffer_size = 4096

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(address)
        s.sendall(payload.encode())
        s.shutdown(socket.SHUT_WR)

        full_data = s.recv(BUFFER_SIZE)
        print(full_data)
    except Exception as e:
        print(e)
    finally:
        s.close()


def main():
    address = [('127.0.0.1', 8001)]
    with Pool() as p:
        p.map(proxyClient, address * 10)

if __name__ == "__main__":
    main()