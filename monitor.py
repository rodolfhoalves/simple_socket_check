
import socket
from datetime import datetime
import time

HOST = "YOUR SERVER NAME HERE"
PORT = 443

def currente_datetime():
    yield datetime.now().strftime("%Y-%m-%d %H:%M:%S")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex((HOST, PORT))
sock.close()

while True:
    with open("logs.log", 'a') as file:     
        if result == 0:
            print(next(currente_datetime()))
            pass 
        else:
            file.write(f' {next(currente_datetime())} - [{HOST}]:{PORT} Port is not open\n')
    time.sleep(1)
