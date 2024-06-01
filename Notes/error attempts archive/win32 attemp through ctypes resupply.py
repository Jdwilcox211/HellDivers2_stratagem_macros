from icecream import ic
import os
import time
from datetime import datetime
import logging
import sys
import win32con
import os
import ctypes
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


#functions for direct input with ctypes
#script help from https://danieldusek.com/feeding-key-presses-to-reluctant-games-in-python.html


PUL = ctypes.POINTER(ctypes.c_ulong)

class KeyBdInput(ctypes.Structure):
   _fields_ = [("wVk", ctypes.c_ushort),
               ("wScan", ctypes.c_ushort),
               ("dwFlags", ctypes.c_ulong),
               ("time", ctypes.c_ulong),
               ("dwExtraInfo", PUL)]


class HardwareInput(ctypes.Structure):
   _fields_ = [("uMsg", ctypes.c_ulong),
               ("wParamL", ctypes.c_short),
               ("wParamH", ctypes.c_ushort)]


class MouseInput(ctypes.Structure):
   _fields_ = [("dx", ctypes.c_long),
               ("dy", ctypes.c_long),
               ("mouseData", ctypes.c_ulong),
               ("dwFlags", ctypes.c_ulong),
               ("time", ctypes.c_ulong),
               ("dwExtraInfo", PUL)]


class Input_I(ctypes.Union):
   _fields_ = [("ki", KeyBdInput),
               ("mi", MouseInput),
               ("hi", HardwareInput)]


class Input(ctypes.Structure):
   _fields_ = [("type", ctypes.c_ulong),
("ii", Input_I)]

def press_key(key):
   extra = ctypes.c_ulong(0)
   ii_ = Input_I()

   flags = 0x0008

   ii_.ki = KeyBdInput(0, key, flags, 0, ctypes.pointer(extra))
   x = Input(ctypes.c_ulong(1), ii_)
   ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def release_key(key):
   extra = ctypes.c_ulong(0)
   ii_ = Input_I()

   flags = 0x0008 | 0x0002

   ii_.ki = KeyBdInput(0, key, flags, 0, ctypes.pointer(extra))
   x = Input(ctypes.c_ulong(1), ii_)
   ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

time.sleep(5)

#actual keypresses
#############################
#get_game_window()
press_key(0xcf)    # (I bind mine to end) - opens straagym (end key) alt key would be 0x38 
release_key(0xcf)

# Arrow binds: 
# up 0xC8
# down 0xD0
# right 0xCD
# left 0xCB


press_key(0xD0)
release_key(0xD0) # down 

press_key(0xD0)
release_key(0xD0) # down

press_key(0xC8)
release_key(0xC8) # up

press_key(0xCD)
release_key(0xCD) # right


#press_key(0x1C);release_key(0x1C); # Submit it


###############################
# try:



# except Exception as e:
#     logger.warning(f'{e}')
#     sys.exit()
        
  
timestamp=datetime.now()
tlog=timestamp.strftime("%m/%d/%Y %I:%M:%S %p")
logger.info(f' {tlog} macro completed')