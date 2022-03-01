from subprocess import run
from subprocess import PIPE
from sys import argv as arg
from requests import get
from mcstatus import MinecraftServer
from colorama import Fore

checkwhitelist = False

def getinfo(ip):
    try:
        server = MinecraftServer(ip, 25565)

        status = server.status()

        return [status.description, status.players.online, round(status.latency, 2)]
    except:
        raise 'error'

run(['clear'])

print('''
    ██▀███   ▄▄▄        ▄████ ▓█████ 
   ▓██ ▒ ██▒▒████▄     ██▒ ▀█▒▓█   ▀ 
   ▓██ ░▄█ ▒▒██  ▀█▄  ▒██░▄▄▄░▒███   
   ▒██▀▀█▄  ░██▄▄▄▄██ ░▓█  ██▓▒▓█  ▄ 
   ░██▓ ▒██▒ ▓█   ▓██▒░▒▓███▀▒░▒████▒
   ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ░▒   ▒ ░░ ▒░ ░
     ░▒ ░ ▒░  ▒   ▒▒ ░  ░   ░  ░ ░  ░
     ░░   ░   ░   ▒   ░ ░   ░    ░   
      ░           ░  ░      ░    ░  ░
'''
    .replace('░', f'{Fore.RED}░')
    .replace('▓', f'{Fore.RED}▓')
    .replace('▒', f'{Fore.RED}▒')
    .replace('█', f'{Fore.LIGHTWHITE_EX}█')
)

def show(ip):
    try:
        data = getinfo(ip)
        motd = data[0].replace('\n', '\\n')
        online = data[1]
        ping = data[2]

        if checkwhitelist == False:
            result = run(f"timeout 5s node bot.js {ip}".split(), stdout = PIPE).stdout.decode('utf-8')
            if ('false' in result):
                whitelist = 'No'
            else:
                whitelist = 'Probably yes'
        else:
            whitelist = 'Unknown'

        print(f'''
  {Fore.WHITE}IP        ║ {Fore.RED}{ip}
  {Fore.WHITE}Motd      ║ {Fore.RED}{motd}
  {Fore.WHITE}Players   ║ {Fore.RED}{online}
  {Fore.WHITE}Ping      ║ {Fore.RED}{ping}
  {Fore.WHITE}Whitelist ║ {Fore.RED}{whitelist}''')
    except:
        pass

if len(arg) == 1:
    print(f'  {Fore.RED}No file selected! {Fore.WHITE}Enabling integrated scraper! ')
    allips = []
    try:
        for line in get('http://k0rnh0l.io/griefbuddy').text.replace('        <p class="ipblue">', '').replace('        <p class="ipred">', '').split('\n'):
            if (line.count('.') == 3) and (':25565' in line):
                ip = line.replace(':25565</p>', '')
                show(ip)
    except:
        pass
else:
    with open(arg[1], 'r') as file:
        print(f'  {Fore.RED}File selected! {Fore.WHITE}Starting scan!')
        for line in file.readlines():
            ip = line.replace('\n', '')
            if ip.count('.') == 3:
                show(ip)