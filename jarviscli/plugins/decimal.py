from plugin import plugin

from colorama import Fore


@plugin("revert_binary")

def rev_binary(jarvis,s):
    """
    Convert Binary number in Decimal Base
    """
    if s=="":
        s = jarvis.input("What's your number in binary ? ")
        cpt = 0
        for i in range(len(s)):
            if s[-1-i]=="1" or s[-1-i]=="0":
                cpt+=(int(s[-1-i]))*2**i
            else :
                jarvis.say("It's not a number in binary")
                return
        jarvis.say(str(cpt),Fore.GREEN)

@plugin("revert_hex")




def rev_hex(jarvis,s):
    """
    Convert Hexadecimal number in Decimal Base
    """
    dict_hex={
    "0":0, 
    "1":1,
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,
    "A":10,
    "B":11,
    "C":12,
    "D":13,
    "E":14,
    "F":15
    }   
    if s=="":
        s = jarvis.input("What's your number in hexadecimal ? ")
        cpt = 0
        for i in range(len(s)):
            if s[-1-i].upper() in dict_hex.keys():
                cpt+=(dict_hex[s[-1-i].upper()])*16**i
            else :
                jarvis.say("It's not a number in hexadecimal")
                return
        jarvis.say(str(cpt),Fore.GREEN)
    
        