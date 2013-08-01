import socket
import sys

try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error:
    print('falied')
    sys.exit()

host='172.18.84.28'
port=4444
#ip=socket.gethostbyname(host)
s.connect((host , port))
print ('Socket Connected to ' + host )

f=open('D:\sendbank\\sendabc.xml',)

message = f.read()

#print (message)

try:
    s.sendall(b'message')
except socket.error:
    print('send failed')
    sys.exit()

reply = s.recv(10240)

print(repr(reply))
