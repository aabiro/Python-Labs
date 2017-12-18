from socket import *
import base64
import datetime
import ssl

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver

mailserver = ("smtp.gmail.com", 587) #Fill in start   #Fill in end

# Create socket called clientSocket and establish a TCP connection with mailserver

#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(bytes(heloCommand, 'utf-8'))
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send MAIL FROM command and print server response.

command = 'STARTTLS\r\n'
clientSocket.send(bytes(command, 'utf-8'))
recv11 = clientSocket.recv(1024).decode()

if recv11[:3] != '220':
    print('220 reply not received from server.')

#wrappedSocket = ssl.wrap_socket(clientSocket)  #, ssl_version=ssl.PROTOCOL_TLSv1, ciphers="ADH-AES256-SHA")
wrappedSocket = ssl.wrap_socket(clientSocket)

#username and password

username = input("Enter username: ").encode('utf-8')  #uwo4436
password = input("Enter password: ").encode('utf-8')  #eceuwo2017

authMsg = "AUTH LOGIN\r\n"
wrappedSocket.send(bytes(authMsg, 'utf-8'))
recv_auth = wrappedSocket.recv(1024)
print(recv_auth.decode())


wrappedSocket.send(base64.b64encode(username) +'\r\n'.encode('utf-8'))
recv111 = wrappedSocket.recv(1024).decode()

print(recv111)


wrappedSocket.send(base64.b64encode(password) +'\r\n'.encode('utf-8'))
recv1111 = wrappedSocket.recv(1024).decode()

print(recv1111)


# Fill in start
mailFrom = "MAIL FROM:<aaryn.alexander@gmail.com>\r\n"
wrappedSocket.send(bytes(mailFrom,'utf-8'))
recv2 = wrappedSocket.recv(1024)
recv2 = recv2.decode()
print("After MAIL FROM command: " + recv2)
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
reciever = input("Enter the email address you wish to send the email to: ")

rcptTo = "RCPT TO:<" + reciever + ">\r\n"
wrappedSocket.send(bytes(rcptTo, 'utf-8'))
recv3 = wrappedSocket.recv(1024)
recv3 = recv3.decode()
print("After RCPT TO command: "+recv3)
# Fill in end

# Send DATA command and print server response.
# Fill in start
data = "DATA\r\n"
wrappedSocket.send(bytes(data, 'utf-8'))
recv4 = wrappedSocket.recv(1024)
recv4 = recv4.decode()
print("After DATA command: "+recv4)
# Fill in end

# Read picture.jpg, encode it with base64, and turn it into a string
with open('test.jpg', 'rb') as f:
    img_data = f.read()
    img_data = str(base64.b64encode(img_data))[1:]

print(img_data)

# Send message data. Image is encoded between the boundary
# the_img_to_send, and the encoding and content
# is specified through Multipurpose Internet Mail Extensions (MIME)
msg_cmd = '''From: "Aaryn Alexander" <aaryn.alexander@gmail.com>
To: "Nikita Sahni" <nikitasahni97@gmail.com>
Cc:
Date: %s
Subject: Test
MIME-Version: 1.0
Content-Type:multipart/mixed;boundary="the_img_to_send"
--the_img_to_send
Content-Type:application/octet-stream;name="test.jpg"
Content-Transfer-Encoding:base64
Content-Disposition:attachment;filename="test.jpg"

%s

--the_img_to_send
%s
%s
''' % (datetime.datetime.now(), img_data, msg, endmsg)

print('C: ' + msg_cmd)
wrappedSocket.send(msg_cmd.encode())

msg_recv = wrappedSocket.recv(1024).decode()
print('S: ' + msg_recv)

# Send QUIT command and get server response.
quit_cmd = 'QUIT\r\n'
print('C: ' + quit_cmd)
wrappedSocket.send(quit_cmd.encode())
quit_recv = wrappedSocket.recv(1024).decode()
print('S: ' + quit_recv)


# Message ends with a single period.
# Fill in start
wrappedSocket.send(bytes(endmsg, 'utf-8'))
recv_msg = wrappedSocket.recv(1024)
print("Response after sending message body:"+recv_msg.decode())
# Fill in end

# Send QUIT command and get server response.
# Fill in start
quit = "QUIT\r\n"
wrappedSocket.send(bytes(quit, 'utf-8'))
recv5 = wrappedSocket.recv(1024)
print(recv5.decode())
wrappedSocket.close()
