import cv2
import face_recognition
import numpy as np
import serial
import dlib
import time
zbierz=cv2.VideoCapture(0)#kamera wbudowana
#dzieciaczek=serial.Serial('/dev/ttyUSB0',9600,timeout=1)#dorzucamy timeout żeby port nie pomyślał że jest zajęty
jano = face_recognition.load_image_file("/home/r4h/umysl/poznane_osoby/pan jan opiekun.jpg")
mozekiedys=face_recognition.load_image_file("/home/r4h/umysl/poznane_osoby/susum.jpg")
osoba =face_recognition.load_image_file("/home/r4h/umysl/poznane_osoby/marzyciel.jpg")
bycie = face_recognition.face_encodings(jano,num_jitters=40)[0]
mozeznajdzie=face_recognition.face_encodings(mozekiedys,num_jitters=40)[0]
podnoszacanaduchu=face_recognition.face_encodings(osoba)[0]

persony= [    mozeznajdzie,bycie,podnoszacanaduchu ]
nazywalisie= ["Czarodziej","Jojo","bohater"]#tablica, dzięki niej możemy przypisać liczbe dowolnie przez siebie wybranej wartości lub funkcji

twarzolokacja=[]
encodowanietwarzowe=[]
zwalisie=[]
procesuj_te_ramke= True
while True:
    ret, frame = zbierz.read()
    frame =cv2.flip(frame,1)#mirror
    if procesuj_te_ramke:
      rightframe=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

      #rame = cv2.resize(frame,(0,0),fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)
      twarzolokacja = face_recognition.face_locations(frame)
      encodowanietwarzowe=face_recognition.face_encodings(frame,twarzolokacja)
      zwalisie=[]#najpierw wypadało by to zainicjalizować a potem do niego wpisywać
      for encodowanie in encodowanietwarzowe:
        to_sie_zgadza = face_recognition.compare_faces(persony,encodowanie)
        
        imiono = "nieznam"
        if True in to_sie_zgadza:# wszystko mu się kojarzy z jedną osobą
          #  indexujdziada= to_sie_zgadza.index(True)
           # imie = nazywalisie[indexujdziada]
         odleglosci = face_recognition.face_distance(persony,encodowanie)
         indexujpana = np.argmin(odleglosci)
         if nazywalisie[indexujpana]:
          imiono = nazywalisie[indexujpana]
         zwalisie.append(imiono) #aby zwalczyć IndexError: list index out of range 
        #wpisujemy do indeku zostaje wpisane jedno imie które było przypisane do zdięcia
    rocesuj_te_ramke = not procesuj_te_ramke     

    
    
    for (top,right,bottom,left),imiono in zip(twarzolokacja,zwalisie):
        #arduinosprawy{
        pozycja ='[{0:d},{1:d},{2:d},{3:d}]'.format(left,top,right,bottom)
        #print(pozycja)
        time.sleep(.75)
        #odczyt=dzieciaczek.write(pozycja.encode('utf-8'))
        #czytaj=dzieciaczek.readline()
        #pokazdane=str(czytaj,'UTF-8')
        #print(pokazdane)
        cv2.rectangle(frame,(left,top),(right,bottom),(0,0,255),2)
        cv2.rectangle(frame,(left,bottom-35),(right,bottom),(0,0,255),cv2.FILLED)
        font = cv2.FONT_ITALIC
        cv2.putText(frame,imiono,(left + 6,bottom -6),font,1.0,(255,255,255),1)

    cv2.imshow("POV:bycie Marianem",frame)
    
    c= cv2.waitKey(1)
    if c == 27:
        break
    
zbierz.release()
cv2.destroyAllWindows()
#błędy
#wrzuciłem w whilea comendy realise i destroyallwindows z 
#out of range pojawiło się ponieważ nie wstawiłem przestrzeni gdzie imie mogłoby być wstawione
#tolerancja na 0.2 dodaje mi durzo azjatyckiego uroku kolega gubi się w zeznaniach gdy ma mnie odróżnić od legendy
#ciekawostka przy ustawianiu kamery w komendzie cap.set(3,480) 3-oznacza szerokość a 4 to będzie wysokość
#twarz rozpoznawał dobrze ale źle wpisywał imie
#{troche mało miejsca na tekst} jednak nie
#npg nie działa 
#bibliografia
#https://subscription.packtpub.com/book/data/9781785283932/3/ch03lvl1sec28/accessing-the-webcam
#https://learnopencv.com/reading-and-writing-videos-using-opencv/    '
#https://www.youtube.com/watch?v=5yPeKQzCPdI
#https://rollbar.com/blog/python-indexerror/#
#https://github.com/ageitgey/face_recognition/issues/406
#https://www.youtube.com/watch?v=SC1xNsq8CdA
#https://stackoverflow.com/questions/24974827/cascadeclassifier-in-opencv-generates-error
#https://docs.opencv.org/3.4/d1/de5/classcv_1_1CascadeClassifier.html#aaf8181cb63968136476ec4204ffca498
#https://github.com/ageitgey/face_recognition/blob/master/examples/facerec_from_webcam_faster.py
#* `sudo`: This is a command that allows users with administrative privileges to execute commands as if they were root users. In this case, the user is running the command as an administrator, which means they have permission to modify system settings and group memberships.
#* `usermod`: This is a command used to modify user accounts on Linux systems. It can be used to add or remove groups from a user's membership, as well as to change other account settings such as the user's home directory and shell.
#* `-a`: This option tells the command to add the specified group to the user's membership. In this case, the group dialout is being added to the user's membership.
#* `-G`: This option specifies the group that the user should be a member of. In this case, the user is being made a member of the dialout group.
#* `$USER`: This is a placeholder for the username of the user whose group membership is being modified. The actual username will be replaced with this placeholder when the command is executed.
#* `-a -G dialout $USER`: This is the actual command that modifies the user's group membership to the dialout group. The `-a` option specifies that the group should be added, and the `-G` option specifies the group that the user should be a member of. The `$USER` placeholder is replaced with the actual username when the command is executed.
#za co odpowida port S4
#możemy przeżucić się na zapis hexadecymalny żeby wyżucić przecinki i tym przyśpieszyć kod
#gdy zostawimy włączony esrial monitor port uzna że jest zajęty
#bunt portu 0