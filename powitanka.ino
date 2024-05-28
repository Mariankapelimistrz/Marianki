#include<Servo.h>
Servo boki;
Servo lewo;
Servo prawo;

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
boki.attach(11);
lewo.attach(5);
prawo.attach(4);
prawo.write(90);
lewo.write(90);
boki.write(110);
}

void loop() {
  // put your main code here, to run repeatedly:
if (Serial.available()>0){
   String dzialanie = Serial.readStringUntil('\n');  //read until timeout 
  if (dzialanie=="recognition"){
    prawo.write(110);
    lewo.write(110);
  }
  else if (dzialanie=="speak"){
    prawo.write(90);
lewo.write(90);
boki.write(110);
  }
  else if (dzialanie=="confuzed"){
  prawo.write(115);
  lewo.write(65);
  }
  else if (dzialanie=="explane")
  prawo.write(90);
  else if (dzialanie=="glop"){
      prawo.write(115);
  lewo.write(65);
  delay(1650);
   for (int pos = 55, pos2 =115 ; pos <= 100 && pos2>=80; pos += 1,pos2-=1) { 
    lewo.write(pos); 
    prawo.write(pos2);             
    delay(35);      
   }                 
  }
   
    else if(dzialanie=="isit"){
    for (int sop = 110; sop >= 80; sop -= 1) { 
    boki.write(sop);              // tell servo to go to position in variable 'pos'
    delay(65);                       // waits 15 ms for the servo to reach the position
  
    }
    
    
   } 
    
  }
}
