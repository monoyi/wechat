import requests
import re
def queryData(md5):
	url = 'http://md5decryption.com/'
	data = {
		'hash' : md5,
		'submit' : 'Decrypt It!'
	}
	s = requests.post(url, data = data)
	if 'Decrypted Text:' in s.content:
		answer = re.findall('Decrypted Text: </b>(.*)</font>', s.content)
		return answer
	else:
		return 'Cant decrypt it'

