import random
from game_data import situations
from game_data import solutions
from game_data import analisis


def main(): 


 current_situation = 'start'

 profile_zen = 0
 profile_angry = 0
 profile_smart = 0
 profile_exp = 0
 profile_obsess = 0

 def dice_throw(per):
        percentage = random.random() * 100
        if percentage <= per:
           return True
        else:
           return False 
        
 def obsession():
     print("added to obsess profile: ",profile_obsess)
     if dice_throw(5):
        current_situation = 'success'
        print(situations[current_situation])
     else:
        current_situation = 'obsess'
        print("Still Nothing...Crap! continu y / n ?")

    
 print("Welcome to the Coding Adventure Game!")
 input("Press <enter> to start...")
 print(" ")
 print("A plausible situational and psychological analisis")
 print("(Based on personal and shared experience)")
 input("<enter>...")
 print(" ")
 print("Please type 'get to work' when you feel ready to start!")
 print("(type 'help' in case you are blocked)")

 while True:
        command = input("-> ").lower()
        if command in solutions[current_situation]:
             current_situation = solutions[current_situation][command]
             print(situations[current_situation])
        elif command == "get to work":
            print(f"{situations[current_situation]}.")
        elif command == "study":
            current_situation = 'study'
            print(situations["study"])
            input("time passes....<enter>")
            input("more time passes...")
            print("Although you feel like you are getting smarter by the minute, dinner time approaches \
and you are still nowhere close to resolving your coding issues...")
            print("")
            print(situations["study2"])
            print("")
        elif command == "obsess":
            current_situation = 'obsess'
            profile_obsess += 2
            print(situations['obsess'])
            input("Aaaaaarrrgh!!! ....")
            obsession()
        elif command == "y":
            profile_obsess += 1
            obsession()
        elif command == "n":
            current_situation = 'abandon'
            print(situations['abandon'])
        elif command == "help":
            print(" ")
            print("Try typing keywords from the text, such as: duck, fridge, stack overflow...")
            print("...'quit' to end the game or 'score' to watch over your psychological profile! ")
        elif command == "quit":
            break
        else:
            print("Say what???")

if __name__ == "__main__":
    main()