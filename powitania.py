import pyttsx3
import serial
import cv2
import face_recognition as fr
import time

zbierz=cv2.VideoCapture(0)#kamera wbudowana
dzieciaczek=serial.Serial('/dev/ttyUSB0',9600,timeout=1)#dorzucamy timeout żeby port nie pomyślał że jest zajęty
jano = fr.load_image_file("/home/r4h/umysl/poznane_osoby/pan jan opiekun.jpg")
Panrektor = fr.face_encodings(jano)[0]
marian=pyttsx3.init()


nazywalisie= ["Jan"]#tablica, dzięki niej możemy przypisać liczbe dowolnie przez siebie wybranej wartości lub funkcji
zgodnosc=[]
facio=[]
abyniezwracalouwagi=True
while True:
 if abyniezwracalouwagi:
    ret,frame =zbierz.read()
    frame=cv2.flip(frame,1)
    makuch=cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
    zramowany=fr.face_locations(makuch)
    kapitan=fr.face_encodings(makuch,zramowany)
    #zgodnosc=input()
    if kapitan!=[]:
     zgodnosc=fr.compare_faces(Panrektor,kapitan)
    if True in zgodnosc:
      reck=print('recogition')

      dzieciaczek.write("recognition\n".encode('utf-8'))
      time.sleep(4)
      print()
      dzieciaczek.write("speak\n".encode('utf-8'))
      time.sleep(1.5)
      marian.setProperty("rate",80)
      marian.setProperty('volume',1.5)
      marian.say("Welcome Sir")
      marian.runAndWait()
      time.sleep(1)
      
      marian.say("Mister?,    capitan?")
      marian.runAndWait()
   
      time.sleep(1)
      
      marian.say("Recktor!")
      marian.runAndWait()
      time.sleep(.5)
      marian.setProperty('rate',70)
      marian
      marian.say("welcome in house of ours")
      marian.runAndWait()
      time.sleep(1)
      
      dzieciaczek.write("confuzed\n".encode('utf-8'))
      marian.setProperty('volume',0.6)
      marian.setProperty('rate',130)
      marian.say("technicaly it's more your's than ours ")
      marian.runAndWait()
      dzieciaczek.write('explane\n'.encode('utf-8'))
      
      marian.setProperty('rate',150)
      marian.say("cause you know you own this place and all, of course you allredy know that, it will be weird otherwise you know ? ")
      marian.runAndWait()
      time.sleep(.2)
      dzieciaczek.write("recognition\n".encode('utf-8'))
      marian.setProperty('rate',170)
      marian.say("and since everinthing here is yours property so do I, and i know that you can kick me out of this place nay time or  abandoned for ever so I try my best to gain your sympathy     and stuff ")
      marian.runAndWait()
      
      dzieciaczek.write('glop'.encode('utf-8'))
      time.sleep(15)
      dzieciaczek.write('isit'.encode('utf-8'))
      
      time.sleep(5)
      marian.setProperty('volume',1)
      marian.setProperty('rate',130)
 #     slw=uzytk.generate(text="myślę że poszło całkiem nie najgorzej",voice='Giovanni',model="eleven_multilingual_v2")
  #    play(slw) nie wykorzystywane w żaden sposób
 
      marian.say("I think that went well")
      marian.runAndWait()
      dzieciaczek.write('speak'.encode('utf-8'))
      exit()
    else:
      cv2.imshow("proba",makuch)
    
 c= cv2.waitKey(1)
 if c == 27:
   break
    
zbierz.release()
cv2.destroyAllWindows()
