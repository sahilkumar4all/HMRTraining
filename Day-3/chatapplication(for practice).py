from datetime import datetime as dt
import webbrowser
import os
import random
import bs4
import urllib.request as url
hellointent=["hello" ,"hey" ,"hi there",'hi' ,"hey there" ,"Hello there","hola","howdy"]
musicintent=["play music" ,"play" , "start music",'music please']
news_intent=['news','start news','whats the news','news please']
show_music_intent=['show songs','list songs','display songs','display playlist','playlist please']
sportsintent = ['sports','sports news','tell me sports news','whats the Sports news','sports news please']
Entertainment_intent = ['entertainment','entertainment news','tell me entertainment news','whats the entertainment news','entertainment news please']
Business_intent = ['business','business news','tell me Business news','whats the Business news','Business news please']
Health_intent = ['health','health news please','health news','tell me health news','whats the health news']
time_intent=['time please','show me the time','whats the time','tell me the time','current time']
date_intent=['date please','show me the date','whats the date','tell me the date','current date']
chat= True
while(chat):
    msg=input("Enter message : ")
    if msg in hellointent:
        print("hello User")
    elif msg.startswith("open"):
            web= msg.split()[-1]
            webbrowser.open(web+'.com')
    elif msg in musicintent:
        os.chdir('C:\\Users\\SAHIL\\Music\\musics')
        s=random.choice(os.listdir())
        os.startfile(s)
    elif msg in show_music_intent:
        os.chdir('C:\\Users\\SAHIL\\Music\\musics')
        songs=os.listdir()
        for i in range(1,len(songs)):
             print(i , songs[i])
        play = int(input("enter song you wanna play:"))
        os.startfile(songs[play])      
 
    elif msg=="bye":
        print("Bye User")
        chat=False
    elif msg in news_intent:
        path="https://edition.cnn.com"
        httprequest=url.urlopen(path)
        page1=bs4.BeautifulSoup(httprequest, 'lxml')
        a = page1.findAll('a', class_='nav-menu-links__link')
        
        news = True
        while news:
            choice = input("enter news category : ")
            if choice in sportsintent:
                Url = path + a[4]['href']
                print("Sports headlines are as follows:")
                
                httprequest=url.urlopen(Url)
                page2=bs4.BeautifulSoup(httprequest, 'lxml')
                sportsnews = page2.findAll('span',class_='cd__headline-text')
                for i in range(10):
                    news=sportsnews[i]
                    print(i+1,news.text)
                print("****************************************")

            elif choice in Business_intent:
                Url = path + a[2]['href']
                print("Business headlines are as follows:")
                
                httprequest=url.urlopen(Url)
                page2=bs4.BeautifulSoup(httprequest, 'lxml')
                Businessnews = page2.findAll('span',class_='cd__headline-text')
                for i in range(10):
                    news=Businessnews[i]
                    print(i+1,news.text)
                print("****************************************")


                
            elif choice in Entertainment_intent:
                 Url = path + a[3]['href']
                 print("Entertainment headlines are as follows:")
                 httprequest=url.urlopen(Url)
                 page3=bs4.BeautifulSoup(httprequest, 'lxml')
                 entertainmentnews = page3.findAll('span',class_='cd__headline-text')
                 for i in range(10):
                      news=entertainmentnews[i]
                      print(i+1,news.text)
                 print("****************************************")

            elif choice in Health_intent:
                 Url = path + a[7]['href']
                 print("health headlines are as follows:")
                 httprequest=url.urlopen(Url)
                 page4=bs4.BeautifulSoup(httprequest, 'lxml')
                 healthnews = page4.findAll('span',class_='cd__headline-text')
                 for i in range(10):
                      news=healthnews[i]
                      print(i+1,news.text)
                 print("****************************************")

            else:
                print("Invalid Category.....bye...have a nice day")
                news = False
    
    elif msg in time_intent:
        t= dt.now().time()
        curr_time = t.strftime('%H:%M:%S:%p')
        print("current time is {}".format(curr_time))

    elif msg in date_intent:
        t= dt.now().date()
        print("current Date is {}".format(t))
    else:
        print("i don't understand")
        
