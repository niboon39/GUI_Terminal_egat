#!/usr/bin/env python3
from curses.ascii import isdigit
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
    arr[int(n)-1] = "O"

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

        print(f"OUTSIDE (3 POINT) ->  Q , W , E \n")

        ''' 

        xn is position in matrix. 
        x_final is stop position.
        x_start is start position.

        '''

        print("\t\t***********************************\n")
        print("Exit program. ( Pres any keys to exit )\n")

        
        user = input("Enter location : ")


        # outside
        if user == '0' : x,y,z,w = -0.2681446075439453 , 0.11314404010772705 , -0.044969722628593445, 1.0
        elif user == '1' : x,y,z,w = 1.6677541732788086 , -1.2966781854629517 , 3.116734266281128 , 1.0
        elif user == '2' : x,y,z,w = 6.508959770202637 , -1.178796410560608 , -3.13765811920166 , 1.0
        elif user == '3' : x,y,z,w = 12.706883430480957 , -0.9444266557693481 , -3.127406358718872 , 1.0

        elif user == '4' : x,y,z,w = 1.7791656255722046 , 1.1647899150848389 , -0.042337726801633835 , 1.0
        elif user == '5' : x,y,z,w = 7.150696754455566 , 1.2767610549926758, -0.021142948418855667 , 1.0
        elif user == '6' : x,y,z,w = 13.19418716430664 , 1.511828064918518, -0.04700146988034249 , 1.0

        

        elif user == '7' : x,y,z,w = 2.4428787231445312 , 3.4712600708007812 , 3.1159586906433105 , 1.0
        elif user == '8' : x,y,z,w = 7.764065265655518 , 3.6295900344848633 , 3.1212193965911865 , 1.0
        elif user == '9' : x,y,z,w = 13.491460800170898 , 3.9612393379211426 , -3.0760276317596436 , 1.0

        elif user == '10' : x,y,z,w = 2.336583137512207 , 5.989779949188232 , -3.1361117362976074 , 1.0
        elif user == '11' : x,y,z,w = 7.390283107757568 , 6.127702236175537 , -3.134232759475708 , 1.0
        elif user == '12' : x,y,z,w = 13.535938262939453 , 6.184544563293457 , 3.1185755729675293 , 1.0


        elif user == '13' : x,y,z,w = 14.796737670898438 , 5.377570629119873 , 3.1276440620422363 , 1.0

        elif user == 'q' : x,y,z,w = 0 , 0 , 0 , 1.0 
        elif user == 'w' : x,y,z,w = 0 , 0 , 0 , 1.0 
        elif user == 'e' : x,y,z,w = 0 , 0 , 0 , 1.0 
        

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
            user = 'Exit'
            break