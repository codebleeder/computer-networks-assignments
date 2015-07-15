__author__ = 'cloudera'
Skeleton Python Code for the
Mail Client
f
rom socket import *
msg
=
”
\
r
\
n I love computer networks!”
endmsg
=
”
\
r
\
n.
\
r
\
n”
#
C
hoose a mail server (e.g.
Google
mail
server) and call it mailserver
mailserver =
#Fill in start #Fill in end
#
C
reate socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
#Fill in end
r
ecv
=
clientSocket.recv(1024)
print recv
if recv[:3]
!=
'220':
print '220 reply not received from server.'
#
Send HELO command and print server response.
heloCommand
=
'HELO Alice
\
r
\
n'
clientSocket.send(heloCommand)
recv1
=
clientSocket.recv(1024)
print recv1
if recv1[:3]
!=
'250':
print '250 reply not received from server.'
#
Send MAIL FROM command and print server response.
#
Fill in start
#
Fill in end

#
Send RCPT TO command and print server response.
#
Fill in start
#
Fill in end
#
Send DATA command and print server response.
#
Fill in start
#
Fill in end
#
S
end message data.
#
Fill in start
#
Fill in end

#
M
essage ends with a single period.
#
Fill in start
#
Fill in end
#
S
end QUIT command and get server response.
# F
ill in
start
# F
ill in end
