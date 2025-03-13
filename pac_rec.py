from scapy.all import send, IP, TCP, UDP
import logging
import sys

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def send_packets():
    try:
        # Test if we have necessary permissions
        test_packet = IP(dst="127.0.0.1")/TCP(dport=80)
        send(test_packet, verbose=False)
        
        # If test successful, send actual packets
        target_ip = "192.168.1.2"
        logger.info(f"Starting packet transmission to {target_ip}")
        
        for i in range(10):
            pkt = IP(dst=target_ip)/TCP(dport=80, flags="S")
            send(pkt, verbose=False)
            logger.info(f"Sent packet {i+1}")
            
    except OSError as e:
        logger.error("Administrator privileges required!")
        logger.error("Please:")
        logger.error("1. Install Npcap from https://npcap.com/#download")
        logger.error("2. Run VS Code as administrator")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Error sending packets: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    send_packets()