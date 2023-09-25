import pyttsx3
import speech_recognition as sr # sr means string
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5') # sapi5 used to get voice
voices=engine.getProperty('voices')
#     print(voices) # ye show krega ki aapke laptop mai kitni voices hai
#     print(voices[1].id) # voices ki jo id hai girl and boy ki vo print krega
engine.setProperty('voice',voices[1].id)  # engine ki voice property set krega

def speak(audio):  # speak fun AI ko bolne ke liye
    engine.say(audio) # engine audio bolega
    engine.runAndWait()

def wishMe():
   hour=int(datetime.datetime.now().hour)
   if hour>=0 and hour<12:   # means subha ho rahi hai
      speak("Good Morning Sakshi!")
   elif hour >=12 and hour<18:
    speak("Good Afternoon Sakshi!")
   else:
    
    speak("Good Evening Sakshi!")
  
   speak("I am jarvis sakshi Please tell me how may I help you?")

def takeCommand():   # it takes microphone i/p from user and returns string o/p
  r=sr.Recognizer()  # this class help us to recognize audio
  with sr.Microphone() as source:
    print("Listening....")  # listening kiv ki user ko pata chale ki sun raha hai
    r.energy_threshold = 200  # minimum audio energy to consider for recording
    r.pause_threshold=1  # bolte huye agar ham ruk jaye to 1sec tak wait krna uske bad bolna complete ho gaya he pretend krta hai
    audio=r.listen(source)

  try: # try tab krte hai jab hame lagta hai error aa sakta hai
      print("Recognizing...")
      query=r.recognize_google(audio,language='en-in') # en-in  english india
      print(f"user said: {query}\n ")
  except Exception as e:
    # print(e)
    print("Say that again please..")
    return "None" # return none string if any problem comes
  return query
# takecommand ek audio ko le raha hai and usse ek string ke form mai return kr raha hai 
   
if __name__=="__main__":
  wishMe()   # here I am calling wishMe fun
  while True:  # while true bar bar listen krega

# if 1:  # prog ek bar run hoga ani stop ho jayega

    query=takeCommand().lower()  
# lower com se jo bhi query ham de rahe hai vo lower case mai likhe to bhi query se match krega

# logic on executing tasks based on query
    if 'wikipedia' in query:
        speak('searching wikipedia...')
        query=query.replace('wikipedia',"") # hamne jo sentence bola hai usme wekipedia hai to use hata kr bki ki info bol do
        results=wikipedia.summary(query,sentences=2) 
#          setences=2 means search ke according kitne sentence ki info padhni hai
        speak("According to wilipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
       webbrowser.open("youtube.com")

    elif 'open google' in query:
       webbrowser.open("google.com")
    
    elif 'open stackoverflow' in query:
       webbrowser.open("stackoverflow.com")
    
    elif 'play music' in query:
       music_dir ='C:\\SAKSHI\\music'  # \\ for escape char 
# escape char means to insert char that is illegal in string
       songs=os.listdir(music_dir) # listdir list all the songs in music_dir
       print(songs)
       os.startfile(os.path.join(music_dir,songs[0])) # music_dir mese 1st song play krega bcoz we mention it as songs[0]

    elif 'the time' in query:
       strtime=datetime.datetime.now().strftime("%H:%M:%S")
       speak(f"The time is {strtime}")
       
    elif 'open code' in query:
      codepath="C:\\Users\\sw\\AppData\\Local\\Programs\\Microsoft VS Code"
      os.startfile(codepath)


          
