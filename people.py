class People:

    def __init__(self, bag):
        self.bag = bag
        self.people = {"priest": {"Name:": "Heinrich Flogstem", "Met": False, "Relationship": 2},
                    "wildernessShopOwner": {"Name": "Tom Handy", "Met": False, "Relationship": 2},
                    "candyShopOwner": {"Name": "Frieda Snitzle", "Met": False, "Relationship": 2},
                    "hatShopOwner": {"Name": "Harriett Hatter", "Met": False, "Relationship": 2}}
        self.relationships = ["Despise","Dislike","Neutral","Like","Love"]
        self.basePrices = {"wildernessShop": 1, "candyShop": 1, "hatShop": 1, "sketchyShack": 1}
        self.wildernessShopItems = {"Torch": 2, "100 Feet of Rope": 3, "5 Days Rations": 2, "Flimsy Dagger": 3, "Large Elephant Figurine (Porcelin)": 4, "Mini Elephant Figurine (Porcelin)": 2}

    
    def talkTo(self, person):
        if person == "priest":
            self.talkToPriest()
        if person == "wildernessShopOwner":
            self.talkToWildernessShopOwner()
    
    def talkToPriest(self):
        if not self.people["person"]["Met"]:
            print("\nThe priest looks up from his tea and smiles in a very warm and inviting way. \"Ah, a visitor,\" he says. \"Welcome to the Shrine of Memories. Here we pay homage to the gods of our past lives and worship " \
            + "the wisdom that our memories bring. If you worship here at this shrine, you may one day have the opportunity to experience the wisdom and power of more than one life.")
        else:
             print("\nThe priest looks up from his tea and smiles. \"Welcome back to the Shrine of Memories,\" he says calmly. \"It is wonderful to see you wish to once again worship here. I feel it imperative to warn you that though the shrine is " \
            + "powerful and may grant gifts of incredible power to adventurers who worship here, it can do so only once so use the gift wisely.\"")

    def talkToWildernessShopOwner(self):    
        
        print("\nThe owner looks up from his polishing, and greets you warmly with a large smile on his face. \"Hello there! What can I do for you today?\" he says in a loud deep voice.")
 
        while(True):
            response = input("")
            if self.intentToBuy(response):
                itemToBuy = self.wildernessShopWares(response)
                if itemToBuy != "none" and itemToBuy != "elephant":
                    price = int(self.wildernessShopItems[itemToBuy]*self.basePrices["wildernessShop"])
                    print("\n\"Certainly! That will be " + str(price) + " silver coins. You get the payment, and I'll get the item wrapped up and ready to go!\"")
                    if self.bag.buyItem(itemToBuy, price):
                        if "Large Elephant" in itemToBuy:
                            print("\n\"I know you will really really really really really love that one! I made it myself with the utmost care. It is one of my cutest models. Thank you so much for buying it! You have certaintly made " \
                            + "\"Tom\" happy today!\"")
                            self.changeRelationship("wildernessShopOwner",2)
                        elif "Mini Elephant" in itemToBuy:
                            print("\n\"Wow, that's sure a cute one you picked out. I really hope it brings as much love and friendship to you as it did to me. You sure made \"Tom\" happy today!\"")
                            self.changeRelationship("wildernessShopOwner",1)
                    else:
                        print("\n\"It's nothing to be ashamed of to not have a lot of money. Just do some more adventuring and I'm sure you'll find some coin!\"")
                else:
                    if itemToBuy == "elephant":
                        print("\n\"I am simply ecstastic that you wish to buy one of my cute little elephants. I sell two kinds, large and small, so you've got to pick before I can sell you one. If you want to see the prices, just ask!\"")
                    else:
                        print("\n\"I have many fine wares any adventurer would find useful! Plus you must have one of my porcelin elephants. They are just the cutest things in the whole world!\"")
                        print("\n\"My most popular items include torches, rope, rations, daggers, and, of course, my porcelin elephants.\"")
                        response = input("\n\"Are you interested in hearing my item's prices?\"     ")
                        if "yes" in response:
                            self.printPrices("wildernessShop")
                        else:
                            print("\n\"Well, if you're interested in buying, just let me know.")
            elif "price" in response or "how much" in response:
                print("\n\"Here are my current wares and prices!\"")
                self.printPrices("wildernessShop")
            elif self.intentoSell(response):
                itemToSell = self.wildernessShopWares(response)
                if itemToSell != "none" and itemToSell != "elephant":
                    if "elephant" in itemToSell:
                        print("\n\"I'm really sad you want to sell that item. She's a real beauty, and I was certain she would make you happy forever. But if you really want to, I'll take it back for half " \
                        + "the original price.\"")  
                    else:
                        print("\n\"I would be glad to buy that item from you (for half the original sell price of course)\"")
                    if self.bag.sellItem(itemToSell,self.wildernessShopItems[itemToSell]//2):
                        if "elephant" in itemToSell and self.people["wildernessShopOwner"]["Relationship"] > 2:
                            if self.people["wildernessShopOwner"]["Relationship"] == 4:
                                self.basePrices["wildernessShop"] = 1
                                print("\n--------Prices at the Wilderness Shop have increased!------------")
                            self.changeRelationship("wildernessShopOwner",-1)
                        print("\n\"It's been a pleasure doing business with you!\"")
                    else:
                        print("\n\"Very well if you don't have that item or just don't want to sell it, that's your choice.\"")
                else:
                    if itemToSell == "elephant":
                        print("\n\"I'm sad you would want to sell any kind of elephant, but if you're set on selling one, you've got to tell me which kind. I sell both large and small ones you know.\"")
                    else:
                        print("\n\"Currently, I will buy any item from you that you could have originally purchased in my shop (for half of the original sell price of course)\"")
            elif self.seekingInfo(response):
                print("\n\"So you want some info about the town, do you? Well, you've come to the wrong man. I could care less about what's out there. I only care about what's in here. Keeping my elephants safe is top priority, and then " \
                + "keeping you safe by providing you with all the best in wilderness gear, well, that's my second priority I suppose. I'm not lonely though. These elephants keep great company!\"")
            elif "elephant" in response:
                if self.threat(response):
                    print("\n\"How could you say something like that? Elephants are the cutest sweetest awesomest things on the planet! If you just take a look at my figurines, I'm sure you'll see just how cute they are.")
                    response = input("\"Do you like them any better now that you've had a closer look?\"    ")
                    if "yes" in response or "okay" in response:
                        print("\n\"Oh good. I knew I could bring you to my side.")
                    else:
                        print("\n\"Well if that's how it's going to be. While I hate doing business with an elephant hater, business is business, but I won't be giving you any deals!\"")
                        print("\n--------Prices at the Wilderness Shop have increased!------------")
                        self.basePrices["wildernessShop"] *= 2
                        self.changeRelationship("wildernessShopOwner",-2)
                elif "love" in response or "like" in response or "cute" in response or "pretty" in response:
                    print("\n\"Did you say something about how you love elephants? What a coincidence because so do I! Please, take a look over at the north end of my shop and you can find the most beautiful porcelin elephants in all the country. I hope you " \
                    + "will want to purchase one!\"")
                    self.changeRelationship("wildernessShopOwner",1)
                else:
                    print("\n\"Did you say something about elephants? I absolutely love elephants. These elephant figurines are like my family.\"")
            elif self.threat(response):
                print("\n\"How dare you threaten me! And in my own shop no less. With all my elephants as witness, I will not stand for this. If you wish to buy from me, you will pay double the price!\"")
                print("\n--------Prices at the Wilderness Shop have increased!------------")
                self.basePrices["wildernessShop"] *= 2
                self.changeRelationship("wildernessShopOwner",-1)
            elif "bargain" in response or "trade" in response:
                print("\n\"I respect a person who's willing to bargain, but unfortunately the only way my prices going lower is if you make a frind of old \"Tom\"!\"")
            elif "nothing" in response or "leave" in response:
                return
            else:
                print("\n\"I'm sorry I'm not sure what you mean by that.\"")
            
            print("\n\"What else can I help you with today?\"   ")  
        
    def intentToBuy(self, response):
        if "buy" in response or "for sale" in response or "just looking" in response:
            return True
        else:
            return False
    
    def intentoSell(self, response):
        if "sell" in response or "take my stuff" in response or "get rid of my stuff" in response:
            return True
        else:
            return False
    
    def seekingInfo(self, response):
        if "info" in response or ("about" in response and ("town" in response or "area" in response)):
            return True
        else:
            return False
    
    def threat(self, response):
        if "die" in response or "kill" in response or "hate" in response or "destroy" in response or "murder" in response or "death" in response or "stab" in response:
            return True
        else:
            return False
    
    def wildernessShopWares(self, response):
        if "torch" in response:
            return "Torch"
        elif "elephant" in response:
            if "large" in response or "big" in response:
                return "Large Elephant Figurine (Porcelin)"
            elif "small" in response or "mini" in response or "little" in response:
                return "Mini Elephant Figurine (Porcelin)"
            else:
                return "elephant"
        elif "rope" in response:
            return "100 Feet of Rope"
        elif "rations" in response:
            return "5 Days Rations"
        elif "dagger" in response:
            return "Flimsy Dagger"
        else:
            return "none"
    
    def printPrices(self, shop):
        if shop == "wildernessShop":
            print("\nWILDERNESS SHOP ITEMS FOR SALE:")
            print("----------------------------------")
            for item in self.wildernessShopItems:
                print("     " + item + ": " + str(int(self.wildernessShopItems[item]*self.basePrices["wildernessShop"])) + " silver coins")
    
    def changeRelationship(self, person, netChange):
        if netChange > 0:
            relationshipBefore = self.people[person]["Relationship"]
            if relationshipBefore < 4:
                self.people[person]["Relationship"] += netChange
                if self.people[person]["Relationship"] > 4:
                    self.people[person]["Relationship"] = 4
                if self.people[person]["Relationship"] >= 2 and relationshipBefore < 2:
                    if person == "wildernessShopOwner":
                        print("\nOkay kid, I don't hate you anymore, but you gotta stop being so threatening all the time.")
                        print("\n--------Prices at the Wilderness Shop have decreased!------------")
                        self.basePrices["wildernessShop"] = 1
                if self.people[person]["Relationship"] == 4:
                    if person == "wildernessShopOwner":
                        print("\nWow, we have become such good friends since you walked into my shop. You're a pretty great person you know that? \"Tom\'s\" friends are always welcome here!\"")
                        print("\n--------Prices at the Wilderness Shop have decreased!------------")
                        self.basePrices["wildernessShop"] = 0.75
        else:
            if self.people[person]["Relationship"] > 0:
                self.people[person]["Relationship"] += netChange
                if self.people[person]["Relationship"] < 0:
                    self.people[person]["Relationship"] = 0
                
