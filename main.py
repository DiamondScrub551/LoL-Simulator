# Brycen's League of Legends Text Simulator

# Global Functions

import time
import sys
import json


def clear(): # Function clears screen
  print('\n' * 50)

def printSlow(s): # Function prints text letter by letter
  for c in s:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.03)

# Q&A and Rank-Up Functions

def rankName(x): # Input number and get the name of the rank corresponding with the number.
  ranks = ["New League Player", "Unranked", "Bronze V", "Bronze IV", "Bronze III", "Bronze II", "Bronze I", "Silver V", "Silver IV", "Silver III", "Silver II", "Silver I", "Gold V", "Gold IV", "Gold III", "Gold II", "Gold I", "Platinum V", "Platinum IV", "Platinum III", "Platinum II", "Platinum I", "Diamond V", "Diamond IV", "Diamond III", "Diamond II", "Diamond I", "Master", "Challenger", "LCS Pro", "Worlds Champion", "Literally Faker"]
  return ranks[x]

def rankNumber(x): # Input a rank and get the corresponding number.
  ranks = ["New League Player", "Unranked", "Bronze V", "Bronze IV", "Bronze III", "Bronze II", "Bronze I", "Silver V", "Silver IV", "Silver III", "Silver II", "Silver I", "Gold V", "Gold IV", "Gold III", "Gold II", "Gold I", "Platinum V", "Platinum IV", "Platinum III", "Platinum II", "Platinum I", "Diamond V", "Diamond IV", "Diamond III", "Diamond II", "Diamond I", "Master", "Challenger", "LCS Pro", "Worlds Champion", "Literally Faker"]
  return ranks.index(x)

def checkLP(x): # Checks validity of LP.
  lp = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92", "93", "94", "95", "96", "97", "98", "99", "100"]
  return lp.index(x)
  
def checkPos(x): # Checks validity of position.
  pos = ["Top", "Jungle", "Mid", "ADC", "Support"]
  return pos.index(x)

# Global Variables
"""
global personName
global personUsername
global personRank
global personLP
global personPos
global personAttribute
global personSkill
global personStrength
global step # The step of input (ex: step 1 is entering your name) - used for special input checks
global refuseNum # For the Refusal path- used to track how many times the player has refused to comply
"""
	
# Player Function 

class League(object): # Class for player.

  def __init__(self, username, rank, lp, position, attributes, strength, skill):
    self.username = username
    self.rank = rank
    self.lp = lp
    self.position = position
    self.attributes = attributes
    self.strength = strength
    self.skill = skill
    
# Checks for special inputs

  def prank()
    if step == 1:
      pass
    else:
      if step == 2:
        pass
      else:
        if step == 3:
          pass
        else:
          if step == 4:
            pass
          else:
            if step == 5:
              pass
            else:
              if step == 6:
                pass
              else:
                pass

# Special input functions

def refusal()
  if refuseNum == 1:
    pass
  else:
    if refuseNum == 2:
      pass
    else:
      if refuseNum == 3:
        pass
      else:
        pass


# Ranking Functions

  def rankUp(self): # Function increases user's rank by 1. 
    rankA = rankNumber(self.rank)
    if rankA == 31:
      printSlow(str(self.username) + " cannot rank up any farther! Good game!")
      time.sleep(5)
      quit()
    else:
      rankA += 1
      self.rank = rankName(rankA)
      printSlow(str(self.username) + " has ranked up to " + str(self.rank) + "!")
    
  def rankDown(self): # Function decreases user's rank by 1. 
    rankB = rankNumber(self.rank)
    if rankB == 0:
      printSlow(str(self.username) + " cannot rank down any farther! Game over!")
      time.sleep(5)
      quit()
    else:
      rankB -= 1
      self.rank = rankName(rankB)
      printSlow(str(self.username) + " has ranked down to " + str(self.rank) + "!")

def save():
  global personName
  global personUsername
  global personRank
  global personLP
  global personPos
  global personAttribute
  global personSkill
  global personStrength
  with open("playerdata.txt", "w") as text_file:
    print(f"personName = '{personName}'", file=text_file)
    print(f"personUsername = '{personUsername}'", file=text_file)
    print(f"personRank = '{personRank}'", file=text_file)
    print(f"personLP = '{personLP}'", file=text_file)
    print(f"personPos = '{personPos}'", file=text_file)
    print(f"personAttribute = '{personAttribute}'", file=text_file)
    print(f"personStrength = {personStrength}", file=text_file)
    print(f"personSkill = {personSkill}", file=text_file)

def load():
  global personName
  global personUsername
  global personRank
  global personLP
  global personPos
  global personAttribute
  global personSkill
  global personStrength
  try:
    import playerdata
    try:
      personName = League(personUsername, personRank, personLP, personPos, personAttribute, personStrength, personSkill)
      while True: # Checks for compatible prompt.
        print("Name: " + str(personName) + "\nUsername: " + str(personUsername) + "\nRank: " + str(personRank) + "\nLP: " + str(personLP) + "\nPosition: " + str(personPos) + "\nAttributes: " + str(personAttribute))
        personComplete = input("Is this correct? Y/N: ")
        clear()
        prompt = ["Y", "N"]
        try:
          prompt.index(personComplete)
          break
        except ValueError:
          print("\n", "\nError: Type Y or N.", "\n", "\n")
      if personComplete == 'Y':
        clear()
        printSlow("Data succesfully loaded.")
        time.sleep(3)
      else: 
        qa()
        save()
    except NameError:
      clear()
      printSlow("Save data corrupted. Creating new save...")
      time.sleep(1)
      qa()
      save()
  except ModuleNotFoundError:
    clear()
    printSlow("No data found. Creating new save...")
    time.sleep(1)
    qa()
    save()
    

      
# Q&A Function

def qa():
  global personName
  global personUsername
  global personRank
  global personLP
  global personPos
  global personAttribute
  global personSkill
  global personStrength
  while True:
	  clear()
	  personName = input("Enter your name: ")
	  clear()
	  personUsername = input("Enter your League of Legends username: ")
	  clear()
	  
	  while True: # Checks for compatible rank.
	    personRank = input("Enter your League of Legends rank: ")
	    clear()
	    try:
	      rankNumber(personRank)
	      break
	    except ValueError:
	      print("New League Player", "\nUnranked", "\nBronze V", "\nBronze IV", "\nBronze III", "\nBronze II", "\nBronze I", "\nSilver V", "\nSilver IV", "\nSilver III", "\nSilver II", "\nSilver I", "\nGold V", "\nGold IV", "\nGold III", "\nGold II", "\nGold I", "\nPlatinum V", "\nPlatinum IV", "\nPlatinum III", "\nPlatinum II", "\nPlatinum I", "\nDiamond V", "\nDiamond IV", "\nDiamond III", "\nDiamond II", "\nDiamond I", "\nMaster", "\nChallenger", "\nLCS Pro", "\nWorlds Champion", "\nLiterally Faker", "\n", "\nError: Please choose a rank from the above list.", "\n", "\n")
	      
	  while True: # Checks for compatible LP.
	    personLP = input("Enter your League of Legends ranked LP: ")
	    clear()
	    try:
	      checkLP(personLP)
	      break
	    except ValueError:
	      print("\n", "\nError: Please choose a value from 0-100.", "\n", "\n")
	  clear()
	  
	  while True: # Checks for compatible position. 
	    personPos = input("Enter your League of Legends position: ")
	    clear()
	    try: 
	      checkPos(personPos)
	      break
	    except ValueError:
	      print("Top", "\nJungle", "\nMid", "\nADC", "\nSupport", "\n", "\nError: Please choose a position listed above.", "\n", "\n")
	      
	  clear()
	  personAttribute = input("Enter something about yourself: ")
	  clear()
	  
	  while True: # Checks for compatible prompt.
	    print(f"Name: {personName} \nUsername: {personUsername} \nRank: {personRank} \nLP: {personLP} \nPosition: {personPos} \nAttributes: {personAttribute}")
	    personComplete = input("Is this correct? Y/N: ")
	    clear()
	    prompt = ["Y", "N"]
	    try:
	      prompt.index(personComplete)
	      break
	    except ValueError:
	      print("\n", "\nError: Type Y or N.", "\n", "\n")
	      
	  try: # Lets you continue or repeat the Q&A depending on answer.
	    yes = ["Y"]
	    yes.index(personComplete)
	    break
	  except ValueError:
	    clear()
	    printSlow("Redirecting you to the start of the program.")
	    time.sleep(2)
  
  personStrength = 50
  personSkill = rankNumber(personRank) * 5
  save()
  

	# Save function (writing)
      
# Start-up Sequence

clear()
time.sleep(1)
printSlow("Welcome to Brycen's League of Legends text simulator! v0.0.1")
time.sleep(3)
load()
# Player Creator Q&A


	

# Post Q&A Sequence




# Save Function (loading)






print("Thanks for your time!")