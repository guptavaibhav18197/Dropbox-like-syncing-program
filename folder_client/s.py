import socket

port = 60000
s = socket.socket()
host = ""

s.bind((host, port))
s.listen(5)

filename = raw_input("Enter file to share:")
print 'Server listening....'

while True:
    conn, addr = s.accept()
    print 'Got connection from', addr
    data = conn.recv(1024)
    print data
    print('Server received', repr(data))

    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
       conn.send(l)
       print('Sent ',repr(l))
       l = f.read(1024)
    f.close()

    print('Done sending')
    conn.send('Thank you for connecting')
    conn.close()

adqwdwdfqw
