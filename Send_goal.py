#!/usr/bin/env python3
import rospy
import actionlib
import os
# Brings in the .action file and messages used by the move base action
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import * 
from tf.msg import * 
from test_interface import pub_state_led

arr = ["x_start (x0)","x1" , "x2" , "x3" , "x4",
       "x5" , "x6" , "x7" , "x8",
       "x9" , "x10" , "x11" , "x12",
       "x13" , "x14" , "x15" , "x16" ]

def movebase_client(n , x , y , z , w = 1.0 ):

    # Create an action client called "move_base" with action definition file "MoveBaseAction"
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
 
    # Waits until the action server has started up and started listening for goals.
    client.wait_for_server()

    # Creates a new goal with the MoveBaseGoal constructor
    goal = MoveBaseGoal()

    goal.target_pose.header.frame_id = "map"
    #goal.target_pose.header.stamp = rospy.Time.now()
    # arr[int(n)-1] = "O"

    goal.target_pose.pose.position.x = x 
    goal.target_pose.pose.position.y = y 
    goal.target_pose.pose.orientation.z = z 
    goal.target_pose.pose.orientation.w = w


   # Sends the goal to the action server.
    client.send_goal(goal)

   # Waits for the server to finish performing the action.
    wait = client.wait_for_result()

   # If the result doesn't arrive, assume the Server is not available
    if not wait:
        # https://answers.ros.org/question/57772/how-can-i-cancel-a-navigation-command/
        os.system("rostopic pub /move_base/cancel actionlib_msgs/GoalID -- {}")
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
        return False 
    else:
    # Result of executing the action
        return client.get_result()   

if __name__ == '__main__':
    pub_state_led.led_state(n = 1) # State led : green (stand by )
    while(1):
        # Initializes a rospy node to let the SimpleActionClient publish and subscribe

        rospy.init_node('movebase_client_py',anonymous=True) 

        print("\t\t********** EGAT WAREHOUSE **********\n") 
        print(f"\t\t\t-- {arr[0]} --\t\t\n")
        print(f"\t\t\t|{arr[1]} | {arr[4]} | {arr[7]}  | {arr[10]} |\t")
        print(f"\t\t\t|{arr[2]} | {arr[5]} | {arr[8]} | {arr[11]} |\t")
        print(f"\t\t\t|{arr[3]} | {arr[6]} | {arr[9]} | {arr[12]} |\t")
        print(f"\t\t\t\t -- {arr[13]}--")

        print(f"\t\t\tOUTSIDE (3 POINT) ->  14 , 15 , 16 \t\n")

        ''' 

        xn is position in matrix. 
        x_final is stop position.
        x_start is start position.

        Cancel navigation enter -> 99 

        '''

        print("\t\t***********************************\n")
        print("Exit program. ( Pres any keys to exit )\n")

        
        user = input("Enter location : ")


        # outside
        if   user == '0' : x,y,z,w = -0.2525806725025177 , 0.05813882499933243 , 0.01201308332383633, 1.0
        elif user == '1' : x,y,z,w = 2.3162009716033936 , -1.2540520429611206 , 0.008044092915952206 , 1.0
        elif user == '2' : x,y,z,w = 7.697778701782227 , -1.1930816173553467 , 0.03287801891565323 , 1.0
        elif user == '3' : x,y,z,w = 13.217512130737305 , -1.0282347202301025 , 0.07887832075357437 , 1.0

        elif user == '4' : x,y,z,w = 1.935251235961914, 1.013933777809143 , -3.104468822479248 , 1.0
        elif user == '5' : x,y,z,w = 7.363372325897217 , 1.2579491138458252, -3.114806890487671 , 1.0
        elif user == '6' : x,y,z,w = 12.76968765258789 , 1.3444373607635498, -3.127167224884033 , 1.0

        

        elif user == '7' : x,y,z,w = 2.9748191833496094 , 3.3843119144439697 , 3.1026182174682617 , 1.0
        elif user == '8' : x,y,z,w = 6.81138277053833 , 3.5629584789276123 , -3.1405885219573975 , 1.0
        elif user == '9' : x,y,z,w = 12.099881172180176 , 3.782682418823242 , -3.1250689029693604 , 1.0

        elif user == '10' : x,y,z,w = 2.0076065063476562 , 5.938619613647461 , -3.1079671382904053, 1.0
        elif user == '11' : x,y,z,w = 6.87885856628418 , 5.994857311248779 , -3.1397738456726074 , 1.0
        elif user == '12' : x,y,z,w = 11.675626754760742 , 6.245480537414551 , -3.0925588607788086 , 1.0


        elif user == '13' : x,y,z,w = 14.152186393737793 , 5.218862533569336 , 0.5229478478431702 , 1.0

        elif user == '14' : x,y,z,w = 18.169801712036133 , 63.34782028198242 , 1.621294379234314 , 1.0 
        elif user == '15' : x,y,z,w = 18.595335006713867 , 34.86942672729492 , 1.5839771032333374 , 1.0 
        elif user == '16' : x,y,z,w = 20.388240814208984 , 1.6881142854690552 , -1.5700036287307741 , 1.0 

        elif user == '99' : os.system("rostopic pub /move_base/cancel actionlib_msgs/GoalID -- {}")


        # tune 
        # https://answers.ros.org/question/210914/robot-unable-to-rotate-in-place-for-dwa_local_planner/
        
        if user.isdigit():
            pub_state_led.led_state(n = 0 )
            result = movebase_client(user , x, y , z , w )
            ''' Test function ''' 
            # result = int(input("true / false : "))

            
            # Write monitor ask user 
            if result:
                arr[int(user)] = f"x{user}"
                # print(f"State robot x{int(user)}")
                pub_state_led.led_state(n = 1 )
                rospy.loginfo("Goal execution done!")
                rospy.loginfo(f"Location {user} done ! \n") 
                user = ''

            else: 
                try:
                    user_try = input("Try again (Y/N) :")
                    if user_try == 'y' or user_try == 'Y' :
                        os.system("python Send_goal.py")
                        # pass
                    elif user_try == 'n' or user_try == 'N':
                        os.system('rostopic pub /sl std_msgs/Int32 "data: 1"')
                        break
                except NameError : 
                    break
        else:
            user = ''
            break