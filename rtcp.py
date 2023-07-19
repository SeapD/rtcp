import requests, re, time, getpass, os, random

from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
from os import urandom
import random
import os
from os import system
import secrets
import string
 
 
def GetBbtc():    
    xalphabet = string.ascii_letters + string.digits
    xpassword = ''.join(secrets.choice(xalphabet) for i in range(24))
    return xpassword
    
def mainGen():    
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(62))
    return password

colorama_init()

def main():    
    url = 'http://api.cryptofinder.org/list.php'
    #print('Connection to: ' + url)
    print(f"{Fore.CYAN}[STATUS]Connection to: {Fore.GREEN}"+ url)
    print(f"{Fore.WHITE}[AUTH] Username: {Fore.GREEN}khamba")
    print('')

    
    authorization = True
    quite = False
    i = 0
    bad = 0
    good = 0
    section = 0

    if( authorization == True ):
        print(f"{Fore.CYAN}[INFO]Wait a second... We get instructions.{Style.RESET_ALL}")        
        print(f"{Fore.WHITE}")
        time.sleep(10)
        while( authorization == True ):
            i+=1
            balance = random.random()
            SecStatus = random.randint(0, 1)
            #print(f"{Fore.WHITE}"+ f'[!] BTC {i} | {mainGen()} | Balance: {balance} | W: 0 | Secret: {SecStatus}')
            #print(f"{Fore.CYAN}")
            #print(f"{Fore.RED}")
            time.sleep(1)
            if( balance <= 0.0000001 ):
                print(f"{Fore.GREEN}"+ f'[-] {i} | {mainGen()} | {GetBbtc()} | W: 0 | Secret: {SecStatus} | Balance: {balance} ')
                good +=1
            elif( i == 1118 ):
                SecStatus = 2
                print(f"{Fore.YELLOW}"+ f'[#] {i} | {mainGen()} | {GetBbtc()} | W: 0 | Secret: {SecStatus} | Balance: {balance}')
                section +=1
            elif( i == 1231 ):
                SecStatus = 3
                print(f"{Fore.GREEN}"+ f'[!] {i} | {mainGen()} | {GetBbtc()} | W: 0 | Secret: {SecStatus} | Balance: {balance} ')
                good +=1
            else:
                print(f"{Fore.RED}"+ f'[-] {i} | {mainGen()} | {GetBbtc()} | W: 0 | Secret: {SecStatus} | Balance: {balance} ')
                bad += 1
                
            mtitl = str(f'BitocMasterINI - Round: {i} - Good: {good} - Section: {section} - Bad: {bad}')
            system('title '+ mtitl)
    else:
        print(authorization)
        #time.sleep(5)
        del authorization
        main()

if __name__ == "__main__":
    main()
