#include <Servo.h>

//Camera dimensions
#define SCREEN_WIDTH 640
#define SCREEN_HEIGHT 480

//Section sizes in %
#define EYE_SECTION_PRC 40
#define NECK_SECTION PRC 60
#define MOVE_SECTION_PRC 80

//Borders of move
#define MAX_NECK_ROT 150
#define MIN_NECK_ROT 75

#define MAX_LEFT 100
#define MIN_LEFT 10

#define MAX_RIGHT 170
#define MIN_RIGHT 100

//Servo pinout
#define SERV_NECK_ROT 11
#define NOT_USED 6
#define SERV_NECK_LEFT 5
#define SERV_NECK_RIGHT 4

/*
 * Notatka:
 * 
 * Szyja_obr:     120 = 0*    - środek,    75 = 50*    - lewo,  150 = 17*   - prawo
 * Góra dół:      90/100 = 0* - środek,    100/85 = 7* - góra,  10/170 = 54* - dół/smutny marian maks do góry 10*
 * (lewy/prawy)
 */

//Create servo objects
Servo neck_rot;
Servo neck_left;
Servo neck_right;

void setup() {
  Serial.begin(9600);
  neck_rot.attach(SERV_NECK_ROT,600,2300);  // (pin, min, max)
  neck_left.attach(SERV_NECK_LEFT,600,2300);  // (pin, min, max)
  neck_right.attach(SERV_NECK_RIGHT,600,2300);  // (pin, min, max)
}

void loop() {
  setDefaultPose();
  
  while(1){
    Serial.println("Enter angle:");
    while (Serial.available() == 0) {}     //wait for data available
    String angle = Serial.readString();  //read until timeout
    angle.trim();                        // remove any \r \n whitespace at the end of the String
    upDownNeck(angle.toFloat());
  }         
}

void setDefaultPose(){
  neck_rot.write(120);
  neck_left.write(90); 
  neck_right.write(100); 
}

float rotNeck(float deg){
  float x_r=((deg+108)/0.8667);

  neck_rot.write(x_r);
}

float upDownNeck(float deg){
  float x_l=(((3*deg)+180)/2);
  float x_r=((deg-63.53)/(-0.7059));

  Serial.println(x_l);
  Serial.println(x_r);

  neck_left.write(x_l);
  neck_right.write(x_r);
}
