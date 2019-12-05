import socket


def socket_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'www.baidu.com'
    port = 80
    s.connect((host, port))
    s.send(b'GET / HTTP/1.1\r\nHost:www.baidu.com\r\nConnection:close\r\n\r\n')
    buffer = []
    while True:
        d = s.recv(1024)
        if d:
            buffer.append(d)
        else:
            break
    data = b''.join(buffer)

    header, html = data.split(b'\r\n\r\n', 1)
    print(header.decode('utf_8'))
    with open('baidu.html', 'wb') as f:
        f.write(html)
    s.close()


def main():
    socket_client()


if __name__ == '__main__':
    main()
