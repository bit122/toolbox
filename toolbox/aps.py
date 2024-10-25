import AppOpener
from AppOpener import open, close
import colorama
from colorama import Fore, Style
import time
import sys
import os
import platform
import nmap





def open_app():
    t = input(Fore.BLUE + "choice> ")
    print(Fore.RED + "opening ", Fore.GREEN + t)
    time.sleep(0.5)
    open(t, match_closest=True)



def app_closer():
    t = input(Fore.BLUE + "choice> ")
    print(Fore.RED + "closing ", Fore.GREEN + t)
    time.sleep(0.5)
    close(t, match_closest=True)



def clear_screen():
    os.system("cls")

def note():
    open("notepad.exe", match_closest=True)


def name():
    os.system("whoami")

def arc():
    platform.architecture()

def mac():
    platform.machine()

def no():
    platform.node()

def pro():
    platform.processor()


def rel():
    platform.release()

def os_system():
    platform.system()

def tmg():
    open("task manager", match_closest=True)

def remon():
    open("resource monitor", match_closest=True)