# for build the socket
import socket

# for system level commands
import sys

# for doing an array in the TCP checksum

import array

# establishing the packet structure (used later on), this will allow direct access to the methods and funcions in the struct module
from struct import *

# create a raw socket.
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
except socket.error as msg:
    print(msg)
    sys.exit()
packet = ''

src_ip = '127.0.0.1'  #change as needed
dst_ip = '192.168.0.1' #change this as needed

# Lets add the IPv4 header info
ip_ver_ihl = 69 #puts the decimal conversion of 0x45 for version and internet header length
ip_tos = 0      #this combines the DSCP and ECN fields
ip_len = 0      #kernel will fill in the actual length of the packet
ip_id = 12345   #sets the ip identification fo the packet
ip_frag = 0     #sets fragmentation to off
ip_ttl = 64     #Determines the TTL of the packet when leaving the machine
ip_proto = 6    #sets the IP protocol of 6 (TCP)
ip_check = 0    #the kernel will fill in the checksum for the packet
ip_srcadd = socket.inet_aton(src_ip)    #inet_aton(string) will convert IP address to a 32 bit binary number
ip_dstadd = socket.inet_aton(dst_ip)    #same as above

ip_header = pack('!BBHHHBBH4s4s' , ip_ver_ihl, ip_tos, ip_len, ip_id, ip_frag, ip_ttl, ip_proto, ip_check, ip_srcadd, ip_dstadd)
#B = 1 byte (byte)
#H = 2 bytes (half word)
#4s = 4 bytes (Word - converted from string to binary) 


############
#TCP HEADER#
############

#TCP Header Fields
tcp_src = 54321     #source port
tcp_dst = 7777      #destination port
tcp_seq = 454       #sequence number
tcp_ack_seq = 0     #tcp ack sequence number
tcp_data_off = 5    #data offset specifying the size of the tcp header * 4 which is 20
tcp_reserve = 0     #the reserve bits + ns flag in reserve field
tcp_win = 65535     #maximum allowed window size reordered to network order
tcp_chk = 0         #tcp checksum which will be calculated later on
tcp_urg_ptr = 0     #urgent pointer only if urg flag is set

# combine the left shifted 5 it tcp offset and the reserve field

tcp_off_res = (tcp_data_off << 4) + tcp_reserve

# tcp flags by bit starting from right to left
tcp_fin = 0     #finished flag
tcp_syn = 1     #synchronization
tcp_rst = 0     #reset
tcp_psh = 0     #push 
tcp_ack = 0     #acknowledgement
tcp_urg = 0     #urgent
tcp_ece = 0     #Explicit congestion notifciation echo
tcp_cwr = 0     #congestion window

# combine the tcp flags by left shifting the bit locations and adding the bits together
tcp_flags = tcp_fin + (tcp_syn << 1) + (tcp_rst << 2) + (tcp_psh << 3) + (tcp_ack << 4) + (tcp_urg << 5) + (tcp_ece << 6) + (tcp_cwr << 7)

# the ! in the pack format string means network order
tcp_hdr = pack('!HHLLBBHHH', tcp_src, tcp_dst, tcp_seq, tcp_ack_seq, tcp_off_res, tcp_flags, tcp_win, tcp_chk, tcp_urg_ptr)

#B = 1 byte 
#H = 2 bytes (half word)
#L = 4 bytes (32 bit word as integer)

message = b'Hello, is it me you are looking for?'

# psuedo header field

src_address = socket.inet_aton(src_ip)
dst_address = socket.inet_aton(dst_ip)
reserved = 0
protocol = socket.IPPROTO_TCP
tcp_length = len(tcp_hdr) + len(message)

# pack the psuedo header and combine with the message

ps_hdr = pack('!4s4sBBH', src_address, dst_address, reserved, protocol, tcp_length)
ps_hdr = ps_hdr + tcp_hdr + message



def checksum(data):
        if len(data) % 2 != 0:
                data += b'\0'
        res = sum(array.array("H", data))
        res = (res >> 16) + (res & 0xffff)
        res += res >> 16
        return (~res) & 0xffff

tcp_chk = checksum(ps_hdr)

# pack the TCP header to fill in the correct checksum - remember checksum is NOT in network byte order

tcp_hdr = pack('!HHLLBBH', tcp_src, tcp_dst, tcp_seq, tcp_ack_seq, tcp_off_res, tcp_flags, tcp_win) + pack('H', tcp_chk) + pack('!H', tcp_urg_ptr)

# combine all the headers and the message




packet  = ip_header + tcp_hdr + message

#Send the packet

s.sendto(packet, (dst_ip, 0))
