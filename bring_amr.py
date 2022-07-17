import os
import time 

# print(os.getcwd())  

def check_path_go (path):
    if os.path.isdir(path):
        os.chdir(path)
        return f"now:{os.getcwd()}"
    else:
        print("Fail to go path.")
        return False 
        
path_script = "/home/niboon/egat_rb/src/robotamr/Script/GUI_Terminal_egat/"
check_path_go(path_script)

print("\t\t\t  Welcome to EGAT-AMR \n ")
user = input("Select (1 . Navigation ) and (2 . Fix position ) : ")

if user == '1':
    os.system("roslaunch robotamr Keep_position.launch")
elif (user == '2'):
    
    os.system("python Send_goal.py")