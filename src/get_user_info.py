import os
import socket
import getpass
import sys
import platform
import wmi
import datetime
# import psutil
import time
from src.get_user_version import get_version


#--- var --- 
PASSWORD = "6868"
FILENAME = "\os.py"
HOST_NAME = socket.gethostname()
USER_NAME = getpass.getuser()
#--- var ---

def get_specified_info(info):
    if info == "cpu":
        return platform.processor()
    elif info == "gpu":
        g = wmi.WMI()
        return g.Win32_VideoController()[0].Name
    # elif info == "boot_time":
    #     # boot_time_timestamp = psutil.boot_time()
    #     # bt = datetime.datetime.fromtimestamp(boot_time_timestamp)
    #     # return f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}"
    # else:
    #     print("ERROR 100")



def getinfo():

    
    user_name=os.getlogin()
    user_login=getpass.getuser()

    user_ip=socket.gethostbyname(HOST_NAME)
    user_HOSTNAME=HOST_NAME
    user_operating_system=platform.system() + " " + platform.win32_ver()[0]

    user_cpu=get_specified_info("cpu")
    user_gpu=get_specified_info("gpu")

    current_location = os.path.realpath(os.path.dirname(__file__))
    current_time = time.strftime('%H:%M:%S')
    current_version = get_version()

    # "Boot time: " + get_specified_info("boot_time"),
    
    print("user name: ", os.getlogin(),"  ///   PC name: ", HOST_NAME, "  ///   script location:", os.path.realpath(os.path.dirname(__file__)), "  ///   IP:", user_ip, "\n")
    return user_name, user_login, user_ip, user_HOSTNAME, user_operating_system, user_cpu, user_gpu, current_location, current_time, current_version

    # filename = "poubelle26.log"
    # with open(filename, "w") as f:
    #     for info in log:
    #         f.write(info + "\n")           #type everything in the text file from the log list
    # os.startfile(filename)



# def add_to_startup(file_path=""):       #add the file on the startup window folder (C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup)
#     if file_path == "":
#         file_path = os.path.dirname(os.path.realpath(__file__))
#         exact_file_path = file_path + FILENAME

#     bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % os.getlogin()     
#     with open(bat_path + '\\' + "poubelle26.bat", "w+") as bat_file:
#         bat_file.write(r'start "" "%s"' % exact_file_path)       #tell to open the programm at the startup // result = start "" "C:\Users\poubelle26\OneDrive\Bureau\hack\os.py"





#list of error 
#ERROR 100 = line 39 in function : "get_specified_info" no argument specified



