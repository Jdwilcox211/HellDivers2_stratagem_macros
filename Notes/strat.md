Mission-Specific Stratagem Codes
Reinforce - Up, Down, Right, Left, Up.
SOS Beacon - Up, Down, Right, Up.
Resupply - Down, Down, Up, Right.
Eagle Rearm - Up, Up, Left, Up, Right.
SEAF Artillery - Left, Up, Up, Down.
SSSD Delivery - Down, Down, Down, Up, Up.
Upload Data - Left, Right, Up, Up, Up.
Hellbomb - Up, Down, Left, Down, Up, Right, Down, Up.
Seismic Probe - Up, Up, Left, Right, Down, Down.
Prospecting Drill - Down, Down, Left, Right, Down, Down.
Super Earth Flag - Down, Up, Down, Up.
Patriotic Administration Center Stratagem Codes
Machine Gun (level 1) - Down, Left, Down, Up, Right.
Anti-Material Rifle (level 2) - Down, Left, Right, Up, Down.
Stalwart (level 2) - Down, Left, Down, Up, Up, Left.
Expendable Anti-Tank (level 3) - Down, Down, Left, Up, Right.
Recoiled Rifle (level 5) - Down, Left, Right, Right, Left.
Flamethrower (level 10) - Down, Left, Up, Down, Up.
Autocannon (level 10) - Down, Left, Down, Up, Up, Right.
Heavy Machine Gun (level 12) - Down, Left, Up, Down, Down.
Railgun (level 20) - Down, Right, Left, Down, Up, Left, Right.
Spear (level 20) - Down, Down, Up, Down, Down.
Orbital Cannons Stratagem Codes
Orbital Gatling Barrage (level 2) - Right, Down, Left, Up, Up.
Orbital Airburst Strike (level 5) - Right, Right Right.
Orbital 120MM HE Barrage (level 5) - Right, Down, Left, Right, Down.
Orbital 380MM HE Barrage (level 8) - Right, Down, Up, Up, Left, Down, Down.
Orbital Walking Barrage (level 10) - Right, Right, Down, Left, Right, Down.
Orbital Lasers (level 15) - Right, Down, Up, Right, Down.
Orbital Railcannon Strike (level 20) - Right, Up, Down, Down, Right.
Hangar Stratagem Codes
Eagle Strafing Run (level 2) - Up, Right, Right.
Eagle Airstrike (level 2) - Up, Right, Down, Right.
Eagle Cluster Bomb (level 3) - Up, Right, Down, Down, Right.
Eagle Napalm Airstrike (level 5) - Up, Right, Down, Up.
Jump Pack (level 8) - Down, Up, Up, Down, Up.
Eagle Smoke Strike (level 8) - Up, Right, Up, Down.
Eagle 110MM Rocket Pods (level 10) - Up, Right, Up, Left.
Eagle 500KG Bomb (level 15) - Up, Right, Down, Down, Down.
Bridge Stratagem Codes
Orbital Precision Strike (level 1) - Right, Right, Up.
Orbital Gas Strike (level 3) - Right, Right, Down, Right.
Orbital EMS Strike (level 5) - Right, Right, Left, Down.
Orbital Smoke Strike (level 8) - Right, Right, Down, Up.
HMG Emplacement (level 10) - Down, Up, Left, Right, Right, Left.
Shield Generation Relay (level 10) - Down, Up, Left, Down, Right, Right.
Tesla Tower (15) - Down, Up, Right, Up, Left, Right.
Engineering Bay Stratagem Codes
Anti-Personnel Minefield (level 2) - Down, Left, Up, Right.
Supply Pack (level 3) - Down, Left, Down, Up, Up, Down.
Grenade Launcher (level 5) - Down, Left, Up, Left, Down.
Laser Cannon (level 5) - Down, Left, Down, Up, Left.
Incendiary Mines (level 8) - Down, Left, Left, Down.
"Guard Dog" Rover (level 10) - Down, Up, Left, Up, Right, Right.
Ballistic Shield Backpack (level 12) - Down, Left, Up, Up, Right.
Arc Thrower (level 15) - Down, Right, Up, Left, Down.
Quasar Cannon (level 18) - Down, Up, Left, Right, Left, Right.
Shield Generator Pack (level 20) - Down, Up, Left, Right, Left, Right.
Robotic Workshop Stratagem Codes
Machine Gun Sentry (level 3) - Down, Up, Right, Right, Up.
Gatling Sentry (level 5) - Down, Up, Right, Left.
Mortar Sentry (level 8) - Down, Up, Right, Right, Down.
"Guard Dog" (level 10) - Down, Up, Left, Up, Right, Down.
Autocannon Sentry (level 13) - Down, Up, Right, Up, Left, Up.
Rocket Sentry (level 15) - Down, Up, Right, Right, Left.
EMS Mortar Sentry (level 20) - Down, Down, Up, Up, Left.
Patriot Exosuit (level 25) - Left, Down, Right, Up, Left, Down, Down

STRATAGEMS: dict[T_Stratagems, T_Inputs] = {
    'resupply': ['Down', 'Down', 'Up', 'Right'],
    'orbital illumination flare': ['Right', 'Right', 'Left', 'Left'],
    'hellbomb': ['Down', 'Up', 'Left', 'Down', 'Up', 'Right', 'Down', 'Up'],
    'reinforce': ['Up', 'Down', 'Right', 'Left', 'Up'],
    'machine gun': ['Down', 'Left', 'Down', 'Up', 'Right'],
    'heavy machine gun': ['Down', 'Left', 'Up', 'Down', 'Down'],
    'anti-material rifle': ['Down', 'Left', 'Right', 'Up', 'Down'],
    'stalwart': ['Down', 'Left', 'Down', 'Up', 'Up', 'Left'],
    'expendable anti-tank': ['Down', 'Down', 'Left', 'Up', 'Right'],
    'recoilless rifle': ['Down', 'Left', 'Right', 'Right', 'Left'],
    'flamethrower': ['Down', 'Left', 'Up', 'Down', 'Up'],
    'autocannon': ['Down', 'Left', 'Down', 'Up', 'Up', 'Right'],
    'railgun': ['Down', 'Right', 'Down', 'Up', 'Left', 'Right'],
    'spear': ['Down', 'Down', 'Up', 'Down', 'Down'],
    'eagle strafing run': ['Up', 'Right', 'Right'],
    'eagle airstrike': ['Up', 'Right', 'Down', 'Right'],
    'eagle cluster bomb': ['Up', 'Right', 'Down', 'Down', 'Right'],
    'eagle napalm airstrike': ['Up', 'Right', 'Down', 'Up'],
    'jump pack': ['Down', 'Up', 'Up', 'Down', 'Up'],
    'eagle smoke strike': ['Up', 'Right', 'Up', 'Down'],
    'eagle 110mm rocket pods': ['Up', 'Right', 'Up', 'Left'],
    'eagle 500kg bomb': ['Up', 'Right', 'Down', 'Down', 'Down'],
    'orbital gatling barrage': ['Right', 'Down', 'Left', 'Up', 'Up'],
    'orbital airburst strike': ['Right', 'Right', 'Right'],
    'orbital 120mm he barrage': ['Right', 'Right', 'Down', 'Left', 'Right', 'Down'],
    'orbital walking barrage': ['Right', 'Down', 'Up', 'Up', 'Left', 'Down', 'Down'],
    'orbital 380mm he barrage': ['Right', 'Down', 'Up', 'Up', 'Left', 'Down', 'Down'],
    'orbital lasers': ['Right', 'Down', 'Up', 'Right', 'Down'],
    'orbital railcannon strike': ['Right', 'Up', 'Down', 'Down', 'Right'],
    'orbital precision strike': ['Right', 'Right', 'Up'],
    'orbital gas strike': ['Right', 'Right', 'Down', 'Right'],
    'orbital ems strike': ['Right', 'Right', 'Left', 'Down'],
    'orbital smoke strike': ['Right', 'Right', 'Down', 'Up'],
    'hmg emplacement': ['Down', 'Up', 'Left', 'Right', 'Right', 'Left'],
    'shield generation relay': ['Down', 'Down', 'Left', 'Right', 'Left', 'Right'],
    'tesla tower': ['Down', 'Up', 'Right', 'Up', 'Left', 'Right'],
    'machine gun sentry': ['Down', 'Up', 'Right', 'Right', 'Up'],
    'gatling sentry': ['Down', 'Up', 'Right', 'Left'],
    'mortar sentry': ['Down', 'Up', 'Right', 'Right', 'Down'],
    'guard dog': ['Down', 'Up', 'Left', 'Up', 'Right', 'Down'],
    'autocannon sentry': ['Down', 'Up', 'Right', 'Up', 'Left', 'Up'],
    'rocket sentry': ['Down', 'Up', 'Right', 'Right', 'Left'],
    'ems mortar sentry': ['Down', 'Up', 'Right', 'Down', 'Right'],
    'anti-personnel minefield': ['Down', 'Left', 'Up', 'Right'],
    'supply pack': ['Down', 'Left', 'Down', 'Up', 'Up', 'Down'],
    'grenade launcher': ['Down', 'Left', 'Up', 'Left', 'Down'],
    'quasar cannon': ['Down', 'Down', 'Up', 'Left', 'Right'],
    'laser cannon': ['Down', 'Left', 'Down', 'Up', 'Left'],
    'incendiary mines': ['Down', 'Left', 'Left', 'Down'],
    'guard dog rover': ['Down', 'Up', 'Left', 'Up', 'Right', 'Right'],
    'ballistic shield backpack': ['Down', 'Left', 'Down', 'Down', 'Up', 'Left'],
    'arc thrower': ['Down', 'Right', 'Down', 'Up', 'Left', 'Left'],
    'shield generator pack': ['Down', 'Up', 'Left', 'Right', 'Left', 'Right'],
    'patriot exosuit': ['Left', 'Down', 'Right', 'Up', 'Left', 'Down', 'Down'],
}