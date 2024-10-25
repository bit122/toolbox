import aps
import colorama
from colorama import Fore, Style
import time
import calendar

colorama.init(autoreset=True)



ntwork_banner = """




  _   _ ______ _________          ______  _____  _  __
 | \ | |  ____|__   __\ \        / / __ \|  __ \| |/ /
 |  \| | |__     | |   \ \  /\  / / |  | | |__) | ' / 
 | . ` |  __|    | |    \ \/  \/ /| |  | |  _  /|  <  
 | |\  | |____   | |     \  /\  / | |__| | | \ \| . \ 
 |_| \_|______|  |_|      \/  \/   \____/|_|  \_\_|\_\
                                                      
                                                      

                                                                                                                                                                                                                                                                               
"""

intro = """
            made by bit122 
            you can find me on github
            

"""


banner = """

 ______   ______     ______     __         ______     ______     __  __    
/\__  _\ /\  __ \   /\  __ \   /\ \       /\  == \   /\  __ \   /\_\_\_\   
\/_/\ \/ \ \ \/\ \  \ \ \/\ \  \ \ \____  \ \  __<   \ \ \/\ \  \/_/\_\/_  
   \ \_\  \ \_____\  \ \_____\  \ \_____\  \ \_____\  \ \_____\   /\_\/\_\ 
    \/_/   \/_____/   \/_____/   \/_____/   \/_____/   \/_____/   \/_/\/_/ 
                                                                           

"""

more_tools = """

    __    __     ______     ______     ______        ______   ______     ______     __         ______    
   /\ "-./  \   /\  __ \   /\  == \   /\  ___\      /\__  _\ /\  __ \   /\  __ \   /\ \       /\  ___\   
   \ \ \-./\ \  \ \ \/\ \  \ \  __<   \ \  __\      \/_/\ \/ \ \ \/\ \  \ \ \/\ \  \ \ \____  \ \___  \  
    \ \_\ \ \_\  \ \_____\  \ \_\ \_\  \ \_____\       \ \_\  \ \_____\  \ \_____\  \ \_____\  \/\_____\ 
     \/_/  \/_/   \/_____/   \/_/ /_/   \/_____/        \/_/   \/_____/   \/_____/   \/_____/   \/_____/ 
                                                                                                         
"""


def start():
    print(Fore.GREEN + intro)
    main_menu()

def main_menu_start():
    print(Fore.MAGENTA + banner)

def main_menu():
    time.sleep(1)
    main_menu_start()
    time.sleep(2)
    aps.clear_screen()
    time.sleep(1)
    print(Fore.LIGHTMAGENTA_EX + "Welcome to the Main Menu!")
    print(Fore.LIGHTMAGENTA_EX + "[0] calendar")
    print(Fore.LIGHTMAGENTA_EX + "[1] open application")
    print(Fore.LIGHTMAGENTA_EX + "[2] close an application")
    print(Fore.LIGHTMAGENTA_EX + "[3] open notepad")
    print(Fore.LIGHTMAGENTA_EX + "[4] name")
    print(Fore.LIGHTMAGENTA_EX + "[5] more")
    print(Fore.LIGHTMAGENTA_EX + "[6] exit")

    choice = input(Fore.LIGHTMAGENTA_EX + "Enter your choice (1-5): ")

    if choice == '1':
        option1()
    elif choice == '0':
        option5()
    elif choice == '2':
        option2()
    elif choice == '3':
        option3()
    elif choice == '4':
        option4()
    elif choice == '5':
        aps.clear_screen()
        more_options()
    elif choice == '6':
        print("closing")
        return
    else:
        print("Invalid choice. Please try again.")
        main_menu()

def option1():
    print("You have selected Option 1.")
    time.sleep(0.5)
    aps.open_app()
    main_menu()

def option2():
    print("You have selected Option 2.")
    time.sleep(0.5)
    aps.app_closer()
    main_menu()

def option3():
    print("You have selected Option 3.")
    time.sleep(0.5)
    aps.note()
    main_menu()

def option4():
    print(Fore.GREEN + "this is your name")
    aps.name()
    main_menu()

def option5():
    print(calendar.calendar(2024))
    main_menu()


def more_options():
    print(Fore.LIGHTRED_EX + more_tools)
    print(Fore.LIGHTYELLOW_EX + "[1] os release")
    print(Fore.LIGHTYELLOW_EX + "[2] processor type")
    print(Fore.LIGHTYELLOW_EX + "[3] network options")
    print(Fore.LIGHTYELLOW_EX + "[4] architecture")
    print(Fore.LIGHTYELLOW_EX + "[5] machine type")
    print(Fore.LIGHTYELLOW_EX + "[6] task manager")
    print(Fore.LIGHTYELLOW_EX + "[7] resource monitor")
    print(Fore.LIGHTYELLOW_EX + "[99] go back ")
    time.sleep(1)
    print(Fore.CYAN + "pick an option 1 - 8 or type 99 to go back")
    time.sleep(1)

    choice = input(">>> ")
    if choice == '1':
        print(Fore.GREEN + "release is ")
        aps.rel()
        yn()
    elif choice == '2':
        print(Fore.GREEN + "you processor is")
        aps.pro()
        yn()
    elif choice == '3':
        network()
        yn()
    elif choice == '4':
        print(Fore.GREEN + "your architecure is ")
        aps.arc()
        yn()
    elif choice == '5':
        print(Fore.GREEN + "your machine type is ")
        aps.mac()
        yn()
    elif choice == '6':
        print("starting task manager")
        aps.tmg()
        yn()
    elif choice == '7':
        print(Fore.GREEN + "starting resouce monitor ")
        aps.remon()
        yn()
    elif choice == '99':
        main_menu()
    else:
        print("thats not an allowed number please try again")
        aps.clear_screen()
        more_options()



def yn():
    print(Fore.YELLOW + "do you want to go back to the  menu? ")
    choice = input("Y/N :> ")
    if choice == 'y':
        print(Fore.LIGHTRED_EX + "okay")
        aps.clear_screen()
        more_options()
    elif choice == 'Y':
        print("okay")
        aps.clear_screen()
        more_options()
    elif choice == 'n':
        print("okay good bye")
        return
    elif choice == 'N':
        print("okay goodbye")
        return
    else:
        print("thats not a valid option please try again")
        aps.clear_screen()
        yn()



def network():
    aps.clear_screen()
    time.sleep(1)
    print(Fore.LIGHTBLUE_EX + ntwork_banner)


start()