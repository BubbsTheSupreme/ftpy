import os
import json
import struct
import socket

class Packet:

    def __init__(self):    
        self.filename = ''
        self.filesize = 0
        self.path = ''

    def construct_packet(self, packet_id, packet_payload):
        return struct.pack(f'i {len(packet_payload)}s', packet_id, packet_payload)

    def handle_packet(self, incoming_packet):
        packet_id, packet_payload = struct.unpack(f'i {len(incoming_packet) - 4}s', incoming_packet)

        if packet_id == 0:
            self.filename = packet_payload.decode('utf-8') 
            return None
        
        elif packet_id == 1:
            self.filesize += int(packet_payload.decode('utf-8'))
            print(f'{self.filesize}')
            return None

        elif packet_id == 2:
            with open(self.path + self.filename, 'wb') as f:
                f.write(packet_payload)
            current_size = os.path.getsize(self.path + self.filename) # for when it needs to track the progress of the transfer
            return None
        
        elif packet_id == 3:
            print(f'\u001b[32m File Transfer Complete! \u001b[0m')
            return packet_payload.decode('utf-8')