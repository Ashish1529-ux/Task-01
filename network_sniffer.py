from scapy.all import *

# Callback function to process each captured packet
def packet_callback(packet):
    print(packet.summary())

# Function to start sniffing
def sniff_network():
    sniff(prn=packet_callback, count=10)  #count=0 for infinite capture 

if __name__ == "__main__":
    print("Sniffer is running. Press Ctrl+C to stop.")
    sniff_network()
