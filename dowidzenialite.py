import cv2
import face_recognition
import serial,time
aktywacjakamery=cv2.VideoCapture(0)
aktywacjakamery.set(3,1600)
aktywacjakamery.set(4,900)
arduinkoport=serial.Serial('/dev/tty/USB0',9600)
while(1):
    ret, frame =aktywacjakamery.read()
    normalny=cv2.flip(frame,1)
    pozycja=''
    #mega=cv2.resize(normalny,None,2,4,interpolation=cv2.INTER_CUBIC)
    cv2.imshow("widze",normalny)

    if cv2.waitKey(1)==27:
        break
aktywacjakamery.release()
cv2.destroyAllWindows