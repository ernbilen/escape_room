'''
Here is a text-based escape-room game designed for ECON 224.

Notes: Make initial house sorting: Ravenclaw, Gryffindor etc.
        Don't forget to put sorting hat's dialogue. Then use this to generate 4 different passwords.
        Use telescope: look through the telescope: you see the quidditch field
        Look inside the telescope: you found a note!
        You can change the demand question (maybe the number instead of p=2-q to p=4-q etc.) to generate different keys.

Author: Eren Bilen
'''

import time

print(f"*"*75)
print("""

  ______ _____ ____  _   _   ___  ___  _  _
 |  ____/ ____/ __ \| \ | | |__ \|__ \| || |
 | |__ | |   | |  | |  \| |    ) |  ) | || |_
 |  __|| |   | |  | | . ` |   / /  / /|__   _|
 | |___| |___| |__| | |\  |  / /_ / /_   | |
 |______\_____\____/|_| \_| |____|____|  |_|

       """)
print("""
▄▄▄ ..▄▄ ·  ▄▄·  ▄▄▄·  ▄▄▄·▄▄▄ .    ▄▄▄              • ▌ ▄ ·.
▀▄.▀·▐█ ▀. ▐█ ▌▪▐█ ▀█ ▐█ ▄█▀▄.▀·    ▀▄ █·▪     ▪     ·██ ▐███▪
▐▀▀▪▄▄▀▀▀█▄██ ▄▄▄█▀▀█  ██▀·▐▀▀▪▄    ▐▀▀▄  ▄█▀▄  ▄█▀▄ ▐█ ▌▐▌▐█·
▐█▄▄▌▐█▄▪▐█▐███▌▐█ ▪▐▌▐█▪·•▐█▄▄▌    ▐█•█▌▐█▌.▐▌▐█▌.▐▌██ ██▌▐█▌
 ▀▀▀  ▀▀▀▀ ·▀▀▀  ▀  ▀ .▀    ▀▀▀     .▀  ▀ ▀█▄▀▪ ▀█▄▀▪▀▀  █▪▀▀▀""")
print("")
print("")
print("Made by Prof. Bilen")
print(f"*"*75)
name=input(f"Enter your name:").title()

response=input(f"Hello, {name}... Have you ever done an escape room before?\n").lower()

if response=="yes" or response=="y":
  print("Great! So you know the gist of it. Find the clues and solve the codes etc etc!\n")
  time.sleep(.3)
elif response=="no" or response=="n":
  print(f"That's fine. Here's the basic idea:")
  time.sleep(.1)
  print(f"You will find clues, decode them, and solve puzzles in order to win the game. If you don't find a way out in time, you lose! (But don't worry, this is a video game, so real-life-you will be fine).\n")
  time.sleep(.6)
else:
  response=input(f"Please enter 'yes' or 'no'.").lower()
  if response=="yes" or response=="y":
    print(f"Great! So you know the gist of it. Find the clues and solve the codes and etc etc!\n")
    time.sleep(.2)
  elif response=="no" or response=="n":
    print(f"That's fine. Here's the basic idea:")
    time.sleep(1)
    print(f"You will find clues, decode them, and solve puzzles in order to win the game. If you don't find a way out in time, you lose! (But don't worry, this is a video game, so real-life-you will be fine).\n")
    time.sleep(.6)

print(f"Here are the basic rules for this game:")
print(f"1. Read the descriptions carefully.\n2. Hit enter to continue the story at each step.\n3. Type in one of the options when prompted to (be careful with typos!)\n")
time.sleep(5)
print(f"Ready? Here we go!")

print(f"-"*30)
time.sleep(.2)
code=8354

%matplotlib inline
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img = plt.imread(r'C:\users\eren\downloads\pixedlart.png')
plt.xticks([])
plt.yticks([])
plt.imshow(img)
plt.show()

input(f"You find yourself in a room resembling an old classroom. On the right, there are desks with stationary materials. In the corner there is a bookshelf covered in cobwebs. On the walls there are photos of a family, a clock, and a telephone.\n")
input(f"You try leaving the classroom, but the door is locked! To open it, you need a 4 digit code.\n")
input(f"You notice one of the desks has a piece of paper with writing on it. You decide to investigate it.\n")
print(f"The paper reads:\n  'I've been waiting for you to visit me.\n   You answer me often but I never ask you a question.\n   What am I?'\n")
time.sleep(.1)
guess=0
location=input(f"Where would you like to go? Your options are: the bookshelf(1), the photos(2), the clock(3), or the telephone(4)\n")
while guess!=code:
  if (location!="1") & (location!="2") & (location!="3") & (location!="4"):
    location=input("Invalid number! Rememeber, your options are: the bookshelf(1), the photos(2), the clock(3), or the telephone(4). Where would you like to go?\n")
    while (location!="1") & (location!="2") & (location!="3") & (location!="4"):
      location=input("Invalid number! Rememeber, your options are: the bookshelf(1), the photos(2), the clock(3), or the telephone(4). Where would you like to go?\n")

  if location=="4":
    print(f"\nThe telephone is an older phone. There is a phone number scratched into the side but the last digit is faded.\nConsidering you are only one digit short, you start trying random numbers.\n")
    time.sleep(1)
    number=int(input(f"Which number will you try for the last digit?\n"))
    while number>0:
      if number==8:
        print(f"\nYou hear a voice on the other side of the line.\n   'Hello. To find the next number in the code, search where the tiny weaver has made his trap.'\n")
        break
      else:
        print(f"The number you have dialed is not in service. Please try again later.\n")
        number=int(input("Which number will you try now?\n"))
  if location=="1":
    print(f"\nYou look at the bookcase covered in spider webs. You pick up a book. The cover has something written on it:\n'((3*5)+10)*3+175'\n")
    page=int(input(f"Which page do you turn to?\n"))
    while page>0:
      if page==250:
        print(f"\nThe number 3 is written in red ink. Underneath there is:\n  '_._. ._.. _ _ _  _._. _._'\n")
        time.sleep(4)
        print(f"You check the back of the book. There is a chart:")
        print(f"A ._  B _...  C _._.  D _..\nE .  F .._.  G __. H ....  I ..\nJ ._ _ _  K _._ L ._..  M __\nN _.  O _ _ _ P .__.  Q __._\nR ._. S ... T _ U .._\nV ..._ W .__ X _.._  Y _.__  Z __..")
        break
      else:
        print(f"The page is blank.\n")
        page=int(input("Which page will you turn to now?\n"))
  if location=="3":
    print(f"\nYou look at the clock on the wall. You realize it is stuck at 5 o clock. Probably a number in the code!\n")
    time.sleep(1)
    print(f"After staring at the clock for a bit, you decide to take it off the wall and turn it over. There is writing on the back!\n")
    input(f"It reads:\n  'Go to the place where time stops.'\n")
  if location=="2":
    print(f"\nYou look at the photos hanging on the wall. You see the same young girl, a young boy, a woman, and a man in all of the photos. They must be a family.")
    print(f"There seems to be no other information on the photos. You decide to look elsewhere.\n")

  response_3=input(f"Do you want to guess the code for the door?\n").lower()
  if response_3=="yes" or response_3=="y":
    guess=int(input(f"\nEnter your guess:\n"))
    if guess==code:
      print(f"\nYou enter your code. The lock flashes green and you hear the door unlock. You made it!\n")
      print(f"Congratulations! You won the game! Thank you for playing!")
        # get student completion confirmation here.
    if guess!=code:
      print(f"The lock flashes red. Looks like you're wrong.\n")
      location=int(input(f"\nWhere would you like to go? Your options are: the bookshelf(1), the photos(2), the clock(3), or the telephone(4)\n"))
  if response_3=="no" or response_3=="n":
    location=int(input(f"\nWhere would you like to go? Your options are: the bookshelf(1), the photos(2), the clock(3), or the telephone(4)\n"))
