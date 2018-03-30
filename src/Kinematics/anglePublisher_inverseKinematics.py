#!/usr/bin/env python

# import rospy
#from beginner_tutorials.msg import Num
# from std_msgs.msg import UInt16
#from motor_driver.msg import Servo_angle

##Computation Libraries
import numpy as np
import math 

pi_by_2 = math.pi/2
pi = math.pi

##Variables
link1_length = 2.5
correction_factor = 0
link_length_1 = 12
link_length_2 = 12
##Compute angles from provided co-ordinates


def compute_angles(x,y,z):
	
	theta_3 = (math.acos((x**2 + y**2 + (z-link1_length)**2)/((link_length_2**2)+(link_length_1**2)) - 1)) 

	#Condition to eliminate divide by infinity error

	theta_1 = (math.atan2(y,x))

	# if y == 0:
	# 	if x > 0:
	# 		theta_1 = theta_1
	# 	elif x < 0:
	# 		theta_1 = pi - theta_1

	# if x == 0 and y == 0:
	# 	theta_2 = math.degrees(pi_by_2 - (math.acos((x**2 + y**2 + (z-link1_length)**2)/((link_length_1**2)+(link_length_2**2)) - 1)/2))
	# else:
	theta_2 = math.atan2((z-link1_length),((x**2 + y**2)**0.5))-(theta_3)/2

	print "theta2",math.degrees(theta_2)
	print "theta3",math.degrees(theta_3+(pi/2))

	if theta_2<0:
		theta_2+=(pi/2)
		theta_3-=pi

	theta_3+=pi/2

	theta_1 = math.degrees(theta_1)
	theta_2 = math.degrees(theta_2)
	theta_3 = math.degrees(theta_3) 


	#Hard-coding for 0-0-0 position
	

	# theta_1,theta_2,theta_3 = adjust(theta_1,theta_2,theta_3)


	print theta_1," ",theta_2," ",theta_3

	return theta_1, theta_2, theta_3


def adjust(theta_1,theta_2,theta_3):
	if theta_1 < 0:
		theta_1 = 180 + theta_1
	if theta_2 < 0:
		theta_2 = 180 + theta_2
	if theta_3 < 0:
		theta_3 = 180 + theta_3

	return theta_1,theta_2,theta_3

while(1):
	a = input()
	b = input()
	c = input()

	compute_angles(a,b,c)
# def angle_publisher():
# 	pub = rospy.Publisher('servo',UInt16, queue_size = 10)
# 	rospy.init_node('angle_publisher', anonymous=True)
# 	rate = rospy.Rate(10)
# 	i = 0
# 	while not rospy.is_shutdown():

# 		x = input("1:")
# 		y = input("2:")
# 		z = input("3:")

# 		servo_angle_1,servo_angle_2,servo_angle_3 = compute_Angles(x,y,z)

# 		pub.publish(servo_angle_1)
# 		pub.publish(servo_angle_2)
# 		pub.publish(servo_angle_3)

# 		rate.sleep()

# if __name__ == '__main__':
#     try:
#         angle_publisher()
#     except rospy.ROSInterruptException: 
#         pass
