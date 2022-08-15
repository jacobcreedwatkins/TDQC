# for build the socket
import socket

# for system level commands
import sys

# establishing the packet structure (used later on), this will allow direct access to the methods and funcions in the struct module
from struct import *

# create a raw socket.
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
except socket.error as msg:
    print(msg)
    sys.exit()
packet = ''

src_ip = '127.0.0.1' #change this as needed
dst_ip = '192.168.0.1' #change this as needed

# Lets add the IPv4 header info
ip_ver_ihl = 69 #puts the decimal conversion of 0x45 for version and internet header length
ip_tos = 0      #this combines the DSCP and ECN fields
ip_len = 0      #kernel will fill in the actual length of the packet
ip_id = 12345   #sets the ip identification fo the packet
ip_frag = 0     #sets fragmentation to off
ip_ttl = 64     #Determines the TTL of the packet when leaving the machine
ip_proto = 16   #sets the IP protocol of 16 (CHAOS). If this was 6 (TCP) or 17 (UDP), additional headers would be required
ip_check = 0    #the kernel will fill in the checksum for the packet
ip_srcadd = socket.inet_aton(src_ip)    #inet_aton(string) will convert IP address to a 32 bit binary number
ip_dstadd = socket.inet_aton(dst_ip)    #same as above

ip_header = pack('!BBHHHBBH4s4s' , ip_ver_ihl, ip_tos, ip_len, ip_id, ip_frag, ip_ttl, ip_proto, ip_check, ip_srcadd, ip_dstadd)
#B = 1 byte (byte)
#H = 2 bytes (half word)
#4s = 4 bytes (Word - converted from string to binary) 

message = b'This is a message'  #note the b sends this as a bytes-like object
packet  = ip_header + message

#Send the packet

s.sendto(packet, (dst_ip, 0))
