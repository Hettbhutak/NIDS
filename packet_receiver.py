from scapy.all import sniff, IP, TCP, UDP
import logging
import sys
import csv
from datetime import datetime
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize CSV file for packet logging
CSV_HEADERS = [
    'timestamp', 'protocol_type', 'service', 'flag', 'logged_in', 'count',
    'srv_serror_rate', 'srv_rerror_rate', 'same_srv_rate', 'diff_srv_rate',
    'dst_host_count', 'dst_host_srv_count', 'dst_host_same_srv_rate',
    'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate',
    'dst_host_serror_rate', 'dst_host_rerror_rate'
]

class PacketReceiver:
    def __init__(self):
        self.packet_count = 0
        self.connections = {}
        self.output_file = f"captured_packets_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        
        # Create CSV file with headers
        with open(self.output_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(CSV_HEADERS)

    def process_packet(self, packet):
        """Process each captured packet and extract features"""
        try:
            if IP in packet:
                self.packet_count += 1
                
                # Extract basic features
                features = {
                    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'protocol_type': self.get_protocol(packet),
                    'service': self.get_service(packet),
                    'flag': self.get_flag(packet),
                    'logged_in': 0,  # Default value
                    'count': self.packet_count
                } 
                
                # Calculate rates and additional features
                features.update(self.calculate_rates(packet))
                
                # Log packet info
                logger.info(f"Captured packet #{self.packet_count}: {features['protocol_type']} "
                          f"{features['service']} {features['flag']}")
                
                # Save to CSV
                self.save_to_csv(features)
                
        except Exception as e:
            logger.error(f"Error processing packet: {str(e)}")

    def get_protocol(self, packet):
        """Determine protocol type"""
        if TCP in packet:
            return 'tcp'
        elif UDP in packet:
            return 'udp'
        else:
            return 'other'

    def get_service(self, packet):
        """Determine service type based on port"""
        if TCP in packet:
            dport = packet[TCP].dport
            if dport == 80:
                return 'http'
            elif dport == 21:
                return 'ftp'
            else:
                return 'other'
        return 'unknown'

    def get_flag(self, packet):
        """Determine TCP flag"""
        if TCP in packet:
            if packet[TCP].flags & 0x02:  # SYN
                return 'S0'
            elif packet[TCP].flags & 0x10:  # ACK
                return 'SF'
            elif packet[TCP].flags & 0x14:  # RST+ACK
                return 'REJ'
        return 'OTH'

    def calculate_rates(self, packet):
        """Calculate various rates and counts"""
        return {
            'srv_serror_rate': 0.0,
            'srv_rerror_rate': 0.0,
            'same_srv_rate': 0.0,
            'diff_srv_rate': 0.0,
            'dst_host_count': 0,
            'dst_host_srv_count': 0,
            'dst_host_same_srv_rate': 0.0,
            'dst_host_diff_srv_rate': 0.0,
            'dst_host_same_src_port_rate': 0.0,
            'dst_host_serror_rate': 0.0,
            'dst_host_rerror_rate': 0.0
        }

    def save_to_csv(self, features):
        """Save packet features to CSV file"""
        with open(self.output_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([features[h] for h in CSV_HEADERS])

def start_capture():
    try:
        receiver = PacketReceiver()
        logger.info("Starting packet capture... Press Ctrl+C to stop")
        
        # Start capturing packets
        sniff(prn=receiver.process_packet, store=0)
        
    except KeyboardInterrupt:
        logger.info(f"Capture stopped. Packets saved to {receiver.output_file}")
    except Exception as e:
        logger.error(f"Error during capture: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    start_capture()