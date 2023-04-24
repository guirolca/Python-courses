import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('en.wikipedia.org', 80))
cmd = 'GET https://en.wikipedia.org/wiki/PDF HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(2000)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
