/* 
 * rosserial Subscriber Example
 * Blinks an LED on callback
 */

#include <ros.h>
#include <std_msgs/Int16.h>

ros::NodeHandle  nh;

void messageCb( const std_msgs::Int16& toggle_msg)
{
  PORTC = 0xff;
}

ros::Subscriber<std_msgs::Int16> sub("toggle_led", &messageCb );

void setup()
{ 
  DDRC = 0xff;
  nh.initNode();
  nh.subscribe(sub);
}

void loop()
{  
  nh.spinOnce();
  delay(1);
}

