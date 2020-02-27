from collections import OrderedDict
from bag import *
from people import *
import random

class Location:
  
  def __init__(self, bag, effects):
    self.effects = effects
    self.bag = bag
    self.people = People(bag)
    self.dead = False
    self.currentLocation = "townCenter"
    self.inside = False
    self.insidePlace = ""
    self.itemsInLocation = {"cave": ["rocks"], 
                            "westLake": [], 
                            "eastLake": [], 
                            "castle": [], 
                            "shrine": [], 
                            "northForest": [],
                            "graveyard": [], 
                            "mountainPass": [], 
                            "townCenter": [], 
                            "potionStand": [], 
                            "crossRoads": [],
                            "mountains": [], 
                            "shoppingDistrict": [], 
                            "southForest": [], 
                            "shadyDistrict": [], 
                            "southSouthForest": [], 
                            "witchGarden": [], 
                            "witchHut": [], 
                            "caveEntrance": [], 
                            "caveLake": [],
                            "banditHideout": [], 
                            "kingChamber": [], 
                            "trapRoom": [], 
                            "dragonLair": [], 
                            "wildernessShop": [],
                            "candyShop": [], 
                            "hatShop": []}
    self.exitAreas = {"leave": self.leave,"cliffs": self.cliffs,"canyon": self.canyon,"river": self.river}
    self.locationFunctions = {"cave": self.cave, "westLake": self.westLake, "eastLake": self.eastLake, "castle": self.castle, "shrine": self.shrine, "northForest": self.northForest,
                              "graveyard": self.graveyard, "mountainPass": self.mountainPass, "townCenter": self.townCenter, "potionStand": self.potionStand, "crossRoads": self.crossRoads,
                              "mountains": self.mountains, "shoppingDistrict": self.shoppingDistrict, "southForest": self.southForest, "shadyDistrict": self.shadyDistrict, 
                              "southSouthForest": self.southSouthForest, "witchGarden": self.witchGarden, "witchHut": self.witchHut, "caveEntrance": self.caveEntrance, "caveLake":self.caveLake,
                              "banditHideout": self.banditHideout, "kingChamber": self.kingChamber, "trapRoom": self.trapRoom, "dragonLair": self.dragonLair, "wildernessShop": self.wildernessShop,
                              "candyShop": self.candyShop, "hatShop": self.hatShop}
    self.locationMapping = OrderedDict([("cave", ["cliffs","shrine","westLake","river",False,"|------- CAVE ------->","caveEntrance"]),
                                  ("westLake", ["cliffs","northForest","eastLake","cave",False,"<-----WEST LAKE ----->"]),
                                  ("eastLake", ["cliffs","graveyard","noPath","westLake",False,"<-----EAST LAKE       "]),
                                  ("castle", ["cliffs","mountainPass","blockedMtn","blockedMtn",False,"       CASTLE        "]),
                                  ("shrine", ["cave","townCenter","northForest","river",False,"|-------SHRINE------->"]),
                                  ("northForest", ["westLake","potionStand","graveyard","shrine",False,"<----NORTH FOREST---->"]),
                                  ("graveyard", ["eastLake","crossRoads","noPath","northForest",False,"<-----GRAVEYARD       "]),
                                  ("mountainPass", ["castle","mountains","blockedMtn","blockedMtn",False,"    MOUNTAIN PASS     "]),
                                  ("townCenter", ["shrine","shoppingDistrict","potionStand","leave",True,"<----TOWN CENTER ---->"]),
                                  ("potionStand", ["northForest","southForest","crossRoads","townCenter",False,"<----POTION STAND---->"]),
                                  ("crossRoads", ["graveyard","witchGarden","mountains","potionStand",False,"<---- CROSSROADS ---->"]),
                                  ("mountains", ["mountainPass","witchHut","leave","crossRoads",False,"<-----MOUNTAINS ----->"]),
                                  ("shoppingDistrict", ["townCenter","shadyDistrict","blockedTown","blockedTown",False,"  SHOPPING DISTRICT   ","wildernessShop","candyShop","hatShop"]),
                                  ("southForest", ["potionStand","southSouthForest","noPath","noPath",False,"     SOUTH FOREST     "]),
                                  ("shadyDistrict", ["shoppingDistrict","canyon","blockedTown","blockedTown",False,"    SHADY DISTRICT    "]),
                                  ("southSouthForest", ["southForest","canyon","witchGarden","noPath",False,"  SOUTH SOUTH FOREST->"]),
                                  ("witchGarden", ["crossRoads","canyon","witchHut","southSouthForest",False,"<----WITCH GARDEN---->"]),
                                  ("witchHut", ["mountains","canyon","leave","witchGarden",False,"<-----WITCH HUT ----->"]),
                                  ("caveEntrance", ["caveLake","blockedInside","trapRoom","banditHideout",False,"cave"]),
                                  ("caveLake", ["blockedInside","caveEntrance","blockedInside","blockedInside",False]),
                                  ("banditHideout", ["kingChamber","blockedInside","caveEntrance","blockedInside",False]),
                                  ("kingChamber", ["blockedInside","banditHideout","blockedInside","blockedInside",False]),
                                  ("trapRoom", ["blockedInside","blockedInside","dragonLair","caveEntrance",False]),
                                  ("dragonLair", ["blockedInside","blockedInside","blockedInside","trapRoom",False]),
                                  ("wildernessShop", ["blockedInside","blockedInside","blockedInside","blockedInside",False,"shoppingDistrict"]),
                                  ("candyShop", ["blockedInside","blockedInside","blockedInside","blockedInside",False,"shoppingDistrict"]),
                                  ("hatShop", ["blockedInside","blockedInside","blockedInside","blockedInside",False,"shoppingDistrict"])])
   
  
  def talkTo(self, input):
    if self.currentLocation == "shrine":
      if "priest" in input or "guy" in input or "person" in input:
        self.people.talkTo("priest")
      else:
        print("\nThere is no person here fitting that description to talk to. You begin mumbling to yourself and the priest glances at you with a knowing look.")
    if self.currentLocation == "wildernessShop":
      if "tom" in input or "owner" in input or "guy" in input:
        self.people.talkTo("wildernessShopOwner")
        self.locationFunctions[self.currentLocation]()
      else:
        print("\nThere is no person here fitting that description to talk to. You begin mumbling to yourself and the owner continues to polish his elephant figurine.")

  def view(self, item):
    if item in self.itemsInLocation[self.currentLocation]:
      self.itemToString(item)
    else:
      self.bag.view(item)
  
  def use(self, item):
    if item == "Torch":
      if self.bag.itemInUse("Torch"):
        if self.insidePlace == "cave":
            print("\nYou light the torch you had in your bag for just such a moment and a large pool of fiery dancing light erupts around you.")
            print("\nYou can now see that before you is a massive cave chamber. Your torch illuminates the space at least thirty feet in front of you and you can see " \
            + "the damp cave floor glistening in the dancing firelight.")
        else:
          print("\nYou light the torch you had in your bag. It's still pretty light where you are so it doesn't make too much of a difference, but hey the small " \
          + "warm fire is kind of nice.")
      else:
        if self.insidePlace == "cave":
            print("\nYou are entrenched in darkness and can no longer see your hand in front of your face. You can see lingering dots of light from your vision still " \
            + "trying to get used to the dark and remembering the beautiful light of your torch.")
            if self.currentLocation != "caveEntrance":
              self.caveDeath()
            
  def itemToString(self, item):
    if item == "Wanted Poster":
      print("\nLook at wanted poster.")
       
  def investigate(self):
    if(self.currentLocation == "cave"):
      print("\nYou snoop around the entrance of the cave and after taking a closer look, you notice that the ground near the cave entrance is well-trodden." \
      + " It's likely that many 'somethings' come through here quite often. You aren't an expert tracker, but noticing some footprints in the dirt, you are " \
      + "fairly certain that these 'somethings' are humanoids.")
    if(self.currentLocation == "caveEntrance"):
      if self.bag.itemInUse("Torch"):
        print("\nInvestigating this room further, you notice that the cave begins to slop upward toward the back of the room. Perhaps you could go up and explore this area. " \
        + "You also find to the far left of the room, a narrow hall winding off into the distance. To the far right of the cave, you find a much wider, larger hall that also " \
        + "appears to go deeper into the cave. The stalagmites are beautiful and you don't feel you are in any immediate danger here.")
      else:
        print("\nYou feel along the cave walls with your hands. After stumbling a few times, you finally feel like you have a decent scope of the room. You still can't see a " \
        + "thing, and you have no idea what dangers are lurking near you or what fate might befall you if you continue without a light, but from your investiagation of this " \
        + "pitch black room, you believe you could try and stumble to the right or left. Maybe it will lead somewhere with more light or maybe it will lead to your death...")
    if(self.currentLocation == "shoppingDistrict"):
      print("\nThe people here seem generally lively and doing okay for the most part, but as you explore even deeper into the shopping district, there seems to become increasingly less people and your uneasiness starts to grow. You get the feeling that " \
      + "if you continued South from here, you would be entering a more shady part of town.")
    if(self.currentLocation == "shrine"):
      print("\nTaking a closer look at the shrine's central statue, you notice subtle generic human faces carved all over the rock face as if to represent a great many people or perhaps, a great many lives. The grass is growing over the cobblestones that " \
      + "were laid in the clearing and moss creeps up the base of the statue. It seems nature is slowly taking over and yet a good many people must worship here since many incense has been placed and is still burning.")
  
  def resetCurrLocation(self):
    self.locationFunctions[self.currentLocation]()
  
  def changeLocation(self, input):
    
    if self.insidePlace == "cave" and (not self.bag.itemInUse("Torch")):
      self.caveDeath()
      return
    
    if "north" in input or "up" in input:
      newLocation = self.locationMapping[self.currentLocation][0]
    elif "south" in input or "down" in input:
      newLocation = self.locationMapping[self.currentLocation][1]
    elif "east" in input or "right" in input:
      newLocation = self.locationMapping[self.currentLocation][2]
    elif "west" in input or "left" in input:
      newLocation = self.locationMapping[self.currentLocation][3]
    elif "in" in input or "enter" in input:
      if (not self.inside) and (len(self.locationMapping[self.currentLocation]) > 6):
        if(self.currentLocation == "shoppingDistrict"):
          if "wilderness" in input or "survival" in input:
            newLocation = self.locationMapping[self.currentLocation][6]
          elif "candy" in input:
            newLocation = self.locationMapping[self.currentLocation][7]
          elif "hat" in input:
            newLocation = self.locationMapping[self.currentLocation][8]
          elif "shop" in input:
            print("\nYou enter a random store of interest.")
            newLocation = self.locationMapping[self.currentLocation][6+random.randint(0,2)]
          else:
            print("\nThere are so many shops here! Please type which shop you want to enter. To learn more about which shops are here, investigate the area!")
            return
          self.insidePlace = "shop"
        else:
          self.insidePlace = "cave"
          newLocation = self.locationMapping[self.currentLocation][6] 
      else:
        print("\nThere is no building or structure to enter into here!")
        return
      self.inside = True
    elif "out" in input or "leave" in input:
      if self.inside:
        if len(self.locationMapping[self.currentLocation]) > 4:
          self.inside = False
          self.insidePlace = ""
          newLocation = self.locationMapping[self.currentLocation][5]
        else:
          print("\nThere is no way to leave this building or structure from here! Make your way back to the entrance and you can go from there.")
          return
      else:
        print("\nYou are not inside a building or structure!")
        return
    else:
      print("Not a valid direction. If you wish to go somewhere, you may try typing a direction such as North, South, Inside, Up, or Right.")
      return
    
    if(newLocation == "noPath"):
      print("You attempt to travel in this direction and realize there is nothing of importance this way. You then return from whence you came.")
      self.resetCurrLocation()
    elif(newLocation == "blockedMtn"):
      print("You are blocked in on both sides by massive mountains! You cannot go East or West from here!")
      return
    elif(newLocation == "blockedTown"):
      print("Though you try to find a way out of town, going this direction just doesn't appear to be getting you anywhere. If you make your way back to town center, you should" \
      + " be able to exit through the main gates.")
      self.resetCurrLocation()
    elif(newLocation == "blockedInside"):
      print("\nThere is a wall here! It is impossible to go this way!")
      return
    elif(any(newLocation == location for location in self.exitAreas)):
      return self.exitAreas[newLocation]()
    else:
        self.locationMapping[newLocation][4] = True
        self.currentLocation = newLocation
        self.locationFunctions[newLocation]()
  
  # EXIT AREAS FUNCTIONS
  def leave(self):
    print("The road is open and the way is clear, but be warned! If you leave this way, you will be leaving the area of the adventure, and you can never return!")
    response = input("\nWould you like to leave before your adventure is done?")
    if "yes" in response.lower():
      print("\n\nHaving had enough adventure, you head out toward the next kingdom in search of a new and (hopefully) more peaceful life. \n\nUnfortunately, evil takes over" \
      + " and destroys the universe due to your cowardice. The End.")
      self.dead = True
    else:
      self.locationFunctions[self.currentLocation]()
  
  def cliffs(self):
    print("\nYou travel North for a while and eventually come to a towering cliff-face.")
    print("\nUnfortunately, these cliffs appear far too dangerous and unscaleable even with training and a rope.")
    print("You may attempt to climb them, but you get this terrible feeling that if you do, you will most likely DIE.")
    response = input("\nWill you attempt to climb the cliffs?")
    if "yes" in response:
      print("\nYou attempt to scale the cliff. It's actually going miraculously well for the first half hour.")
      print("Then suddenly the cliff starts to crumble beneath your hands. You knew this would happen but you climbed anyway.")
      print("You have chosen your fate and so you begin to accept you inevitable demise as you begin to fall.....")
      self.death()
    else:
      print("\nAfter contemplating your imminent demise, you decide it's probably best not to try and scale these cliffs.")
      print("You turn around and head South back from whence you came.")
      self.locationFunctions[self.currentLocation]()
  
  def canyon(self):
    print("You travel South for a while until suddenly you find yourself at the edge of a canyon wider than your entire town!")
    print("After looking around you conclude that there is no safe way down this canyon. You could jump to your death or leave but there's no way you're getting across.")
    response = input("\nWhat course of action do you choose?")
    if "jump" in response or "die" in response or "death" in response:
      print("\nDeciding that now is as good a time as any, you decide to greet the Grim Reaper head on and take a mighty leap!")
      print("You, of course, immediately regret this at least 100 times throughout the course of your 7,000 foot fall....")
      self.death()
    else:
      print("\nAfter contemplating death and a 7,000 foot free fall, you decide it's probably better to just turn around.")
      print("You head North until you end up back from whence you came.")
      self.locationFunctions[self.currentLocation]()
  
  def river(self):
    print("You travel East for some time before reaching the banks of a large river, so large that if you barely squint, you might be able to see to the other side.")
    print("To make matters worse, this river is covered in massive white water rapids. You just know that there is no way you will make it across this river alive.")
    response = input("\nWhat will you do?")
    if "cross" in response or "swim" in response or "across" in response:
      print("\nDespite your knowledge of the dangers of this river, you decide to brave the white water rapids anyway.")
      print("You instantly get sucked under the water by the powerful flow of the river. Your foot gets caught between some rocks and though you struggle to free it," \
      + " you feel yourself rapidly losing consciousness and the last you can think before your world disappears is, 'If only I had been born a frog.'")
      self.death()
    else:
      print("\nAfter staring at the dangerous water, you realize: 'I can't die yet because I have an adventure to complete!' so you turn around and head back from whence you came.")
      self.locationFunctions[self.currentLocation]()
  
 #DUMB WAYS TO DIE
  def death(self):
    if self.effects.worshipEffect == "active":
      print("\nAs you pass into the world of death, you remember the vision you had at the Shrine of Memories. Suddenly you open your eyes and find yourself seated at the base of the shrine. " \
      + "You realize the vision is now fulfilled as you have been given a second chance at life with all the memories from your life before. Unfortuantely, your bag was unable to be transported and " \
      + "revived across time and space, and you have lost all of the items you are carrying.")
      self.effects.worshipEffect = "used"
      self.insidePlace = ""
      self.inside = False
      self.currentLocation = "shrine"
      self.locationFunctions[self.currentLocation]()
    else:
      print("\nIt appears that you have died. Unfortunate...for you. Bye bye dead guy!")
      self.dead = True
  
  def caveDeath(self):
    print("\nYou stumble through the darkness when suddenly, you feel a sharp pain in your stomach. You cry out in pain and reach down to feel something warm and " \
            + "sticky. Blood, perhaps? Your mind races to consider the possibilities: Did someone stab you? Did you run into a stray stalagmite? A trap, maybe? Or was it the " \
            + "ghost of your old neighbor come to seek revenge from the incident that must not be named? Whatever the cause, you soon come to realize that you will " \
            + "never know as your thoughts fade to nonsense and your body falls to the cold, cave floor. Your final words coughed up through blood echo solemnly throughout the cave: " \
            + "\n         \"If only..if only...I had...a...torch....\"")
    self.death()
  
  #LOCATION FUNCTIONS
  def cave(self):
    self.locationMapping["cave"][4] = True
    print("\n\nCAVE")
    print("--------")
    print("You find yourself standing at the mouth of a rather large cave set deep inside a dangerous cliffside.")
    print("The entrance appears easily accessible and there is no sign of anyone lurking about the outside.")
  
  def caveEntrance(self):
    print("\n\nCAVE ENTRANCE")
    print("-----------------")
    if self.bag.itemInUse("Torch"):
      print("You have entered the large ominous cave. Before you is a massive cave chamber. Your torch illuminates the space at least thirty feet in front of you and you can see " \
      + "the damp cave floor glistening in the dancing firelight.")
    else:
      print("You have entered the large ominous cave. Before you is a pitch black room, or at least you think it's a room, but you honestly can't see a thing!")
      print("\nYou can smell dampness in the cool cave air and if you hold your breath, you might hear the hint of something large breathing deeply.")
    
  def caveLake(self):
    print("\nCAVE LAKE")
  
  def banditHideout(self):
    print("\nTHE HIDEOUT OF THIEVES")
  
  def kingChamber(self):
    print("\nTHE KING OF THIEVES' PERSONAL CHAMBER")
  
  def trapRoom(self):
    print("\nA SUSPICIOUSLY EMPTY ROOM")
  
  def dragonLair(self):
    print("\nTHE DRAGON'S LAIR!")
  
  def westLake(self):
    self.locationMapping["westLake"][4] = True
    print("\nWEST LAKE")
    
  def eastLake(self):
    self.locationMapping["eastLake"][4] = True
    print("\nEAST LAKE")
    
  def castle(self):
    self.locationMapping["castle"][4] = True
    print("\nCASTLE")
    
  def shrine(self):
    self.locationMapping["shrine"][4] = True
    print("\nSHRINE OF MEMORIES")
    print("---------------------")
    print("\nYou wind up a small well-kept path into a peaceful clearing where a large rock statue towers above the trees. There is a small wooden lean-to to the right of the statue that seems to provide some shelter for the old priest who sits beneath it, " \
    + "peacefully sipping tea from a small wooden cup. At the base of the statue is some burning incense.")
    
  def northForest(self):
    self.locationMapping["northForest"][4] = True
    print("\nNORTH FOREST")
    
  def graveyard(self):
    self.locationMapping["graveyard"][4] = True
    print("\nGRAVEYARD")
  
  def mountainPass(self):
    self.locationMapping["mountainPass"][4] = True
    print("\nMOUNTAIN PASS")
    
  def townCenter(self):
    self.locationMapping["townCenter"][4] = True
    print("\nTOWN CENTER")
  
  def potionStand(self):
    self.locationMapping["potionStand"][4] = True
    print("\nINCONSPICUOUS POTION STAND")
  
  def crossRoads(self):
    self.locationMapping["crossRoads"][4] = True
    print("\nCROSSROADS")
  
  def mountains(self):
    self.locationMapping["mountains"][4] = True
    print("\nMOUNTAINS")
  
  def shoppingDistrict(self):
    self.locationMapping["shoppingDistrict"][4] = True
    print("\nSHOPPING DISTRICT")
    print("--------------------")
    print("You enter the busy shopping district of the town.")
    print("\nAs you wind your way among the peoples and shops, you find a few points of particular interest. There is a candy shop that claims their candies have 'out of this world'" \
      + " effects. There is also a small 'Wilderness Survival Shop' that might have some useful goods for adventurers. There is also a hatter that has some pretty awesome hats. None " \
      + "of the other shops really stand out to you that much.")
  
  def wildernessShop(self):
    print("\nTOM'S SHOP OF HARD-CORE WILDERNESS SURVIVAL AND MINI-ELEPHANT FIGURINES")
    print("--------------------------------------------------------------------------")
    print("You enter the small shop. There are items in bins and hanging on the wall. There is also a section of shelving dedicated to mini-elephant figurines. " \
    + "The shop owner stands at the counter polishing a porceline elephant no larger than a thumbnail.")
  
  def candyShop(self):
    print("\nCANDY SHOP OF WONDERS")
    print("-----------------------")
  
  def hatShop(self):
    print("\nHARRIET'S HOT HATTERY")
    print("-----------------------")
  
  def southForest(self):
    self.locationMapping["southForest"][4] = True
    print("\nSOUTH FOREST")
  
  def shadyDistrict(self):
    self.locationMapping["shadyDistrict"][4] = True
    print("\nSHADY DISTRICT")
  
  def southSouthForest(self):
    self.locationMapping["southSouthForest"][4] = True
    print("\nSOUTH SOUTH FOREST")
  
  def witchGarden(self):
    self.locationMapping["witchGarden"][4] = True
    print("\nWITCH'S GARDEN")
  
  def witchHut(self):
    self.locationMapping["witchHut"][4] = True
    print("\nWITCH'S HUT")
  
  def printMap(self):
    map = [""] * 5
    locationNum = 1
    for location in self.locationMapping:
      if locationNum > 20:
        break
      if(self.locationMapping[location][4]):
        if(locationNum < 5):
          map[0] += "          _           "
        else:  
          map[0] += "          ^           "
        map[1] += "          |           "
        map[2] += self.locationMapping[location][5]
        map[3] += "          |           "
        if(locationNum > 16):
          map[4] += "          _           "
        else:
          map[4] += "          v           "
      else:
          map[0] += "                      "
          map[1] += "                      "
          map[2] += "                      "
          map[3] += "                      "
          map[4] += "                      "
      
      if location == "southForest":
        if self.locationMapping["crossRoads"][4] and self.locationMapping["witchGarden"][4]:
          map[0] += "          ^           "
          map[1] += "          |           "
          map[2] += "          |           "
          map[3] += "          |           "
          map[4] += "          v           "
        if self.locationMapping["mountains"][4] and self.locationMapping["witchHut"][4]:
          map[0] += "          ^           "
          map[1] += "          |           "
          map[2] += "          |           "
          map[3] += "          |           "
          map[4] += "          v           "
        locationNum += 2
      
      if(locationNum % 4 == 0):
        for i in range(len(map)):
          print(map[i])
        map = [""] * 5
      
      locationNum += 1

                                   
