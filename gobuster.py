import sys
import socket
import requests
import progressbar
import os
from time import sleep

def checkpath(url, path):
    try:
        response = requests.get(url + '/' + path)
        if response.status_code == 200:
            print('[+] Valid Path Found: {}'.format(path))
    except requests.exceptions.RequestException as e:
        print('[!] Error: An Unexpected Error Occurred: {}'.format(e))

def animated_marker():
    widgets = ['Loading: ', progressbar.AnimatedMarker()]
    bar = progressbar.ProgressBar(widgets=widgets).start()
    for i in range(50):
        sleep(0.1)
        bar.update(i)

os.system("clear")
rhost = input("[+] URL: ")
wordlist = input("[+] Wordlist: ")
port = int(input("[+] Port: "))  

print('[*] Checking Host...')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
animated_marker()

try:
    status = s.connect_ex((rhost, port))
    s.close()
    if status == 0:
        print('!!! DONE !!!')
    else:
        print('[-] FAIL')
        print('[!] Error: Cannot Reach RHOST: {}'.format(rhost))
        sys.exit(1)

except socket.error as e:
    print('[-] FAIL')
    print('[!] Error: Cannot Connect to RHOST: {}'.format(e))
    sys.exit(1)

print('[*] Parsing WordList')
try:
    with open(wordlist, 'r') as file:
        to_check = file.read().strip().split('\n')
    print('!!! DONE !!!')
    print('[*] Total paths to check: {}'.format(len(to_check)))

except IOError:
    print('[-] FAIL')
    print('[!] Error: Failed to read WordList\n')
    sys.exit(1)

try:
    print('\n[*] Beginning Scan...')
    for path in to_check:
        checkpath(rhost, path)
    print('\nScan complete!')

except KeyboardInterrupt:
    print('\n[!] Error: User Interrupted Scan')
    sys.exit(1)
