__author__ = 'cloudera'
from datetime import datetime
from socket import *
from time import time

clientSocket = socket(AF_INET, SOCK_DGRAM)
message = 'randomnumb'
counter = 10
while counter < 10:
    counter = counter + 1
