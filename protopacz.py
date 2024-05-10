import speech_recognition as sr
import pyaudio
import whisper
r=sr.Recognizer()
traskrysor=whisper.load_model("base")

while (1):
   
    with sr.Microphone() as source:
        print("sprawdź to") 
        r.adjust_for_ambient_noise(source=source)
        komenda = r.listen(source)
           
    with open("kometa.wav","wb") as prosba:
        prosba.write(komenda.get_wav_data())
        text = traskrysor.transcribe('kometa.wav',language="pl",verbose=True)#{verbose wpisuje to co powiedziałeś działa jak print w tej komendzie}
        promptte = text['text']#dict na str
            
        print("did you say",promptte,"?")
        if 'wyłącz'in promptte.lower():#działa to ciężkie słowo dla kolegi
            print("wkońcu")
            break
        elif 'word' in promptte.lower(): 
            print("chwalmy Peruna")
            break
        #podpowiedzi
        #nie podkręcaj mikrofonu na maxa
        #jak mikrofon nie odbiera poprawnie pozmieniajczułość

       