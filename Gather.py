import requests
from pyfiglet import Figlet
import socket
import colorama

rd = colorama.Fore.RED
cv = colorama.Fore.WHITE
gn = colorama.Fore.GREEN
mag = colorama.Fore.MAGENTA
print (mag + Figlet(font="standard").renderText("Remax Box>
print (gn + "Created By Maximum Radikali")

host = input(rd + "Enter a site without http://  -> ")

print (cv + "Ip address is : " + socket.gethostbyname(host>


fl = requests.get("https://ipinfo.io/"+socket.gethostbynam>

print (fl.text)
