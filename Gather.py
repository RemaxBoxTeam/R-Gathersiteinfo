import requests
from pyfiglet import Figlet
import socket
import colorama
from pprint import pprint
rd = colorama.Fore.RED
cv = colorama.Fore.WHITE
gn = colorama.Fore.GREEN
mag = colorama.Fore.MAGENTA
print (mag + Figlet(font="standard").renderText("Remax Box"))
print (gn + "Created By Maximum Radikali")
selector = input(rd+'Please Enter Your Choice That You Want:\n-1 ip\n-2 site\n\n-> ')

if selector == "1":
    ip = input(gn + "Enter a IP Address :")
    print (cv + "IP Address is "+ip)
    fl = requests.get(f"http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,queryDEMO")

    print(gn + fl.text + cv)
elif selector == "2":
    host = input(rd + "Enter a site without http://  -> ")

    print (cv + "Ip address is : " + socket.gethostbyname(host))

    ip = socket.gethostbyname(host)
    fl = requests.get(f"http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,queryDEMO")

    print(gn + fl.text + cv)
else:
    print (rd + "Invalid option !\n Try run again this script")
    exit()
