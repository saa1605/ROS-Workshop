/*
 * rosserial Publisher with Subscriber Example
 * 
 */

#include <ros.h>
#include <std_msgs/Int16.h>

#include <std_msgs/String.h>

ros::NodeHandle  nh;

int count = 0;
bool start = false;

std_msgs::Int16 int_msg;
std_msgs::String str_msg, msg1;

ros::Publisher Count("Count", &int_msg);
ros::Publisher Log("Log", &int_msg);

void messageCb(const std_msgs::Int16& msg_rec)
{
  if(msg_rec.data == 1)
  {
    start = true;
  }
  else if(msg_rec.data == 0)
  {
    start = false;
  }
}

ros::Subscriber<std_msgs::Int16> sub("Log", &messageCb );

void setup()
{
  nh.initNode();
  
  nh.advertise(Count);

  nh.advertise(Log);

  nh.subscribe(sub);
}

void loop()
{
  if(start == true)
  {
    count ++ ;
    int_msg.data = count;
    
    Count.publish( &int_msg );
  }
  nh.spinOnce();
  delay(10);
}
