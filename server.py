import socket 
import packet
import struct

IP = '192.168.1.146'
PORT = 12345
p = packet.Packet()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((IP, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f'Connected by {addr}')
        while True:
            buffer = conn.recv(1025)
            if not buffer:
                break
            unpacked_buffer = struct.unpack(buffer)
            print(f'buffer: {unpacked_buffer}')
            response = p.packet_handler(unpacked_buffer)
            conn.send(response.encode('utf-8'))
            break