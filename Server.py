from socket import *
from time import ctime

host = '' #监听所有的ip
port = 55008 #接口必须一致
bufsize = 1024
addr = (host,port)

udpServer = socket(AF_INET,SOCK_DGRAM)
udpServer.bind(addr) #开始监听

rfile = open('test_message.txt', 'w')
while True:
    print('Waiting for connection...')
    data,addr = udpServer.recvfrom(bufsize)  #接收数据和返回地址
    #处理数据
    data  = data.decode(encoding='utf-8').upper()
    data = "at %s :%s"%(ctime(),data)
    rfile = open('test_message.txt', 'a')
    rfile.write(data + '\n')
    udpServer.sendto(data.encode(encoding='utf-8'),addr)
    #发送数据
    print('...recevied from and return to :',addr)
rfile.close()#在内容写完后再关闭文件
os.chdir(basePath)
udpServer.close()