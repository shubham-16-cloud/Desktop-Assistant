import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia as wiki
import webbrowser
import random
import smtplib
import cv2 as cv
import time
import random
import winsound
import requests
from bs4 import BeautifulSoup
import speedtest
import sys
from tkinter import * 
import psutil as ps
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import json
import webbrowser
import urllib.request
import re
from googlesearch import *
from account import *

window = Tk()

window.minsize(900,500)
window.maxsize(900,500)
#window.overrideredirect(True)
window.call('wm', 'iconphoto', window._w, PhotoImage(file='icon.png'))

global var_query
global var

greeting = ['hi','hai','hello']
what_can_do = ['what can you do for me']
song = ['play song','play music','song']
internet =['speed test', 'internet test','test', 'internet speed']

var_query = StringVar()
var = StringVar()

en = pyttsx3.init('sapi5')
voices = en.getProperty('voices')
en.setProperty('voice', voices[0].id)

def speak(audio):
    en.say(audio)
    en.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=11:
        speak("Good Morning")
    elif hour>=12 and hour<=17:
        speak("Good Afternoon")
    elif hour>=18 and hour<=19:
        speak("Good Evening")
    elif hour>=20 and hour<=24:
        speak("Good night")

def speech_command():
        r = sr.Recognizer()
        with sr.Microphone()as s:
            print("Listening......")
            var.set("Listening.....")
            window.update()
            #r.pause_threshold =1
            r.adjust_for_ambient_noise(s,duration=1)
            audio =r.listen(s)
        try:
            print("Recongnize...")
            var.set("Recongnize.......")
            window.update()
            query = r.recognize_google(audio, language='en-in')
            print(f"user said :-{query}\n")
        except Exception as e:
            print(e)
            print("please say again..")
            return 'none'
        var_query.set(query)
        window.update()
        return query

def removeal(query):
    prerpositon = []
    f= open('files\prepositions.txt','r')
    for line in f:
        for word in line.split():
            prerpositon.append(word)
    str1 =""
    word = query.split()
    for words in word:
        if words not in prerpositon:
            #str.append(words +" ")
            str1 += words+' '
    re = str1
    return re

def createjson(idname):
    uname = input("enter name :- ").lower()
    upassword = input("number :- ")
    dict1 = {}
    dict1[uname] = [idname,str(upassword)]
    with open("info.json", "r+") as outfile:
        data = json.load(outfile)
        data.update(dict1)
        outfile.seek(0)
        json.dump(data,outfile)

def writespecial_char(q):
    if 'underscore' in q:
        q = q.replace('underscore','_')
    elif 'at the rate' in q:
        q = q.replace('at the rate','@')
    elif 'dot' in q:
        q = q.replace('dot','.')
    q = q.replace(' ','')
    print(q)
    return q

def readinfo(idname):
    user={}
    with open('info.json', 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)
        for key in json_object.keys():
            list_values = json_object[key]
            if list_values[0] == idname:
                user[key] = list_values[1]
        
        if len(user) > 1:
                speak(f"Sir , i found {str(len(user))} instagram account, what would you open it?")
                var.set(f"usenames :- {list(user.keys())}")
                window.update()
                for user1 in user:
                    speak(user1)
                var.set("Say the username you want to login")
                window.update()
                speak("Say the username you want to login")
                q = speech_command().lower()
                username = writespecial_char(q)
                var.set(username)
                window.update()
                #username = input("Enter the username you want to login :- ").lower()
                if username in user.keys():
                    id = username
                    password=user.get(username)
                else:
                    speak("Sorry sir i didnt fond any of this name, please doit again")
                    id,password =None,None
        else:
            id = next(iter(user))
            password = user.get(str(id))

    return id,password

def weather_fetch(city):
    speak("let me check the weather")
    url = "https://www.google.com/search?q="+"weather%20"+city
    print(url)
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
    var.set(temp + str)
    window.update()
    speak('it is'+temp +', ' + str  )

def sendmail(to, bodytext):
    host = smtplib.SMTP('smtp.gmail.com',587)
    host.ehlo()
    host.starttls()
    host.login('Add your email credential here')
    host.sendmail('email',to, bodytext)
    host.close()

def play():

    wishme()
    speak("Hello Sir,I am Your Assistant, How may I help you?")
    speak(f"Today is {str(dt)}")

    if getbettery()<=40:
        speak(f"Sir your laptop battery is {battery}%, Please, Pluged in Charge")
    while True:
        query = speech_command().lower()
    
        if 'bye' in query:
            speak("Good by sir")
            sys.exit()

        elif 'wikipedia' in query or 'who' in query:
            try:
                result =removeal(query)
                speak("Serching wikipedia")
                var.set("Serching wikipedia")
                window.update()
                result = result.replace('wikipedia','')
                wikiresult = wiki.wikipedia.summary(result, sentences=1)
                speak("According to wikipedia")
                var.set(wikiresult)
                window.update()
                speak(wikiresult)
            except Exception as e:
                print(e)
                print(f"I cant found anythig about {result}")
                speak(f"I cant found anythig about {result}")
        
        elif "who made you" in query or "who created you" in query or "who discovered you" in query:
            var.set("shubham Brahmbhatt")
            window.update()
            speak("Shubham Brahmbhatt")
        
        #Write all the code from previous code
        elif any(x in query for x in song):
            try:
                keyword = removeal(query)
                var.set('playing song')
                speak('Playing song')
                window.update()
                options = webdriver.ChromeOptions()
                options.add_argument("--ignore-certificate-error")
                options.add_argument("--ignore-ssl-errors")
                    #options.add_argument("--headless")
                options.add_argument("--disable-gpu")
                driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
                    #keyword = 'sanm re'
                driver.get(f"https://gaana.com/search/{keyword}")
                btn_song = driver.find_element_by_xpath('//*[@id="new-release-album"]/li[1]/div/div[1]/a/img')
                driver.implicitly_wait(10)
                btn_song.click()
                driver.implicitly_wait(20)
                btn_play = driver.find_element_by_xpath('//*[@id="p-list-play_all"]')
                btn_play.click()
                speak("Loop is breking")
                time.sleep(10)
                window.update()
            except Exception as e:
                print(e)
                driver.close()
        
        elif 'open instagram'in query:
            var.set('opening Instagram')
            window.update()
            speak("Ok sir opeing Instagram")
            id,password = readinfo('in')
            if id != None:
                autologin.instabot(id,password,speak)
        
        elif 'open facebook' in query:
            speak('Ok Sir opeing Facebook')
            var.set('opening Facebook')
            window.update()
            id,password = readinfo('fb')
            if id != None:
                autologin.facebook(id,password,speak)
        
        elif 'youtube' in query:
            var.set('opening Youtube')
            window.update()
            keyword = removeal(query)
            keyword = keyword.replace(" ", '+')
            html = urllib.request.urlopen("https://www.youtube.com/results?search_query="+ keyword)
            video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
            webbrowser.open("https://www.youtube.com/watch?v=" + video_ids[0])
            time.sleep(2)

        elif 'the time' in query:
            d=datetime.datetime.now().strftime("%H:%H:%S")
            var.set(d)
            window.update()
            speak(f"sir, the time is {d}")
        
        elif 'camera' in query:
            var.set('opening Camera')
            window.update()
            try:
                timer = int(5)
                cap = cv.VideoCapture(0)
                speak('Sir get ready for capture picture')
                while True:
                    ret,frame = cap.read()
                    cv.imshow('Capture with AI',frame)
                    cv.waitKey(125)
                    prev = time.time()
                    while timer >= 0:
                        ret,frame = cap.read()
                        font = cv.FONT_HERSHEY_SCRIPT_SIMPLEX
                        cv.putText(frame, str(timer), (50, 200), font, 3, (191,154,154), 8, cv.LINE_AA)
                        cv.imshow('Capture with AI', frame)
                        cv.waitKey(125)
                        winsound.Beep(1300,90)
                        #speak(str(timer))
                        cur = time.time()
                        if cur - prev >= 1:
                            prev = cur
                            timer -= 1      
                    else:
                        ret,frame = cap.read()
                        cv.imshow('Capture with AI',frame)
                        cv.waitKey(1000)
                        cv.imwrite('Add path where you want to save your images',frame)
                        #here you have to write code for track images.
                        speak('your picture saved successfully on your storage')
                        break
                cap.release()
                cv.destroyAllWindows()
            except Exception as e:
                speak("Sorry sir I could't click your pictuer , plese try again")
                cap.release()
                cv.destroyAllWindows()

        elif 'weather' in query:
            var.set('Checking weather..')
            window.update()
            speak('Checking weather..')
            try:
                query = removeal(query)
                if len(query) == 0:
                    speak('Say the name of city')
                    city = removeal(speech_command())
                else:
                    city = query
                weather_fetch(city)
            except Exception as e:
                print(e)
                speak(f"Soory,i did't find weather of your {city} city")

        elif any(x in query for x in internet):
            try:
                time.sleep(1)
                speak("Let me test the internet speed")   
                s= speedtest.Speedtest()
                d= str(s.download())
                u = str(s.upload())
                best_server = s.get_best_server()
                i = dict((k, best_server[k]) for k in ['name', 'latency'] if k in best_server)
                var.set(f"your Download speed is {d[:2]} MBps, upload speed {u[:2]}MBps, latency['latency'] and  server name is {i['name']}")
                window.update()
                speak(f"your Download speed is {d[:2]} MBps, upload speed {u[:2]}MBps, latency['latency'] and  server name is {i['name']}")
                
            except Exception as e:
                print(e)
                speak("sorry Sir, I could't test your internet speed.")

        elif 'email' in query or 'mail' in query:
            if 'send' in query: 
                try:
                    speak("what shoud i say sir?")
                    bodytext = speech_command()
                    sendmail('Email address you want to send email',bodytext)
                    speak("your email has been sent!.")
                except Exception as e:
                    speak("Sorry sir, I am not able to send the email. PLesase try again later.")
            else:
                webbrowser.open("https://mail.google.com/mail")

        elif any(x in query for x in what_can_do):
            read = open('files\what_i_do.txt','r')
            speak(read.read())

        elif 'who are you' in query:
            speak('I am your assistant version 1 point O. I am programmed to minor tasks like'
                  'opening youtube,google chrome, gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                  'In different cities, get top headline news from times of india and you can ask me computational or geographical questions too!')

        elif 'hello' in query:
            reply = ['I am fine, What about you', 'I am good sir','i am doing well']
            n =random.randrange(0,len(reply))
            var.set(reply[n])
            window.update()
            speak(reply[n])

        else:
            if query != 'none':
                query = query
                search_links=[]
                y =search(query, tld="co.in", num=4, stop=4, pause=2)#this line get 4 links from google search
                for j in y:
                    search_links.append(j)
                webbrowser.open(search_links[1])
                time.sleep(1)

def getbettery():
    battery = ps.sensors_battery()
    return battery.percent   

bg1 = PhotoImage(file="r-removebg-preview (1).png")

canvas1 = Canvas(window,width=850,height=550,bg="#262626", bd=-2)
canvas1.pack(fill = "both", expand = True)
#canvas1.create_image( 0, 0, image = bg1, anchor = "nw")

lbl_bg =Label(window,image=bg1,bg='#262626')
lbl_bg.pack()

dt = datetime.date.today()
lbl_datetime = Label(window,bg="#262626",text='Date 📅 \n'+str(dt),fg="white",bd=1,relief=RAISED,font=('Courier', 12))
lbl_datetime.pack()

lbl_battery = Label(window,bg="#262626",text=f"Battery 🔋 \n {str(getbettery())}%",fg="white",bd=1,relief=RAISED,font=('Courier', 12))
lbl_battery.pack(padx=100)

lbl_user = Label(window, textvariable = var_query, bg = '#FAB60C')
lbl_user.config(font=("Courier", 14))
var_query.set('User Said:')
lbl_user.pack()

lbl_input = Label(window, textvariable = var, wraplength=390,justify=CENTER,bg = '#ADD8E6')
lbl_input.config(font=("Courier", 14))
var.set('Welcome')
lbl_input.pack()

window.title('Desktop Assistant')

play = Button(window,text = 'PLAY',width = 20,command =play, bg = '#f5a720')
play.config(font=("Courier", 12))
play.pack()

exit = Button(window,text = 'EXIT',width = 20, command = window.destroy, bg = '#f5a720')
exit.config(font=("Courier", 12))
exit.pack()


#canvas window
user_canvas = canvas1.create_window(480,80,anchor ='nw',window = lbl_user)
input_canvas = canvas1.create_window(480,130,anchor ='nw',window = lbl_input)
play_canvas = canvas1.create_window(200,450,anchor ='nw',window = play)
exit_canvas = canvas1.create_window(500,450,anchor ='nw',window = exit)
bg =canvas1.create_window(10,0,anchor='nw',window=lbl_bg)
date_time = canvas1.create_window(650,5,anchor='nw',window=lbl_datetime)
battery = canvas1.create_window(790,5,anchor='nw',window=lbl_battery)

window.mainloop()
