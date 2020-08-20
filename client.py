import os
import sys
import socket
import packet
from time import sleep

p = packet.Packet()
ip = sys.argv[2]
filename = sys.argv[1]
filesize = str(os.path.getsize(filename))

size_packet = p.construct_packet(1, filesize.encode('utf-8'))
name_packet = p.construct_packet(0, filename.encode('utf-8'))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((ip, 12345))
    s.send(name_packet)
    sleep(.5)
    s.send(size_packet)
    with open(filename, 'rb') as f:
        while True:
            buffer = f.read(8388612)
            if not buffer:
                break
            file_packet = p.construct_packet(2, buffer)
            s.send(file_packet)
    complete_packet = p.construct_packet(3, 'File Transfer Complete!'.encode('utf-8'))
    s.send(complete_packet)
    recv_buffer = s.recv(1024)
    print(recv_buffer.decode())