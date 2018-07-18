import socket

#TCP通信の明示
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#サーバに接続
client.connect(("www.google.com",80))

client.send(b"GET/HTTP/1.1\r\nHost:google.com\r\n\r\n")

response = client.recv(4096)

print(response)