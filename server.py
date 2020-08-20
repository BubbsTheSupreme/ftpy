import socket 
import struct
import packet

ip = '192.168.1.146'
port = 12345
p = packet.Packet()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((ip, port))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f'Connected by {addr}')
        while True:
            buffer = conn.recv(8388612)
            if not buffer:
                break
            handler = p.handle_packet(buffer)
            if handler == None:
                continue
            else:
                conn.send(handler.encode())
                break
