"""
Name: Sean Pardy
ID: R00186157
"""
import socket
import threading

header = 64
port = 5050
server = socket.gethostbyname(socket.gethostname())
addr = (server, port)
server_format = 'utf-8'
disconnect = "!dc"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(addr)


def handleclient(conn, addr):
    print(f"{addr} now connected!!\n")

    connected = True
    while connected:
        msg_len = conn.recv(header).decode(server_format)
        if msg_len:
            msg_len = int(msg_len)
            msg = conn.recv(msg_len).decode(server_format)
            if msg == disconnect:
                connected = False

        # Check dicts for values
        # employee_ids = (msg == "E00123" or msg == "E01033")

        if msg in ["E00123", "E01033"]:
            print(f"{addr} message has been received: {msg} ")
            conn.send(f"{addr} Client value exists: {msg}".encode(server_format))

        elif msg in ["s", "t", "c", "C", "X", "y", 2016, 2018, "!dc"]:
            print(f"{addr} message has been received: {msg} ")
            conn.send(f"{addr} Client value exists: {msg}".encode(server_format))

        else:
            print(f"{addr} message has been received: {msg}")
            conn.send(f"{addr} Client value does not exist")

        print(f"{addr} {msg}")
        conn.send("Message received".encode(server_format))

    # close the connection
    conn.close()


def start():
    s.listen()
    print(f"Server is listening on {server} ")

    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handleclient, args=(conn, addr))
        thread.start()
        print(f"Active connections = {threading.active_count() - 1}")


print("Starting!!")
start()
