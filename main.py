# allows time in code
import time
# interacts with operating system 
import os
# commands specific functions
import sys

import random

from earth import questions

score = 0
question_number = 0
question_amount = 0
number = 0
wrong_answers = []


def typewriter(words): # allows type writting effect
    for char in words:
        time.sleep(0.05) # time for letters to apear
        sys.stdout.write(char)
        sys.stdout.flush()

def earth_questions(questions):
    global score
    global question_number
    global question_amount
    global number
    global wrong_answers

    os.system('cls' if os.name == 'nt' else 'clear')
    random.shuffle(questions)

    decision = input("What lenth of quiz are you wanting to do? Type: | short | medium | long | ") # first of all get the input
    print("\n\n")
    # check if the input is valid
    while decision.lower() != ("short") and decision.lower() != ("medium") and decision.lower() != ("long"):
     # repeat the question with a warning
        typewriter("Invalid choice. Please type a valid length ")
        print("\n\n")
        decision = input("What lenth of quiz are you wanting to do? Type: | short | medium | long | ") 
        print("\n\n")
 
    if decision.lower() == "short":
        question_amount = 5
    elif decision.lower() == "medium":
        question_amount = 10
    elif decision.lower() == "long":
        question_amount = 15
    
    while number < question_amount:
        question = questions[number]  # Select the question based on the current number
        typewriter(question["Question"])
        print("\n")
        for option in question["Options"]:
            typewriter(option)

        answer = input("What do you choose? ")
        while answer.lower() != "a" and answer.lower() != "b" and answer.lower() != "c" and answer.lower() != "d":
            typewriter("Invalid anwser. Please type a valid option ")
            print("\n\n")
            answer = input("What do you choose? ")

        if answer.lower() == question["Answer"]:
            typewriter("That is...\n")
            time.sleep(1.5)
            typewriter("CORRECT! \n")
            typewriter(question["Explanation"])
            question_number = question_number + 1
            score = score + 1
            print("\n")
            typewriter("Your current score is {}/{}\n".format(score, question_number))
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            number = number + 1

        else:
            typewriter("That is...\n")
            time.sleep(1.5)
            typewriter("INCORRECT! \n")
            typewriter(question["Explanation"])
            question_number = question_number + 1
            wrong_answers.append(question)
            print("\n")
            typewriter("Your current score is {}/{}\n".format(score, question_number))
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            number = number + 1

    percentage = score / question_amount * 100

    typewriter("You got {:.2f}% on this test.".format(percentage))
    typewriter("Your rank is...")
    time.sleep(3)
    if percentage <= 20:
        typewriter("Talc!")
        time.sleep(1.5)
        typewriter("You crumble under the slightest pressure. A mere touch can wear you down, ")
        typewriter("and even a fingernail is too much for you. You’re soft, flaky, and honestly,")
        typewriter("no one’s picking you first for the team. But hey, at least you're useful in baby powder. ")
        
    elif percentage <= 40:
        typewriter("Gypsum!")
        time.sleep(1.5)
        typewriter("You try, but you're still easily scratched, a simple copper coin can still leave a mark on you.")
        typewriter("At least you're useful in drywall and plaster, holding houses together.")
        typewriter("Just don’t expect to be the foundation.")
        

    elif percentage <= 60:
        typewriter("Apatite!")
        time.sleep(1.5)
        typewriter("You’re no pushover, but you’re not indestructible either. Harder than your weaker cousins, ")
        typewriter("you’re tough enough to resist everyday wear but still won’t last against the real heavyweights.") 
        typewriter("You help build bones and teeth, so at least you're part of the reason people can actually chew their food.")


    elif percentage <= 80:
        typewriter("Quartz!")
        time.sleep(1.5)
        typewriter("You’re tough, durable, and versatile. You make up sand, glass, and even tech components.")
        typewriter("You might not be the hardest, but people rely on you for watches, buildings, and even some beautiful gemstones.")
        typewriter("You’ve earned your place.")


    else:
        typewriter("Diamond!")
        time.sleep(1.5)
        typewriter("You’ve been under immense pressure, and instead of breaking, ")
        typewriter("you became the toughest mineral on Earth.")
        typewriter("No one scratches you, and you shine bright, whether in industry or in luxury. ")
        typewriter("You’re the ultimate performer, proving that pressure makes diamonds!")

    ###

    if wrong_answers:
        typewriter("\nYou got the following questions wrong:")
        print("\n")
        for wrong in wrong_answers:
            typewriter(wrong["Question"])
            print("\n")
            typewriter("Answer: {}\n".format(wrong["Explanation"]))
    else:
        typewriter("\nYou got all the questions right!")

    decision = input("Would you like to try the test again? Type: | yes | no | ")
    print("\n\n")
    while decision.lower() != "yes" and decision.lower() != "no":
        typewriter("Invalid choice. Please type a valid option ")
        print("\n\n")
        decision = input("Would you like to try the test again? Type: | yes | no | ")
    
    if decision.lower() == "yes":
        os.system('cls' if os.name == 'nt' else 'clear')
        chemistry_questions(questions)

    if decision.lower() == "no":
        decision = input("Would you like to try a different quiz or exit? Type: | quiz | exit | ")  
        print("\n\n")
        while decision.lower() != "quiz" and decision.lower() != "exit":
            typewriter("Invalid choice. Please type a valid option ")
            print("\n\n")
            decision = input("Would you like to try a different quiz or exit? Type: | quiz | exit | ")
        

        if decision.lower() == "quiz":
            decision = input("What science quiz are you wanting to try? Type: | earth | chemistry | biology | ")
            print("\n\n")
            while decision.lower() != "earth" and decision.lower() != "chemistry" and decision.lower() != "biology":
                typewriter("Invalid choice. Please type a valid topic ")
                print("\n\n")
                decision = input("What science quiz are you wanting to try? Type: | earth | chemistry | biology | ")
            
            if decision.lower() == "earth":
                earth_questions(questions)

            elif decision.lower() == "chemistry":
                chemistry_questions(questions)
            
            elif decision.lower() == "biology":
                biology_questions(questions)

        if decision.lower() == "exit":
            ending()

def chemistry_questions(questions):
    global score
    global question_number
    global question_amount
    global number
    global wrong_answers

    os.system('cls' if os.name == 'nt' else 'clear')
    random.shuffle(questions)

    decision = input("What lenth of quiz are you wanting to do? Type: | short | medium | long | ") # first of all get the input
    typewriter("\n\n")
    # check if the input is valid
    while decision.lower() != ("short") and decision.lower() != ("medium") and decision.lower() != ("long"):
     # repeat the question with a warning
        typewriter("Invalid choice. Please type a valid length ")
        print("\n\n")
        decision = input("What lenth of quiz are you wanting to do? Type: | short | medium | long | ") 
        print("\n\n")
 
    if decision.lower() == "short":
        question_amount = 5
    elif decision.lower() == "medium":
        question_amount = 10
    elif decision.lower() == "long":
        question_amount = 15
    
    while number < question_amount:
        question = questions[number]  # Select the question based on the current number
        typewriter(question["Question"])
        print("\n")
        for option in question["Options"]:
            typewriter(option)

        answer = input("What do you choose? ")
        while answer.lower() != "a" and answer.lower() != "b" and answer.lower() != "c" and answer.lower() != "d":
            typewriter("Invalid anwser. Please type a valid option ")
            print("\n\n")
            answer = input("What do you choose? ")

        if answer.lower() == question["Answer"]:
            typewriter("That is...\n")
            time.sleep(1.5)
            typewriter("CORRECT!\n")
            typewriter(question["Explanation"])
            question_number = question_number + 1
            score = score + 1
            print("\n")
            typewriter("Your current score is {}/{}\n".format(score, question_number))
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            number = number + 1

        else:
            typewriter("That is...\n")
            time.sleep(1.5)
            typewriter("INCORRECT!\n")
            typewriter(question["Explanation"])
            question_number = question_number + 1
            wrong_answers.append(question)
            print("\n")
            typewriter("Your current score is {}/{}\n".format(score, question_number))
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            number = number + 1

    percentage = score / question_amount * 100

    typewriter("You got {:.2f}% on this test.".format(percentage))
    typewriter("Your rank is...")
    time.sleep(3)
    if percentage <= 20:
        typewriter("Francium!")
        time.sleep(1.5)
        typewriter("You barely exist before breaking down! The most unstable of the alkali metals,")
        typewriter("you’re radioactive, extremely rare, and decay in seconds.")
        typewriter("No one can even study you properly before you disappear.")


    elif percentage <= 40:
        typewriter("Lithium!")
        time.sleep(1.5)
        typewriter("You’re soft, reactive, and float on water.")
        typewriter("You might not be the toughest, but you're crucial in batteries, keeping the world’s tech running.")

    elif percentage <= 60:
        typewriter("Iron!")
        time.sleep(1.5)
        typewriter("You’re strong, magnetic, and essential for life without you, blood wouldn’t carry oxygen.")
        typewriter("You rust under pressure, but no one can deny you’re a foundation of civilization!")
        

    elif percentage <= 80:
        typewriter("Carbon!")
        time.sleep(1.5)
        typewriter("You can be soft as graphite or harder than steel as graphene.")
        typewriter("Shape-shifter, tech innovator, life giver—carbon does it all.")
        typewriter("You hold life together and make up the hardest known natural material.")


    else:
        typewriter("Uranium!")
        time.sleep(1.5)
        typewriter("You’re heavy, unstable, and unstoppable. You pulse with raw nuclear energy, capable of powering cities or unleashing unimaginable destruction.")
        typewriter("Your radioactive glow is a warning and a promise wherever you go, ")
        typewriter("change follows. Whether fueling the future or shaping history, you are a force that cannot be ignored.")
    
    ###

    if wrong_answers:
        typewriter("\nYou got the following questions wrong:")
        print("\n")
        for wrong in wrong_answers:
            typewriter(wrong["Question"])
            print("\n")
            typewriter("Answer: {}\n".format(wrong["Explanation"]))
    else:
        typewriter("\nYou got all the questions right!")

    decision = input("Would you like to try the test again? Type: | yes | no | ")
    typewriter("\n\n")
    while decision.lower() != "yes" and decision.lower() != "no":
        typewriter("Invalid choice. Please type a valid option ")
        typewriter("\n\n")
        decision = input("Would you like to try the test again? Type: | yes | no | ")
    
    if decision.lower() == "yes":
        os.system('cls' if os.name == 'nt' else 'clear')
        chemistry_questions(questions)

    if decision.lower() == "no":
        decision = input("Would you like to try a different quiz or exit? Type: | quiz | exit | ")  
        print("\n\n")
        while decision.lower() != "quiz" and decision.lower() != "exit":
            typewriter("Invalid choice. Please type a valid option ")
            print("\n\n")
            decision = input("Would you like to try a different quiz or exit? Type: | quiz | exit | ")
        

        if decision.lower() == "quiz":
            decision = input("What science quiz are you wanting to try? Type: | earth | chemistry | biology | ")
            print("\n\n")
            while decision.lower() != "earth" and decision.lower() != "chemistry" and decision.lower() != "biology":
                typewriter("Invalid choice. Please type a valid topic ")
                print("\n\n")
                decision = input("What science quiz are you wanting to try? Type: | earth | chemistry | biology | ")
            
            if decision.lower() == "earth":
                earth_questions(questions)

            elif decision.lower() == "chemistry":
                chemistry_questions(questions)
            
            elif decision.lower() == "biology":
                biology_questions(questions)

        if decision.lower() == "exit":
            ending()
  
def biology_questions(questions):    
    global score
    global question_number
    global question_amount
    global number
    global wrong_answers

    os.system('cls' if os.name == 'nt' else 'clear')
    random.shuffle(questions)

    decision = input("What lenth of quiz are you wanting to do? Type: | short | medium | long | ") # first of all get the input
    typewriter("\n\n")
    # check if the input is valid
    while decision.lower() != ("short") and decision.lower() != ("medium") and decision.lower() != ("long"):
     # repeat the question with a warning
        typewriter("Invalid choice. Please type a valid length ")
        typewriter("\n\n")
        decision = input("What lenth of quiz are you wanting to do? Type: | short | medium | long | ") 
        typewriter("\n\n")
 
    if decision.lower() == "short":
        question_amount = 5
    elif decision.lower() == "medium":
        question_amount = 10
    elif decision.lower() == "long":
        question_amount = 15
    
    while number < question_amount:
        question = questions[number]  # Select the question based on the current number
        print(question["Question"])
        print("\n")
        for option in question["Options"]:
            typewriter(option)

        answer = input("What do you choose? ")
        while answer.lower() != "a" and answer.lower() != "b" and answer.lower() != "c" and answer.lower() != "d":
            typewriter("Invalid anwser. Please type a valid option ")
            print("\n\n")
            answer = input("What do you choose? ")

        if answer.lower() == question["Answer"]:
            typewriter("That is..\n")
            time.sleep(1.5)
            typewriter("CORRECT!\n")
            typewriter(question["Explanation"])
            question_number = question_number + 1
            score = score + 1
            print("\n")
            typewriter("Your current score is {}/{}\n".format(score, question_number))
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            number = number + 1

        else:
            typewriter("That is...\n")
            time.sleep(1.5)
            typewriter("INCORRECT!\n")
            typewriter(question["Explanation"])
            question_number = question_number + 1
            wrong_answers.append(question)
            print("\n")
            typewriter("Your current score is {}/{}\n".format(score, question_number))
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            number = number + 1

    percentage = score / question_amount * 100

    typewriter("You got {:.2f}% on this test.".format(percentage))
    typewriter("Your rank is...")
    time.sleep(3)
    if percentage <= 20:
        typewriter("Mycoplasma!")
        time.sleep(1.5)
        typewriter("You’re microscopic, fragile, and barely holding it together.")
        typewriter("With no cell wall, even antibiotics push you around.")
        typewriter("You survive by leeching off stronger organisms, parasitic and pathetic.")
        
    elif percentage <= 40:
        typewriter("Amoeba!")
        time.sleep(1.5)
        typewriter("You’ve got no backbone, no real structure, and you move by oozing around.")
        typewriter("But don’t underestimate yourself your adaptability lets you survive in places others can’t.")
        

    elif percentage <= 60:
        typewriter("Mushroom!")
        time.sleep(1.5)
        typewriter("You work in the shadows, breaking down the dead and recycling life itself.")
        typewriter("Your roots spread like an underground network, influencing entire ecosystems.")
        typewriter("People might not always notice you, but without you, nature falls apart.")


    elif percentage <= 80:
        typewriter("Redwood Tree!")
        time.sleep(1.5)
        typewriter("You don’t need to move when you’re this big.")
        typewriter("Towering over the competition, you’ve stood strong for centuries, unshaken by storms, fires, or time.")
        typewriter("You breathe life into the world, and even when you fall, you shape ecosystems for generations.")

    else:
        typewriter("Orca!")
        time.sleep(1.5)
        typewriter("You dominate the ocean with intelligence, teamwork, and raw power.")
        typewriter("No natural predators, no real threats you decide who lives and who dies.")
        typewriter("Whether hunting in packs or outsmarting your prey, you rule your domain like no other.")
        typewriter("You are the king of the sea.")
    
    ###

    if wrong_answers:
        typewriter("\nYou got the following questions wrong:")
        print("\n")
        for wrong in wrong_answers:
            typewriter(wrong["Question"])
            print("\n")
            typewriter("Answer: {}\n".format(wrong["Explanation"]))
    else:
        print("\nYou got all the questions right!")

    decision = input("Would you like to try the test again? Type: | yes | no | ")
    typewriter("\n\n")
    while decision.lower() != "yes" and decision.lower() != "no":
        typewriter("Invalid choice. Please type a valid option ")
        typewriter("\n\n")
        decision = input("Would you like to try the test again? Type: | yes | no | ")
    
    if decision.lower() == "yes":
        os.system('cls' if os.name == 'nt' else 'clear')
        chemistry_questions(questions)

    if decision.lower() == "no":
        decision = input("Would you like to try a different quiz or exit? Type: | quiz | exit | ")  
        typewriter("\n\n")
        while decision.lower() != "quiz" and decision.lower() != "exit":
            typewriter("Invalid choice. Please type a valid option ")
            typewriter("\n\n")
            decision = input("Would you like to try a different quiz or exit? Type: | quiz | exit | ")
        

        if decision.lower() == "quiz":
            decision = input("What science quiz are you wanting to try? Type: | earth | chemistry | biology | ")
            typewriter("\n\n")
            while decision.lower() != "earth" and decision.lower() != "chemistry" and decision.lower() != "biology":
                typewriter("Invalid choice. Please type a valid topic ")
                typewriter("\n\n")
                decision = input("What science quiz are you wanting to try? Type: | earth | chemistry | biology | ")
            
            if decision.lower() == "earth":
                earth_questions(questions)

            elif decision.lower() == "chemistry":
                chemistry_questions(questions)
            
            elif decision.lower() == "biology":
                biology_questions(questions)

        if decision.lower() == "exit":
            ending()  
           
def filter_topic(questions):
    topics = []
    for question in questions:
        topics.append(question["Topic"])
    unique_topics = list(set(topics))

    typewriter("The following science quizzes are available: \n\n")
    for topic in unique_topics:
        print(topic)

    decision = input("What science quiz are you wanting to try? ") # first of all get the input
    typewriter("\n\n")
    # check if the input is valid
    while decision.lower() not in [topic.lower() for topic in unique_topics]:
        # repeat the question with a warning
        typewriter("Invalid choice. Please type a valid topic ")
        typewriter("\n\n")
        decision = input("What science quiz are you wanting to try? ") 
        typewriter("\n\n")


    filtered_questions = [question for question in questions if question["Topic"].lower() == decision.lower()]
    
    if decision.lower() == "earth":
        earth_questions(filtered_questions)
        
    elif decision.lower() == "chemistry":
        chemistry_questions(filtered_questions)

    elif decision.lower() == "biology":
        biology_questions(filtered_questions)

def intro():
    os.system('cls' if os.name == 'nt' else 'clear')
    typewriter("Hello!\n")
    typewriter("Welcome to my series of quizzes!\n")
    filter_topic(questions)

def main():
    intro()

def ending():
    os.system('cls' if os.name == 'nt' else 'clear')
    typewriter("Thank you for doing my series of quizzes. I hope you now have an idea of which science interests you.")
    
# clear the screen
os.system('cls' if os.name == 'nt' else 'clear')
# informs player to open terminal
typewriter("Please open the terminal as much as you can. \n\n")
# question
decision = input("Are you ready to begin? Type:| ready | >> ") # first of all get the input
typewriter("\n\n")
# check if the input is valid
while decision.lower() != "ready":
    # repeat the question with a warning
    typewriter("Invalid choice.\n\n")
    decision = input("Are you ready to begin? Type:| ready | >> ") 

# if read said
if decision.lower() == "ready":
    main()