import os
from signal import pause
import sys
import webbrowser
import fade
import time
import requests
from colorama import Fore
import concurrent.futures

test_url = 'https://www.youtube.com/channel/UCjqJ3HJkiyu12fzFKIGEovQ?sub_confirmation=1'

# Clear the console to get better view :)
if os.name == "nt":        # Check if the system is windows
    os.system("cls")
else:
    os.system("clear")     # All the other systems 

# ========================================================================================================================================================= #

banner = """
 _   _                          _     
| \ | |                        (_)    
|  \| | ___ _ __ ___   ___  ___ _ ___ 
| . ` |/ _ \ '_ ` _ \ / _ \/ __| / __|
| |\  |  __/ | | | | |  __/\__ \ \__ \\
\_| \_/\___|_| |_| |_|\___||___/_|___/          
"""
faded_banner = fade.greenblue(banner)
print(faded_banner)

info = """
╭─────────────────────────────────────╮
│ Nemesis Proxy Scraper v1.0          │
│ Developed by gokiimax               │
│ !! For Educational Purposes Only !! │
╰─────────────────────────────────────╯
"""
faded_info = fade.greenblue(info)
print(faded_info)

# ========================================================================================================================================================= #

text = f"{Fore.LIGHTGREEN_EX}[+] This program will scrape (Https,Socks4,Socks5) proxies into separate files"
for x in text:
  time.sleep(0.03) # In seconds
  sys.stdout.write(x)
  sys.stdout.flush()
print()

# ========================================================================================================================================================= #

option = int(input(f'''{Fore.LIGHTGREEN_EX}
[+] Options [+]

[1] Https
[2] Socks4
[3] Socks5

| Type >> '''))

if option == 1:
    out_file = "Https_Proxies.txt"
    proxies = open(out_file, 'wb')
    r1 = requests.get('https://api.openproxylist.xyz/http.txt')
    proxies.write(r1.content)
    length = []
    length.append(r1.content)
    length = length[0].splitlines()
    length1 = len(length)
    print(f"Completed! Successfully added {length1} proxies, Check the {out_file} file!")
    time.sleep(1) # In seconds
    sys.exit()

elif option == 2:
    out_file = "Socks4_Proxies.txt"
    proxies = open(out_file, 'wb')
    r1 = requests.get('https://api.openproxylist.xyz/socks4.txt')
    proxies.write(r1.content)
    length = []
    length.append(r1.content)
    length = length[0].splitlines()
    length1 = len(length)
    print(f"Completed! Successfully added {length1} proxies, Check the {out_file} file!")
    time.sleep(1) # In seconds
    sys.exit()

elif option == 3:
    out_file = "Socks5_Proxies.txt"
    proxies = open(out_file, 'wb')
    r1 = requests.get('https://api.openproxylist.xyz/socks4.txt')
    proxies.write(r1.content)
    length = []
    length.append(r1.content)
    length = length[0].splitlines()
    length1 = len(length)
    print(f"Completed! Successfully added {length1} proxies, Check the {out_file} file!")
    time.sleep(1) # In seconds
    sys.exit()

else:
    print("[-] Not a valid choice!")