 # -*- coding: utf8 -*- 
import os
import subprocess
import time 

stdprog=False
print ("Запуск программ через терминал")
while stdprog == False:
    prog = input("Teminal\nVSc - VScode\nFirefox\nSteam\nBlizzard\nNox\nTelegram\nPhotoshop\nYACreader\nExit-выйти\nВвод:")
    if "vsc" in prog.lower():
        os.system("cls")
        print("Запуск ")
        print("╔╗──╔╗╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗\n║╚╗╔╝║║╔═╗║║╔═╗║║╔═╗║╚╗╔╗║║╔══╝\n ╚╗║║╔╝║╚══╗║║─╚╝║║─║║─║║║║║╚══╗\n─║╚╝║─╚══╗║║║─╔╗║║─║║─║║║║║╔══╝\n─╚╗╔╝─║╚═╝║║╚═╝║║╚═╝║╔╝╚╝║║╚══╗\n──╚╝──╚═══╝╚═══╝╚═══╝╚═══╝╚═══╝")
        os.startfile(r'C:\Users\taibe\AppData\Local\Programs\Microsoft VS Code\Code.exe')
        input("")
        os.system("cls")
    elif "firefox" in prog.lower():
        os.system("cls")
        print("Запуск ")
        print("─╔═╗──────────╔═╗────────\n─║╔╝──────────║╔╝────────\n╔╝╚╗╔╗╔═╗╔══╗╔╝╚╗╔══╗╔╗╔╗\n╚╗╔╝─╣║╔╝║║═╣╚╗╔╝║╔╗║╚╬╬╝\n─║║─║║║║─║║═╣─║║─║╚╝║╔╬╬╗\n─╚╝─╚╝╚╝─╚══╝─╚╝─╚══╝╚╝╚╝")
        os.startfile(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
        input("")
        os.system("cls")
    elif "steam" in prog.lower():
        os.system("cls ")
        print ("Запуск")
        print ("▄▀▀ ▀█▀ █▀▀ ▄▀▄ █▄░▄█\n░▀▄ ░█░ █▀▀ █▀█ █░█░█\n▀▀░ ░▀░ ▀▀▀ ▀░▀ ▀░░░▀\n")
        os.startfile(r'Z:\Steam\Steam.exe')
        input("")
        os.system("cls")
    elif "blizzard" in prog.lower():
        os.system("cls")
        print("Запуск")
        print("╔══╗─╔═══╗╔════╗╔════╗╔╗───╔═══╗╔═╗─╔╗╔═══╗╔════╗\n║╔╗║─║╔═╗║║╔╗╔╗║║╔╗╔╗║║║───║╔══╝║║╚╗║║║╔══╝║╔╗╔╗║\n║╚╝╚╗║║─║║╚╝║║╚╝╚╝║║╚╝║║───║╚══╗║╔╗╚╝║║╚══╗╚╝║║╚╝\n║╔═╗║║╚═╝║──║║────║║──║║─╔╗║╔══╝║║╚╗║║║╔══╝──║║──\n║╚═╝║║╔═╗║──║║────║║──║╚═╝║║╚══╗║║─║║║║╚══╗──║║──\n╚═══╝╚╝─╚╝──╚╝────╚╝──╚═══╝╚═══╝╚╝─╚═╝╚═══╝──╚╝──\n")
        os.startfile(r'C:\Program Files (x86)\Battle.net\Battle.net Launcher.exe')
        input("")
        os.system("cls")
    elif "Nox" in prog.lower():
        os.system("cls")
        print("Запуск")
        print("╔═╗─╔╗╔═══╗╔═╗╔═╗\n║║╚╗║║║╔═╗║╚╗╚╝╔╝\n║╔╗╚╝║║║─║║─╚╗╔╝─\n ║║╚╗║║║║─║║─╔╝╚╗─\n ║║─║║║║╚═╝║╔╝╔╗╚╗\n ╚╝─╚═╝╚═══╝╚═╝╚═╝\n")
        os.startfile(r'C:\Program Files (x86)\Nox\bin\Nox.exe')
        input("")
        os.system("cls")
    elif str("telegram" and "telega") in prog.lower():
        os.system("cls")
        print("Запуск")
        print("▀█▀ █▀▀ █░░ █▀▀ ▄▀▀░ █▀▀▄ ▄▀▄ █▄░▄█\n░█░ █▀▀ █░▄ █▀▀ █░▀▌ █▐█▀ █▀█ █░█░█\n░▀░ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀░ ▀░▀▀ ▀░▀ ▀░░░▀\n")
        os.startfile(r'C:\Users\taibe\AppData\Roaming\Telegram Desktop\Telegram.exe')
        input("")
        os.system("cls")  
    elif "photoshop" in prog.lower():
        os.system("cls")
        print("Запуск")
        print("╔══╗╔╗───────╔╗─────────╔╗──────╔══╗\n║╔╗║║║──────╔╝╚╗────────║║──────║╔╗║\n ║╚╝║║╚═╗╔══╗╚╗╔╝╔══╗╔══╗║╚═╗╔══╗║╚╝║\n║╔═╝║╔╗║║╔╗║─║║─║╔╗║║══╣║╔╗║║╔╗║║╔═╝\n║║──║║║║║╚╝║─║╚╗║╚╝║─══║║║║║║╚╝║║║──\n╚╝──╚╝╚╝╚══╝─╚═╝╚══╝╚══╝╚╝╚╝╚══╝╚╝──\n")
        os.startfile(r'C:\Program Files\Adobe\Adobe Photoshop 2020\Photoshop.exe')   
        input("")
        os.system("cls")
    elif str("yac" and "yreader" and "yacreader") in prog.lower():
        os.system("cls")
        print("Запуск")
        print("▀▄░▄▀ ▄▀▄ ▄▀ █▀▀▄ █▀▀ ▄▀▄ █▀▄ █▀▀ █▀▀▄\n░░█░░ █▀█ █░ █▐█▀ █▀▀ █▀█ █░█ █▀▀ █▐█▀\n░░▀░░ ▀░▀ ░▀ ▀░▀▀ ▀▀▀ ▀░▀ ▀▀░ ▀▀▀ ▀░▀▀\n")
        os.startfile(r'C:\Program Files\YACReader\YACReader.exe') 
        input("")
        os.system("cls")
    elif str("term" and "cmd") in prog.lower():
        os.system("cls")
        print ("Запуск")
        print("▀█▀ █▀▀ █▀▀▄ █▄░▄█\n░█░ █▀▀ █▐█▀ █░█░█\n░▀░ ▀▀▀ ▀░▀▀ ▀░░░▀\n ")
        os.startfile(r'C:\Windows\system32\cmd.exe')
        input("")
        os.system("cls")
    elif "exit" in prog.lower():
        print ("Exit")
        break
    else:
        print ("░▐█▀▀▒▐█▀▀▄▒▐█▀▀█▌▒▐█▀▀▄\n░▐█▀▀▒▐█▒▐█▒▐█▄▒█▌▒▐█▒▐█\n░▐█▄▄▒▐█▀▄▄▒▐██▄█▌▒▐█▀▄▄\n")