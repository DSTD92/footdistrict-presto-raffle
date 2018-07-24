import requests
from random import getrandbits
import time
from colorama import Fore, Back, Style
from colorama import init
init(autoreset=True)
requests.packages.urllib3.disable_warnings()

print "\n"
print (Fore.YELLOW + " Made by https://twitter.com/thebotsmith")
print "\n"
posturl = "https://footdistrict.typeform.com/app/form/submit/zyWFlA"

count = 1

postheaders= {
    "Origin": "https://www.typeform.com/",
    "Upgrade-Insecure-Requests": "1",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
    "Accept": "application/json",
    "Referer": "http://jumpman.amongstfew.com/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
    }


# x IS THE AMOUNT OF ENTRIES YOU WANT. MAY HAVE TO USE PROXIES IF DOING 100S/1000S
# ts IS THE TIME SLEEP VALUE INCASE YOU WANT TO BE CAREFUL ABOUT IP BANS DO NOT LOWER UNDER 1 SECOND
#DEFAULT IS 2 SECONDS

x = raw_input("how many extries do you want? : ")
ts = raw_input("please select a delay in seconds (default 2) : " )

if ts == "":
    ts = 2
#CHANGE THESE VALUES TO YOURS
name = "YOUR NAME"
size = "10 US - 44 EU" #TODO whole sizes only and in this format
instagram = "YOUR INSTA USERNAME" # TODO make sure you follow them https://www.instagram.com/footdistrict/

for i in range(int(x)):


    email = 'PUT YOUR EMAIL ADDRESS HERE WITHOUT SPACESho+{}@gmail.com'.format(getrandbits(40)) # CHANGE YOUR.EMAIL.HERE to your email prefix. don't change the +{} after.

    postdata = {
        "form[textfield:q6RKK7bF6ebf]":instagram, #TODO change this
        "form[list:BiEUnJf6bgtk][choices]":"English",
        "form[list:BiEUnJf6bgtk][other]":"",
        "form[textfield:vJ2FTdN6cZTS]":name,
        "form[email:STr1mGLl3zU3]": email,
        "form[dropdown:WKVUeu71TT3i]":size, #TODO change this
        "form[terms:MZhWSE3hdm5q]":"true",
        "form[terms:hS1EMadZN128]":"true",
        "form[token]":"517b14953b3ea760b996624d78f151bd$2y$11$e2dJZC0zIXZQK1pxbSZbL.y0oj6kjdjd9qMgYfYS9jgmTz9tc2B/C",#They dont even check this value lol
        "form[landed_at]":"1532429341",
        "form[language]":"en"
        }

    r = requests.post(posturl,headers=postheaders,verify=False,data=postdata)

    if '"message":"success"' in r.text:
        print (Fore.GREEN + "Entry {}/{} successful with {}".format(count,int(x),email))
    else:
        print (Fore.RED +"Failed using {}".format(email))
    print "sleeping for {} seconds".format(int(ts))
    time.sleep(int(ts))
