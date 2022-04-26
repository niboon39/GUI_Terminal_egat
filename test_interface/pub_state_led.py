#!/usr/bin/env python3
import rospy 
from std_msgs.msg import Int32

def led_state (n): # Default do any nothing. 
    pub = rospy.Publisher("sl" , Int32 , queue_size=10)
    rospy.init_node("movebase_client_py" , anonymous=True)
    rate = rospy.Rate(10)
    if (n == 1):
        green = 1 
        pub.publish(green)
        print("\tGreen (Standby) : ON \t  Blue (Working) : OFF \n")
        print("\tMotor = OFF \n")
        # rospy.loginfo("state blue : ON")
    else:
        blue = 0
        pub.publish(blue)
        print("\tGreen (Standby) : OFF \t  Blue (Working) : ON \n")
        print("\tMotor  = ON \n")
        # rospy.loginfo("state green : ON")
    rate.sleep()

if __name__ == '__main__':
    pass
    # try: 
    #     led_state(n=1)
    # except rospy.ROSInterruptException : 
    #     pass