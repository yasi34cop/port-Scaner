#!/bin/python
from scapy.all import sniff, IP, TCP

def packet_callback(packet):
    # Check if the packet is TCP and the destination IP matches the target
    if TCP in packet and packet[IP].dst == target_ip:
        print(packet.summary())

def capture_packets(interface, target):
    global target_ip

    # Set the target IP address
    target_ip = target

    # Start the packet capture
    try:
        sniff(iface=interface, filter=f"tcp and dst host {target_ip}", prn=packet_callback, store=False)
    except PermissionError:
        print("Error: You need root/admin privileges to capture packets.")
        return

if __name__ == "__main__":
    interface = input("Enter the network interface to capture packets from: ")
    target = input("Enter the target IP address to capture packets for: ")
    capture_packets(interface, target)
