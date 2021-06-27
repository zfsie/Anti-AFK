class SELFBOT():
    __linecount__ = 69
    __version__ = 4.0
import discord, subprocess, sys, time, os, colorama, ctypes, json, requests, random, pytz
from re import findall
from json import loads, dumps
from base64 import b64decode
from subprocess import Popen, PIPE
from urllib.request import Request, urlopen
from datetime import datetime
from threading import Thread
from time import sleep
from sys import argv
from colorama import Fore, Style
from discord.ext import commands
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
tz_NY = pytz.timezone('America/New_York')
datetime_NY = datetime.now(tz_NY)

def clear():
    os.system('cls')

clear()

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"))


def OnOpen():
    print(f'''
{Fore.WHITE}                        ┌─┐┌┐┌┌┬┐┬  ┌─┐┌─┐┬┌─  ┌─┐┬ ┬┌─┐┌─┐┬┌─
                        {Fore.MAGENTA}├─┤│││ │ │  ├─┤├┤ ├┴┐  │  ├─┤├┤ │  ├┴┐
                        {Fore.LIGHTWHITE_EX}┴ ┴┘└┘ ┴ ┴  ┴ ┴└  ┴ ┴  └─┘┴ ┴└─┘└─┘┴ ┴
{Fore.MAGENTA}                        ┍━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┑
                    {Fore.WHITE}               Created By: {Fore.MAGENTA}Zordo
                              {Fore.WHITE}Enter Your {Fore.MAGENTA}Token{Fore.WHITE} To Continue
                        {Fore.MAGENTA}┕━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┙
''')
OnOpen()

token = input(f'{Fore.WHITE}Enter {Fore.MAGENTA}Token:{Fore.WHITE} ')
responsez = input(f'{Fore.WHITE}Enter {Fore.MAGENTA}Response:{Fore.WHITE} ')
delaybz = input(f'{Fore.WHITE}Enter {Fore.MAGENTA}Delay {Fore.WHITE}(In {Fore.MAGENTA}Seconds{Fore.WHITE}){Fore.MAGENTA}:{Fore.WHITE} ')

clear()

def start():
    print(f'''
{Fore.WHITE}        ┌─┐┌┐┌┌┬┐┬  ┌─┐┌─┐┬┌─  ┌─┐┬ ┬┌─┐┌─┐┬┌─
{Fore.MAGENTA}        ├─┤│││ │ │  ├─┤├┤ ├┴┐  │  ├─┤├┤ │  ├┴┐
{Fore.WHITE}        ┴ ┴┘└┘ ┴ ┴  ┴ ┴└  ┴ ┴  └─┘┴ ┴└─┘└─┘┴ ┴
{Fore.MAGENTA}          ┍━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┑
{Fore.WHITE}                    Dev: {Fore.MAGENTA}Zordo
{Fore.WHITE}                    Login:{Fore.MAGENTA}[{Fore.WHITE}{bot.user.name}{Fore.MAGENTA}#{Fore.WHITE}{bot.user.discriminator}{Fore.MAGENTA}]
{Fore.WHITE}                    Response:{Fore.MAGENTA}[{Fore.WHITE}{responsez}{Fore.MAGENTA}]
{Fore.WHITE}                    Delay:{Fore.MAGENTA}[{Fore.WHITE}{delaybz}{Fore.MAGENTA}]{Fore.WHITE} Sec
{Fore.MAGENTA}          ┕━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┙
''')

@bot.event
async def on_ready():
    os.system(f'title [Anti AFK] - Zordo')
    clear()
    start()

@bot.event
async def on_message(message):
    lowercase = message.content.lower()
    channel = message.channel
    author = message.author
    if (f"<@!{bot.user.id}>" in lowercase) or ('afk' in lowercase) and ('1' in lowercase):
        time.sleep(int(delaybz))
        await message.channel.send(responsez)
        print(f'{Fore.MAGENTA}<{Fore.WHITE}+{Fore.MAGENTA}> {Fore.WHITE}1{Fore.MAGENTA} AFK Check Blocked -> {Fore.WHITE}{message.author} {Fore.MAGENTA}At {Fore.WHITE}', time.strftime("%I:%M:%S"))

while True:
    bot.run(token, bot=False)
