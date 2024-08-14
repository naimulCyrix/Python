import pyttsx3
import requests
import json 
engine =pyttsx3.init('sapi5')

voices =engine.getProperty('voices')
#print(voice)
engine.setProperty('voice',voices[0].id)
#print(voice[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

if __name__=="__main__":
     speak("Hello welcome to Jamuna Tv")

     url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=cd5842620c42437092b1313aceae9061"
     news = requests.get(url).text
     news = json.loads(news)
     print(news["totalResults"])
     arts = news['articles']
     for article in arts:
          print(article['author'])
          speak(article['author'])
          print(article['title'])
          speak(article['title'])
          print(article['description'])
          speak(article['description'])
          speak("Moving on to the next news")

          
     
