import random
import pyautogui
import keyboard
import time
import math
import configparser

# Scum Drop Generator
# by Aaron D. Gallaway
# (c)2023
# Version 1.0
###############################
###############################
# Generates a random number
# of cargo drops in random
# locations on the Scum map
# and enters the complete
# Scum cargodrop command
# into the Scum in game chat.
#
# The drops can be random, or
# in specified zones.
###############################
###############################

# dictionary = {zone: [x1, y1, x2, y2]}
# x2 > x1 & y1 > y2
zone_dict = {
    'Z4': tuple([617226, -903239, 318177, -601989]),
    'Z3': tuple([309836, -901453, 13170, -603775]),
    'Z2': tuple([6021, -900262, -292432, -603775]),
    'Z1': tuple([-299581, -902644, -596843, -602585]),
    'Z0': tuple([-605183, -902644, -902446, -603180]),
    'A4': tuple([616035, -595440, 315003, -295109]),
    'A3': tuple([312950, -597373, 13765, -297167]),
    'A2': tuple([6021, -596036, -294219, -296572]),
    'A1': tuple([-295485, -599515, -600287, -294925]),
    'A0': tuple([-601130, -598425, -905387, -294863]),
    'B4': tuple([617226, -292404, 315794, 8249]),
    'B3': tuple([312219, -291214, 9713, 9942]),
    'B2': tuple([8702, -293893, -295208, 9732]),
    'B2': tuple([8702, -293893, -295208, 9732]),
    'B1': tuple([-295522, -294640, -600343, 9924]),
    'B0': tuple([-600864, -294339, -905350, 9868]),
    'C4': tuple([618767, 12626, 314677, 314764]),
    'C3': tuple([314304, 10411, 9670, 314783]),
    'C2': tuple([9239, 10363, -295317, 314746]),
    'C1': tuple([-295576, 10179, -600362, 314802]),
    'C0': tuple([-600511, 10128, -905331, 314746]),
    'D4': tuple([618556, 316574, 315049, 619530]),
    'D3': tuple([314451, 315021, 9744, 619604]),
    'D2': tuple([9502, 314968, -295317, 619661]),
    'D1': tuple([-295485, 314950, -600324, 619642]),
    'D0': tuple([-600511, 314969, -905331, 619698]),
    'WORLD': tuple([637685, -922896, -922896, 619200]),
    }

def get_settings():
    config = configparser.ConfigParser()
    config.read('settings.ini')
    min = int(config['settings']['minimum_random'])                     # the minimum number of drops for random drops
    max = int(config['settings']['maximum_random'])                     # the maximum number of drops for random drops
    set = int(config['settings']['set_number'])                         # the set number of drops to create
    lst = config.items('multiple.zones')                                # the zone (or zones) in which to create drops
    num_of_zones = int(config['settings']['number_of_zones_to_drop'])   # the number of random zones in which to create drops (drops will be even split
    aoe = []

    # creates list of zones from ini file
    for key, value in lst:
        aoe.append(value)

    main(min, max, set, num_of_zones, aoe)
    
# Creates drops for a list of zones
# for multi zones, the given number (random or set)
# will be split evenly, rounded up, among each zone
def multi_zone(zones, drops):

    print(f'{drops} in multiple zones {zones}')
    print(len(zones))
    num_of_zones = int(len(zones))
    max = math.ceil(drops / num_of_zones)
    for zone in zones:
        get_locations(zone, max)
        
# Creates drops for a random zone, which includes the world
def random_zone(drops, num_of_zones):
    
    print(f'{drops} in {num_of_zones} random zones')
    dict_list = sorted(zone_dict)
    drops = math.ceil(drops / num_of_zones)
    
    while num_of_zones > 0:
        zone = random.choice(dict_list)
        if zone == 'WORLD':
            continue
        get_locations(zone, drops)
        num_of_zones = num_of_zones - 1

# Creates drops for a given zone, including the world
def get_locations(zone, num_of_drops):

    print(f'{num_of_drops} in {zone}')
    # gets the coordinates of a zone from the dictionary
    coord = zone_dict[zone.upper()]
    x1 = coord[2]
    x2 = coord[0]
    y1 = coord[1]
    y2 = coord[3]

    # creates the given number of drops in random locations in a zone
    for loc in range(0, num_of_drops):
       x_loc = random.randint(x1, x2)
       y_loc = random.randint(y1, y2)
       keyboard.write(f'#ScheduleWorldEvent BP_CargoDropEvent {x_loc} {y_loc} 0')   # writes cargo drop admin command in Scum chat
       keyboard.press_and_release('enter')
       time.sleep(0.5)                                                              # necessary delay to prevent getting booted from server for spam
    keyboard.write(f'{num_of_drops} cargo drops in {zone}')                        # writes control message indicating how many drops were created in which zone
    keyboard.press_and_release('enter')

def main(min, max, set, num_of_zones, aoe):

    # if set is assigned a number, that will be the number of drops
    # else, the number of drops will be random
    if set > 0:
        num_of_drops = set
    else:
        num_of_drops = random.randint(min, max)

    # creates a slight delay to move mouse to appropriate monitor
    # and opens the chat in scum
    time.sleep(3)
    pyautogui.click(button="left")
    keyboard.press_and_release('t')
    print(num_of_zones)

    # determines if drops will be created in multiple given zones,
    # a random zone, or a single given zone including the world
    if num_of_zones > 0:
        random_zone(num_of_drops, num_of_zones)
    elif len(aoe) > 1:
        multi_zone(aoe, num_of_drops)
    else:
        aoe = aoe[0]
        get_locations(aoe, num_of_drops)

    keyboard.press_and_release('escape')

if __name__ == '__main__':
    get_settings()