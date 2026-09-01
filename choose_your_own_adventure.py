# CHOOSE YOUR OWN ADVENTURE

# 🌲 THE MYSTERIOUS FOREST

# Introduce the player
    # Ask their name
    # Welcome them to the adventure

name = input("\n    Type your name: ")
print("🚪 Welcome", name, "to the adventure :)\n")

# 🚪 The adventure begins
answer = input("You enter the mysterious forest. Do you go left or right? ")
if answer.lower() == "left":
    monster_encounter = input("You come across a swamp monster do you walk around it or have a dance battle 💃🏽?"
                             " Type walk to walk around or dance to dance battle? ")
    if monster_encounter.lower() == "walk":
        answer_direction = input("You chose to walk around and discovered a hidden path do you follow it? yes or no. ")
        if answer_direction.lower() == "yes":
            help_troll = input("You come across a troll who needs help. What will you do? Type help or ignore. ")
            if help_troll.lower() == "help":
                print("Your a kind one",name, "! Here lies a bag of air and a pot of gold! 💰")
            if help_troll.lower() == "ignore":
                print("Lack of kindness",name, "! GAME OVER!")
        if answer_direction.lower() == "no":
            print("Lack of curiosity",name, "! GAME OVER!")

    elif monster_encounter.lower() == "dance":
        answer_direction = input("You win the dance battle and are awarded the ability to see at night. "
                                 "Do you continue and see what follows or exit game? Type continue to continue or exit game. ")
        if answer_direction.lower() == "continue":
            boat_adventures = input("You come across a boat 🚤 do you see where it take you or continue moving forward?"
                           " Type boat to adventure or forward to see what lies ahead? ")
            if boat_adventures.lower() == "boat":
                answer_boat = input(
                    "Nice choice! You drive and reach a dead end but there's a pier do you get out or turn around? "
                    "Type pier or turn around. ")
            elif boat_adventures.lower() == "pier":
                answer_pier = input("Oh no there's something waiting for you! Do you continue ahead or "
                                          "retrieve back to the boat? Type continue or boat. ")
                if answer_pier.lower() == "continue":
                    print("Your a curious one",name, "! Here lies a pot of gold! 💰")
                elif answer_pier.lower() == "boat":
                    print("Lack of curiosity",name, "! GAME OVER!")
        elif answer_direction.lower() == "exit":
            print("Thank you for playing",name, ":) ⭐️")

elif answer.lower() == "right":
    answer_boat = input("You come across a boat 🚤 do you see where it take you or continue moving forward?"
                           " Type boat to adventure or forward to see what lies ahead? ")
    if answer_boat.lower() == "boat":
        answer_boat = input("Nice choice! You drive and reach a dead end but there's a pier do you get out or turn around? "
                            "Type pier or turn around. ")
        if answer_boat.lower() == "pier":
            answer_pier = input("Oh no there's something waiting for you! Do you continue ahead or "
                                "retrieve back to the boat? Type continue or boat. ")
            if answer_pier.lower() == "continue":
                print("Your a curious one", name, "! Here lies a pot of gold! 💰")
            elif answer_pier.lower() == "turn around":
                print("Lack of curiosity", name, "! GAME OVER!")
        elif answer_boat.lower() == "turn around":
            print("Lack of curiosity",name,"! GAME OVER!")
    elif answer_boat.lower() == "forward":
        answer_bridge = input("You discover an old bridge do you cross the bridge or turn around? Type bridge or turn around? ")
        if answer_boat.lower() == "bridge":
            answer_bridge = input("Oh no there's something on the other end! Do you continue ahead or "
                                  "retrieve back to the boat? Type continue or boat. ")
            if answer_bridge.lower() == "continue":
                print("Your a curious one",name, "! Here lies a pot of gold! 💰")
            elif answer_bridge.lower() == "boat":
                print("Lack of curiosity",name,"! GAME OVER!")
else:
    print("Sorry, I didn't understand you.")
