

#Printing Title
print("SHE WAS KIDNAPPED?!?")
print("A Mario Text Adventure by Aarthi and Merry :D")


#Backstory
print("Mario is a programmer at Nintendo. One day, as he enters work, he sees that he has a voicemail from Bowser...")
print("Bowser: Hey Mario. If you ever want to see Princess Peach alive, come find me... MWAHAHAHAHA! See you soon.")

#Choice 1
print("Do you want to leave work to save Peach?")
going = input("YES or NO? ")
if going == "YES":
    print("You leave work and encounter a pack of mushrooms!!! AHHH..")
    mushroom = input("Would you like to AVOID or FIGHT them? ")
    if mushroom == "AVOID":
        print("You've successfully avoided the mushrooms")
        print("Another obstacle!!! OH NOOO...")
        print("You meet a piranha plant... but your boss rings your phone to get back to work")
        piranha = input("JUMP over the piranha or RETURN to work? ")
        if  piranha == "JUMP":
            print("WHOOHOO! You made it to Bowser's castle alive! Let's hope you stay that way...")
            print("It's not too late to turn back though...You just got a text from your boss. He says he'll fire you if you don't get back right now!")
            bowser = input("Do you want to FIGHT Bowser or RETURN to work? ")
            if bowser == "FIGHT":
                print("You saved Peach! Hooray!")
                print("You now control Bowser's castle")
                to_rent = input("Will you MOVE IN or let it out to RENT for some extra cash. PS: You were fired and are now unemployed... ")
                if to_rent == "MOVE IN":
                    print("You live happily ever after!")
                    print("THE END!!!!!")
                elif to_rent == "RENT":
                        print("The mushrooms move in and kill you while you sleep")
                        print("The end ; _ ;")
            elif bowser == "RETURN":
                print("Peach unfollowed you on Twitter. You died of shock...")
                print("The end ; _ ;")
        elif piranha == "RETURN":
            print("The mushrooms tracked you down and kill you on your way back. Ouch.")
            print("The end ; _ ;")
    elif mushroom == "FIGHT":
        print("Prepare for battle. Choose a weapon.")
        weapon = input("Will you fight with TURTLE SHELLS or with your BARE HANDS? ")
        if weapon == "TURTLE SHELLS":
            print("YOU WIN!!!")
            print("Another obstacle!!! OH NOOO...")
            print("You meet a piranha plant... but your boss rings your phone to get back to work")
            piranha = input("JUMP over the piranha or RETURN to work?")
            if  piranha == "JUMP":
                print("WHOOHOO! You made it to Bowser's castle alive! Let's hope you stay that way...")
                print("It's not too late to turn back though...You just got a text from your boss. He says he'll fire you if you don't get back right now!")
                bowser = input("Do you want to FIGHT Bowser or RETURN to work? ")
                if bowser == "FIGHT":
                    print("You saved Peach! Hooray!")
                    print("You now control Bowser's castle")
                    to_rent = input("Will you MOVE IN or let it out to RENT for some extra cash. PS: You were fired and are now unemployed... ")
                    if to_rent == "MOVE IN":
                        print("You live happily ever after!")
                        print("THE END!!!!!")
                    elif to_rent == "RENT":
                        print("The mushrooms move in and kill you while you sleep.")
                        print("The end ; _ ;")
                    else:
                        print("Invalid answer")
                        print("The end ; _ ;")
                elif bowser == "RETURN":
                    print("Peach unfollowed you on Twitter. You died of shock...")
                    print("The end ; _ ;")
                else:
                    print("Invalid answer")
                    print("The end ; _ ;")
            elif piranha == "RETURN":
                print("Peach unfollowed you on Twitter. You died of shock...")
                print("The end ; _ ;")
            else:
                print("Invalid answer")
                print("The end ; _ ;")
        elif weapon == "BARE HANDS":
            print("Bad move. You die of poison two hours later")
            print("The end ; _ ;")
        else:
            print("Invalid answer")
            print("The end ; _ ;")
    else:
        print("Invalid answer")
        print("The end ; _ ;")
elif going == "NO":
    print("Peach unfollowed you on Twitter. You died of shock...")
    print("The end ; _ ;")
else:
    print("Invalid answer")
    print("The end ; _ ;")
      
    
      
                            
            
                    
      
