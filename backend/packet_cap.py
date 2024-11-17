# Import necessary libraries
from scapy.all import sniff, conf, IP, TCP, UDP
import sqlite3

# Detect active network interface
active_interface = conf.iface
print(f"Active interface detected: {active_interface}")

# Connect to SQLite database
conn = sqlite3.connect("network_traffic.db")
cursor = conn.cursor()

# Create a table to store session data if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS sessions (
                    session_key TEXT PRIMARY KEY,
                    src_ip TEXT,
                    dst_ip TEXT,
                    protocol TEXT,
                    src_port INTEGER,
                    dst_port INTEGER,
                    packet_count INTEGER,
                    total_volume INTEGER)''')

# Function to process and save each packet
def packet_callback(packet):
    if IP in packet:
        # Extract packet details
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto
        src_port = packet[TCP].sport if TCP in packet else (packet[UDP].sport if UDP in packet else None)
        dst_port = packet[TCP].dport if TCP in packet else (packet[UDP].dport if UDP in packet else None)
        packet_size = len(packet)
        
        # Define a unique session key
        session_key = f"{src_ip}:{src_port}-{dst_ip}:{dst_port}-{protocol}"
        
        # Check if the session already exists in the database
        cursor.execute('''SELECT * FROM sessions WHERE session_key = ?''', (session_key,))
        existing_session = cursor.fetchone()
        
        if existing_session:
            # Session exists, update packet count and volume
            cursor.execute('''UPDATE sessions SET packet_count = ?, total_volume = ? WHERE session_key = ?''',
                           (existing_session[6] + 1, existing_session[7] + packet_size, session_key))
        else:
            # New session, insert into the database
            cursor.execute('''INSERT INTO sessions (session_key, src_ip, dst_ip, protocol, src_port, dst_port, packet_count, total_volume)
                              VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', 
                           (session_key, src_ip, dst_ip, protocol, src_port, dst_port, 1, packet_size))
        
        # Commit the transaction
        conn.commit()
        
        # Print session details
        print(f"Session: {session_key} | Packets: {existing_session[6] + 1 if existing_session else 1} | Volume: {existing_session[7] + packet_size if existing_session else packet_size} bytes")

# Start packet capture on the detected active interface
sniff(iface=active_interface, prn=packet_callback, store=0)
