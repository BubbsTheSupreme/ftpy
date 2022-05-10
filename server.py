import socket 
import packet
import os

ip = '192.168.1.221'
port = 12345
p = packet.Packet()
filename = ''
filesize = 0
path = ''

try:
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.bind((ip, port))
		s.listen()
		conn, addr = s.accept()
		with conn:
			print(f'Connected by {addr}')
			while True:
				buffer = conn.recv(1028)
				if not buffer:
					break
				packet_id, packet_payload = p.unpack_packet(buffer)
				if packet_id == 0:
					# filename = packet_payload.decode('ascii')
					filename = 'test2.txt'

				elif packet_id == 1:
					filesize += int(packet_payload.decode('ascii').strip('\x00'))

				elif packet_id == 2:
					with open(filename, 'ab') as f:
						f.write(packet_payload)
					current_size = os.path.getsize(path + filename) # for when it needs to track the progress of the transfer
			
				elif packet_id == 3:
					print('\u001b[32mFile Transfer Complete!\u001b[0m')
				elif packet_id == 4:
					print('Closing Connection')
					conn.send(p.construct_packet(4, 'done'.encode('ascii')))
					break
except KeyboardInterrupt:
	pass