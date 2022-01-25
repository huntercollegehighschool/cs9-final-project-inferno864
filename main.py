"""
Name(s): Colby O'Connor
Name of Project: Choose Your Own Adventure
"""

#Write the main part of your program here. Use of the other pages is optional.
def start(): 
  waitcount = 0
  print('You wake up in a bed that\'s not your own.\nYou look around and see you are in a room with a locked door. You \nget up and look out a window, seeing only snowy forest outside. You\nnotice you are on the second floor of a house.')
  choice = int(input('Enter "1" to try to unlock the door\nEnter "2" to go out the window\nEnter "3" to wait in the room\n'))
  if choice == 1:
    unlock()
  elif choice == 2:
    window()
  elif choice == 3: 
    wait(waitcount)
def unlock():
  waitcount = 0
  print("You walk over to the door and squat down to examine the lock. It \nappears to need a key to open.")
  unlockchoice = int(input('Enter "1" to search for a key \nEnter "2" to try to pull the lock off \nEnter "3" to wait in the room\n'))
  if unlockchoice == 1:
    key()
  elif unlockchoice == 2:
    lockpull()
  elif unlockchoice == 3:
    wait(waitcount)
def window():
  print("You push open the window with a grunt and lean outside. The first \nthing you notice is the freezing cold and the wind blowing snow \nonto your face. You look around and all you see is snow and trees, \nother than the house you're locked in. ")
  windowchoice = int(input('Enter "1" to jump out the window \nEnter "2" to find a coat and then jump out \nEnter "3" to attempt to climb to the roof\n'))
  if windowchoice == 1:
    jump() 
  elif windowchoice == 2:
    coatjump() 
  elif windowchoice == 3:
    roofclimb()
def wait(waitcount):
  while waitcount < 2:
    waitcount +=1
    print("You wait for around an hour, and no one comes. ")
    waitchoice = int(input('Enter "1" to try to unlock the door\nEnter "2" to go out the window\nEnter "3" to wait in the room\n'))
    if waitchoice == 1:
      unlock() 
    elif waitchoice == 2:
      window() 
    elif waitchoice == 3:
      waitcount += 1
      wait(waitcount) 
  while waitcount >= 2:
    print("After waiting for hours, you hear the jingle of keys from outside the door. The door opens and a hooded figure comes in. They look at you and silently draw a sword. The figure starts to move towards \nyou.")
    figurechoice = int(input('Enter "1" to try to speak to the figure\nEnter "2" to try to run through the door\nEnter "3" to go through the window\nEnter "4" to fight the figure\n'))
    waitcount = 1
    if figurechoice == 1:
      figuredeath1()
    elif figurechoice == 2:
      figureescape()
    elif figurechoice == 3:
      window()
    elif figurechoice == 4:
      figuredeath2()
def key():
  print("You search the room and find a key under the bed. You walk over to\nthe lock and stick it in. It turns and the door unlocks. You go\ndownstairs and see a small kitchen. No one is here, but you can see\nsomebody was recently.")
  house = int(input("Enter \"1\" to wait in the kitchen\nEnter \"2\" to leave through the front door\n"))
  if house == 1:
    kitchenwait()
  elif house == 2:
    door()
def lockpull():
  print("You grab onto the lock with both hands. You attempt to pull the lock off but fail.")
  pullchoice = int(input('Enter "1" to continue pulling\nEnter "2" to search for a key\n'))
  if pullchoice == 1:
    pulltime = int(input("How many more attempts would you like to make?\nEnter the amount:"))
    if pulltime > 3:
      print("You continue pulling at the lock to no effect. After the 4th\nattempt, you hear the lock click on the other side, and the door \nflies open. You are pushed to the floor and stare up helplessly as\na hooded figure draws a sword.\n\bThe End\b")
      exit()
    elif pulltime <= 3:
      print("The lock does not come off, so you get up and sit on the bed to \nconsider your next move. While doing this, the lock clicks open and \na hooded figure walks into the room. The figure silently draws a \nsword.")
      figurechoice = int(input('Enter "1" to try to speak to the figure\nEnter "2" to try to run through the door\nEnter "3" to try to escape through the window\nEnter "4" to fight the figure\n'))
      if figurechoice == 1:
        figuredeath1()
      elif figurechoice == 2:
        figurescape()
      elif figurechoice == 3:
        window()
      elif figurechoice == 4:
        figuredeath2()
  elif pullchoice == 2:
    key()
def jump():
  print("You jump out of the window and land safely on the soft snow. You \nwalk into the forest and as the sun starts to set the frigid cold \nsets in. You are too far to find your way back to the house. \nThe End") 
  exit()
def coatjump():
  print("You grab a coat off a chair before jumping out of the window. You \nland safely on the soft snow. You walk into the forest, and around\nwhen the sun is setting you arrive at a river. ")
  riverchoice = int(input('Enter "1" to follow the river\nEnter "2" to go the other direction\n'))
  if riverchoice == 1:
    outsidedeath()
  elif riverchoice == 2:
    rightway()
def roofclimb():
  print("You put on a coat and climb out of the window, jumping up to reach the roof. You look around and see a large snowy forest, with a \nriver on one side and a town on the other. ")
  roofchoice = int(input('Enter "1" to jump down and start walking into the forest\nEnter "2" to go back into the house\n'))
  if roofchoice == 1:
    roofjump()
  elif roofchoice == 2:
    roofhouse()
def figuredeath1():
  print("You try to talk to the figure, but they ignore you and just slowly walk slower. By the time you realize they aren't going to respond, the sword is raised.\nThe End")
  exit()
def figuredeath2():
  print('You decide to fight and charge at the figure, trying to punch them.\nThis was a mistake.\nThe End')
  exit()
def figureescape():
  print("You try to run past the figure, but with almost inhuman speed their\nhand reaches out and catches you. You should've went the other way.\nThe End")
  exit()
def kitchenwait():
  print("You sit down at the kitchen table and wait for whoever lives here\nto come home. Later, you hear the door open and a hooded figure\ncomes in. They jump a bit when they see you, excepting you to be\nupstairs. A sword is drawn and you think you should have escaped\nwhile you still could.\nThe End")
  exit()
def door():
  print("The front door is unlocked, and you walk out of it and into a\nforest. You walk into the forest, and around when the sun is\nsetting you arrive at a river.")
  riverchoice = int(input('Enter "1" to follow the river\nEnter "2" to go the other direction\n'))
  if riverchoice == 1:
    outsidedeath()
  elif riverchoice == 2:
    rightway()
def outsidedeath():
  print("You wander around aimlessly in the woods as it gets darker and\ndarker and colder and colder. Eventually you colapse from\nexhaustion and drift off. \nThe End")
  exit()
def rightway():
  print('You walk away from the river and after around an hour you see a\nsmall town. You walk to it and the townspeople welcome you with\nopen arms. Apparently you aren\'t the first person to escape from\nthe"grim reaper"\nThe End!')
  exit()
def roofhouse():
  print("You climb back into the room.")
  choice = int(input('Enter "1" to try to unlock the door\nEnter "2" to go out the window\nEnter "3" to wait in the room\n'))
  if choice == 1:
    unlock()
  elif choice == 2:
    window()
  elif choice == 3: 
    wait(waitcount)
start()

