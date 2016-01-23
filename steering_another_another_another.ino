#include <Servo.h>
///signals are sent like "120a90" where, forward_backward=120 & left_right=90

//Using mega 2560 and sabertooth dip switch 010111 *make sure its set to that specific order*
int servo1=10;//pin 10 for servo 1
int servo2=11;//pin 11 for servo 2
int forward_backward;
int left_right;

Servo myservo;
Servo myservo2;
 
void setup() {
  // put your setup code here, to run once:s
  pinMode(servo1, OUTPUT);
  pinMode(servo2, OUTPUT);
  Serial.begin(9600);
  myservo.attach(servo1);//attach servo1
  myservo2.attach(servo2);//attach servo2
  Serial.setTimeout(10);//works for 10ms set timeout and 0.9s python signal. Need to figure out the optimization.
}

void loop() {
  
 if (Serial.available()>0){ // Wait for characters
  forward_backward = Serial.parseInt();
  left_right = Serial.parseInt();
  Serial.println(forward_backward);
  Serial.println(left_right);

  myservo.write(forward_backward);// 93 is stop backward and forward is scalable range 25 to 155
  myservo2.write(left_right);//93 is no steering, steering range(in degrees) 30 to 160
  
  }
  }
  
 

