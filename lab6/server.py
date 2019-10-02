import socket
import os
import re

LEN = 32


def get_filename(s):
    base_name = s[:s.index('#')]
    ind = base_name.index(".")
    name, extension = base_name[:ind], base_name[ind + 1:]

    pattern = f"{name}(_copy(\d+))?\.{extension}"
    maxi = -1
    for x in os.listdir("output"):
        q = re.search(pattern, x)
        if q is None:
            continue
        if q[2] is None:
            maxi = max(maxi, 0)
        else:
            maxi = max(maxi, int(q[2]))

    if maxi == -1:
        return base_name
    else:
        return f"{name}_copy{maxi + 1}.{extension}"


def recieve():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 8756))
    sock.listen(1)

    while True:
        conn, address = sock.accept()
        print("READY TO RECIEVE FILES...")

        while True:
            data = conn.recv(LEN)

            if data != b'':  # BEGIN
                data = conn.recv(LEN)
                file_name = get_filename(data.decode('utf-8'))
                print(f"STARTED RECIEVING NEW FILE {file_name}")
                fw = open("output/" + file_name, "wb")

                while data != b'':
                    data = conn.recv(32)
                    fw.write(data)
                fw.close()
                print("FINISHED RECIEVING\n")
                break

    ssFT.close()


recieve()
