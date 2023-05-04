import socket

HOST = "192.168.1.44"
PORT = 12380

""" 
with关键字是Python中用于处理文件、网络连接、数据库连接等资源的一种语法结构。
它可以自动管理资源的打开和关闭，避免了人为的错误。
"""

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"hello")
    data = s.recv(1024)
print(repr(data))
