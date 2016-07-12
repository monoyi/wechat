import threading 
from subprocess import Popen, PIPE, STDOUT
import os


def scan(site, random):
    with open('Vulscan_' + random, 'a') as output:
        cmd = 'python /root/BBScan/BBScan.py --host ' + site
        p = Popen(cmd, stdout = PIPE, stdin = PIPE, stderr = STDOUT, shell = True)
        stdout, _ = p.communicate(input = None)
        output.write(stdout)

def main(site):
    print "main thread start"
    random = ''.join(map(lambda xx:(hex(ord(xx))[2:]),os.urandom(8)))
    th = threading.Thread(target = scan, args = [site, random])
    th.start()
    print "main thread end"
    return 'Vulscan_' + random
