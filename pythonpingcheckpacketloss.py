import pythonping

def check_packet_loss(destination_ip, count=4, timeout=5):

    # Perform the ping test
    packet_loss = pythonping.ping(target = destination_ip, count=count, timeout=timeout)

    # Check for packet loss
    if packet_loss is not None:
        packet_loss_percentage = (1 - packet_loss / count) * 100
        print(f"Packet loss: {packet_loss_percentage:.2f}%")
    else:
        print("Ping test failed. No response received.")

if __name__ == "__main__":
    destination_ip = "192.168.111.235"  # Replace with the IP address you want to test
    check_packet_loss(destination_ip)