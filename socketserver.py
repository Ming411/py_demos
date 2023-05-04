import socket

HOST = "192.168.1.44"
PORT = 12380

#  AF_INET  ipv4
# SOCK_STREAM 流式协议即tcp协议
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print("Connected by", addr)
        while True:
            data = conn.recv(1024)  # 设置最大接收字节
            if not data:
                break
            conn.sendall(data)
