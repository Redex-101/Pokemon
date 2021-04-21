import random, time ,math

def numCheck(n):
  temp = n
  while not(temp.isdigit()):
    temp = input("That is not an option; try again: ")
  temp = int(temp)
  return temp


def alphaCheck(a):
  temp2 = a
  while not(temp2.isalpha()):
    temp2 = input("That's not a word; try again: ")
  return temp2

Charizard = [275,110,252]
#hp0 = 275
#atk0 = 110
#spd0 = 252
Squirtle = [252,110,253]
#hp1 = 252
#atk1 = 110
#spd1 = 253
Pikachu = [300,80,265]
#hp2 = 300
#atk2 = 80
#spd2 = 255
Geodude = [225,150,4]
#hp3 = 225
#atk3 = 150
#spd3 = 4
Nathaneellion = [230,130,254]
Rattata = [10,500,2]
#hp4 = 10
#atk4 = 500
#spd4 = 2 

pokemon = [Charizard,Squirtle,Pikachu,Geodude,Nathaneellion,Rattata]
pokemonName = ["Charizard","Squirtle","Pikachu","Geodude","Nathaneellion","Rattata"]
f = open("stats.txt","r")
foo = f.read()
f.close()
print(foo)
print("------------------------------")
print("Charzard = 0")
print("Squirtle = 1")
print("Picachu = 2")
print("Geodude = 3")
print("Nathaneellion = 4")
print("Rattata = 5")
print("------------------------------")
print("Select any pokemon")
select = input("Select 0, 1, 2, 3, 4, or 5 : ")
select = numCheck(select)

while not ((select == 0) or (select == 1) or (select == 2) or (select == 3) or (select == 4)or(select == 5)):
  select = input("Select 0, 1, 2, 3, 4, or 5 ")
  select = numCheck(select)
print("------------------------------")
if (select == 0):
  CharM = ["Fire Blast","Roost","Defense Curl"]
  your = pokemon[0]
  yourPN = pokemonName[0]
if (select == 1):
  SquiM = ["Blizzard","Rest","Iron Defense"]
  your = pokemon[1]
  yourPN = pokemonName[1]
if (select == 2):
  PikaM = ["Extreme Speed","Rest","Calm Mind"]
  your = pokemon[2]
  yourPN = pokemonName[2]
if (select == 3):
  GeoM = ["Earthquake","Rest","Defence Curl"]
  your = pokemon[3]
  yourPN = pokemonName[3]
if (select == 4):
  NathM = ["Wip","Sleep","Porta-Fortress"]
  your = pokemon[4]
  yourPN = pokemonName[4]
if (select == 5):
  RattM = ["Cho?!?","Rest","Defense Curl"]
  your = pokemon[5]
  yourPN = pokemonName[5]

print("You are now using",yourPN)
time.sleep(2)
foePokemon = [Charizard,Squirtle,Pikachu,Geodude,Nathaneellion,Rattata]
foePokemonName = ["Charizard","Squirtle","Pikachu","Geodude","Nathaneellion","Rattata"]

aiselect = random.randint(0,4)
if (aiselect == 0):
  CharM = ["Fire Blast","Roost","Defense Curl"]
  foe = foePokemon[0]
  foePN = foePokemonName[0]
if (aiselect == 1):
  SquiM = ["Blizzard","Rest","Iron Defense"]
  foe = foePokemon[1]
  foePN = foePokemonName[1]
if (aiselect == 2):
  PikaM = ["Extreme Speed","Rest","Calm Mind"]
  foe = foePokemon[2]
  foePN = foePokemonName[2]
if (aiselect == 3):
  GeoM = ["Earthquake","Rest","Defence Curl"]
  foe = foePokemon[3]
  foePN = foePokemonName[3]
if (aiselect == 4):
  NathM = ["Wip","Sleep","Porta-Fortress"]
  foe = foePokemon[4]
  foePN = foePokemonName[4]

opponent = ["Kevin","Olivia","Jeff","Ava","Nathaniel","Rafael","Charlotte","Chloe","Jeff"]
opponent = random.choice(opponent)
print(opponent , "wants to battle you! They are using", foePN ,"!")

flee = input("Would you like to fight? (Yes/No) ").lower()
if (flee.startswith("y")):
  print("Get ready to fight! (press enter when ready)")
  print("------------------------------")
else:
  print("You coward!")
  exit()
yo=input("")
#user
hp1 = your[0]
atk1 = your[1]
spd1 = your[2]

#computer
hp2 = foe[0]
atk2 = foe[1]
spd2 = foe[2]


while (hp1 > 0) and (hp2 > 0):
  while (spd1 > spd2):
    action = input("What move would you like to use, 1 = attack, 2 = heal (1/2) ")
    action = numCheck(action)
    print("------------------------------")
    if (action == 1):
      if (select == 0):
        print("You selected the attack" ,CharM[0] ,"which deals", atk1 ,"damage!")
        hp2 = hp2 - atk1
        time.sleep(2)
        if (hp2 < 0):
          hp2 = 0
          print( opponent +"'s" , foePN , "has" , hp2 , "health left!")
          print("------------------------------")
        else:
          print( opponent +"'s" , foePN , "has" , hp2 , "health left!")
          print("------------------------------")
      if (select == 1):
        print("You selected the attack" , SquiM[0] , "which deals" , atk1 , "damage!")
        hp2 = hp2 - atk1
        print("------------------------------")
        time.sleep(2)
        if (hp2 < 0):
          hp2 = 0
          print( opponent +"'s" , foePN , "has" , hp2 , "health left!")
          print("------------------------------")
        else:
          print( opponent +"'s" , foePN , "has" , hp2 , "health left!")
          print("------------------------------")
      if (select == 2):
        print("You selected the attack" ,PikaM[0] ,"which deals", atk1 ,"damage!")
        hp2 = hp2 - atk1
        print("------------------------------")
        time.sleep(2)
        if (hp2 < 0):
          hp2 = 0
          print( opponent +"'s" , foePN , "has" , hp2 , "health left!")
          print("------------------------------")
        else:
          print( opponent +"'s" , foePN , "has" , hp2 , "health left!")
          print("------------------------------")
      if (select == 3):
        print("You selected the attack" , GeoM[0] , "which deals" , atk1 , "damage!")
        hp2 = hp2 - atk1
        print("------------------------------")
        time.sleep(2)
        if (hp2 < 0):
          hp2 = 0
          print( opponent +"'s" , foePN , "has" , hp2 , "health left!")
          print("------------------------------")
        else:
          print( opponent +"'s" , foePN , "has" , hp2 , "health left!")
          print("------------------------------")
      if (select == 4):
        print("You selected the attack" , NathM[0] , "which deals" , atk1 , "damage!")
        hp2 = hp2 - atk1
        print("------------------------------")
        time.sleep(2)
        if (hp2 < 0):
          hp2 = 0
          print( opponent +"'s" , foePN , "has" , hp2 , "health left!")
          print("------------------------------")
        else:
          print( opponent +"'s" , foePN , "has" , hp2 , "health left!")
          print("------------------------------")
      if (select == 5):
        print("You selected the attack" , RattM[0] , "which deals" , atk1 , "damage!")
        hp2 = hp2 - atk1
        print("------------------------------")
        time.sleep(2)
        if (hp2 < 0):
          hp2 = 0
          print( opponent +"'s" , foePN , "has" , hp2 , "health left!")
          print("------------------------------")
        else:
          print( opponent +"'s" , foePN , "has" , hp2 , "health left!")
          print("------------------------------")
      if (hp1 <= 0):
        print(opponent , "has won the game!")
        exit()
      elif (hp2 <= 0):
        print("You won!")
        exit()
      if (action == 2):
        if (select == 0):
          hp1 = hp1 + 100
          if (hp1 > 275):
            hp1 = 275
            print("Your" , yourPN , "has healed up to" , hp1 , "health!") 
            print("------------------------------")
          else:
            print("Your" , yourPN , "has healed up to" , hp1 , "health!")
            print("------------------------------")
          if (select == 1):
            hp1 = hp1 + 100
            if (hp1 > 252):
              hp1 = 252
              print("Your" , yourPN , "has healed up to" , hp1 , "health!") 
              print("------------------------------")
            else:
              print("Your" , yourPN , "has healed up to" , hp1 , "health!") 
              print("------------------------------")
          if (select == 2):
            hp1 = hp1 + 100
            if (hp1 > 300):
              hp1 = 300
              print("Your" , yourPN , "has healed up to" , hp1 , "health!") 
              print("------------------------------")
            else:
              print("Your" , yourPN , "has healed up to" , hp1 , "health!")
              print("------------------------------")
          if (select == 3):
            hp1 = hp1 + 100
            if (hp1 > 225):
              hp1 = 225
              print("Your" , yourPN , "has healed up to" , hp1 , "health!") 
              print("------------------------------")
            else:
              print("Your" , yourPN , "has healed up to" , hp1 , "health!")
              print("------------------------------")
          if (select == 4):
            hp1 = hp1 + 100
            if (hp1 > 230):
              hp1 = 230
              print("Your" , yourPN , "has healed up to" , hp1 , "health!") 
              print("------------------------------")
            else:
              print("Your" , yourPN , "has healed up to" , hp1 , "health!")
              print("------------------------------")
          if (select == 5):
            hp1 = hp1 + 100
            if (hp1 > 10):
              hp1 = 10
              print("Your" , yourPN , "has healed up to" , hp1 , "health!") 
              print("------------------------------")
            else:
              print("Your" , yourPN , "has healed up to" , hp1 , "health!") 
              print("------------------------------")
          if (hp1 <= 0):
            print(opponent , "has won the game!")
            exit()
          elif (hp2 <= 0):
            print("You won!")
            exit()
      if (hp2 >= 100) and (aiselect == 0):
        print(opponent , "used" , CharM[0] , "which deals" , atk2 , "damage!")
        hp1 = hp1 - atk2
        print("------------------------------")
        time.sleep(2)
        if (hp1 < 0):
          hp1 = 0
          print("Your" , yourPN , "has" , hp1 , "health left!")
          print("------------------------------")
        else:
          print("Your" , yourPN , "has" , hp1 , "health left!")
          print("------------------------------")
      if (hp2 >= 100) and (aiselect == 1):
        print(opponent , "used" , SquiM[0] , "which deals" , atk2 , "damage!")
        hp1 = hp1 - atk2
        print("------------------------------")
        time.sleep(2)
        if (hp1 < 0):
          hp1 = 0
          print("Your" , yourPN , "has" , hp1 , "health left!")
          print("------------------------------")
        else:
          print("Your" , yourPN , "has" , hp1 , "health left!")
          print("------------------------------")
      if (hp2 >= 100) and (aiselect == 2):
        print(opponent , "used" , PikaM[0] , "which deals" , atk2 , "damage!")
        hp1 = hp1 - atk2
        print("------------------------------")
        time.sleep(2)
        if (hp1 < 0):
          hp1 = 0
          print("Your" , yourPN , "has" , hp1 , "health left!")
          print("------------------------------")
        else:
          print("Your" , yourPN , "has" , hp1 , "health left!")
      if (hp2 >= 100) and (aiselect == 3):
        print(opponent , "used" , GeoM[0] , "which deals" , atk2 , "damage!")
        hp1 = hp1 - atk2
        print("------------------------------")
        time.sleep(2)
        if (hp1 < 0):
          hp1 = 0
          print("Your" , yourPN , "has" , hp1 , "health left!")
          print("------------------------------")
        else:
          print("Your" , yourPN , "has" , hp1 , "health left!")
          print("------------------------------")
      if (hp2 >= 100) and (aiselect == 4):
        print(opponent , "used" , NathM[0] , "which deals" , atk2 , "damage!")
        hp1 = hp1 - atk2
        print("------------------------------")
        time.sleep(2)
        if (hp1 < 0):
          hp1 = 0
          print("Your" , yourPN , "has" , hp1 , "health left!")
          print("------------------------------")
        else:
          print("Your" , yourPN , "has" , hp1 , "health left!")
          print("------------------------------")
      if (hp1 <= 0):
        print(opponent , "has won the game!")
        exit()
      elif (hp2 <=0):
        print("You won!")
        exit()
      if (hp2 < 100) and (aiselect == 0):
        hp2 = hp2 + 100
        if (hp2 > 275):
          hp2 = 275
          print(opponent + "'s" , foePN , "has healed up to" , hp2 , "health!") 
          print("------------------------------")
        else:
          print(opponent + "'s" , foePN , "has healed up to" , hp2 , "health!") 
          print("------------------------------")
      if (hp2 < 100) and (aiselect == 1):
        hp2 = hp2 + 100
        if (hp2 > 252):
          hp2 = 252
          print(opponent + "'s" , foePN , "has healed up to" , hp2 , "health!") 
          print("------------------------------")
        else:
          print(opponent + "'s" , foePN , "has healed up to" , hp2 , "health!") 
          print("------------------------------")
      if (hp2 < 100) and (aiselect == 2):
        hp2 = hp2 + 100
        if (hp2 > 300):
          hp2 = 300
          print(opponent + "'s" , foePN , "has healed up to" , hp2 , "health!") 
          print("------------------------------")
        else:
          print(opponent + "'s" , foePN , "has healed up to" , hp2 , "health!") 
          print("------------------------------")
      if (hp2 < 100) and (aiselect == 3):
        hp2 = hp2 + 100
        if (hp2 > 225):
          hp2 = 225
          print(opponent + "'s" , foePN , "has healed up to" , hp2 , "health!") 
          print("------------------------------")
        else:
          print(opponent + "'s" , foePN , "has healed up to" , hp2 , "health!") 
          print("------------------------------")
      if (hp2 < 100) and (aiselect == 4):
        hp2 = hp2 + 100
        if (hp2 > 230):
          hp2 = 230
          print(opponent + "'s" , foePN , "has healed up to" , hp2 , "health!") 
          print("------------------------------")
        else:
          print(opponent + "'s" , foePN , "has healed up to" , hp2 , "health!") 
          print("------------------------------")
      if (hp1 <= 0):
        print(opponent , "has won the game!")
        exit()
      elif (hp2 <=0):
        print("You won!")
        exit()
    else:
      action = input("What move would you like to use, 1 = attack, 2 = heal (1/2) ")
      action = numCheck(action)
      print("------------------------------")
  else:
    if (hp2 > 100) and (aiselect == 0):
      print(opponent , "used" , CharM[0] , "which deals" , atk2 , "damage!")
      hp1 = hp1 - atk2
      print("------------------------------")
      time.sleep(2)
      if (hp1 < 0):
        hp1 = 0
        print("Your" , yourPN , "has" , hp1 , "health left!")
        print("------------------------------")
      else:
        print("Your" , yourPN , "has" , hp1 , "health left!")
        print("------------------------------")
      if (select == 5):
        print("Rattata used self res, Rattata has 1 Hp left!")
        hp1 = 1
    if (hp2 > 100) and (aiselect == 1):
      print(opponent , "used" , SquiM[0] , "which deals" , atk2 , "damage!")
      hp1 = hp1 - atk2
      print("------------------------------")
      time.sleep(2)
      if (hp1 < 0):
        hp1 = 0
        print("Your" , yourPN , "has" , hp1 , "health left!")
        print("------------------------------")
      else:
        print("Your" , yourPN , "has" , hp1 , "health left!")
        print("------------------------------")
      if (select == 5):
        print("Rattata used self res, Rattata has 1 Hp left!")
        hp1 = 1
    if (hp2 > 100) and (aiselect == 2):
      print(opponent , "used" , PikaM[0] , "which deals" , atk2 , "damage!")
      hp1 = hp1 - atk2
      print("------------------------------")
      time.sleep(2)
      if (hp1 < 0):
        hp1 = 0
        print("Your" , yourPN , "has" , hp1 , "health left!")
        print("------------------------------")
      else:
        print("Your" , yourPN , "has" , hp1 , "health left!")
        print("------------------------------")
      if (select == 5):
        print("Rattata used self res, Rattata has 1 Hp left!")
        hp1 = 1
    if (hp2 > 100) and(aiselect == 3):
      print(opponent , "used" , GeoM[0] , "which deals" , atk2 , "damage!")
      hp1 = hp1 - atk2
      print("------------------------------")
      time.sleep(2)
      if (hp1 < 0):
        hp1 = 0
        print("Your" , yourPN , "has" , hp1 , "health left!")
        print("------------------------------")
      else:
        print("Your" , yourPN , "has" , hp1 , "health left!")
        print("------------------------------")
      if (select == 5):
        print("Rattata used self res, Rattata has 1 Hp left!")
        hp1 = 1
    if (hp2 > 100) and(aiselect == 4):
      print(opponent , "used" , NathM[0] , "which deals" , atk2 , "damage!")
      hp1 = hp1 - atk2
      time.sleep(2)
      if (hp1 < 0):
        hp1 = 0
        print("Your" , yourPN , "has" , hp1 , "health left!")
        print("------------------------------")
      else:
        print("Your" , yourPN , "has" , hp1 , "health left!")
        print("------------------------------")
      if (select == 5):
        print("Rattata used self res, Rattata has 1 Hp left!")
        hp1 = 1
    if (hp1 <= 0):
      print(opponent , "has won the game!")
      exit()
    elif (hp2 <=0):
      print("You won!")
      exit()
    if (hp2 < 100) and (aiselect == 0):
      hp2 = hp2 + 100
      if (hp2 > 275):
        hp2 = 275
        print(opponent + "'s" , foePN , "has healed up to" , hp2 , "health!") 
        print("------------------------------")
      else:
        print(opponent + "'s" , foePN , "has healed up to" , hp2 , "health!") 
        print("------------------------------")
    if (hp2 < 100) and (aiselect == 1):
      hp2 = hp2 + 100
      if (hp2 > 252):
        hp2 = 252
        print(opponent + "'s" , foePN , "has healed up to" , hp2 , "health!") 
        print("------------------------------")
      else:
        print(opponent + "'s" , foePN , "has healed up to" , hp2 , "health!") 
        print("------------------------------")
    if (hp2 < 100) and (aiselect == 2):
      hp2 = hp2 + 100
      if (hp2 > 300):
        hp2 = 300
        print(opponent + "'s" , foePN , "has healed up to" , hp2 , "health!") 
        print("------------------------------")
      else:
        print(opponent + "'s" , foePN , "has healed up to" , hp2 , "health!") 
        print("------------------------------")
    if (hp2 < 100) and (aiselect == 3):
      hp2 = hp2 + 100
      if (hp2 > 225):
        hp2 = 225
        print(opponent + "'s" , foePN , "has healed up to" , hp2 , "health!") 
        print("------------------------------")
      else:
        print(opponent + "'s" , foePN , "has healed up to" , hp2 , "health!") 
        print("------------------------------")
    if (hp2 < 100) and (aiselect == 4):
      hp2 = hp2 + 100
      if (hp2 > 230):
        hp2 = 230
        print(opponent + "'s" , foePN , "has healed up to" , hp2 , "health!") 
        print("------------------------------")
      else:
        print(opponent + "'s" , foePN , "has healed up to" , hp2 , "health!") 
        print("------------------------------")
    if (hp1 <= 0):
      print(opponent , "has won the game!")
      exit()
    elif (hp2 <=0):
      print("You won!")
      exit()
    action = input("What move would you like to use, 1 = attack, 2 = heal (1/2) ")
    action = numCheck(action)
    print("------------------------------")
    if (action == 1):
      if (select == 0):
        print("You selected the attack" ,CharM[0] ,"which deals", atk1 ,"damage!")
        hp2 = hp2 - atk1
        time.sleep(2)
        if (hp2 < 0):
          hp2 = 0
          print( opponent +"'s" , foePN , "has" , hp2 , "health left!")
          print("------------------------------")
        else:
          print( opponent +"'s" , foePN , "has" , hp2 , "health left!")
          print("------------------------------")
      if (select == 1):
        print("You selected the attack" , SquiM[0] , "which deals" , atk1 , "damage!")
        hp2 = hp2 - atk1
        time.sleep(2)
        if (hp2 < 0):
          hp2 = 0
          print( opponent +"'s" , foePN , "has" , hp2 , "health left!")
          print("------------------------------")
        else:
          print( opponent +"'s" , foePN , "has" , hp2 , "health left!")
          print("------------------------------")
      if (select == 2):
        print("You selected the attack" ,PikaM[0] ,"which deals", atk1 ,"damage!")
        hp2 = hp2 - atk1
        time.sleep(2)
        if (hp2 < 0):
          hp2 = 0
          print( opponent +"'s" , foePN , "has" , hp2 , "health left!")
          print("------------------------------")
        else:
          print( opponent +"'s" , foePN , "has" , hp2 , "health left!")
          print("------------------------------")
      if (select == 3):
        print("You selected the attack" , GeoM[0] , "which deals" , atk1 , "damage!")
        hp2 = hp2 - atk1
        time.sleep(2)
        if (hp2 < 0):
          hp2 = 0
          print( opponent +"'s" , foePN , "has" , hp2 , "health left!")
          print("------------------------------")
        else:
          print( opponent +"'s" , foePN , "has" , hp2 , "health left!")
          print("------------------------------")
      if (select == 4):
        print("You selected the attack" , NathM[0] , "which deals" , atk1 , "damage!")
        hp2 = hp2 - atk1
        time.sleep(2)
        if (hp2 < 0):
          hp2 = 0
          print( opponent +"'s" , foePN , "has" , hp2 , "health left!")
          print("------------------------------")
        else:
          print( opponent +"'s" , foePN , "has" , hp2 , "health left!")
          print("------------------------------")
      if (select == 5):
        print("You selected the attack" , RattM[0] , "which deals" , atk1 , "damage!")
        hp2 = hp2 - atk1
        time.sleep(2)
        if (hp2 < 0):
          hp2 = 0
          print( opponent +"'s" , foePN , "has" , hp2 , "health left!")
          print("------------------------------")
        else:
          print( opponent +"'s" , foePN , "has" , hp2 , "health left!")
          print("------------------------------")
      if (hp1 <= 0):
        print(opponent , "has won the game!")
        exit()
      elif (hp2 <= 0):
        print("You won!")
        exit()
    if (action == 2):
      if (select == 0):
        hp1 = hp1 + 100
        if (hp1 > 275):
          hp1 = 275
          print("Your" , yourPN , "has healed up to" , hp1 , "health!") 
          print("------------------------------")
        else:
          print("Your" , yourPN , "has healed up to" , hp1 , "health!")
          print("------------------------------")
      if (select == 1):
        hp1 = hp1 + 100
        if (hp1 > 252):
          hp1 = 252
          print("Your" , yourPN , "has healed up to" , hp1 , "health!") 
          print("------------------------------")
        else:
          print("Your" , yourPN , "has healed up to" , hp1 , "health!") 
          print("------------------------------")
      if (select == 2):
        hp1 = hp1 + 100
        if (hp1 > 300):
          hp1 = 300
          print("Your" , yourPN , "has healed up to" , hp1 , "health!") 
          print("------------------------------")
        else:
          print("Your" , yourPN , "has healed up to" , hp1 , "health!")
          print("------------------------------")
      if (select == 3):
        hp1 = hp1 + 100
        if (hp1 > 225):
          hp1 = 225
          print("Your" , yourPN , "has healed up to" , hp1 , "health!") 
          print("------------------------------")
        else:
          print("Your" , yourPN , "has healed up to" , hp1 , "health!")
          print("------------------------------")
      if (select == 4):
        hp1 = hp1 + 100
        if (hp1 > 230):
          hp1 = 230
          print("Your" , yourPN , "has healed up to" , hp1 , "health!") 
          print("------------------------------")
        else:
          print("Your" , yourPN , "has healed up to" , hp1 , "health!")
          print("------------------------------")
      if (select == 5):
        hp1 = hp1 + 100
        if (hp1 > 10):
          hp1 = 10
          print("Your" , yourPN , "has healed up to" , hp1 , "health!") 
          print("------------------------------")
        else:
          print("Your" , yourPN , "has healed up to" , hp1 , "health!") 
          print("------------------------------")
      if (hp1 <= 0):
        print(opponent , "has won the game!")
        exit()
      elif (hp2 <= 0):
        print("You won!")
        exit()
if (hp1 <= 0):
  print(opponent , "has won the game!")
  exit()
elif (hp2 <= 0):
  print("You won!")
  exit()
