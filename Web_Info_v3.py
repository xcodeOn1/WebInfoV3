#!/usr/bin/env python
import time
import requests
import time as mm
import sys as n
import os
from pip._vendor.colorama import Fore, Style

# path1 = '''
#  /$$   /$$ /$$       /$$       /$$                           /$$$$$$$             /$$     /$$
# | $$  | $$|__/      | $$      | $$                          | $$__  $$           | $$    | $$
# | $$  | $$ /$$  /$$$$$$$  /$$$$$$$  /$$$$$$  /$$$$$$$       | $$  \ $$ /$$$$$$  /$$$$$$  | $$$$$$$   /$$$$$$$
# | $$$$$$$$| $$ /$$__  $$ /$$__  $$ /$$__  $$| $$__  $$      | $$$$$$$/|____  $$|_  $$_/  | $$__  $$ /$$_____/
# | $$__  $$| $$| $$  | $$| $$  | $$| $$$$$$$$| $$  \ $$      | $$____/  /$$$$$$$  | $$    | $$  \ $$|  $$$$$$
# | $$  | $$| $$| $$  | $$| $$  | $$| $$_____/| $$  | $$      | $$      /$$__  $$  | $$ /$$| $$  | $$ \____  $$
# | $$  | $$| $$|  $$$$$$$|  $$$$$$$|  $$$$$$$| $$  | $$      | $$     |  $$$$$$$  |  $$$$/| $$  | $$ /$$$$$$$/
# |__/  |__/|__/ \_______/ \_______/ \_______/|__/  |__/      |__/      \_______/   \___/  |__/  |__/|_______/
#
# '''
# os.system('clear')
# slow1(Fore.LIGHTYELLOW_EX + Style.BRIGHT + path1)
sub = '''

  /$$$$$$            /$$       /$$$$$$$                          /$$                    
 /$$__  $$          | $$      | $$__  $$                        |__/                    
| $$  \__/ /$$   /$$| $$$$$$$ | $$  \ $$  /$$$$$$  /$$$$$$/$$$$  /$$  /$$$$$$  /$$$$$$$ 
|  $$$$$$ | $$  | $$| $$__  $$| $$  | $$ /$$__  $$| $$_  $$_  $$| $$ |____  $$| $$__  $$
 \____  $$| $$  | $$| $$  \ $$| $$  | $$| $$  \ $$| $$ \ $$ \ $$| $$  /$$$$$$$| $$  \ $$
 /$$  \ $$| $$  | $$| $$  | $$| $$  | $$| $$  | $$| $$ | $$ | $$| $$ /$$__  $$| $$  | $$
|  $$$$$$/|  $$$$$$/| $$$$$$$/| $$$$$$$/|  $$$$$$/| $$ | $$ | $$| $$|  $$$$$$$| $$  | $$
 \______/  \______/ |_______/ |_______/  \______/ |__/ |__/ |__/|__/ \_______/|__/  |__/

'''
meun = '''
 [1]Brute force Subdomains 
 [2]Subdomains Discoverd By Api  
 [3]Hidden Paths
 [4]CloudFail Bypass
 [00]exit
'''
logo = '''
           ;               ,           
         ,;                 '.         
        ;:                   :;        
       ::                     ::       
       ::                     ::       
       ':                     :        
        :.                    :        
     ;' ::                   ::  '     
    .'  ';                   ;'  '.    
   ::    :;                 ;:    ::   
   ;      :;.             ,;:     ::   
   :;      :;:           ,;"      ::   
   ::.      ':;  ..,.;  ;:'     ,.;:   
    "'"...   '::,::::: ;:   .;.;""'    
        '"""....;:::::;,;.;"""         
    .:::.....'"':::::::'",...;::::;.   
   ;:' '""'"";.,;:::::;.'""""""  ':;   
  ::'         ;::;:::;::..         :;  
 ::         ,;:::::::::::;:..       :: 
 ;'     ,;;:;::::::::::::::;";..    ':.
::     ;:"  ::::::"""'::::::  ":     ::
 :.    ::   ::::::;  :::::::   :     ; 
  ;    ::   :::::::  :::::::   :    ;  
   '   ::   ::::::....:::::'  ,:   '   
    '  ::    :::::::::::::"   ::       
       ::     ':::::::::"'    ::       
       ':       """""""'      ::       
        ::                   ;:        
        ':;                 ;:"        
   --     ';              ,;'          
            "'           '"            
              '  WebInfo   v3.0
        **************************************
        * -> Development: Xcode          *
        * -> Telegram: https://t.me/x0Saudi *
        * -> Twitter @XcodeOn1              *      
        **************************************                                                 
\033'''

def slow(M):  ## By Twitter : @Matrix0700
    for c in M + '\n':
        n.stdout.write(c)
        n.stdout.flush()
        mm.sleep(1. / 20)


def slow2(M):  ## By Twitter : @Matrix0700
    for c in M + '\n':
        n.stdout.write(c)
        n.stdout.flush()
        mm.sleep(1. / 25)


def slow1(M):  ## By Twitter : @Matrix0700
    for c in M + '\n':
        n.stdout.write(c)
        n.stdout.flush()
        mm.sleep(1. / 2000)

def sublogo():
    sub = '''

      /$$$$$$            /$$       /$$$$$$$                          /$$                    
     /$$__  $$          | $$      | $$__  $$                        |__/                    
    | $$  \__/ /$$   /$$| $$$$$$$ | $$  \ $$  /$$$$$$  /$$$$$$/$$$$  /$$  /$$$$$$  /$$$$$$$ 
    |  $$$$$$ | $$  | $$| $$__  $$| $$  | $$ /$$__  $$| $$_  $$_  $$| $$ |____  $$| $$__  $$
     \____  $$| $$  | $$| $$  \ $$| $$  | $$| $$  \ $$| $$ \ $$ \ $$| $$  /$$$$$$$| $$  \ $$
     /$$  \ $$| $$  | $$| $$  | $$| $$  | $$| $$  | $$| $$ | $$ | $$| $$ /$$__  $$| $$  | $$
    |  $$$$$$/|  $$$$$$/| $$$$$$$/| $$$$$$$/|  $$$$$$/| $$ | $$ | $$| $$|  $$$$$$$| $$  | $$
     \______/  \______/ |_______/ |_______/  \______/ |__/ |__/ |__/|__/ \_______/|__/  |__/

    '''
    os.system('clear')
    print(slow1(Fore.LIGHTYELLOW_EX + Style.BRIGHT + sub))

def Pahtlogo():
    path1 = '''
     /$$   /$$ /$$       /$$       /$$                           /$$$$$$$             /$$     /$$                
    | $$  | $$|__/      | $$      | $$                          | $$__  $$           | $$    | $$                
    | $$  | $$ /$$  /$$$$$$$  /$$$$$$$  /$$$$$$  /$$$$$$$       | $$  \ $$ /$$$$$$  /$$$$$$  | $$$$$$$   /$$$$$$$
    | $$$$$$$$| $$ /$$__  $$ /$$__  $$ /$$__  $$| $$__  $$      | $$$$$$$/|____  $$|_  $$_/  | $$__  $$ /$$_____/
    | $$__  $$| $$| $$  | $$| $$  | $$| $$$$$$$$| $$  \ $$      | $$____/  /$$$$$$$  | $$    | $$  \ $$|  $$$$$$ 
    | $$  | $$| $$| $$  | $$| $$  | $$| $$_____/| $$  | $$      | $$      /$$__  $$  | $$ /$$| $$  | $$ \____  $$
    | $$  | $$| $$|  $$$$$$$|  $$$$$$$|  $$$$$$$| $$  | $$      | $$     |  $$$$$$$  |  $$$$/| $$  | $$ /$$$$$$$/
    |__/  |__/|__/ \_______/ \_______/ \_______/|__/  |__/      |__/      \_______/   \___/  |__/  |__/|_______/ 

    '''
    os.system('clear')
    slow1(Fore.LIGHTYELLOW_EX + Style.BRIGHT + path1)
def logo1():
    os.system('clear')
    logo = '''
               ;               ,           
             ,;                 '.         
            ;:                   :;        
           ::                     ::       
           ::                     ::       
           ':                     :        
            :.                    :        
         ;' ::                   ::  '     
        .'  ';                   ;'  '.    
       ::    :;                 ;:    ::   
       ;      :;.             ,;:     ::   
       :;      :;:           ,;"      ::   
       ::.      ':;  ..,.;  ;:'     ,.;:   
        "'"...   '::,::::: ;:   .;.;""'    
            '"""....;:::::;,;.;"""         
        .:::.....'"':::::::'",...;::::;.   
       ;:' '""'"";.,;:::::;.'""""""  ':;   
      ::'         ;::;:::;::..         :;  
     ::         ,;:::::::::::;:..       :: 
     ;'     ,;;:;::::::::::::::;";..    ':.
    ::     ;:"  ::::::"""'::::::  ":     ::
     :.    ::   ::::::;  :::::::   :     ; 
      ;    ::   :::::::  :::::::   :    ;  
       '   ::   ::::::....:::::'  ,:   '   
        '  ::    :::::::::::::"   ::       
           ::     ':::::::::"'    ::       
           ':       """""""'      ::       
            ::                   ;:        
            ':;                 ;:"        
       --     ';              ,;'          
                "'           '"            
                  '  WebInfo   v3.0
            **************************************
            * -> Development: Xcode          *
            * -> Telegram: https://t.me/x0Saudi *
            * -> Twitter @XcodeOn1              *      
            **************************************                                                 
    \033'''
    os.system('clear')
    slow1(Fore.LIGHTWHITE_EX + Style.BRIGHT + logo)

    slow(
        Fore.LIGHTRED_EX + Style.BRIGHT + 'WELCOME IN WEB INFO v3 ' + Fore.LIGHTWHITE_EX + Style.BRIGHT + " ^^ Happy Gather Xd")
    slow(
        Fore.LIGHTRED_EX + Style.BRIGHT + "Coded By Xcode " + Fore.LIGHTBLUE_EX + Style.BRIGHT + "Twitter :" + Fore.LIGHTWHITE_EX + Style.BRIGHT + '@Xcodeone1')
    time.sleep(2)
    os.system('clear')
def programStartMain():
    meun = '''
     [1]Brute force Subdomains 
     [2]Subdomains Discoverd By Api  
     [3]Hidden Paths
     [4]CloudFail Bypass
     [00]exit
    '''
    logo = '''
               ;               ,           
             ,;                 '.         
            ;:                   :;        
           ::                     ::       
           ::                     ::       
           ':                     :        
            :.                    :        
         ;' ::                   ::  '     
        .'  ';                   ;'  '.    
       ::    :;                 ;:    ::   
       ;      :;.             ,;:     ::   
       :;      :;:           ,;"      ::   
       ::.      ':;  ..,.;  ;:'     ,.;:   
        "'"...   '::,::::: ;:   .;.;""'    
            '"""....;:::::;,;.;"""         
        .:::.....'"':::::::'",...;::::;.   
       ;:' '""'"";.,;:::::;.'""""""  ':;   
      ::'         ;::;:::;::..         :;  
     ::         ,;:::::::::::;:..       :: 
     ;'     ,;;:;::::::::::::::;";..    ':.
    ::     ;:"  ::::::"""'::::::  ":     ::
     :.    ::   ::::::;  :::::::   :     ; 
      ;    ::   :::::::  :::::::   :    ;  
       '   ::   ::::::....:::::'  ,:   '   
        '  ::    :::::::::::::"   ::       
           ::     ':::::::::"'    ::       
           ':       """""""'      ::       
            ::                   ;:        
            ':;                 ;:"        
       --     ';              ,;'          
                "'           '"            
                  '  WebInfo   v3.0
            **************************************
            * -> Development: Xcode          *
            * -> Telegram: https://t.me/x0Saudi *
            * -> Twitter @XcodeOn1              *      
            **************************************                                                 
    \033'''
    slow1(Fore.LIGHTWHITE_EX + Style.BRIGHT + logo)
    slow2(Fore.LIGHTWHITE_EX + Style.BRIGHT + meun)



logo1()
programStartMain()
numper = int(input(Fore.LIGHTWHITE_EX + Style.BRIGHT + '#Enter number>>  '))
while numper > 4:
    print(slow(Fore.LIGHTRED_EX + Style.BRIGHT + 'Oh Here we go Agin'))
    print(slow(Fore.LIGHTRED_EX + Style.BRIGHT + 'Nice Try'))
    os.system('clear')
    programStartMain()
    numper = int(input(Fore.LIGHTWHITE_EX + Style.BRIGHT + '#Enter number>>  '))
while True:
    if numper == 00:
        break
    if numper == 1:
        sublogo()
        def request(url):
            try:
                return requests.get("http://" + url)
            except requests.exceptions.ConnectionError:
                pass


        target_url = input(Fore.LIGHTWHITE_EX + Style.BRIGHT + "Target url >> ")
        sublogo()
        listfile = input(Fore.LIGHTWHITE_EX + Style.BRIGHT + '#Put Word list >>')
        sublogo()
        slow(
            Fore.LIGHTWHITE_EX + Style.BRIGHT + "[+] Now Brute force SubDomains For " + Fore.LIGHTYELLOW_EX + Style.BRIGHT + target_url)
        slow(Fore.LIGHTWHITE_EX + Style.BRIGHT + '-' * 40)
        time.sleep(3)
        with open(listfile, "r") as word_list:
            for line in word_list:
                word = line.strip()
                dom_url = word + "." + target_url
                rsp = request(dom_url)
                if rsp:
                    print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "[ * Found] --> " + dom_url)
                    with open('FoundSub.txt', 'a') as x:
                        x.write(dom_url + '\n')
                else:
                    print(Fore.LIGHTRED_EX + Style.BRIGHT + "[* Not found ] --> " + dom_url)
        slow(Fore.LIGHTRED_EX + Style.BRIGHT + '# This all SubDomians of this target ˆ_ˆ ')
        slow(Fore.LIGHTRED_EX + Style.BRIGHT + 'Dont Forget Follow My @Xcodeone1')
        exit()
    if numper == 2:
        sublogo()
        target = input(Fore.LIGHTWHITE_EX + Style.BRIGHT + '#Put you target >>')
        sublogo()
        req = requests.get('https://api.hackertarget.com/hostsearch/?q=%s' % target)
        slow(
            Fore.LIGHTWHITE_EX + Style.BRIGHT + "[+] Now Gahter SubDoiman For " + Fore.LIGHTYELLOW_EX + Style.BRIGHT + target)
        slow(Fore.LIGHTWHITE_EX + Style.BRIGHT + '-' * 40)
        data = req.text
        print(Fore.LIGHTGREEN_EX + Style.BRIGHT + data)
        print('\n')
        if data:
            with open('FoundDierctSub.txt', 'a') as x:
                x.write(data + '\n')
        slow(Fore.LIGHTYELLOW_EX + Style.BRIGHT + '# This all SubDomians of this target ˆ_ˆ ')
        slow(Fore.LIGHTYELLOW_EX + Style.BRIGHT + 'Dont Forget Follow My @Xcodeone1')
        exit()
    if numper == 3:
        Pahtlogo()


        def request(url):
            try:
                return requests.get("http://" + url)
            except requests.exceptions.ConnectionError:
                pass


        url = input(Fore.LIGHTWHITE_EX + Style.BRIGHT + "#Target >> ")
        Pahtlogo()
        listfile = input(Fore.LIGHTWHITE_EX + Style.BRIGHT + '#Put Word list >>')
        Pahtlogo()
        slow(
            Fore.LIGHTWHITE_EX + Style.BRIGHT + "[+] Now Show Heddin Path For  " + Fore.LIGHTYELLOW_EX + Style.BRIGHT + url)
        slow(Fore.LIGHTWHITE_EX + Style.BRIGHT + '-' * 40)
        with open(listfile, "r") as word_list:
            for line in word_list:
                word = line.strip()
                path_url = url + "/" + word
                path = request(path_url)
                if path:
                    print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "  [*Found] --> " + path_url)
                    with open('FoundPaths.txt', 'a') as x:
                        x.write(path_url + '\n')
                else:
                    print(Fore.LIGHTRED_EX + Style.BRIGHT + "[ * Not found] --> " + path_url)
                    slow(Fore.LIGHTYELLOW_EX + Style.BRIGHT + '# This all SubDomians of this target ˆ_ˆ ')
                    slow(Fore.LIGHTYELLOW_EX + Style.BRIGHT + 'Dont Forget Follow My @Xcodeone1')
                    exit()
    if numper == 4:
        try:
            os.system('pip3 install -r requirements.txt')
            os.system('clear')
        except:
            R = Fore.LIGHTRED_EX + Style.BRIGHT
            W = Fore.LIGHTWHITE_EX + Style.BRIGHT
            print(
                R + 'Try' + W + 'pip3 install -r requirements.txt' + R + 'or ' + W + 'sudo apt-get install python3-setuptools')
            os.system('clear')
        os.system('clear')
        slow1(R + '''


              /$$$$$$  /$$                           /$$ /$$$$$$$$       /$$ /$$
             /$$__  $$| $$                          | $$| $$_____/      |__/| $$
            | $$  \__/| $$  /$$$$$$  /$$   /$$  /$$$$$$$| $$    /$$$$$$  /$$| $$
            | $$      | $$ /$$__  $$| $$  | $$ /$$__  $$| $$$$$|____  $$| $$| $$
            | $$      | $$| $$  \ $$| $$  | $$| $$  | $$| $$__/ /$$$$$$$| $$| $$
            | $$    $$| $$| $$  | $$| $$  | $$| $$  | $$| $$   /$$__  $$| $$| $$
            |  $$$$$$/| $$|  $$$$$$/|  $$$$$$/|  $$$$$$$| $$  |  $$$$$$$| $$| $$
             \______/ |__/ \______/  \______/  \_______/|__/   \_______/|__/|__/
                                                                       by m0rtem 
                    ''')
        target_Bypass = input(W + "#Target >>")
        os.system('clear')
        os.system('python3 cloudfail.py -t %s ' % target_Bypass)
        os.systeam('clear')
    exit()
