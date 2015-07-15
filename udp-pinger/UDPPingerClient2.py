__author__ = 'sharad'
from datetime import datetime
from socket import *
from time import time

clientSocket = socket(AF_INET, SOCK_DGRAM)
message = 'randomnumb'
counter = 0
rtt_list = []
while counter < 10:
    # send one letter at a time
    clientSocket.sendto(message[counter], ('localhost', 12000))
    t1 = datetime.now()
    # wait for one second
    clientSocket.settimeout(1)
    try:
        modified_message, server_address = clientSocket.recvfrom(1024)
        t2 = datetime.now()
        rtt = (t2-t1).microseconds
        print modified_message+' RTT = ', rtt
        rtt_list.append(rtt)
    except timeout:
        print 'time out!'
    counter = counter + 1

print 'counter end'
print 'max RTT = ', max(rtt_list)
print 'min RTT = ', min(rtt_list)
print 'avg RTT = ', sum(rtt_list)/len(rtt_list)
clientSocket.close()
