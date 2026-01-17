from scapy.all import sniff, IP, TCP, UDP, ICMP

def packet_handler(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        # TCP Packet
        if packet.haslayer(TCP):
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            print(f"[TCP] {src_ip}:{src_port} --> {dst_ip}:{dst_port}")

        # UDP Packet
        elif packet.haslayer(UDP):
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
            print(f"[UDP] {src_ip}:{src_port} --> {dst_ip}:{dst_port}")

        # ICMP Packet
        elif packet.haslayer(ICMP):
            print(f"[ICMP] {src_ip} --> {dst_ip}")

print("Starting enhanced network sniffer...")
sniff(prn=packet_handler, store=False)

