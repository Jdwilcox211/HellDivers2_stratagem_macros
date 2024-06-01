from icecream import ic
import os
import time
from datetime import datetime
import logging
import sys
import win32api
import win32com.client

#icecream status
#ic.enable()
#ic.disable()

#remove last log file
#os.remove("rand_wasd.log")

#timestamp for script run
runtimestamp=datetime.now()
runtlog=runtimestamp.strftime("%m/%d/%Y %I:%M:%S %p")

#setup logging
logging.basicConfig(filename="helldivers2_macro.log", filemode="a")
logger = logging.getLogger("rand_wasd")
handler = logging.StreamHandler()
formatter = logging.Formatter("%(name)-12s %(levelname) -8s %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

timestamp=datetime.now()
tlog=timestamp.strftime("%m/%d/%Y %I:%M:%S %p")
logger.info(f' {tlog} - Starting macro script...')

time.sleep(2)


#pydirectinput.press('left')  

shell = win32com.client.Dispatch("WScript.Shell")

#shell.AppActivate("myApp")
shell.SendKeys("{END}")
shell.SendKeys("{DOWN}")
shell.SendKeys("{DOWN}")
shell.SendKeys("{UP}")
shell.SendKeys("{RIGHT}")



try:
    # #Resupply - Down, Down, Up, Right.
    # pydirectinput.press('end')
    # #pydirectinput.press(['down', 'down', 'up', 'right'])
    # pydirectinput.press('down')
    # pydirectinput.press('down')
    # pydirectinput.press('up')
    # pydirectinput.press('right')
    shell = win32com.client.Dispatch("WScript.Shell")

    #shell.AppActivate("myApp")
    shell.SendKeys("{END}")
    shell.SendKeys("{DOWN}")
    shell.SendKeys("{DOWN}")
    shell.SendKeys("{UP}")
    shell.SendKeys("{RIGHT}")



except Exception as e:
    logger.warning(f'{e}')
    sys.exit()
        
  
timestamp=datetime.now()
tlog=timestamp.strftime("%m/%d/%Y %I:%M:%S %p")
logger.info(f' {tlog} macro completed')