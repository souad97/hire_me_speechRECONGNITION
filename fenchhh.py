# coding: utf-8
import speech_recognition as sr
from time import ctime
import time
import webbrowser
import pyttsx3


def assistant_voix(sortie):
    if sortie != None:
        voix = pyttsx3.init()
        rate = voix.getProperty('rate')   # getting details of current speaking rate
        voix.setProperty('rate', 170)     # setting up new voice rate

        print("A.I : " + sortie)
        voix.say(sortie)
        voix.runAndWait()

def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source :
        assistant_voix("qu'est que tu veut")
        audio = r.listen(source)
        
    data =""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio,language='fr-FR')
        assistant_voix("un moment s'il vous plait")
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        #assistant_voix("i cna't understand what you say , repeat ")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return data

def rec(data):
    if "nom" in data:
        assistant_voix("je suis souad nissabouri")

    if "stage" in data:
        assistant_voix(" j'ai un stage d'observation au 2018 dans la sociéte NABC casablanca , dans le département du plannification et logistique  au cours de ce stage j'ai connu plusieurs fonctionnemnt de production et savoir les taches correspondante")

    if "tu cherches" in data:
        assistant_voix("je suis en cherche active  d'un stage thecnique du durée 2 mois juillet et aout ")

    if "projets" in data :
        assistant_voix("j'ai fais plusieurs projets academique mais je vais partager avec vous les plus immportantes suivantes : smart meter , face reservation , train system tracking ")

    if "domaine" in data:
        assistant_voix("je veux un stage dans les domaines suivants : électrothecnique , électronique , instrumentation , automobile , embarqué , électrique et automatique ")

    if "présentez-vous" in data:
        assistant_voix("je suis élève ingénieure en génie électrique et systèmes embarqués à l'école nationale des sciences appliquées du khouribga ,j'ai 23 ans et j'habite à casablanca") 

    if "what time is it" in data:
        assistant_voix(ctime())

    if "connaissez" in data:
        assistant_voix("souad nissabouri une personne motivée dynamique et active , il distingue par le sens d'initiative et creativité , elle a eu des capacités sur la gestion de temps , et d'équipe") 

    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        assistant_voix(" I will show you where " + location + " is.")
        os.system("start  https://www.google.com/maps/place/" + location + "/&amp;")

        
    if "Google" in data:
        assistant_voix(" I will open google for you ")
        #os.system("start  https://www.google.com")
        webbrowser.open("google.com")
        

    if "github" in data :
        assistant_voix(" le profil github de souad nissabouri")
        webbrowser.open("https://github.com/souad97")

        
    if "linkedin" in data :
        assistant_voix(" le profil linkedin de souad nissabouri")
        webbrowser.open("https://www.linkedin.com/in/souad-nissabouri-bb9195166/")

        
    if "web" in data :
        assistant_voix(" la page web de souad nissabouri")
        webbrowser.open("file:///C:/Users/hp/Downloads/Compressed/New%20folder/index.html")

  
# initialization
time.sleep(2)
assistant_voix("salut , je suis l'assistante vocale de  souad nissabouri ")
active= True 
while active :
    data = recordAudio()
    rec(data)
    if "arrête" in data :
        assistant_voix(" Au revoir ")
        active = False 

