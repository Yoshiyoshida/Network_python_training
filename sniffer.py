import socket

sniff = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

sniff.bind(('192.168.3.17',0))

sniff.socketopt(socket.IPPROTO_IP, socket.IP_HDRINCL,1)

print("sniff is lisning")

print(sniff.recvfrom(4096))