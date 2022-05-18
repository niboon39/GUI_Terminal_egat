import os
import time 

# os.system("roslaunch robotamr Keep_position.launch")
# time.sleep(2)

''' Check Path  '''
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
os.system("python Send_goal.py")