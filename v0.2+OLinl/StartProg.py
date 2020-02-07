 # -*- coding: utf8 -*-
import os
import subprocess
import time 

from flink import browse, misc

stdprog=False
print ("Запуск программ через терминал")
while stdprog == False:
    prog = input("____Progs____\nTeminal\nVSc - VScode\nFirefo\nTor\nSteam\nBlizzard\nNox\nTelegram\nPhotoshop\nYACreader\nXming\nQTDesigner\n____Browse____\nVk.com\nDuckDuckGo\nGoogle\nYoutube\nHabr\nLabworks\nMPT\n____Misc____\nВремя и дата\nIpConfig\n_________________\nExit-выйти\nВвод:")
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
    elif str("qtdesign" and "qt") in prog.lower():
        os.system("cls")
        print("Запуск")
        print("▄▀█ ▀█▀ █▀▄ █▀▀ ▄▀▀ ▀ ▄▀▀░ █▄░█ █▀▀ █▀▀\n█░█ ░█░ █░█ █▀▀ ░▀▄ █ █░▀▌ █░▀█ █▀▀ █▐█▀\n░▀█ ░▀░ ▀▀░ ▀▀▀ ▀▀░ ▀ ▀▀▀░ ▀░░▀ ▀▀▀ ▀░▀▀\n")
        os.startfile(r'C:\Program Files (x86)\Qt Designer\designer.exe')
        input("")
        os.system("cls")
    elif str("xm" and "xming") in prog.lower():
        os.system("cls")
        print("Запуск")
        print("█░█ █▄░▄█ ▀ █▄░█ ▄▀▀░\n▄▀▄ █░█░█ █ █░▀█ █░▀▌\n▀░▀ ▀░░░▀ ▀ ▀░░▀ ▀▀▀░\n")
        os.startfile(r'C:\Program Files (x86)\Xming\Xming.exe')
        input('')
        os.system("cls")
    elif "tor" in prog.lower():
        os.system("cls")
        print("Запуск")
        print("▀█▀ ▄▀▄ █▀▀▄\n░█░ █░█ █▐█▀\n ░▀░ ░▀░ ▀░▀▀\n")
        os.startfile(r'C:\Users\taibe\Desktop\Tor Browser\Browser\firefox.exe')
        input("")
        os.system("cls")        
    elif "vk" in prog.lower():
        os.system("Cls")
        print("Открыт vk.com")
        browse.vk()
        input("")
        os.system("cls")
    elif "google" in prog.lower():
        os.system("cls")
        print("Открыт goole")
        browse.google()
        input("")
        os.system("cls")
    elif "ddgo" in prog.lower():
        os.system("cls")
        print("Открыт DuckDuckGo")
        browse.duck()
        input("")
        os.system("cls")
    elif "youtube" in prog.lower():
        os.system("cls")
        print ("Открыт youtube")
        browse.youtube()
        input("")
        os.system("cls")
    elif "habr" in prog.lower():
        os.system("cls")
        print("Открыт Habr")
        browse.Habr()
        input("")
        os.system("cls")
    elif "labworks" in prog.lower():
        os.system("cls")
        print("Открыт LabWorks")
        browse.labworks()
        input("")
        os.system("cls")
    elif "mpt" in prog.lower():
        os.system("cls")
        print("Открыт MPT.ru")
        browse.mpt()
        input("")
        os.system("cls")
    elif "time" in prog.lower():
        os.system("cls")
        print("Время и Дата")
        misc.Dateandtime()
        input("")
        os.system("cls")
    elif "ip" in prog.lower():
        os.system("cls")
        os.system("ipconfig /all")
        input("")
        os.system("cls")
    elif "exit" in prog.lower():
        print ("Exit")
        break
    else:
        print ("░▐█▀▀▒▐█▀▀▄▒▐█▀▀█▌▒▐█▀▀▄\n░▐█▀▀▒▐█▒▐█▒▐█▄▒█▌▒▐█▒▐█\n░▐█▄▄▒▐█▀▄▄▒▐██▄█▌▒▐█▀▄▄\n")
        os.system("cls")