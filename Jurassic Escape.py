# allows time in code
import time
# interacts with operating system 
import os
# commands specific functions
import sys

# all the variables used in the code
computer_done = False 
torch_done = False
lights_on = False
gun = False
DNA = False
game_done = False
put_in = False

############### FUNCTIONS FOR EACH OF THE AREAS INCLUDING INTRO ###############

def typewriter(words): # allows type writting effect
    for char in words:
        time.sleep(0.05) # time for letters to apear
        sys.stdout.write(char)
        sys.stdout.flush()






def intro():
    # clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

    #into to game
    typewriter("You wake up alone in a dark room which seems mostly empty.\n\n")
    typewriter("All the lights are turned off and it's hard to see. \n\n")
    typewriter("The only thing you can see are these doors with signs above them. \n\n")
    typewriter("You see three doors listed as... \n\n")

    #list of rooms in the game
    typewriter("   Exit\n\n")
    typewriter("   Security\n\n")
    typewriter("   Kitchen\n\n\n")
    # dialogue
    typewriter("You walk to the Exit and it's locked shut. It needs a key to open. \n\nMaybe the key is found around this place?...\n\n")
    typewriter("ROOOOOOOOAAAAAAAARRRRRR!!!!!!\n\n")
    typewriter("Whatever made that sound was big.\n\n")
    typewriter("You need to get out of this place QUICKLY.\n\n")

    # question
    decision = input("What door do you open? Type:| security | kitchen | >> ") # first of all get the input
    typewriter("\n\n")
    # check if the input is valid
    while decision.lower() != "security" and decision.lower() != "kitchen" and decision.lower() != "theater":
        # repeat the question with a warning
        typewriter("Invalid choice. Please type a valid room:| security | kitchen | >> ")
        typewriter("\n\n")
        decision = input("What door do you open? >> ") 
        typewriter("\n\n")

    # if security said
    if decision.lower() == "security":
        security()
        # goes to security

    # if kitchen said
    if decision.lower() == "kitchen":
        kitchen()
        # goes to kitchen





def main_room():

    # clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # if you haven't fixed lights or got gun
    if lights_on == False:
        # dialogue
        typewriter("You have returned to the original room. \n\n")

        # question
        decision = input("What door do you open? Type:| security | kitchen | >> ") # first of all get the input
        typewriter("\n\n")
        # check if the input is valid
        while decision.lower() != "security" and decision.lower() != "kitchen":
            # repeat the question with a warning
            typewriter("Invalid choice. Please type a valid room: | security | kitchen | >>  ")
            typewriter("\n\n")
            decision = input("What door do you open? >> ") 
            typewriter("\n\n")

        # if security said
        if decision.lower() == "security":
            security()  
            # goes to security

        # if kitchen said
        if decision.lower() == "kitchen":
            kitchen()
            # goes to kitchen

    else:
        # only works if you have fixed the lights only
        if gun == False:
             # clear the screen
            os.system('cls' if os.name == 'nt' else 'clear')

            # dialogue
            typewriter("The lights are on in the main room.\n\n")
            typewriter("You see a key in a box high above the Exit.\n\n")
            typewriter("How can you get that down?.\n\n")

            # question
            decision = input("What door do you open? Type:| security | kitchen | >> ") # first of all get the input
            typewriter("\n\n")
            # check if the input is valid
            while decision.lower() != "security" and decision.lower() != "kitchen":
                # repeat the question with a warning
                typewriter("Invalid choice. Please type a valid room: | security | kitchen | >>  ")
                typewriter("\n\n")
                decision = input("What door do you open? >> ") 
                typewriter("\n\n")

            # if security said
            if decision.lower() == "security":
                security()  
                # goes to security

            # if kitchen said
            if decision.lower() == "kitchen":
                kitchen()
                # goes to kitchen

            # only works if you've got the gun and fixed the lights
        else:
            # dialogue
            typewriter("You see a key in a box high above the Exit.\n\n")
            typewriter("You aim your gun towards it.\n\n")

            # question
            decision = input("What is the compass bearing of the key if it's North of where you are? (type the three digits) >> ") # first of all get the input
            typewriter("\n\n")
            # check if the input is valid
            while decision.lower() != "000" and decision.lower() != "360": 
                # repeat the question with a warning
                typewriter("That's not right, try again >>  ")
                typewriter("\n\n")
                decision = input("What is the bearing? >> ") 
                typewriter("\n\n")
    
            #if answer is right
            if decision.lower() == "000" or "360":
                # dialogue
                typewriter("You aim straight at the bearing of 000°.\n\n")
                typewriter("BANG!\n\n")
                typewriter("The key comes falling down.\n\n")
                typewriter("You catch it and walk towards the Exit.\n\n")
                # wait 3 seconds
                time.sleep(3)
                # goes to exit
                exit()







def security():
    # clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # dialogue
    typewriter("You open the door and take a quick glance around.\n\n")
    typewriter("Around the room you see... computers, a keypad and lastly a torch.\n\n")
   
    
    valid = False
    while valid == False:

        # question
        decision = input("Do you go inside the room or go back out? Type:| inside | out | >> ")
        typewriter("\n\n")
        while decision.lower() != "inside" and decision.lower() != "out" and decision.lower() != "torch":
            # repeat the question with a warning
            typewriter("Invalid choice. Type a valid command:| inside | out | >> ")
            typewriter("\n\n")
            decision = input("What do you want to inspect? >> ")
            typewriter("\n\n")

        # if inside said
        if decision.lower() == "inside":
            valid = True
            
            # question
            decision = input("What do you want to inspect? Type:| computer | pad | torch | >> ")
            typewriter("\n\n")
            while decision.lower() != "computer" and decision.lower() != "pad" and decision.lower() != "torch":
                # repeat the question with a warning
                typewriter("Invalid choice. Type a valid object:| computer | pad | torch | >> ")
                typewriter("\n\n")
                decision = input("What do you want to inspect? >> ") 
                typewriter("\n\n")
            
            # if computer said
            if decision.lower() == "computer":
                computer()
                # goes to computer

            
            # if computer said
            if decision.lower() == "pad":
                pad()
                # goes to pad


            # if computer said
            if decision.lower() == "torch":
                torch()
                # goes to torch
        
        if decision.lower() == "out":
            main_room()
        # repeat the question with a warning



def computer():
    # refers to variables
    global computer_done
    global lights_on
    global put_in

    # clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # only works if you've got the batteries and put it in for the first time
    if computer_done == True and lights_on == False and put_in == False:
            # dialogue
            typewriter("You approach an old computer.\n\n")
            typewriter("You put in the new batteries.\n\n")
            typewriter("ZWOOOOP!\n\n")
            put_in = True
            typewriter("The computer turns on.\n\n")
            typewriter("The password comes up.\n\n")
            typewriter("Not knowing the password you press forgot password.\n\n")
            typewriter("What is more powerful than God, the rich need it, the poor have it and if you eat it you'll die?\n\n")

            # question   
            decision = input("What is the answer to this riddle? >> ")
            typewriter("\n\n")
            if decision.lower() == "nothing":
                # dialogue
                typewriter("You unlock the computer. \n\n")
                typewriter("You see a button that says system reset. \n\n")
                typewriter("You click it and hear the power turn on in the original room. \n\n")
                typewriter("The lights are now on in the main room. \n\n")
                lights_on = True
                # turns on the lights
            
                # question
                decision = input("What do you want to do? Type:| out | inspect | >> ")
                typewriter("\n\n")
                while decision.lower() != "out" and decision.lower() != "inspect":
                    # repeat the question with a warning
                    typewriter("Invalid choice. Type a valid command:| out | inspect | >> ")
                    typewriter("\n\n")
                    decision = input("What do you want to do? >> ")
                    typewriter("\n\n")

                # if said out
                if decision.lower() == "out":
                    main_room()
                    # goes to main_room
            

                 # if said inspect
                if decision.lower() == "inspect":

                    # question
                    decision = input("What do you want to inspect? Type:| computer | pad | torch | >> ")
                    typewriter("\n\n")
                    while decision.lower() != "computer" and decision.lower() != "pad" and decision.lower() != "torch":
                        # repeat the question with a warning
                        typewriter("Invalid choice. Type a valid object:| computer | pad | torch | >> ")
                        typewriter("\n\n")
                        decision = input("What do you want to inspect? >> ")
                        typewriter("\n\n")

                    # if said computer
                    if decision.lower() == "computer":
                        computer()
                        # goes to computer

                    # if said pad
                    if decision.lower() == "pad":
                        pad()
                        # goes to pad

                    # if said torch
                    if decision.lower() == "torch":
                        torch()
                        # goes to torch
            

            else:
                # got riddle wrong
                typewriter("That's not the answer.\n\n")
                typewriter("\n\n")
                # question
                decision = input("What do you want to do? Type:| out | inspect | >> ")
                typewriter("\n\n")
                while decision.lower() != "out" and decision.lower() != "inspect":
                    # repeat the question with a warning
                    typewriter("Invalid choice. Type a valid object:| out | inspect | >> ")
                    typewriter("\n\n")
                    decision = input("What do you want to do? >> ")
                    typewriter("\n\n")


                # if said out
                if decision.lower() == "out":
                    main_room()
                     # goes to main_room

                # if said inspect
                if decision.lower() == "inspect":
                    # question
                    decision = input("What do you want to inspect? Type:| computer | pad | torch | >> ")
                    typewriter("\n\n")            
                    while decision.lower() != "computer" and decision.lower() != "pad" and decision.lower() != "torch":
                        # repeat the question with a warning
                        typewriter("Invalid choice. Type a valid object:| computer | pad | torch | >> ")
                        typewriter("\n\n")
                        decision = input("What do you want to inspect? >> ")
                        typewriter("\n\n")


                    # if said computer
                    if decision.lower() == "computer":
                        computer()
                        # goes to computer
                    
                    
                    # if said pad
                    if decision.lower() == "pad":
                        pad()
                        # goes to pad

                    # if said torch
                    if decision.lower() == "torch":
                        torch()
                        # goes to torch

    # if you have put batteries in before and got riddle wrong
    if computer_done == True and lights_on == False and put_in == True:
        # dialogue
        typewriter("The computer turns on.\n\n")
        typewriter("The password comes up.\n\n")
        typewriter("Not knowing the password you press forgot password.\n\n")
        typewriter("What is more powerful than God, the rich need it, the poor have it and if you eat it you'll die?\n\n")

        # question   
        decision = input("What is the answer to this riddle? >> ")
        typewriter("\n\n")
        if decision.lower() == "nothing":
            # dialogue
            typewriter("You unlock the computer. \n\n")
            typewriter("You see a button that says system reset. \n\n")
            typewriter("You click it and hear the power turn on in the original room. \n\n")
            typewriter("The lights are now on. \n\n")
            lights_on = True
            # turns on the lights

            # question
            decision = input("What do you want to do? Type:| out | inspect | >> ")
            typewriter("\n\n")
            while decision.lower() != "out" and decision.lower() != "inspect":
                # repeat the question with a warning
                typewriter("Invalid choice. Type a valid command:| out | inspect | >> ")
                typewriter("\n\n")
                decision = input("What do you want to do? >> ")
                typewriter("\n\n")

            # if said out
            if decision.lower() == "out":
                main_room()
                # goes to main_room
        

                # if said inspect
            if decision.lower() == "inspect":

                # question
                decision = input("What do you want to inspect? Type:| computer | pad | torch | >> ")
                typewriter("\n\n")
                while decision.lower() != "computer" and decision.lower() != "pad" and decision.lower() != "torch":
                    # repeat the question with a warning
                    typewriter("Invalid choice. Type a valid object:| computer | pad | torch | >> ")
                    typewriter("\n\n")
                    decision = input("What do you want to inspect? >> ")
                    typewriter("\n\n")

                # if said computer
                if decision.lower() == "computer":
                    computer()
                    # goes to computer

                # if said pad
                if decision.lower() == "pad":
                    pad()
                    # goes to pad

                # if said torch
                if decision.lower() == "torch":
                    torch()
                    # goes to torch
        

        else:
            # got riddle wrong
            typewriter("That's not the answer.\n\n")
            typewriter("\n\n")
            # question
            decision = input("What do you want to do? Type:| out | inspect | >> ")
            typewriter("\n\n")
            while decision.lower() != "out" and decision.lower() != "inspect":
                # repeat the question with a warning
                typewriter("Invalid choice. Type a valid object:| out | inspect | >> ")
                typewriter("\n\n")
                decision = input("What do you want to do? >> ")
                typewriter("\n\n")


            # if said out
            if decision.lower() == "out":
                main_room()
                    # goes to main_room

            # if said inspect
            if decision.lower() == "inspect":
                # question
                decision = input("What do you want to inspect? Type:| computer | pad | torch | >> ")
                typewriter("\n\n")            
                while decision.lower() != "computer" and decision.lower() != "pad" and decision.lower() != "torch":
                    # repeat the question with a warning
                    typewriter("Invalid choice. Type a valid object:| computer | pad | torch | >> ")
                    typewriter("\n\n")
                    decision = input("What do you want to inspect? >> ")
                    typewriter("\n\n")


                # if said computer
                if decision.lower() == "computer":
                    computer()
                    # goes to computer
                
                
                # if said pad
                if decision.lower() == "pad":
                    pad()
                    # goes to pad

                # if said torch
                if decision.lower() == "torch":
                    torch()
                    # goes to torch






    # if you don't have batteries
    if computer_done == False:
        # dialogue
        typewriter("You approach an old computer.\n\n")
        typewriter("You try hitting the start button but nothing turns on.\n\n")
        typewriter("Maybe it needs new batteries.\n\n")

        # question
        decision = input("What do you want to do? Type:| out | inspect | >> ")
        typewriter("\n\n")
        while decision.lower() != "out" and decision.lower() != "inspect":
            # repeat the question with a warning
            typewriter("Invalid choice. Type a valid command:| out | inspect | >> ")
            typewriter("\n\n")
            decision = input("What do you want to do? >> ")
            typewriter("\n\n")

        # if said out
        if decision.lower() == "out":
                main_room()
                # goes to main_room
            
            
        # if said inspect
        if decision.lower() == "inspect":
            # question
            decision = input("What do you want to inspect? Type:| computer | pad | torch | >> ")
            typewriter("\n\n")
            while decision.lower() != "computer" and decision.lower() != "pad" and decision.lower() != "torch":
                # repeat the question with a warning
                typewriter("Invalid choice. Type a valid object:| computer | pad | torch | >> ")
                typewriter("\n\n")
                decision = input("What do you want to inspect? >> ")
                typewriter("\n\n")

            # if said computer
            if decision.lower() == "computer":
                computer()
                # goes to computer
            
            # if said pad
            if decision.lower() == "pad":
                pad()
                # goes to pad

            # if said torch
            if decision.lower() == "torch":
                torch()
                # goes to torch

    # if you have already put the lights on
    if computer_done == True and lights_on == True:
        typewriter("You approach an old computer.\n\n")
        typewriter("You've already turned the power back on.\n\n")
        # question
        decision = input("What do you want to do? Type:| out | inspect | >> ")
        typewriter("\n\n")
        while decision.lower() != "out" and decision.lower() != "inspect":
            # repeat the question with a warning
            typewriter("Invalid choice. Type a valid command:| out | inspect | >> ")
            typewriter("\n\n")
            decision = input("What do you want to do? >> ")
            typewriter("\n\n")

        # if said out
        if decision.lower() == "out":
            main_room()
            # goes to main_room

        # if said inspect
        if decision.lower() == "inspect":
            # question
            decision = input("What do you want to inspect? Type:| computer | pad | torch | >> ")
            typewriter("\n\n")
            while decision.lower() != "computer" and decision.lower() != "pad" and decision.lower() != "torch":
                # repeat the question with a warning
                typewriter("Invalid choice. Type a valid object:| computer | pad | torch | >> ")
                typewriter("\n\n")
                decision = input("What do you want to inspect? >> ")
                typewriter("\n\n")

            # if said computer
            if decision.lower() == "computer":
                computer()
                # goes to computer
            
            # if said pad
            if decision.lower() == "pad":
                pad()
                # goes to pad

            # if said torch
            if decision.lower() == "torch":
                torch()
                # goes to torch


def pad():
    # refers to variables
    global gun
    global DNA
    # clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # dialogue
    typewriter("You approach a key pad. \n\n")
    typewriter("On this pad are numbers from 0 - 9. \n\n")
    typewriter("It needs a 4 digit passcode. \n\n")

    # question
    decision = input("What is the passcode? >> ")
    typewriter("\n\n")
    
                
    # if said correct password which is 4382
    if decision.lower() == "4382":
        # clear the screen
        os.system('cls' if os.name == 'nt' else 'clear')

        # only works if this is the first time the DNA puzzle has been solved
        if DNA == False:
            # dialogue
            typewriter("Creeeeeek!\n\n")
            typewriter("A door opens in security. \n\n")
            typewriter("You walk inside and take a glance at a sign that says... DNA extraction room.\n\n")
            typewriter("You see a container with muddled Velociraptor DNA.\n\n")
            typewriter("Maybe if you sequence it you'll be rewarded?\n\n")
            typewriter("DNA sequencing is determined by the order of the nucleotides.\n\n")
            typewriter("In other words, it's about decoding the DNA strand.\n\n")
            typewriter("A pairs with T \n\n")
            typewriter("C pairs with G \n\n")
            typewriter("Decode it by using the key above.\n\n")
            typewriter("AATCATCGGTCAGTT \n\n")

            # question
            decision = input("What are the nucleotides in this DNA sequnce? >> ")
            typewriter("\n\n")            
            while decision.lower() != "ttagtagccagtcaa":
                    # repeat the question with a warning
                    typewriter("That's wrong try again >> ")
                    typewriter("\n\n")
                    decision = input("What are the nucleotides in this DNA sequnce? >> ")

            #if said correct anwser of DNA sequencing
            if decision.lower() == "ttagtagccagtcaa":
                # clear the screen
                os.system('cls' if os.name == 'nt' else 'clear')

            
                # dialogue
                typewriter("You hear a little click!\n\n")
                typewriter("You see a gun in the corner.\n\n")
                typewriter("It only has one bullet.\n\n")
                typewriter("You put it in your pocket.\n\n")
                typewriter("You walk back to security.\n\n")
                typewriter("The DNA door closes behind you.\n\n")
                #timer for 4 seconds
                time.sleep(4)
                gun = True
                # gain the gun
                DNA = True
                security()
                # goes to security

            # only works if you have already done the DNA puzzle    
        if DNA == True:    
            # dialogue
            typewriter("Creeeeeek!\n\n")
            typewriter("A door opens in security. \n\n")
            typewriter("You walk inside and take a glance at a sign that says... DNA extraction room.\n\n")
            typewriter("There's nothing left to do in this room.\n\n")
            typewriter("You pull out your gun from earlier.\n\n")
            typewriter("It only has one bullet.\n\n")
            typewriter("You put it back in your pocket.\n\n")
            typewriter("You walk back to security.\n\n")
            typewriter("The DNA door closes behind you.\n\n")
            #timer for 4 seconds
            time.sleep(4)
            security()
            # goes to security
            


            

    else:
        # dialogue
        typewriter("That's the wrong passcode.")
        typewriter("\n\n")
        # question
        decision = input("What do you want to do? Type:| out | inspect | >> ")
        typewriter("\n\n")
        while decision.lower() != "out" and decision.lower() != "inspect":
            # repeat the question with a warning
            typewriter("Invalid choice. Type a valid command:| out | inspect | >> ")
            typewriter("\n\n")
            decision = input("What do you want to do? >> ")
            typewriter("\n\n")

        # if said out
        if decision.lower() == "out":
                main_room()
                #goes to main_room

        # if said inspect
        if decision.lower() == "inspect":
            # question
            decision = input("What do you want to inspect? Type:| computer | pad | torch | >> ")
            typewriter("\n\n")            
            while decision.lower() != "computer" and decision.lower() != "pad" and decision.lower() != "torch":
                # repeat the question with a warning
                typewriter("Invalid choice. Type a valid object:| computer | pad | torch | >> ")
                typewriter("\n\n")
                decision = input("What do you want to inspect? >> ")
                typewriter("\n\n")

            # if said computer
            if decision.lower() == "computer":
                computer()
                # goes to computer
            
            # if said pad 
            if decision.lower() == "pad":
                pad()
                #goes to pad

            # if said torch
            if decision.lower() == "torch":
                torch()
                # goes to torch
        

def torch():
    # refers to variables
    global torch_done
    # clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # only works if you don't have torch
    if torch_done == False:
        # dialogue
        typewriter("You approach the torch.\n\n")
        typewriter("Maybe it could be used to light up a small dark area?\n\n")
        typewriter("You put the torch in your pocket.\n\n")
        # collect the torch for fridge
        torch_done = True

        # question
        decision = input("What do you want to do? Type:| out | inspect | >> ")
        typewriter("\n\n")
        while decision.lower() != "out" and decision.lower() != "inspect":
            # repeat the question with a warning
            typewriter("Invalid choice. Type a valid command:| out | inspect | >> ")
            typewriter("\n\n")
            decision = input("What do you want to do? >> ")
            typewriter("\n\n")

        # if said out
        if decision.lower() == "out":
            main_room()
            # goes to main_room

        # if said inspect
        if decision.lower() == "inspect":
            # question
            decision = input("What do you want to inspect? Type:| computer | pad | torch | >> ")
            typewriter("\n\n")
            while decision.lower() != "computer" and decision.lower() != "pad" and decision.lower() != "torch":
                # repeat the question with a warning
                typewriter("Invalid choice. Type a valid object:| computer | pad | torch | >> ")
                typewriter("\n\n")
                decision = input("What do you want to inspect? >> ")
                typewriter("\n\n")

            # if said computer
            if decision.lower() == "computer":
                computer()
                # goes to computer
                    
                    
            # if said pad
            if decision.lower() == "pad":
                pad()
                # goes to pad


            if decision.lower() == "torch":
                torch()
                # goes to torch

    # if you have already picked up the torch    
    if torch_done == True:
        typewriter("You pull out the torch from your pocket.\n\n")
        typewriter("Maybe it could be used to light up a small dark area?\n\n")
        typewriter("You put the torch back in your pocket.\n\n")

        # question
        decision = input("What do you want to do? Type:| out | inspect | >> ")
        typewriter("\n\n")
        while decision.lower() != "out" and decision.lower() != "inspect":
            # repeat the question with a warning
            typewriter("Invalid choice. Type a valid command:| out | inspect | >> ")
            typewriter("\n\n")
            decision = input("What do you want to do? >> ")
            typewriter("\n\n")


            # if said out
        if decision.lower() == "out":
            main_room()
            # goes to main_room

        # if said inspect
        if decision.lower() == "inspect":
            # question
            decision = input("What do you want to inspect? Type:| computer | pad | torch | >> ")
            typewriter("\n\n")
            while decision.lower() != "computer" and decision.lower() != "pad" and decision.lower() != "torch":
                # repeat the question with a warning
                typewriter("Invalid choice. Type a valid object:| computer | pad | torch | >> ")
                typewriter("\n\n")
                decision = input("What do you want to inspect? >> ")
                typewriter("\n\n")


            # if said computer
            if decision.lower() == "computer":
                computer()
                # goes to computer
                    
                    
            # if said pad
            if decision.lower() == "pad":
                pad()
                # goes to pad


            if decision.lower() == "torch":
                torch()
                # goes to torch






def kitchen():
    global torch_done
    # clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # dialogue
    typewriter("You open the door and take a quick glance around.\n\n")
    typewriter("Around the room you see... a fridge and three draws.\n\n")

    valid = False
    while valid == False:

        # question
        decision = input("Do you go inside the room or go back out? Type:| inside | out | >> ")
        typewriter("\n\n")
        while decision.lower() != "inside" and decision.lower() != "out" and decision.lower() != "torch":
            # repeat the question with a warning
            typewriter("Invalid choice. Type a valid command:| inside | out | >> ")
            typewriter("\n\n")
            decision = input("What do you want to inspect? >> ")
            typewriter("\n\n")

        # if said inside
        if decision.lower() == "inside":
            valid = True
            # question
            decision = input("What do you want to inspect? Type: | fridge | draws | >> ")
            typewriter("\n\n")
            while decision.lower() != "fridge" and decision.lower() != "draws":
                # repeat the question with a warning
                typewriter("Invalid choice. Please type a valid object: | fridge | draws | >> ")
                typewriter("\n\n")
                decision = input("What do you want to inspect? >> ")
                typewriter("\n\n")

            # if said fridge
            if decision.lower() == "fridge":
                fridge()
                # goes to fridge

            #if said draws
            if decision.lower() == "draws":
                draws()
                # goes to draws

        if decision.lower() == "inside":
            main_room()
            # goes to main_room



def fridge():
    # refers to variables
    global torch_done
    global computer_done
    # clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # only works if you've got the batteries already 
    if torch_done == True and computer_done == True:
        typewriter("You approach the fridge.\n\n")
        typewriter("You open it and cold air comes flowing through the air.\n\n")
        typewriter("The lights are off though and you're unable to see anything inside it.\n\n")
        typewriter("You bring out your torch from your pocket and turn it on.\n\n")
        typewriter("The fridge is empty.\n\n")

        decision = input("What do you want to do? Type:| out | inspect | >> ")
        typewriter("\n\n")
        while decision.lower() != "out" and decision.lower() != "inspect":
            # repeat the question with a warning
            typewriter("Invalid choice. Type a valid object:| out | inspect | >> ")
            typewriter("\n\n")
            decision = input("What do you want to do? >> ")
            typewriter("\n\n")

        # if said out
        if decision.lower() == "out":
            main_room()
            # goes to main_room

        # if said inspect
        if decision.lower() == "inspect":
            # question
            decision = input("What do you want to inspect? Type:| fridge | draws | >> ")
            typewriter("\n\n")
            while decision.lower() != "fridge" and decision.lower() != "draws":
                    # repeat the question with a warning
                    typewriter("Invalid choice. Type a valid object:| fridge | draws | >> ")
                    typewriter("\n\n")
                    decision = input("What do you want to inspect? >> ")
                    typewriter("\n\n")

            # if said fridge
            if decision.lower() == "fridge":
                fridge()
                # goes to fridge
            
            
            # if said draws
            if decision.lower() == "draws":
                draws()
                # goes to draws



    # only works if you have torch
    if torch_done == True and computer_done == False:
        # dialogue
        typewriter("You approach the fridge.\n\n")
        typewriter("You open it and cold air comes flowing through the air.\n\n")
        typewriter("The lights are off though and you're unable to see anything inside it.\n\n")
        typewriter("You bring out your torch from your pocket and turn it on.\n\n")
        typewriter("You see batteries inside the fridge.\n\n")
        typewriter("You put them in your pocket.\n\n")
        computer_done = True
        # gain batteries for computer

        # question
        decision = input("What do you want to do? Type:| out | inspect | >> ")
        typewriter("\n\n")
        while decision.lower() != "out" and decision.lower() != "inspect":
            # repeat the question with a warning
            typewriter("Invalid choice. Type a valid object:| out | inspect | >> ")
            typewriter("\n\n")
            decision = input("What do you want to do? >> ")
            typewriter("\n\n")

        # if said out
        if decision.lower() == "out":
            main_room()
            # goes to main_room

        # if said inspect
        if decision.lower() == "inspect":
            # question
            decision = input("What do you want to inspect? Type:| fridge | draws | >> ")
            typewriter("\n\n")
            while decision.lower() != "fridge" and decision.lower() != "draws":
                    # repeat the question with a warning
                    typewriter("Invalid choice. Type a valid object:| fridge | draws | >> ")
                    typewriter("\n\n")
                    decision = input("What do you want to inspect? >> ")
                    typewriter("\n\n")

            # if said fridge
            if decision.lower() == "fridge":
                fridge()
                # goes to fridge
            
            
            # if said draws
            if decision.lower() == "draws":
                draws()
                # goes to draws

    
    if torch_done == True and computer_done == False:
        pass

        


    # if you don't have the torch
    if torch_done == False:
        # dialogue
        typewriter("You approach the fridge.\n\n")
        typewriter("You open it and cold air comes flowing through the air.\n\n")
        typewriter("The lights are off though and you're unable to see anything inside it.\n\n")
        typewriter("Maybe if you had a light source you'd be able to see what's inside?\n\n")

        # question
        decision = input("What do you want to do? Type:| out | inspect | >> ")
        typewriter("\n\n")
        while decision.lower() != "out" and decision.lower() != "inspect":
            # repeat the question with a warning
            typewriter("Invalid choice. Type a valid command:| out | inspect | >> ")
            typewriter("\n\n")
            decision = input("What do you want to do? >> ")
            typewriter("\n\n")

        # if said out
        if decision.lower() == "out":
            main_room()
            # goes to main_room

        # if said inspect
        if decision.lower() == "inspect":
            # question
            decision = input("What do you want to inspect? Type:| fridge | draws | >> ")
            typewriter("\n\n")
            while decision.lower() != "fridge" and decision.lower() != "draws":
                # repeat the question with a warning
                typewriter("Invalid choice. Type a valid object:| fridge | draws | >> ")
                typewriter("\n\n")
                decision = input("What do you want to inspect? >> ")
                typewriter("\n\n")

            # if said fridge
            if decision.lower() == "fridge":
                fridge()
                # goes to fridge
            
            
            # if said draws
            if decision.lower() == "draws":
                draws()
                # goes to draws


def draws():
    # clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # dialogue
    typewriter("You approach the draws.\n\n")

    # question
    decision = input("What draw do you want to open? Type:| one | two | three | >> ")
    typewriter("\n\n")
    while decision.lower() != "one" and decision.lower() != "two" and decision.lower() != "three":
        # repeat the question with a warning
        typewriter("Invalid choice. Type a valid draw:| one | two | three | >> ")
        typewriter("\n\n")
        decision = input(" What draw do you want to open? >> ")
        typewriter("\n\n")

    # if said one
    if decision.lower() == "one":
            draw_one()
            # goes to draw_one
            
    # if said two        
    if decision.lower() == "two":
            draw_two()
            # goes to draw_two
            
    # if said three
    if decision.lower() == "three":
            draw_three()
            # goes to draw_three

def draw_one():
    # clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # you said this to me on DOE camp
    typewriter("You open draw one and you see a note from Andrew Fong from Duke of Ed Camp.\n\n")
    typewriter("\"You are my least favorite student Nathan.\" \n\n")

    # question
    decision = input("Do you want to open another draw?:| yes | no | >> ")
    typewriter("\n\n")
    while decision.lower() != "yes" and decision.lower() != "no":
        # repeat the question with a warning
        typewriter("Invalid choice. Type a valid command:| yes | no | >> ")
        typewriter("\n\n")
        decision = input("Do you want to open another draw? >> ")
        typewriter("\n\n")

    # if said no
    if decision.lower() == "no":
        # question
        decision = input("What do you want to do? Type:| out | inspect | >> ")
        typewriter("\n\n")
        while decision.lower() != "out" and decision.lower() != "inspect":
            # repeat the question with a warning
            typewriter("Invalid choice. Type a valid command:| out | inspect | >> ")
            typewriter("\n\n")
            decision = input("What do you want to do? >> ")
            typewriter("\n\n")

        # if said out
        if decision.lower() == "out":
            main_room()
            # goes to main_room

        if decision.lower() == "inspect":
            # question
            decision = input("What do you want to inspect? Type:| fridge | draws | >> ")
            typewriter("\n\n")
            while decision.lower() != "fridge" and decision.lower() != "draws":
                    # repeat the question with a warning
                    typewriter("Invalid choice. Type a valid object:| fridge | draws | >> ")
                    typewriter("\n\n")
                    decision = input("What do you want to inspect? >> ")
                    typewriter("\n\n")

            # if said fridge
            if decision.lower() == "fridge":
                fridge()
                # goes to fridge
            
            # if said draws
            if decision.lower() == "draws":
                draws()
                # goes to draws


            
            
    # if said yes
    if decision.lower() == "yes":
            # question
            decision = input("What draw do you want to open? Type:| two | three | >> ")
            typewriter("\n\n")
            while decision.lower() != "two" and decision.lower() != "three":
                    # repeat the question with a warning
                    typewriter("Invalid choice. Type a valid draw:| two | three | >> ")
                    typewriter("\n\n")
                    decision = input("What draw do you want to open? >> ")
                    typewriter("\n\n")

            # if said two
            if decision.lower() == "two":
                draw_two()
                # goes to draw_two
            
            
            # if said three
            if decision.lower() == "three":
                draw_three() 
                # goes to draw three

def draw_two():
    # clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

    typewriter("You open draw two.\n\n")
    # it's a red herring
    typewriter("You see a painting of a red herring in the draw.\n\n")

    # question
    decision = input("Do you want to open another draw?:| yes | no | >> ")
    typewriter("\n\n")
    while decision.lower() != "yes" and decision.lower() != "no":
        # repeat the question with a warning
        typewriter("Invalid choice. Type a valid command:| yes | no | >> ")
        typewriter("\n\n")
        decision = input("Do you want to open another draw? >> ")
        typewriter("\n\n")

    # if said no
    if decision.lower() == "no":
        # question
        decision = input("What do you want to do? Type:| out | inspect | >> ")
        typewriter("\n\n")
        while decision.lower() != "out" and decision.lower() != "inspect":
            # repeat the question with a warning
            typewriter("Invalid choice. Type a valid command:| out | inspect | >> ")
            typewriter("\n\n")
            decision = input("What do you want to do? >> ")
            typewriter("\n\n")

        if decision.lower() == "out":
            main_room()

        # if said inspect
        if decision.lower() == "inspect":
            # question
            decision = input("What do you want to inspect? Type:| fridge | draws | >> ")
            typewriter("\n\n")
            while decision.lower() != "fridge" and decision.lower() != "draws":
                    # repeat the question with a warning
                    typewriter("Invalid choice. Type a valid object:| fridge | draws | >> ")
                    typewriter("\n\n")
                    decision = input("What do you want to inspect? >> ")
                    typewriter("\n\n")

            # if said fridge
            if decision.lower() == "fridge":
                fridge()
                # goes to fridge
            
            
            # if said draws
            if decision.lower() == "draws":
                draws()
                # goes to draws

    # if said yes
    if decision.lower() == "yes":
            # question
            decision = input("What draw do you want to open? Type:| one | three | >> ")
            typewriter("\n\n")
            while decision.lower() != "one" and decision.lower() != "three":
                    # repeat the question with a warning
                    typewriter("Invalid choice. Type a valid draw:| one | three | >> ")
                    typewriter("\n\n")
                    decision = input("What draw do you want to open? >> ")
                    typewriter("\n\n")

            # if said one
            if decision.lower() == "one":
                draw_one()
                # goes to draw_one
            
            
            # said three
            if decision.lower() == "three":
                draw_three() 
                # goes to draw_three

def draw_three():
    # clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # shows code for the pad
    typewriter("You open draw three.\n\n")
    typewriter("You see a posted note that has the following numbers.\n\n")
    typewriter(" 4 \n\n")
    typewriter(" 3 \n\n")
    typewriter(" 8 \n\n")
    typewriter(" 2 \n\n")

    # question
    decision = input("Do you want to open another draw?:| yes | no | >> ")
    typewriter("\n\n")
    while decision.lower() != "yes" and decision.lower() != "no":
        # repeat the question with a warning
        typewriter("Invalid choice. Type a valid command:| yes | no | >> ")
        typewriter("\n\n")
        decision = input("Do you want to open another draw? >> ")
        typewriter("\n\n")

    # if said no
    if decision.lower() == "no":
        # question
        decision = input("What do you want to do? Type:| out | inspect | >> ")
        typewriter("\n\n")
        while decision.lower() != "out" and decision.lower() != "inspect":
            # repeat the question with a warning
            typewriter("Invalid choice. Type a valid command:| out | inspect | >> ")
            typewriter("\n\n")
            decision = input("What do you want to do? >> ")
            typewriter("\n\n")

        #if said out
        if decision.lower() == "out":
            main_room()

        # if said inspect
        if decision.lower() == "inspect":
            # question
            decision = input("What do you want to inspect? Type:| fridge | draws | >> ")
            typewriter("\n\n")
            while decision.lower() != "fridge" and decision.lower() != "draws":
                    # repeat the question with a warning
                    typewriter("Invalid choice. Type a valid object:| fridge | draws | >> ")
                    typewriter("\n\n")
                    decision = input("What do you want to inspect? >> ")
                    typewriter("\n\n")

            # if said fridge
            if decision.lower() == "fridge":
                fridge()
                # goes to fridge
            
            
            # if said draws
            if decision.lower() == "draws":
                draws()
                # goes to draws

    # if said yes       
    if decision.lower() == "yes":
            # question
            decision = input("What draw do you want to open? Type:| one | two | >> ")
            typewriter("\n\n")
            while decision.lower() != "one" and decision.lower() != "two":
                    # repeat the question with a warning
                    typewriter("Invalid choice. Type a valid draw:| one | two | >> ")
                    typewriter("\n\n")
                    decision = input("What draw do you want to open? >> ")
                    typewriter("\n\n")

            # if said one
            if decision.lower() == "one":
                draw_one()
                # goes to draw_one
            

            # if said two
            if decision.lower() == "two":
                draw_two() 
                # goes to draw_two





def exit():
    global game_done
    # clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # dialogue
    typewriter("You unlock the door and walk out.\n\n")
    typewriter("You see an abundance of trees.\n\n")
    typewriter("ROOOAAAAAAARRRRRR!\n\n")
    typewriter("You see none other than a giant Tyrannosaurus Rex!\n\n")
    typewriter("In the distance you see a helicopter.\n\n")
    typewriter("You run towards it as the beast chases you.\n\n")
    typewriter("One thought, however, remains in your head that you can't stop thinking about.\n\n")

    # question
    decision = input("What was the name of the dinosaur that you DNA sequenced ealier? >> ") # first of all get the input
    typewriter("\n\n")
    
    # if said velociraptor
    if decision.lower() == "velociraptor":
        # dialogue
        typewriter("You were able to snap out of it and continued sprinting.\n\n")
        typewriter("You open the door to the helicopter and fly away as the T-Rex stares with daggers.\n\n")
        # clear the screen
        os.system('cls' if os.name == 'nt' else 'clear')
        # dialogue
        typewriter("CONGRATULATIONS YOU WON JURASSIC ESCAPE!!!!!!!!! 👏👏👏\n\n")
        # end game
        sys.exit()

        


            
    else:
        # clear the screen
        os.system('cls' if os.name == 'nt' else 'clear')

        # dialogue
        typewriter("You overthink this stupid question and the T-Rex catches up and swallows you with one bite.\n\n")
        typewriter("You must now start from the very start of this escape room.\n\n")
        typewriter("I'm just kidding that would be too cruel.\n\n")
        typewriter("You restart from the exit.\n\n")
        # wait 3 seconds
        time.sleep(3)
        # goes to exit
        exit()
        



################# MAIN PROGRAM WHICH EXECUTES EACH FUNCTION ####################

# clear the screen
os.system('cls' if os.name == 'nt' else 'clear')
# informs player to open terminal
typewriter("Please open the terminal as much as you can. \n\n")
# question
decision = input("Are you ready to begin Jurassic Escape? Type:| ready | >> ") # first of all get the input
typewriter("\n\n")
# check if the input is valid
while decision.lower() != "ready":
    # repeat the question with a warning
    typewriter("Invalid choice.\n\n")
    decision = input("Are you ready to begin Jurassic Escape? Type:| ready | >> ") 

# if read said
if decision.lower() == "ready":
    intro() # run the introduction to the game