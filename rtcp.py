import requests, re, time, getpass, os, random

from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init()

def main():    
    url = '192.168.1.133/index.php'
    print(f"{Fore.CYAN}Connection to: {Fore.GREEN}"+ url)
    print(f"{Fore.WHITE}")
    username = input("Username: ")
    password = getpass.getpass("Password: ")
        
    def auth():
        result = requests.post(url, data={'user_login': username, 'user_password': password})
        return result.text
        
    authorization = auth()

    if( authorization == '{"Authorization":"Wellcome, '+username+'!"}' ):
        
        print(f"{Fore.CYAN}Write '!help' for get instructions.{Style.RESET_ALL}")        
        while( authorization == '{"Authorization":"Wellcome, '+username+'!"}' ):
            shell = input(username+"@")
            shell_result = requests.post(url, data={'user_login': username, 'user_password': password, 'shell': shell})
            quite = shell_result.text
            print(f"{Fore.WHITE}"+ quite)
            print(f"{Fore.CYAN}")

            result = quite.find('{"Authorization":"Disconnect..."}')

            if (quite.find('{"Authorization":"Disconnect..."}') != -1):
                print(f"{Fore.MAGENTA}Disconnect...{Style.RESET_ALL}")
                del authorization
                main()
            else:
                print ("")

            if (quite.find('{"Authorization":"Accept denied!","Your access token":null}') != -1):
                print(f"{Fore.RED}Your token has been removed!")
                print(f"{Style.RESET_ALL}")
                exit(0)
            else:
                print ("")

            if (quite.find('User not found!{"Authorization":"Accept denied!"}') != -1):
                print(f"{Fore.RED}Your token has been removed!")
                print(f"{Style.RESET_ALL}")
                exit(0)
            else:
                print ("") 
            if (quite.find('{cls}') != -1):
                os.system('cls')
            else:
                print ("")

            if (quite.find('{exit}') != -1):
                print(f"{Fore.MAGENTA}Disconnect...")
                exit(0)
            else:
                print ("")

    else:
        print(authorization)
        del authorization
        main()

if __name__ == "__main__":
    try:
        main()
    except Exception:
        os.system('cls')
        print(f"{Fore.RED}\t\t\t\t\t\tError to connection!")
        print(f"{Fore.RED}\t\t\t\t\t\tError to connection!")
        print(f"{Fore.RED}\t\t\t\t\t\tError to connection!")
