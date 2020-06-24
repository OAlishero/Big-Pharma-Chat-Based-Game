#Different Planet 
from random import *
from copy import deepcopy
import re

xSize = 20
ySize = 20
maxNegY = 10
Map = []
shackMap = []
pharmacyMap = []
courthouseMap = []
insuraHeadquartersMap=[]
talklimit=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
maps = {'outsideMap' : Map, 'shackMap' : shackMap, 'pharmacyMap' : pharmacyMap, 'courthouseMap' : courthouseMap, 'insuraHeadquartersMap' : insuraHeadquartersMap}
for v in maps:
  for x in range(xSize):
    maps[v].append([])
    maps[v][x] = list(range(ySize))

class NPC:
  def __init__(self, givenName, maxHealth, givenAttack):
    self.Name = givenName
    self.Health = maxHealth
    self.Attack = givenAttack

currentCoords = [10,10]
name = None

acceptedCommands = {
  'back' : 'backward',
  'backwards' : 'backward',
  'down' : 'backward',
  'up' : 'forward',
  'inv' : 'inventory'

}

globalFuncs = ['die', 'inventory', 'fight', 'dev']

Map[10][10] = {'RoomName' : 'Beginner Room', 'People' : {'Guide':NPC ('Guide', 100, 30)}, 'isLocked' : False, 'AvailabeFunctions' : ['talk to', 'left', 'right', 'backward', 'examine'], 'desc' : "There's a guide, but the room is mostly empty."}

Map[9][10] = {'RoomName' : 'Near Johnson and Johnson Base', 'People' : {'Guide':NPC ('Guide', 100, 30)}, 'isLocked' : False, 'AvailabeFunctions' : ['right' 'examine'], 'desc' : 'You see a clan of Johnson and Johnson Pharmaceuticals in the distance'}

Map[9][9] = {'RoomName' : 'Johnson and Johnson Base', 'People' : {'Johnson and Johnson Pharmaceuticals':NPC ('Johnson and Johnson Pharmaceuticals', 110, 35)}, 'isLocked' : False, 'AvailabeFunctions' : ['talk to', 'forward', 'examine', 'right'], 'desc' : 'You have entered a clan of Johnson and Johnson Pharmaceuticals'}

Map[11][10] = {'RoomName' : 'Neutral Base', 'People' : {'Neutral Pharmaceuticals':NPC('Neutral Pharmaceuticals', 100, 30)}, 'isLocked' : False, 'AvailabeFunctions' : ['talk to','left', 'examine'], 'desc' : 'You have entered a Neutral Base'}

Map[10][9] = {'RoomName' : 'Dark Forest', 'People' : {'Guide':NPC ('Guide', 100, 30)}, 'isLocked' : False, 'AvailabeFunctions' : ['forward', 'backward', 'left', 'examine'], 'desc' : 'You are now entering The Dark Forest'}

Map[10][8] = {'RoomName' : ' Tall brown trees with green leaves', 'People' : {'Guide':NPC ('Guide', 100, 30)}, 'isLocked' : False, 'AvailabeFunctions' : ['forward', 'backward', 'examine'], 'desc' : 'You are now walking through The Dark Forest'}

Map[10][7] = {'RoomName' : ' Insurance goon trees', 'People' : {'Guide':NPC ('Guide', 100, 30)}, 'isLocked' : False, 'AvailabeFunctions' : ['forward', 'backward', 'examine'], 'desc' : 'Tall brown trees with insurance goons that if they touch you they kill you.'}

Map[10][6] = {'RoomName' : ' Tall brown trees with green leaves', 'People' : {'Guide':NPC ('Guide', 100, 30)}, 'isLocked' : False, 'AvailabeFunctions' : ['forward', 'backward', 'examine'], 'desc' : 'Tall brown trees with green leaves and low cut green grass'}

Map[10][5] = {'RoomName' : ' Shack', 'People' : {'Guide':NPC ('Guide', 100, 30)}, 'isLocked' : False, 'AvailabeFunctions' : ['forward', 'backward', 'examine', 'enter'], 'desc' : 'Brown, seemingly abandoned shack'}

shackMap[10][10] = {'RoomName' : ' Shack', 'enter' : 'outsideMap', 'People' : {'Guide':NPC ('Guide', 100, 30)}, 'isLocked' : False, 'AvailabeFunctions' : ['forward', 'backward', 'left', 'right', 'enter', 'examine'], 'desc' : 'You see a gold table with a vile of Adalimumab '}

Map[10][4] = {'RoomName' : ' Desert Wasteland', 'People' : {'Guide':NPC ('Guide', 100, 30)}, 'isLocked' : False, 'AvailabeFunctions' : ['forward', 'backward', 'examine'], 'desc' : 'You are now entering The Desert Wasteland'}

Map[10][3] = {'RoomName' : ' Orange Desert', 'People' : {'Insurance goon1' : NPC('Insurance goon1', 40, 15), 'Insurance goon2' : NPC('Insurance goon2', 40, 15), 'Insurance goon3' : NPC('Insurance goon3', 40, 15)}, 'isLocked' : False, 'AvailabeFunctions' : ['forward', 'backward', 'examine'], 'desc' : 'You are now walking through an orange barren desert with metal shrapnel and insurance goons who will attack you '}

Map[10][2] = {'RoomName' : ' Pharmacy', 'enter': 'pharmacyMap', 'People' : {'Guide':NPC ('Guide', 100, 30)}, 'isLocked' : False, 'AvailabeFunctions' : ['forward', 'backward', 'examine', 'enter'], 'desc' : 'White, dilapated Pharmacy'}

pharmacyMap[10][10] = {'RoomName' : ' Pharmacy',
 'People' : {'Guide':NPC ('Guide', 100, 30)}, 
 'enter' : 'outsideMap',
 'isLocked' : False,
 'AvailabeFunctions' : ['forward', 'backward', 'left', 'right', 'enter', 'examine'],
 'desc' : 'You see a white Pharmacy counter with a package of apixaban and lenalidomide pills. '}

Map[10][1] = {'RoomName' : 'The Gray Rolling Hills', 'People' : {'Guide':NPC ('Guide', 100, 30)}, 'isLocked' : False, 'AvailabeFunctions' : ['forward', 'backward', 'examine'], 'desc' : 'You are now entering The Gray Rolling Hills'}

Map[10][0] = {'RoomName' : 'Low lying hills', 'People' : {'Guide':NPC ('Guide', 100, 30)}, 'isLocked' : False, 'AvailabeFunctions' : ['forward', 'backward', 'examine'], 'desc' : 'You can see gray, desolate, low lying hills.'}

Map[10][-1] = {'RoomName' : 'Courthouse', 'enter': 'courthouseMap', 'People' : {'Guide':NPC ('Guide', 100, 30)}, 'isLocked' : False, 'AvailabeFunctions' : ['forward', 'backward', 'examine', 'enter'], 'desc' : 'You can see a prestine and somehow untouched courthouse.'}

courthouseMap[10][10] = {'RoomName' : 'Courthouse', 'enter' : 'outsideMap', 'People' : {'Guide':NPC ('Guide', 100, 30)}, 'isLocked' : False, 'AvailabeFunctions' : ['forward', 'backward', 'left', 'right', 'enter', 'examine'], 'desc' : 'You can see a rare lawyer that has the power to destory the in Insura once and for all.'}

Map[10][-2] = {'RoomName' : 'The Brown Dirt Road', 'People' : {'Guide':NPC ('Guide', 100, 30)}, 'isLocked' : False, 'AvailabeFunctions' : ['forward', 'backward', 'examine'], 'desc' : 'You are now entering The Brown Dirt Road'}

Map[10][-3] = {'RoomName' : 'Brown dirt road', 'People' : {'Guide':NPC ('Guide', 100, 30)}, 'isLocked' : False, 'AvailabeFunctions' : ['forward', 'backward', 'examine', 'enter'], 'desc' : 'You can see an empty, brown dirt road, leading to the headquarters of the Insura.'}

Map[10][-4] = {'RoomName' : 'Insura Headquarters Entrance', 'enter': 'insuraHeadquartersMap', 'People' : {'Guide':NPC ('Guide', 100, 30)}, 'isLocked' : False, 'AvailabeFunctions' : ['forward', 'examine', 'enter'], 'desc' : 'You have arrived at the entrance of the headquarters of the Insura.'}

insuraHeadquartersMap[10][10] = {'RoomName' : 'Insura Headquarters', 'enter' : 'outsideMap', 'People' : {'Guide':NPC ('Guide', 100, 30)}, 'isLocked' : False, 'AvailabeFunctions' : ['forward', 'backward', 'left', 'right', 'enter' 'examine'], 'desc' : 'You have entered the belly of the beast. The headquarters of the Insura.'}

insuraHeadquartersMap[11][10] = {'RoomName' : 'Allstate', 'People' : {'Allstate' : NPC('Allstate', 130, 45)}, 'isLocked' : False, 'AvailabeFunctions' : ['examine', 'left'], 'desc' : 'You have entered the domain of the Allstate Insura.'}

insuraHeadquartersMap[9][10] = {'RoomName' : NPC('State Farm', 140, 50), 'People': {'State Farm' : NPC('State Farm', 140, 50)}, 'isLocked' : False, 'AvailabeFunctions' : ['backward', 'right', 'examine'], 'desc' : 'You have entered the domain of the State Farm Insura.'}

insuraHeadquartersMap[11][9] = {'RoomName' : NPC('Geico', 150, 55), 'People': {'Geico' : NPC('Geico', 150, 55)}, 'isLocked' : False, 'AvailabeFunctions' : ['forward','examine'], 'desc' : 'You have entered the domain of the Geico Insura.'}

insuraHeadquartersMap[9][9] = {'RoomName' : NPC('Nationwide', 160, 60), 'People': {'Nationwide' : NPC('Nationwide', 160, 60)}, 'isLocked' : False, 'AvailabeFunctions' : ['forward', 'examine'], 'desc' : 'You have entered the domain of the Nationwide Insura.'}

currentMap = 'outsideMap'
#################################################
#Welcome
#################################################
def welcome():
  print("Hello! What's your name?")
  global name 
  name = input('--> ') 
  print("\nNice to meet you " + name + "! Welcome to our game! \n\n ********Quick Tutorial:******** \n Forward/Backward/Left/Right- to move to a different room. \n Use [item]- to wear or use an item. \n Examine- examine the current room and interact with it.\n Inventory- check your inventory \n Attack [person]- Attacks the person targeted. \n\nYou are a 25 year old man, who is fighting the insurance companies in the name of pharma, who have been wronged by the insura, you will see why we are at war with them!\n Get ready... START!")  

welcome()
#################################################
#Character Stats
#################################################
hp= 100
attack= 35
critattack= 65
#################################################
#items
#################################################
inventory = {
  'health potion' : 1, 
}

weapons = {
  'sword':{'Name':'sword', 'damage' : 35, 'critChance' : 10, 'missChance' : 5},
  'knife':{'Name':'knife', 'damage' : 16.5, 'critChance' : 5, 'missChance' : 2.5},
  'gun':{'Name':'gun', 'damage' : 40, 'critChance' : 15, 'missChance' : 10},
  'brick':{'Name':'brick', 'damage' : 10, 'critChange' : 2.5, 'missChance' : 0},
  'bow and arrow':{'Name':'brick', 'damage' : 25, 'critChance' : 7.5, 'missChance' : 10}
  }

equippedWeapon = weapons['sword']

def healthpotion():
  global healthpotions
  if inventory['health potion']>0:
    global hp 
    hp+=20
    print("Your HP is now "+str(hp))
    inventory['health potion']-=1
  else: 
    print("You have no health potions!")
  
sword1=0
def sword1():
  global attack
  attack=45

def mapFunc():
  for y in range(ySize):
    for x in range(xSize):
      cell = maps[currentMap][x][10-y]
      if type(cell) == int:
        print(' ', end = ' ')
      elif x == currentCoords[0] and 10-y == currentCoords[1]:
        print('x', end = ' ')
      else:
        print('o', end = ' ')
    print('')
  

items= {'health potion': healthpotion,
        'map' : mapFunc
} 

def use(x):
  if x in inventory:
    if x in items:
      item = items[x]
      item()
    elif x in weapons:
      global equippedWeapon
      equippedWeapon = weapons[x]
      print(x + ' equipped')
  else:
    print(x + ' not found in inventory')

#################################################
#People
#################################################

def guide():
  if talklimit[0]==1:  
    print("'Hello! You must destroy insurance companies that have infested our world. Seek out the pharmaceuticals for alliance.'")
    ans= input('You: ')
    print("'here take this potion!'")
    inventory['health potion']+=1
    inventory['map'] = 1
    print('You received a map')
    print("You received one potion")
    talklimit[0]=0
  else: 
    print("Good Luck")

def insurance_goons():
  if talklimit[1]==1:  
    print("Who are you?")
    ans= input('You: ') 
    print("You're working with the Pharma! For that you must die!")
    talklimit[1]=0
  else:
    print("KILL THEM!")

def johnson_and_johnson():
  if talklimit[2]==1: 
    print("Are you on our side?")
    ans= input
    print("We do not trust you! Leave now, and never come back!")
    talklimit[2]=0
  else:
    print("GET OUT!!!")
    
def neutral_pharmaceuticals():
  if talklimit[3]==1: 
    print("Who are you?")
    ans= input('You: ') 
    print("You are welcome here, and we trust you.")
    talklimit[3]=0
  else:
    print("Hello Commrade")

def allstate():
  if talklimit[4]==1:
    print("Are you in good hands?")
    ans= input('You: ')
    print("In this case, no. You’re such an annoying thorn in all of our sides. I can’t wait to be rid of you. ")
    talklimit[4]=0
  else:
    print("Your existence will soon be terminated")

def state_farm():
  if talklimit[5]==1:
    print("Like a good neighbor, State Farm takes cares of pests that pose problems to their friends. Goodbye.")
    talklimit[5]=0
  else:
    print("Death awaits you.")

def geico():
  if talklimit[6]==1:
    print("In MUCH less than 15 minutes, you’ll have kicked the bucket you troublemaker.")
    talklimit[0]=0
  else:
    print("The Grim Reaper calls for you")
def nationwide():
  if talklimit[7]==1:
    print("You think can defeat me?!")
    ans= input('You: ')
    print("Oh, that’s adorable. My lawsuits have killed almost the entire Pharma race, and bankrupted the rest of them. I am the most powerful entity on this planet. Who even are you?")
    ans= input('You: ')
    print("It doesn’t matter, you’ll soon be dead. Nationwide is NOT on your side, dirtbag. ")
    talklimit[7]=0
  else:
    print("DIE!")
#################################################
#Definitions
#################################################

def goto(x, y): 
  currentCoords[0] = x
  currentCoords[1] = y

def getRoom(x, y):
  global currentMap
  return maps[currentMap][x][y]

def getCRoom():
  x = currentCoords[0]
  y = currentCoords[1]
  return getRoom(x, y)

def canAccess(x = None, y = None):
  x = x or currentCoords[0]
  y = y or currentCoords[1]
  room = getRoom(x, y)
  return not room['isLocked']

def informEnter():
  print('You entered ' + getCRoom()['RoomName'])

def forward():
  if canAccess(y = currentCoords[1] + 1):
    currentCoords[1] += 1
    informEnter()
  else:
    print('Front door is locked')

def backward():
  if canAccess(y = currentCoords[1] - 1):
    currentCoords[1] -= 1
    informEnter()
  else:
    print('Back door is locked')

def leftward():
  if canAccess(x = currentCoords[0] - 1):
    currentCoords[0] -= 1
    informEnter()
  else:
    print('Left door is locked')

def rightward():
  if canAccess(x = currentCoords[0] + 1):
    currentCoords[0] += 1
    informEnter()
  else:
    print('Right door is locked')

def die():
  global gameOn
  gameOn = False
  print('You died')

def viewInv():
  print('You have:')
  for i in inventory:
    print(i + ' x' + str(inventory[i]))
  print('')

def examine():
  room = getCRoom()
  print(room['desc'])
  print('')

talks = {
  'Guide': guide
         
}

def talk(name): 
  room = getCRoom() 
  name = (name.lower()).capitalize()
  if name in room['People']:
    y= talks[name]
    y() 
  
    
    


def attack(name):
  room = getCRoom()
  name = (name.lower()).capitalize()
  if name in room['People']:
    ppl = room['People']
    person = ppl[name]
    damage = equippedWeapon['damage']
    if randint(1,100) <= equippedWeapon['critChance']:
      damage = randint(100,200)/100.00 * damage
    elif randint(1, 100) <= equippedWeapon['missChance']:
      damage = 0
      print('You missed!')
    person.Health -= damage
    print('You dealt ' + str(damage) + ' damage to ' + person.Name)
    newHealth = person.Health
    if newHealth > 0:   #If died
      print(name + ' has ' + str(newHealth) + ' HP')
    else:
      print(name + ' died!')
      del ppl[name]
      print(ppl)
      hPotions = randint(2,5)
      if hPotions > 0:
        print('You got ' + str(hPotions) + ' Health potions')
        inventory['health potion'] += hPotions
      if randint(0,100) < 10:
        weapon = choice(list(weapons.keys()))
        print('You got ' + weapon)
        if not weapon in inventory:
          inventory[weapon] = 1
        else:
          inventory[weapon] += 1
      global hp 
      hp = hp - person.Attack
      if hp > 0: 
        print("The enemy dealt "+str(person.Attack)+" damage. You have "+str(hp)+" health left.")
      else:
        global gameOn
        gameOn = False
        print("You died.") 

def enter():
  room = getCRoom()
  mapToUse = room['enter']
  if (mapToUse) in maps:
    global currentMap
    currentMap = mapToUse
    goto(10,10)
    print('Went to '  + mapToUse[0:-3].capitalize())

devMode = False

def tp(coords):
  global devMode
  if devMode:
    try:
      x, y = re.findall('\d+' ,coords)
      goto(int(x),int(y))
      print('Teleported to ' + str(x) + ', ' + str(y))
    except ValueError:
      print('Not enough args')

def devGive(arg):
  global devMode
  if devMode:
    try:
      splitArg = arg.split()
      amount = splitArg[-1]
      lenAmount = len(amount)
      amount = int(amount)
      item = arg[0:(len(arg) - (lenAmount + 1))]
    except ValueError:
      amount = 1
      item = arg
    tab = None
    if item in items:
      tab = items
    elif item in weapons:
      tab = weapons
    if tab and amount > 0:
      if item in inventory:
        inventory[item] += amount
      else:
        inventory[item] = amount
      print('Gave ' + item + ' x' + str(amount))


def enableDev():
  global devMode
  devMode = True
  print('Enabled Cheats')

commands = {'forward' : forward, 'backward' : backward, 'left' : leftward, 'right' : rightward, 'die' : die, 'inventory' : viewInv, 'examine' : examine, 'enter' : enter, 'dev' : enableDev, 'tp':tp, 'give' : devGive}

def executeCommand():
  command = input('--> ').lower()
  room = getCRoom()
  funcs = room['AvailabeFunctions']
  command = command.replace('go ', '')
  if command in acceptedCommands:
    command = acceptedCommands[command]
  if command in funcs or command in globalFuncs:
    commands[command]()
  elif 'enter ' in command and 'enter' in funcs:
    enter()
  elif 'use ' in command and len(command) > 4:
    use(command[4::])
  elif 'attack ' in command and len(command) > 7:
    attack(command[7::])
  elif 'talk to ' in command and len(command)> 8:
    talk(command[8::])
  elif 'tp ' in command and len(command) > 3:
    tp(command[3::])
  elif 'give ' in command and len(command) > 5:
    devGive(command[5::])
  elif command == 'right' and type(getRoom(currentCoords[0] + 1, currentCoords[1])) != int:
    if 'left' in getRoom(currentCoords[0] + 1, currentCoords[1])['AvailabeFunctions']:
      rightward()
  elif command == 'left' and type(getRoom(currentCoords[0] - 1, currentCoords[1])) != int:
    if 'right' in getRoom(currentCoords[0] - 1, currentCoords[1])['AvailabeFunctions']:
      leftward()
  elif command == 'backward' and type(getRoom(currentCoords[0], currentCoords[1] - 1)) != int:
    if 'forward' in getRoom(currentCoords[0], currentCoords[1] - 1)['AvailabeFunctions']:
      backward()
  elif command == 'forward' and type(getRoom(currentCoords[0], currentCoords[1] + 1)) != int:
    if 'backward' in getRoom(currentCoords[0], currentCoords[1] + 1)['AvailabeFunctions']:
      forward()
  elif command == 'forward' or command == 'backward' or command == 'left' or command == 'right':
    print("I don't see a way to get there")

gameOn = True

while gameOn:
  executeCommand()