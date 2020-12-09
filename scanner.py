#!/usr/bin/env python3

import socket
import time
import datetime
import os
import re
from sys import argv
import threading
from queue import Queue
from colorama import Fore, Back, Style

open_ports = []
start = time.time()

IP = "10.10.10.215"
lock = threading.Lock()
q = Queue()


def b():
    # banner grabbing if able
    pass


def o():
    # outputs the scan into a file with the ip address as the name of the file along with time stamp
    pass


def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect_ex((IP, port))
        with lock:
            if con == 0:
                open_ports.append(port)
                try:
                    service = socket.getservbyport(port)
                    info_message(f"Open port found {port}: {service}")
                except OSError:
                    info_message(f"Open port found {port}: unknown service")
            else:
                return False
    except(socket.timeout, socket.error):
        error_message("Error when scanning the port")


def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()


def s():
    start = time.time()
    for x in range(300):
        t = threading.Thread(target=threader)
        t.daemon = True
        t.start()

    for worker in range(1, 65535):
        q.put(worker)

    q.join()
    finish = time.time()
    info_message("Scan finnished in {0:0.1f} seconds".format(finish - start))



def u():
    # Usage function
    print("[ USAGE ] ./scanner.py [ PARAMETERS ] [ IP ADDRESS ]")
    print("""
    \t-b\tFlag for banner grabbing
    \t-o\tOutputs scan into a text file where the files name is ip and time stamp
    \t-s\tScans IP for open ports
    \t-u\tPrints This page
    """)
    print("[ USAGE ] EX: ./scanner.py -bos 127.0.0.1")


def info_message(message):

    print(Fore.GREEN + f"[+] {message} | {datetime.datetime.now()}")


def error_message(message):
    print(Fore.RED + f"[-] {message} | {datetime.datetime.now()}")


def console_report():
    print(f"")


function_list = {'b': b, 'o': o, 's': s, 'u': u}

s()
print(open_ports)
