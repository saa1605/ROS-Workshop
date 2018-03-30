#include <Servo.h> 
#include <ros.h>
#include <std_msgs/Int16.h>

ros::NodeHandle  nh;

Servo servo1;
Servo servo2;
Servo servo3;
int flag = 0;

void servo_cb( const std_msgs::Int16& cmd_msg){
  if(flag == 0) {
  servo1.write(cmd_msg.data); //set servo angle, should be from 0-180  
  flag = 1;   
  }
  else if (flag == 1) {
  servo2.write(cmd_msg.data); //set servo angle, should be from 0-180
  flag = 0;   
  }
  else {
  servo3.write(cmd_msg.data); //set servo angle, should be from 0-180
  flag = 0;  
  }
 
}


ros::Subscriber<std_msgs::Int16> sub("servo", servo_cb);

void setup(){
 
  nh.initNode();
  nh.subscribe(sub);
  
  servo1.attach(13); //attach it to pin 7
  servo2.attach(14);
  servo3.attach(15);
}

void loop(){
  nh.spinOnce();
  delay(1);
}
