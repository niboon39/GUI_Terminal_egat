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

arr = ["x_final (x17)","x1" , "x2" , "x3" , "x4",
       "x5" , "x6" , "x7" , "x8",
       "x9" , "x10" , "x11" , "x12",
       "x13" , "x14" , "x15" , "x16" , "x_start (x0)"]

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
        print(f"\t\t\t-- {arr[17]} --\t\t\n")
        print(f"\t\t\t|{arr[1]} | {arr[5]} | {arr[9]}  | {arr[13]} |\t")
        print(f"\t\t\t|{arr[2]} | {arr[6]} | {arr[10]} | {arr[14]} |\t")
        print(f"\t\t\t|{arr[3]} | {arr[7]} | {arr[11]} | {arr[15]} |\t")
        print(f"\t\t\t|{arr[4]} | {arr[8]} | {arr[12]} | {arr[16]} |\t\n")
        print(f"\t\t\t\t -- {arr[0]}--")

        ''' 

        xn is position in matrix. 
        x_final is stop position.
        x_start is start position.

        '''

        print("\t\t***********************************\n")
        print("Exit program. ( Pres any keys to exit )\n")

        
        user = input("Enter location : ")

        if user == '0' : x,y,z,w = 16.212724685668945 , 4.567800521850586 , -3.1295251846313477, 1.0  # Stand by  : start 

        elif user == '5' : x,y,z,w = 12.942115783691406 , 3.569549322128296 , 3.040299415588379 , 1.0 # 4 
        elif user == '6' : x,y,z,w = 8.700674057006836 , 3.8169920444488525 , 3.080739736557007 , 1.0 # 5 
        elif user == '7' : x,y,z,w = 4.428078651428223 , 4.0588603019714355 , 3.072641611099243 , 1.0 # 6

        elif user == '17': x,y,z,w = 0.45002269744873047 , 0.050867676734924316 , -3.1041104793548584 , 1.0 # final

        # outside
        elif user == '1' : x,y,z,w = 26.14203643798828 , 0.6365156173706055 , 1.557976484298706 , 1.0
        elif user == '2' : x,y,z,w = 26.044910430908203 , 17.760746002197266 , 1.5618308782577517 , 1.0
        elif user == '3' : x,y,z,w = 42.07557678222656 , 0.3966207504272461 , -0.07080415636301039 , 1.0
        elif user == '4' : x,y,z,w = 55.612213134765625 , 0.41779136657714844 , 0.0040978342294693 , 1.0
        elif user == '10' : x,y,z,w = 1.3815135955810547 , -0.03851890563964844 , 0.0033116305712610488 , 1.0


    
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
                        break
                except NameError : 
                    break
        else:
            user = 'Exit'
            break