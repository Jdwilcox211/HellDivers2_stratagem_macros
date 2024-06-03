import time
from datetime import datetime
import sys
import re
import win32con
import win32api
import win32gui
from icecream import ic


#icecream status
#ic.enable()
ic.disable()

timestamp=datetime.now()
tlog=timestamp.strftime("%m/%d/%Y %I:%M:%S %p")
ic(f'{tlog} - Script start')

inputArgs = sys.argv

ic(inputArgs[1])

#timestamp for script run
ic(f'Input arguments {inputArgs}')


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


#VirtualKey Code:
STRATKEY = 0x23 #end key. alt = 0x12. ctrl = 0x11.
Up = 0x26 #up arrow. w = 0x57
Down = 0x28 #down arrow. s = 0x53
Right = 0x27 # right arrow. d = 0x44
Left = 0x25 #left arrow a = 0X41


#Dictionary of stratagems
STRATAGEMS = {
'airburst_rocket_launcher': [Down, Up, Up, Left, Right],
'anti-material_rifle': [Down, Left, Right, Up, Down],
'anti-personnel_minefield': [Down, Left, Up, Right],
'arc_thrower': [Down, Right, Down, Up, Left, Left],
'autocannon_sentry': [Down, Up, Right, Up, Left, Up],
'autocannon': [Down, Left, Down, Up, Up, Right],
'ballistic_shield_backpack': [Down, Left, Down, Down, Up, Left],
'eagle_110mm_rocket_pods': [Up, Right, Up, Left],
'eagle_500kg_bomb': [Up, Right, Down, Down, Down],
'eagle_airstrike': [Up, Right, Down, Right],
'eagle_cluster_bomb': [Up, Right, Down, Down, Right],
'eagle_napalm_airstrike': [Up, Right, Down, Up],
'eagle_rearm': [Up, Up, Left, Up, Right],
'eagle_smoke_strike': [Up, Right, Up, Down],
'eagle_strafing_run': [Up, Right, Right],
'emancipator_exosuit': [Left, Down, Right, Up, Left, Down, Up],
'ems_mortar_sentry': [Down, Up, Right, Down, Right],
'expendable_anti-tank': [Down, Down, Left, Up, Right],
'flamethrower': [Down, Left, Up, Down, Up],
'gatling_sentry': [Down, Up, Right, Left],
'grenade_launcher': [Down, Left, Up, Left, Down],
'guard_dog_rover': [Down, Up, Left, Up, Right, Right],
'guard_dog': [Down, Up, Left, Up, Right, Down],
'heavy_machine_gun': [Down, Left, Up, Down, Down],
'hellbomb': [Down, Up, Left, Down, Up, Right, Down, Up],
'hmg_emplacement': [Down, Up, Left, Right, Right, Left],
'incendiary_mines': [Down, Left, Left, Down],
'jump_pack': [Down, Up, Up, Down, Up],
'laser_cannon': [Down, Left, Down, Up, Left],
'machine_gun_sentry': [Down, Up, Right, Right, Up],
'machine_gun': [Down, Left, Down, Up, Right],
'mortar_sentry': [Down, Up, Right, Right, Down],
'orbital_120mm_he_barrage': [Right, Right, Down, Left, Right, Down],
'orbital_380mm_he_barrage': [Right, Down, Up, Up, Left, Down, Down],
'orbital_airburst_strike': [Right, Right, Right],
'orbital_ems_strike': [Right, Right, Left, Down],
'orbital_gas_strike': [Right, Right, Down, Right],
'orbital_gatling_barrage': [Right, Down, Left, Up, Up],
'orbital_illumination_flare': [Right, Right, Left, Left],
'orbital_laser': [Right, Down, Up, Right, Down],
'orbital_precision_strike': [Right, Right, Up],
'orbital_railcannon_strike': [Right, Up, Down, Down, Right],
'orbital_smoke_strike': [Right, Right, Down, Up],
'orbital_walking_barrage': [Right, Down, Up, Up, Left, Down, Down],
'patriot_exosuit': [Left, Down, Right, Up, Left, Down, Down],
'prospecting_drill': [Down, Down, Left, Right, Down, Down],
'quasar_cannon': [Down, Down, Up, Left, Right],
'railgun': [Down, Right, Down, Up, Left, Right],
'recoilless_rifle': [Down, Left, Right, Right, Left],
'reinforce': [Up, Down, Right, Left, Up],
'resupply': [Down, Down, Up, Right],
'rocket_sentry': [Down, Up, Right, Right, Left],
'seaf_artillery': [Right, Up, Up, Down],
'seismic_probe': [Up, Up, Left, Right, Down, Down],
'shield_generation_relay': [Down, Down, Left, Right, Left, Right],
'shield_generator_pack': [Down, Up, Left, Right, Left, Right],
'sos_beacon': [Up, Down, Left, Up],
'spear': [Down, Down, Up, Down, Down],
'sssd_delivery': [Down, Down, Down, Up, Up],
'stalwart': [Down, Left, Down, Up, Up, Left],
'super_earth_flag': [Down, Up, Down, Up],
'supply_pack': [Down, Left, Down, Up, Up, Down],
'tesla_tower': [Down, Up, Right, Up, Left, Right],
'upload_data': [Left, Right, Up, Up, Up],                      
}


def pushkey(keytopush):
    win32api.keybd_event(keytopush,0,0,0) # holds the key down
    time.sleep(0.03) # waits 1 second
    win32api.keybd_event(keytopush,0,win32con.KEYEVENTF_KEYUP,0) # releases the key
    time.sleep(0.03)


try:
    # pull stratagem keys from dictionary
    strat=STRATAGEMS.get(inputArgs[1])
    ic(f'Stratagem - {inputArgs[1]} : {strat}')
    pushkey(STRATKEY)
    for arrowkey in strat:
        pushkey(arrowkey)

except Exception as e:
    ic(f'{e}')
    sys.exit()


timestamp=datetime.now()
tlog=timestamp.strftime("%m/%d/%Y %I:%M:%S %p")
ic(f' {tlog} macro completed')
