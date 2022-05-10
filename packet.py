from struct import pack, unpack

class Packet:
	def construct_packet(self, short, buf):
		return pack('h 1024s', short, buf)

	def unpack_packet(self, incoming_packet):
		return unpack('h 1024s', incoming_packet)
