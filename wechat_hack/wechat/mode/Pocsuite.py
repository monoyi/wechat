import threading 
from subprocess import Popen, PIPE, STDOUT
import os


def scan(site, random):
	# what site it is , depends on what kind of exp it is
	if site == 'joomla':
		f1 = open(site + '.txt', 'r')
		if os.path.isfile(site + '_url.txt'):
			pass
		else:
			f2 = open(site + '_url.txt', 'a')
			for lines in f1:
				f2.write(lines.split('\t')[0] + '\n')

		argmt = '-r ' + site + '_url.txt'
		print argmt
	with open('Shell_' + random, 'a') as output:
		cmd = 'python /root/wechat_hack/wechat/mode/hackUtils/hackUtils.py ' + argmt
                print cmd
		p = Popen(cmd, stdout = PIPE, stdin = PIPE, stderr = STDOUT, shell = True)
		stdout, _ = p.communicate(input = None)
		output.write(stdout)

def Pocsuite(site):
    print "main thread start"
    random = ''.join(map(lambda xx:(hex(ord(xx))[2:]),os.urandom(8)))
    th = threading.Thread(target = scan, args = [site, random])
    th.start()
    print "main thread end"
    return 'Shell_' + random
