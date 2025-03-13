import pandas as pd # type: ignore
import numpy as np # type: ignore
import scapy as sc
import os

# Define column names
columns = ['protocol_type','service','flag','logged_in','count','srv_serror_rate','srv_rerror_rate',
           'same_srv_rate','diff_srv_rate','dst_host_count','dst_host_srv_count','dst_host_same_srv_rate',
           'dst_host_diff_srv_rate','dst_host_same_src_port_rate','dst_host_serror_rate','dst_host_rerror_rate']

# Generate random traffic
np.random.seed(42)
rows = 150  # Number of samples

# Generate categorical data
protocol_types = ['tcp', 'udp', 'icmp']
services = ['http', 'ftp_data', 'private', 'eco_i', 'imap4', 'systat', 'other']
flags = ['SF', 'S3', 'REJ', 'S0']

data = {
    'protocol_type': np.random.choice(protocol_types, rows),
    'service': np.random.choice(services, rows),
    'flag': np.random.choice(flags, rows),
    'logged_in': np.random.randint(0, 2, rows),
    'count': np.random.randint(1, 500, rows),
    'srv_serror_rate': np.random.rand(rows),
    'srv_rerror_rate': np.random.rand(rows),
    'same_srv_rate': np.random.rand(rows),
    'diff_srv_rate': np.random.rand(rows),
    'dst_host_count': np.random.randint(1, 255, rows),
    'dst_host_srv_count': np.random.randint(1, 255, rows),
    'dst_host_same_srv_rate': np.random.rand(rows),
    'dst_host_diff_srv_rate': np.random.rand(rows),
    'dst_host_same_src_port_rate': np.random.rand(rows),
    'dst_host_serror_rate': np.random.rand(rows),
    'dst_host_rerror_rate': np.random.rand(rows)
}

# Create DataFrame
df = pd.DataFrame(data)

# Define output directory and file path
output_dir = os.path.join(os.path.dirname(__file__), "Uploaded_files")
output_file = os.path.join(output_dir, "fs_test.csv")

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Save to CSV with error handling
try:
    df.to_csv(output_file, index=False)
    print(f"Dataset successfully saved as {output_file}")
except PermissionError:
    print("Permission denied. Please try:")
    print("1. Run VS Code as administrator")
    print("2. Check folder permissions")
    print(f"3. Ensure {output_file} is not open in another program")
except Exception as e:
    print(f"Error saving file: {str(e)}")
