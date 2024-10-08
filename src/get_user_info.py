import os
from datetime import datetime
import time




def get_info():
    # print(datetime.now())
    current_time = time.strftime('%H:%M:%S')
    script_path = os.getcwd()
    return current_time, script_path


