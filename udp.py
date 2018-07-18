import socket

#UDP通信の明示
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#ローカルはなんでも良い("送信するデータ","送信先")
client.sendto(b"12345",("192.168.3.17",80))

data, addr = client.recvfrom(4096)

print(data)
print(addr)