import noiklasa 
import whisper
import threading
import maskarwiz
#from ciagdalszy import dajglos
mowie=noiklasa.promptte


kom=''
wh=noiklasa.glos('small')
#lock=threading.Lock()
p=noiklasa.widok(0)#rzecz w tym żeby inicjalizować zmienne inita zanim będziesz chciał wykorzystać jakieś podfunkcje klasy
ru=noiklasa.ruch()
cotambyło=threading.enumerate()#czyli to co sie dzieje przed threadingiem to mainthread
widzecie=threading.Thread(target=p.aktototaki)#daemon czyli czy chcesz żeby program działał bez udziału użytkownika
#gdy do funkcji dodasz () (np dajglos()) wtedy thread włączy się odrazu {dajemy sygnał aby odpalić funkcje bez argumentów}
ko=ru.animacje(0)
cotamjest=threading.enumerate()
# pic=widzecie.run()
def pentelka():
 comowisz=threading.Thread(target=wh.dajglos)
 comowisz.start()
 

while (1):
 
#  comowisz.run()
 kon=0

 
#  wymowa=wh.dajglos()
#  print(wymowa)
#  kom=wymowa[1]
 yes=noiklasa.glos.pobudka()
 if yes==True:
    ko=ru.animacje(2)

 

    while kon!=2:
     

     petluje=threading.Thread(target=pentelka)
     petluje.start()
     
    # p.aktototaki()#aktualnie program się wyłącza gdy jest już stranscribowane czy to nie stworzy laga poznawczego
     maskarwiz()
     kon=wh.odpowiedz(True)
     
    
 #cotambedzie=threading.enumerate()
    #animacja budzenia sie
    #sleep(3)
# można podać w threading.Thread().start jeśli to coś da``
    
     
#deamon nie musi wcale działą wyłącza się gdy wszystkie inne programy już skończyły
"""
    tworzenie w pythonie funkcji działa w ten sposób że tworzysz program 
    w którym siedzą wszystkie zdefiniowane funkcje następnie 
    tworzysz program (init) do który ma za zadanie przetrzymywać
    funkcje ale ich nie odpalać i taki program możesz importować do 
    innych programów bez odpalania ich odrazu po improcie

    patrzy na rozmówce dopóki nie dostanie komendy by słuchać pytania
    
    """
