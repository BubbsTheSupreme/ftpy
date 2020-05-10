import socket
import struct
import packet

IP = '192.168.1.146'
PORT = 12345
p = packet.Packet()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((IP, PORT))
    while True:
        packet_data = []
        p.write_packet_id(packet_data, 2)
        p.write_packet_data(packet_data, b'test.py')
        PACKET = struct.pack(*packet_data)
        s.send(PACKET)
        buffer = s.recv(1024)
        break
    
print(f'Recieved: {repr(buffer)}')