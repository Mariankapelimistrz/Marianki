import cv2
import face_recognition
import numpy as np
import serial
import dlib
import serial
import time

zbierz=cv2.VideoCapture(2)#kamera wbudowana
dzieciaczek=serial.Serial('/dev/ttyUSB0',9600,timeout=1)#dorzucamy timeout żeby port nie pomyślał że jest zajęty
jano = face_recognition.load_image_file("/home/r4h/umysl/poznane_osoby/pan jan opiekun.jpg")
bycie = face_recognition.face_encodings(jano)[0]

nazywalisie= ["Jan"]#tablica, dzięki niej możemy przypisać liczbe dowolnie przez siebie wybranej wartości lub funkcji

tomaszimie=[]
while True:
    ret,frame =zbierz.read()
    frame=cv2.flip(frame,1)
    makuch=cv2.resize(frame,(0,0),fx=0.25,fy=0.25)#zmniejszamy obraz aby komputer przy encodowaniu miał mniej roboty(jaki obrazek chcesz resizować ustalasz na pierwszej zmiennej)
    #gdy chemy zmniejszyć obrazek na przykład 2 razy używamy fx i fy
    facio=face_recognition.face_encodings(makuch)#on musi porównać zencodowane twarze
   
    #porownaj = face_recognition.compare_faces(bycie,facio)#porównujemy to co jest na ramkach z tym co jest na encodowanym zdięciu to będzie się pojawiać gdy pewność spadnie poniżej poziomu
    #if True in porownaj:
     #pewność=print("zgodność z obrazkiem",porownaj[0])
    #for (gora,dol,lewo, prawo) in zip(lokacja,tomaszimie):
    karton=face_recognition.face_locations(makuch)#rysuje kwadraty
    #print(karton)
    for (top,right,bottom,left) in karton:#return: A list of tuples of found face locations in css (top, right, bottom, left) order
    
        ustawnienie='[{0:d},{1:d},{2:d},{3:d}]\n'.format(left,top,right,bottom)#musimy zamienić inty na hexy i usunąć przecinkino 
        #ustawnienie='[{0:02x}{1:02x}{2:02x}{3:02x}]\n'.format(left,top,right,bottom)
        #print(ustawnienie)
        # print(ustawnienie)
        # hex(left)
        # hex(top)
        # hex(right)
        # hex(bottom)
        cv2.rectangle(makuch,(left,top),(right,bottom),(50,180,100),3)
        dzieciaczek.write(ustawnienie.encode('utf-8'))
        
      #  time.sleep(0.5)
      #  czytaj=dzieciaczek.readline()
      #  pokazdane=str(czytaj,'UTF-8')
      #  print(pokazdane)

    #jaksieczujesz=face_recognition.face_landmarks(makuch)#daje pozy1cje poszczególnych elementów twarzy
    #for marki in jaksieczujesz:
     # print(marki['left_eye'])
      #print(marki['right_eye'])
      #cv2.circle(frame,(100,100),140,(40,80,20))
    #cv2.rectangle(frame,(gora,lewo),(dol,prawo),(20,40,80),)
   


    cv2.imshow("proba",makuch)
    
    c= cv2.waitKey(1)
    if c == 27:
        break
    
zbierz.release()
cv2.destroyAllWindows()
#{możliwe że nie mieści się w tabeli 128 bo niektóre liczby wychodzą na minusie co nie pasuje tablicy[0:128]}-[nie]
#resize i resizewindow odpowiadają za dwie różne rzeczy resize zmienia rozdzielczość zdięcia a resizewindow  zmienia wielkość otwieranego okna nie zmieniając rozdzielczości
#ValueError: operands could not be broadcast together with shapes (480,640,3) (128,)
#rozmiary zdięcia nie zgadzają się z rozmiarami sprawdzanych ramek (nie sprawia to wywalenia z programu ale)
#https://face-recognition.readthedocs.io/en/latest/face_recognition.html
#https://stackoverflow.com/questions/70106633/opencv-resize-typeerror-only-integer-scalar-arrays-can-be-converted-to-a-scal
#String string = Serial.readStringUntil('\n');  //read until timeout \n