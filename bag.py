class Bag():
  
  def __init__(self):
    self.items = ["Old Receipt"]
    self.itemBools = {}
    self.coins = 10
  
  def toString(self):
    if len(self.items) == 0 and self.coins == 0:
      print("\nBag is empty!")
    else:
      print("\nYou have the following in your bag: \n")
      if(self.coins > 0):
        print(" 1: A pouch containing " + str(self.coins) + " silver coins")
        itemNum = 2
      else:
        itemNum = 1
      for item in range(len(self.items)):
        print(" " + str(itemNum) + ": " + self.items[item])
        itemNum += 1
      print("\n")
  
  def itemToString(self, item):
    if item == "Old Receipt":
      print("\nYou take a closer look at this old receipt you kept for some strange reason and notice some handwriting on the back.")
      print("\nScribbled in barely legible drunk handwriting, you can make out the following:")
      print("\n         IOU")
      print("\n           -Mayor Chowsky")
    if item == "Torch":
      if self.itemBools["Torch"]:
       print("\nYou take a look at your torch. The fire dances brightly, and you feel like this would certainly help you see if you ever find yourself somewhere dark.")
      else:
        print("\nYou pull the torch out of your bag. It's a pretty decent torch. You have the stuff to light to it if you ever need it in a pinch.")
  
  def badItem(self):
     print("\nThere is no item matching that description in the area or your bag. Type 'bag' to " \
     + "view the contents of your bag, or investigate to see what's in the area.")
  
  def hasItem(self, item):
    return item in self.items
    
  def itemInUse(self, item):
    if item in self.items and self.itemBools[item]:
      return True
    else:
      return False
  
  def view(self, item):
    if item in self.items:
      self.itemToString(item)
    else:
      self.badItem()
  
  def use(self, item):
    if item == "Torch":
      if self.itemBools["Torch"]:
          print("\nYou are about to distinguish your torch. If you are in a dark place, this means you will no longer be able to see!")
          response = input("Are you sure you wish to do this?  ")
          if "yes" in response or "yeah" in response:
            print("\nYou decide its time to put out your torch and you distinguish the flames and shove the torch back into your bag.")
            self.itemBools["Torch"] = False
          else:
            print("\nYou decide to leave your torch lit for now.")
      else:
        self.itemBools["Torch"] = True
    if item == "Old Receipt":
       print("\nYou reach into your bag and find an old receipt. What the heck did you keep this for? You're about to throw it away when you notice some hastily " \
       + "scribbbled writing on the back.")
  
  def buyItem(self, item, price):
    if price <= self.coins:
      print("\n--------->  Paid " + str(price) + " silver coins for " + item + "  <--------------")
      self.coins -= price
      self.items.append(item)
      if item == "Torch":
        self.itemBools["Torch"] = False
      return True
    else:
      print("\nYou rummage through the coin sack in your bag and unfortunately, it seems you've come up short of the asking price for the item.")
      return False

  def sellItem(self, item, price):
    if item in self.items:
      print("\nYou are about to sell " + item + " for " + str(price) + " silver coins.")
      response = input("\nAre you sure you wish to proceed? ")
      if "yes" in response:
        self.coins += price
        self.items.remove(item)
        return True
    else:
      print("\n----->  You do not have that item so you can't sell it!  <------")
    return False



      
  
  
