import webbrowser
import datetime

now = datetime.datetime.now()

class browse():
    @staticmethod
    def vk():
        webbrowser.get(using=None).open_new_tab('https://vk.com')
    @staticmethod
    def duck():
        webbrowser.get(using=None).open_new_tab('https://duckduckgo.com')
    @staticmethod   
    def google():
        webbrowser.get(using=None).open_new_tab('https://google.com')
    @staticmethod
    def youtube():
        webbrowser.get(using=None).open_new_tab('https://youtube.com')
    @staticmethod
    def Habr():
        webbrowser.get(using=None).open_new_tab('https://habr.com/ru/')
    @staticmethod
    def labworks():
        webbrowser.get(using=None).open_new_tab('http://labworks.mpt.ru/')
    @staticmethod
    def mpt():
        webbrowser.get(using=None).open_new_tab("https://mpt.ru/")
class misc():
    @staticmethod
    def Dateandtime():
        print(now.day,".",now.month,",",now.year,"Time:",now.hour,":",now.minute,":",now.second)  

        
