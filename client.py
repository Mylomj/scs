from socket import *

s = socket(AF_INET,SOCK_STREAM)
s.connect((gethostname(),1234))

msg = s.recv(1024)
print(msg.decode("utf-8"))