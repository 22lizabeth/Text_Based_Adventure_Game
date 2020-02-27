from locations import *
from bag import *
from effects import *

class AdventureGame:
  
  def __init__(self):
    self.resetAll()
  
  def resetAll(self):
    self.bag = Bag()
    self.effects = Effects()
    self.location = Location(self.bag, self.effects)
    self.userInput = ""
    
  #GAME PLAY FUNCTIONS
  def playGame(self):
    
    print("\nWelcome to your greatest adventure!")
    print("\nType 'keywords' to view the keywords needed to move throughout the adventure.")
    print("\nSafe travels, brave hero!\n")
    print("-----------------------------------")
    self.location.townCenter()
    
    while(True):
      
      if self.location.dead:
        break
      
      print("\n")
      
      self.userInput = input("")
      self.userInput = self.userInput.lower()
      
      if "exit" in self.userInput:
        response = input("\nAre you sure you want to exit the game? This will restart your entire adventure.")
        if "no" in response:
          self.location.resetCurrLocation()
        else:
          break
      elif "give up" in self.userInput:
        self.location.death()
      elif "keywords" in self.userInput:
        self.showKeywords()
      elif "bag" in self.userInput:
        self.openBag()
      elif "go" in self.userInput or "enter" in self.userInput or "leave" in self.userInput:
        self.userInput = self.location.changeLocation(self.userInput)
      elif "map" in self.userInput:
        self.location.printMap()
      elif "use" in self.userInput or "put out" in self.userInput:
        self.useItem()
      elif "investigate" in self.userInput:
        self.location.investigate()
      elif "read" in self.userInput or "look at" in self.userInput or "view" in self.userInput:
        self.viewSomething()
      elif "talk" in self.userInput or "ask" in self.userInput:
        self.location.talkTo(self.userInput)
      elif "buy" in self.userInput or "sell" in self.userInput:
        if self.location.insidePlace == "shop":
          print("\nTalk to the shop owner if you want to buy or sell something!")
        else:
          print("\nThere is nothing to buy and nowhere to sell here!")
      elif ("worship" in self.userInput or "incense" in self.userInput) and self.location.currentLocation == "shrine":
        self.effects.worship()
      else:
        print("Invalid command. Type 'keywords' to view valid commands.")
    
    self.endGame()
    
  def endGame(self):
    print("\n\n-----------------------------------")
    print("Thank you for playing!")
    self.userInput = input("\nWould you like to play again?")
    if "yes" in self.userInput.lower():
      print("-----------------------------------")
      self.resetAll()
      self.playGame()
    
  #UTILITY FUNCTIONS
  def showKeywords(self):
    print("Keywords: ")
    print(" 1. 'Look at', 'View', or 'Read' to view something closer -> can also be used to view or read items in your bag")
    print(" 2. 'Go (direction)' to travel somewhere [Inside: Up, Down, Right, Left -> Outside: North, South, East, West]")
    print(" 3. 'Bag' to view what is in your bag")
    print(" 4. 'Map' to view the map of your adventures thus far")
    print(" 4. 'Investigate' to learn more about the area you are in")
    print(" 5. 'Pick up (item)' to obtain something")
    print(" 6. 'Use (item)' to use an item from your bag")
    print(" 7. 'Talk to (person)' to enter into a conversation with someone")
    print(" 8. 'Buy (item)' to purchase something")
    print(" 9. 'Drop', 'sell', or 'get rid of' to dispose of an item from your bag")
    print(" 10. 'Exit' to quit or restart the game")
  
  def openBag(self):
    self.bag.toString()
  
  def viewSomething(self):
    if "receipt" in self.userInput:
      self.location.view("Old Receipt")
    elif "torch" in self.userInput:
      self.location.view("Torch")
    else:
      print("\nThe item description you gave doesn't match anything in the known universe. Type " \
      +"'bag' to view your items or 'investigate' to see what might be in the area")
  
  def useItem(self):
    if "torch" in self.userInput and self.bag.hasItem("Torch"):
      self.bag.use("Torch")
      self.location.use("Torch")
    elif "receipt" in self.userInput and self.bag.hasItem("Old Receipt"):
      self.bag.use("Old Receipt")
    else:
      print("\nYou cannot use that item because you do not have that item. Type 'bag' to view your items, 'pick up' or 'buy' to obtain an item.")
  
