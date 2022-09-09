import time
from math import fabs
from operator import truediv
from pickle import GLOBAL


print("                                     Welcome to your adventure!")


print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print("||||                                                                                                     ||||")
print("||||                             Who would you like to be? Peter or Jane:                                ||||")
print("||||                                                                                                     ||||")
print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")

character = input("Enter the name of the person you want to be: ").lower()


def character_selection():
    global choose_character
    choose_character = True
    while choose_character:
        if character == "Jane".lower():
            print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
            print("||||                                                                      ||||")
            print("||||     That's a wonderful name, let's begin your wonderful journey.     ||||")
            print("||||                                                                      ||||")
            print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
            choose_character = False
        elif character == "Peter".lower():
            print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
            print("||||                                                                           ||||")
            print("||||     Peter, let's get you going. You have lot's of stuff to figure out.    ||||")
            print("||||                                                                           ||||")
            print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
            choose_character = False
        else:
            print("That's an invalid option, please enter a correct name: ")
            character_selection()
            return



def beginning():
    global jane_first
    global peter_first
    if character == "jane".lower():
        print("Jane, you start your journey waking up in the middle of the night at 4am.")
        print("You hear a strange noise coming from your kitchen.")
        jane_first = input("What are you going to do? (Bed or Kitchen?: )").lower()
    elif character == "peter".lower():
        print("Alright Peter, you start your journey in a hotel room. You wake up by a loud bang coming from the floor below you.")
        print("You can't go back to bed so you're trying to make up your mind.")
        peter_first = input("Do you want to go and investigate or stay in the room (Enter Room or Investigate)").lower()
    else:
        print("Invalid option, please enter one option above: ")

def second_part():
    global jane_second
    global peter_second
    if jane_first == "kitchen".lower():
        print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("||||                                                                                           ||||")
        print("||||     You head down to the kitchen, to find that your house has been broken into            ||||")
        print("||||     You see a car parked outside and decide to follow it. It takes you to a warehouse.    ||||")
        print("||||                                                                                           ||||")
        print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        jane_second = input("You want to follow them into the warehouse but are scared. (Enter Follow or House) : ")
    elif jane_first == "bed".lower():
        print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("||||                                                                                           ||||")
        print("||||  Jane you already decided to head back to the bed without risk comes no reward.           ||||")
        print("||||                                                                                           ||||")
        print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    elif peter_first == "investigate".lower():
        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("||||                                                                                            ||||")
        print("||||   You head to the main floor in the hotel and see everything has been trashed. As you're   ||||")
        print("||||   Looking around you see three people start running outside the hotel entrance.            ||||")
        print("||||                                                                                            ||||")
        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        peter_second = input("What do you want to do to? (Enter Follow or Room)").lower()
    elif peter_first == "room".lower():
        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("||||                                                                                                  ||||")
        print("||||       Peter you already decided to head back to the hotel room!? Without risk comes no reward.   ||||")
        print("||||                                                                                                  ||||")
        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")

def middle_story():
    global jane_third
    global peter_third
    if jane_second == "Follow".lower():
        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("||||                                                                                                          ||||")
        print("||||   You follow the car to the wareshouse. You watch them enter inside and notice that there is a           ||||")
        print("||||   treasure chest in the middle of the floor. 2 men were in the car and now they are sitting next to it.  ||||")
        print("||||                                                                                                          ||||")
        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        jane_third = input("What do you do next? (Enter Distract or Wait) : ").lower()
    elif jane_second == "House".lower():
        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("||||                                                                                                          ||||")
        print("||||  You stay in the house and the car ends up getting away. The cops are two slow to the house and you lose ||||")
        print("||||                                     a lot of valueable items                                             ||||")
        print("||||                                                                                                          ||||")
        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("                                                                                                                  ")
        print("                                                                                                                  ")
        print("                                                                                                                  ")
        print("||||  You have lost your chance at finding treasure and becoming rich! Please try again.  ||||")



def main():
    character_selection()
    beginning()
    second_part()
    middle_story()

main()