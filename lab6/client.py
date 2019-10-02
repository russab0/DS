import sys
import socket
import os
from math import ceil

from tqdm import tqdm

LEN = 32


def convert_to_fix_len(s):
    return str.encode(s + '#' * (LEN - len(s)))


def print_progress(sent, total):
    sent_proc = round(sent / total * 100)
    left_proc = 100 - sent_proc
    print("|" * sent_proc + "." * left_proc)


def send(file, ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))

    with open(file, 'rb') as fs:
        sock.send(convert_to_fix_len('BEGIN'))
        sock.send(convert_to_fix_len(file))
        print("STARTED SENDING")

        total = os.path.getsize(file)
        sent = 0
        for _ in tqdm(range(ceil(total / LEN))):
            data = fs.read(LEN)
            sock.send(data)
            if not data:
                print('Breaking from sending data')
                break
            sent += LEN
    print(sent)
    print("FINISHED SENDING")
    fs.close()


file, ip, port = sys.argv[1:]
port = int(port)
print(file, ip, port)
send(file, ip, port)
