import os
import random

""" This is a test """

def init_files():
    try:
        os.mkdir('Assets')
    except FileExistsError:
        pass

#Default values
player_stats_default = {'hp': 15, 'dmg': 1, 'dmg_type': 'physical', 'primary_resistance': 'none', 'secondary_resistance': 'none'}
player_equip_default = {'armor': 'none', 'weapon': 'none'}
player_inv_default = []

#sword stats
#rusty sword stats
weapon_stats_sword_rusty_dmg = 5
weapon_stats_sword_rusty_bonus_dmg = random.randint(-3,5)
weapon_stats_sword_rusty_edmg = weapon_stats_sword_rusty_dmg+weapon_stats_sword_rusty_bonus_dmg

def weapon_stats_sword_rusty_evade_chance_generator():
    global weapon_stats_sword_rusty_evade_chance 
    weapon_stats_sword_rusty_evade_chance = bool(random.randint(0,100) <= 100)

weapon_stats_sword_rusty = {'dmg': weapon_stats_sword_rusty_dmg, 'bonus_dmg': weapon_stats_sword_rusty_bonus_dmg, 'edmg': weapon_stats_sword_rusty_edmg, 'evade_chance': weapon_stats_sword_rusty_evade_chance}


weapon_stats_sword_iron_dmg = 10
weapon_stats_sword_iron_bonus_dmg = random.randint(-4,7)
weapon_stats_sword_iron_edmg = weapon_stats_sword_rusty_dmg+weapon_stats_sword_rusty_bonus_dmg
weapon_stats_sword_iron = {'dmg': weapon_stats_sword_rusty_dmg, 'bonus_dmg': weapon_stats_sword_rusty_bonus_dmg, 'edmg': weapon_stats_sword_rusty_edmg}

weapon_stats_sword_rusty_dmg = 15
weapon_stats_sword_rusty_bonus_dmg = random.randint(-5,10)
weapon_stats_sword_rusty_edmg = weapon_stats_sword_rusty_dmg+weapon_stats_sword_rusty_bonus_dmg
weapon_stats_sword_rusty = {'dmg': weapon_stats_sword_rusty_dmg, 'bonus_dmg': weapon_stats_sword_rusty_bonus_dmg, 'edmg': weapon_stats_sword_rusty_edmg}

#advanced sword stats

#bow stats
#basic bow stats
weapon_stats_bow_twig_bow = {}
weapon_stats_bow_shortbow = {}
weapon_stats_bow_longbow = {}
weapon_stats_bow_shieldbow = {}

#advanced bow stats

#wand stats
#basic wand stats


#tier 1 class abilities
class_abilities_knight_default = {}
class_abilities_ranger_default = {}
class_abilities_wizard_default = {}

#tier 2 class abilities
class_abilities_paladin_default = {}
class_abilities_oathbreaker_default = {}

class_abilities_hunter_default = {}
class_abilities_finder_default = {}

class_abilities_mage_default = {}
class_abilities_warlock_default = {}

#tier 3 class abilities
class_abilities_lightbringer_default = {}
class_abilities_plaguebearer_default = {}

class_abilities_tracker_default = {}
class_abilities_seeker_default = {}

class_abilities_archmage_default = {}
class_abilities_lich_default = {}

def file_player_update():
    #writes the current player stats to a text file, which can be read on program start up to save player stats
    file_player_stats = open('Assets\\file_player_stats.txt', 'w+')
    file_player_stats.write(str(player_stats))
    file_player_stats.close()

    #writes the current equipment to a text file, which can be read on program start up to save player equipment
    file_player_equip = open('Assets\\file_player_equip.txt', 'w+')
    file_player_equip.write(str(player_equip))
    file_player_equip.close()

    #writes the current player inventory to a text file, which can be read on program start up to save player inventory
    file_player_inv = open('Assets\\file_player_inv.txt', 'w+')
    file_player_inv.write(str(player_inv))
    file_player_inv.close()

'''
def stat_update():
    #checks players equipment and updates stats accordingly. Use after every equipment change.

    
    #checks and updates armor
    if player_equip['armor'] == 'none':
        player_stats['hp'] = 15
        player_stats['primary_resistance'] = 'none'
        player_stats['secondary_resistance'] = 'none'
        
    elif player_equip['armor'] == 'leather rags':
        player_stats['hp'] = 20
        player_stats['primary_resistance'] = 'none'
        player_stats['secondary_resistance'] = 'none'
        
    elif player_equip['armor'] == 'leather armor':
        player_stats['hp'] = 30
        player_stats['primary_resistance'] = 'none'
        player_stats['secondary_resistance'] = 'none'
        
    elif player_equip['armor'] == 'iron armor':
        player_stats['hp'] = 40
        player_stats['primary_resistance'] = 'fire'
        player_stats['secondary_resistance'] = 'none'
        
    else:
        player_stats['hp'] = 15
        player_stats['primary_resistance'] = 'none'
        player_stats['secondary_resistance'] = 'none'

    #checks and updates weapons
    if player_equip['weapon'] == 'none':
        player_stats['dmg'] = 1
        player_stats['dmg_type'] = 'physical'
        
    elif player_equip['weapon'] == 'rusty sword':
        player_stats['dmg'] = 5
        player_stats['dmg_type'] = 'physical'

    elif player_equip['weapon'] == 'iron sword':
        player_stats['dmg'] = 10
        player_stats['dmg_type'] = 'physical'

    else:
        player_stats['dmg'] = 1
        player_stats['dmg_type'] = 'physical'

    file_player_update()
'''    
init_files()
print(weapon_stats_sword_rusty_dmg)
print(weapon_stats_sword_rusty_bonus_dmg)
print(weapon_stats_sword_rusty_edmg)



'''
npc_old_man_stats = {'hp': 15, 'dmg':1, 'dmg_type': 'physical', 'primary_resistance': 'none', 'secondary_resistance': 'none'}

stat_update()

input('Old Man: Hello, traveler. Do not worry, you are safe...')
input('\nOld Man: We found you just out of town, being attacked by wolves. Its dangerous out there, especially at night...')
player_name = input('\nOld Man: Tell me, boy. What is your name?/n/nEnter Your Name: ')
input(f"\nOld Man: Ah, {player_name}, interesting name.")
input('\nOld Man: Oh, you are heading to the city? Another senseless fool seeking to be a hero?')
input('\nOld Man: Listen, a town like ours doesn\'t need the unwanted attention that comes from heroes like you')
input('\nOld Man: Here, take this for the journey ahead.')
input('The Old Man hands you leather rags to replace your torn up clothes, and gives you a rusty blade')

player_equip['armor'] = 'leather rags'
player_equip['weapon'] = 'rusty sword'
stat_update()

input('The Old Man walks you to the door.')
input('Old Man: Listen, my daughter is still in Erethin. Since you seem to be heading that direction, please find her. Give her this letter.')
input('As you walk out of the door, you see the small town the Old Man has brought you to. It is a quaint village
'''



