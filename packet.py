import struct

class Packet:

    def __init__(self):
        self.filename = ''

    def write_packet_id(self, packet, id):
        packet.append(id)
        return packet

    def write_packet_data(self, packet, bdata):
        packet.append(bdata)
        return packet

    def packet_handler(self, packet):
        response = ''
        packet_id = packet[0]
        if packet_id == 0:
            for i in range(1, len(packet)):
                self.filename += str(packet[i], 'utf-8')
        elif packet_id == 1:
            with open(self.filename, 'ab') as f:
                f.write()
        elif packet_id == 2:
            print(f'2nd element in tuple: {packet[1]}')
            for i in range(1, len(packet)):
                response += str(packet[i], 'utf-8')
                print(f'length of packet: {len(packet)}')
            print(response)
            return response