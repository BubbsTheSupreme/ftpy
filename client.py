import os
import sys
import socket
import packet
from time import sleep

p = packet.Packet()
ip = sys.argv[2]
filename = sys.argv[1]
filesize = os.path.getsize(filename)

print('Sending...')
size_packet = p.construct_packet(1, bytes(str(filesize), 'ascii'))
name_packet = p.construct_packet(0, bytes(filename, 'ascii'))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((ip, 12345))
	s.send(name_packet)
	sleep(.5)
	s.send(size_packet)
	with open(filename, 'rb') as f:
		seek = 0
		while True:
			buffer = f.read(1024)
			if not buffer:
				break
			file_packet = p.construct_packet(2, buffer)
			s.send(file_packet)
			if seek < filesize and (seek + 1024) < filesize:
				seek += 1024
			else:
				seek += (filesize - seek)
			f.seek(seek)
			sleep(0.5)
	complete_packet = p.construct_packet(3, 'EOF'.encode('ascii'))
	s.send(complete_packet)
	sleep(5)
	complete_packet = p.construct_packet(4, 'DONE'.encode('ascii'))
	s.send(complete_packet)
	recv_buffer = s.recv(1024)
	print(recv_buffer.decode())