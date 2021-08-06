import requests 
import os
import time as t 
import sys 
import json 
from datetime import datetime
import colorama 
from colorama import Fore 
from colorama import init 




def restart_program():
   python = sys.executable
   os.execl(python, python, * sys.argv)
   curdir = os.getcwd()


def retrieve_messages(channelid):
    headers = {
        'authorization': 'YOUR KEY'
    }
    
    r = requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages', headers=headers)
    jsonn = json.loads(r.text)
    for value in jsonn:
        t.sleep(1)
        print(Fore.RED+"")
        print("[CREDITS AKA ME] ===> ArkAngeL43 ")
        print(Fore.RED+"[INFO] ===> " + str(datetime.now()))
        t.sleep(1)
        print(Fore.BLUE+"")
        print(value, '\n')
        jsonFile = open("data.json", "w")
        jsonFile.write(f"{r.text}\n")
        jsonFile.close()
        restart_program()
        # if want just the content 

retrieve_messages('855499460511793196')





################# TO EXPERIMENT ######################
''''
how to use| 

its simple as hell, go into your account

enable developer tools

hit F12

send a message to someone with the F12 or DEV tools up

then search for something that says Authorization 

copy and paste it in 

def retrieve_messages(channelid):
    headers = {
        'authorization': 'ODcxODMwNTA0Mzg5ODk4MzAx.YQzQsA.XmI9iW7zw6sdbX08DIqRWCxVDIE'
    }
    ###########################################################################################

########################################EXPERIMENT WITH IT######################################

# USE YOU UID AND AUTH KEY 

join the lofi girl server 

link | https://discord.com/invite/lofigirl

find a channel thats  appealing, active, or very sparky 

find the channels ID to do this you go to 

F12 or the dev tools and or inspect element 

go to network 

then when a message is send hit one that has code 200 on it 

then go to the header and copy and past the number it should look like this 

779297935275458630

and here is an example for you to use and or work on 
LISt

715497168957603840

414991299280633865

779297935275458630

713630598165692416

860383815343538216

'''



