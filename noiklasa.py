import cv2
import face_recognition#wolniacha
import serial,time
import speech_recognition as sr
import pyaudio
import whisper#wolnos
import pyttsx3
import threading
from gpt4all import GPT4All
dzieciaczek=serial.Serial('/dev/ttyUSB0',9600,timeout=1)
bazamysli=GPT4All(model_name="gpt4all-falcon-newbpe-q4_0.gguf",model_path="/home/r4h/umysl/",allow_download=False)
promptte=''
komka=''
wyb=0
robotic=pyttsx3.init()
class widok:
  
  def __init__(self,aktywacjakamery):#potrzebujemy wpisać inita żeby pprzy importowaniu nie zaczął odrazu wykonywać programu
   self.aktywacjakamery=cv2.VideoCapture(0)


  def kamerka(self,pokaz):
   
    self.pokaz=pokaz
  #  while(1):
    ret, frame =self.aktywacjakamery.read()
    such=cv2.flip(frame,1)
    makuch=cv2.resize(such,(0,0),fx=0.2,fy=0.2)
    facio=face_recognition.face_encodings(makuch)
    karton=face_recognition.face_locations(makuch)     
    # pozycja=''
    #mega=cv2.resize(normalny,None,2,4,interpolation=cv2.INTER_CUBIC)
    if pokaz==True:
      cv2.imshow("widze",such)

      if cv2.waitKey(1)==27:
          quit
    return makuch ,karton
        # """czy nie lepiej dopieścić kamerkę do tego stopnia że do aktototakiego wprowadzał byś j
        # edynie jedybue kamerke i póżniej byś ją dalej procesował i wprowadzić tam jakąś zmienną
        #   dzięki której mógłbyś używać tej funkcji jak zwykłej kamerki?"""
  def aktototaki(self):
      while(1):
      #  ret,frame =self.aktywacjakamery.read()
      #  frame=cv2.flip(frame,1)
      #  makuch=cv2.resize(frame,(0,0),fx=0.2,fy=0.2)
      #  facio=face_recognition.face_encodings(makuch)
      #  karton=face_recognition.face_locations(makuch)
        makuch, karton=self.kamerka(pokaz=False)
        for (top,right,bottom,left) in karton:
         ustawnienie='[{0:d},{1:d},{2:d},{3:d}]\n'.format(left,top,right,bottom)#musimy zamienić inty na hexy i usunąć przecinkino 
        #ustawnienie='[{0:02x}{1:02x}{2:02x}{3:02x}]\n'.format(left,top,right,bottom)
        cv2.rectangle(makuch,(left,top),(right,bottom),(50,180,100),3)
        dzieciaczek.write(ustawnienie.encode('utf-8'))
        cv2.imshow("proba",makuch)
        if promptte!='':
           break
    
        c= cv2.waitKey(1)
        if c == 27:
          break
         #tutaj chcemy żeby waitkeyem było co kolwiek wejdzie na mowe
  def poznaj():
      pass
  
class ruch:
   def __init__(self):
      pass
   def animacje(self,wyb):
       self.wyb=wyb
      #  wyb = {
      #  0:dzieciaczek.write("spij\n".encode('utf-8')),
      #  1:dzieciaczek.write("mysl\n".encode('utf-8')),
      #  2:dzieciaczek.write('aterazodpowiedz\n'.encode('utf-8')),
      #  3:dzieciaczek.write("wstań\n".encode('utf-8'))
      #  }
       if wyb==0:
        dzieciaczek.write("spij\n".encode('utf-8'))
       if wyb==1:
        dzieciaczek.write("budz\n".encode('utf-8'))
       if wyb==2:
        dzieciaczek.write("mysl\n".encode('utf-8'))
      #  if wyb==3:
      #   dzieciaczek.write("wstań\n".encode('utf-8'))
      
      
      


       
class glos:
  
    
  def __init__(self,whmodel) :
   self.whmodel = whisper.load_model('small')#spowalniacz
   
  def dajglos(self):
    global promptte
    global komka
    promptte=''#piękny sposób aby nie instalować waylanda
    r = sr.Recognizer()
   
    
    
    with sr.Microphone() as source:
               
               
      soki=r.adjust_for_ambient_noise(source=source)#wyznacza standard szumu generowanego przez otoczenie(recognizer_instance.energy_threshold)
      # glosność=r.energy_threshold
      # r.energy_threshold=glosność+9000
      print("now!!")
      audio = r.listen(source)#gdy program usłyszy coś ponad ambient(recognizer_instance.energy_threshold) rozpocznie akcje słuchanie 
       #nagrywa dźwięk tak długa jak nie hitnie pauzy

      with open("no_zarycz_no.wav","wb") as f:
       f.write(audio.get_wav_data())
       text = self.whmodel.transcribe('no_zarycz_no.wav',verbose=True, language="pl")#(zamula) to musi się odpalać gdy wiemy że warto
       promptte = text['text']#dict na str
       komka=promptte.lower().replace(' ','')
       if 'żegnaj' in komka:
         exit()
       return  promptte,komka
    #chcę mieć możliwości dostania się do samej odpowiedzi
  #
  def odpowiedz(self,mysl):
      kop=0
      while kop!=1:
       glos.odpowiedz.mysl=mysl
       if mysl==True:
        kos=ruch.animacje(self,1)
      #if komka=='wystarczy':{w ten sposób musi być idealnie to co w nawiasach}
       if 'wystarczy' in komka:#czy to jest nam potrzebne czy nie lepiej nie odpalać kompletnie tej funkji gdy będziesz chciał wyjść
        kop=2
        return kop
       talk = bazamysli.generate(promptte)
       print(talk)
       robotic.say(talk)
       ruch.animacje(self,2)

       robotic.runAndWait()
       kop=1
  def poteznapetla(self):
    glos('small')
    comowisz=threading.Thread(target=glos.dajglos,args=self)
    comowisz.start()
    return glos.dajglos
  def pobudka():
   ros=sr.Recognizer()
   yes=False
   with sr.Microphone() as mike:
     while yes==False:
       ros.adjust_for_ambient_noise(source=mike)
       sos=ros.energy_threshold
       print(sos)
       if sos>300:
         yes=True

   return yes
    


  
"""
czy mogę wybierać które części wielkiej funkcji chcę aktywować
tu może chodzić o to że to co chce zainicjalizować też w funkcjach musi być globalem   
załatwiło problem z threatingiem https://stackoverflow.com/questions/11792629/thread-starts-running-before-calling-thread-start 
przy generacji odpowiedzi można wybrać role user bądź assistant różnią się one formatowaniem generowanej odpowiedzi 
assistant   
a tu dobra dusza(ctrl s) wpadłą na pomysł pozwalający na startowanie wiele razy:https://stackoverflow.com/questions/4122188/how-can-i-invoke-a-thread-multiple-times-in-python       
"""