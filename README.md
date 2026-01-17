# Basic Network Sniffer in Python

## Description
This project is a basic network sniffer developed in Python using the Scapy library.
It captures live network traffic and analyzes packets by identifying:
- Source and destination IP addresses
- Protocol type (TCP, UDP, ICMP)
- Source and destination ports

## Tools & Technologies
- Python 3
- Scapy
- Kali Linux
- VirtualBox

## How It Works
The program uses Scapy's sniff() function to capture packets in real time.
Each packet is inspected to determine its protocol and relevant header information.

## Usage
Run the script with root privileges:
sudo python3 basic_sniffer.py
