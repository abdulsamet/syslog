from socket import *

server = "10.10.10.10"
port = 514
buf = 8192*4
addr = (server,port)

TCPSock = socket(AF_INET,SOCK_DGRAM)
TCPSock.bind(addr)

#db=open("receive.log", "w")

while True:
    data,addr = TCPSock.recvfrom(buf)
    if not data:
        print ("No response from systems!")
        break
    else:
	    print (data)
		#print ("Message: ", data, file=db, flush=True)

TCPSock.close()
#db.close()
