
from icecream import ic
import time
from datetime import datetime
import logging
import sys
import win32con
import os
import win32api
import win32gui
import re
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
logger = logging.getLogger("reinforcement")
handler = logging.StreamHandler()
formatter = logging.Formatter("%(name)-12s %(levelname) -8s %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

timestamp=datetime.now()
tlog=timestamp.strftime("%m/%d/%Y %I:%M:%S %p")
logger.info(f' {tlog} - Starting macro script...')

#bring window forward
class WindowMgr:
   #"""Encapsulates some calls to the winapi for window management"""
   def __init__ (self):
      #"""Constructor"""
      self._handle = None

   def find_window(self, class_name, window_name = None):
      #"""find a window by its class_name"""
      self._handle = win32gui.FindWindow(class_name, window_name)

   def _window_enum_callback(self, hwnd, wildcard):
      #'''Pass to win32gui.EnumWindows() to check all the opened windows'''
      if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) != None:
         self._handle = hwnd

   def find_window_wildcard(self, wildcard):
      self._handle = None
      win32gui.EnumWindows(self._window_enum_callback, wildcard)

   def set_foreground(self):
      #"""put the window in the foreground"""
      win32gui.SetForegroundWindow(self._handle)


w = WindowMgr()
w.find_window_wildcard(".*HELLDIVER.*")
w.set_foreground()

end = 0x23 #VirtualKey Code
Up = 0x26
Down = 0x28
Right = 0x27
Left = 0x25

def pushkey(keytopush):
    win32api.keybd_event(keytopush,0,0,0) # holds the key down
    time.sleep(0.03) # waits 1 second
    win32api.keybd_event(keytopush,0,win32con.KEYEVENTF_KEYUP,0) # releases the key
    time.sleep(0.03)


try:
   # Reinforce - Up, Down, Right, Left, Up.
   strat=[Up, Down, Right, Left, Up]
   pushkey(end)
   for arrowkey in strat:
       pushkey(arrowkey)


except Exception as e:
    logger.warning(f'{e}')
    sys.exit()
        
  
timestamp=datetime.now()
tlog=timestamp.strftime("%m/%d/%Y %I:%M:%S %p")
logger.info(f' {tlog} macro completed')
