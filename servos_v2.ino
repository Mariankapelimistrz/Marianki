#include <Servo.h>

//Camera dimensions
#define SCREEN_WIDTH 160
#define SCREEN_HEIGHT 120

//Borders of move
#define MAX_NECK_ROT 16
#define MIN_NECK_ROT -50
#define MAX_UPDOWN 7
#define MIN_UPDOWN -54

//Speed of moving
#define STEP 2

//Servo pinout
#define SERV_NECK_ROT 11
#define NOT_USED 6
#define SERV_NECK_LEFT 5
#define SERV_NECK_RIGHT 4

//Section definitions
#define LEFT_LIMIT 50
#define RIGHT_LIMIT 110
#define TOP_LIMIT 40
#define BOTTOM_LIMIT 80

int camAX = ((SCREEN_WIDTH/2)-10);
int camBX = ((SCREEN_WIDTH/2)+10);
int camAY = ((SCREEN_HEIGHT/2)-10);
int camBY = ((SCREEN_HEIGHT/2)+10);

int camCenX = int((camBX+camAX)/2);
int camCenY = int((camBY+camAY)/2);

int vectX=0;
int vectY=0;

/*
 * Notatka:
 * 
 * Szyja_obr:     120 = 0*    - środek,    75 = 50*    - lewo,  150 = 17*   - prawo
 * Góra dół:      90/100 = 0* - środek,    100/85 = 7* - góra,  10/170 = 54* - dół/smutny marian maks do góry 10*
 * (lewy/prawy)
 * 
 * Sekcje ekranu:
 *  |----|----|----|
 *  | LG | G  | PG |
 *  |----|----|----|
 *  | L  | CEN| P  |
 *  |----|----|----|
 *  | LD | D  | PD |
 *  |----|----|----|
 * 
 */

//Create servo objects
Servo neck_rot;
Servo neck_left;
Servo neck_right;

int neck_rot_ang=0;
int neck_updown_ang=0;

void setup() {
  Serial.begin(9600);
  neck_rot.attach(SERV_NECK_ROT,600,2300);  // (pin, min, max)
  neck_left.attach(SERV_NECK_LEFT,600,2300);  // (pin, min, max)
  neck_right.attach(SERV_NECK_RIGHT,600,2300);  // (pin, min, max)
  setDefaultPose();
}

void loop() {  
  while(1){
    vectX=0;
    vectY=0;
    
    //Serial.println("Enter position:");
    
    //Wait to position
    while (Serial.available() == 0) {}     //wait for data available
    String string = Serial.readStringUntil('\n');  //read until timeout 
    //\n is a last number in string
    //Serial.println(string);
    string.trim();                        // remove any \r \n whitespace at the end of the String
    convertToVariablesINT(string);

    if(camCenX<LEFT_LIMIT){vectX=STEP;}
    if(camCenX>RIGHT_LIMIT){vectX=-STEP;}
    if(camCenY<TOP_LIMIT){vectY=STEP;}
    if(camCenY>BOTTOM_LIMIT){vectY=-STEP;}

    //Move head
    if(((neck_rot_ang+vectX)<MAX_NECK_ROT)&&((neck_rot_ang+vectX)>MIN_NECK_ROT)){
      neck_rot_ang=neck_rot_ang+vectX;
    }else{
      //Move body (in future)
    }
    if(((neck_updown_ang+vectY)<MAX_UPDOWN)&&((neck_updown_ang+vectY)>MIN_UPDOWN)){
       neck_updown_ang=neck_updown_ang+vectY;
    }    

    //Print debug informations
    rotNeck(neck_rot_ang);
    upDownNeck(neck_updown_ang);
    
    
    //Serial.println("Camera center:["+String(camCenX)+","+String(camCenY)+"]");
    //Serial.println("VectX: "+String(vectX) + " ,VectY: "+String(vectY));
    //Serial.println("Rotation angle: "+String(neck_rot_ang) + " ,UpDown angle: "+String(neck_updown_ang));
    
  }         
}

void convertToVariablesINT(String datapack){
  datapack = datapack.substring(1, datapack.length() - 1);
  
  int comma1 = datapack.indexOf(',');
  int comma2 = datapack.indexOf(',', comma1 + 1);
  int comma3 = datapack.indexOf(',', comma2 + 1);
  
  camAX = datapack.substring(1, comma1).toInt();
  camAY = datapack.substring(comma1 + 1, comma2).toInt();
  camBX = datapack.substring(comma2 + 1, comma3).toInt();
  camBY = datapack.substring(comma3 + 1).toInt();

  //Serial.println(camAX);
  //Serial.println(camBX);
  //Serial.println(camAY);
  //Serial.println(camBY  );

  camCenX = int((camBX+camAX)/2);
  camCenY = int((camBY+camAY)/2);

  //Serial.println(camCenY);
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

  //Serial.println(x_l);
  //Serial.println(x_r);

  neck_left.write(x_l);
  neck_right.write(x_r);
}
