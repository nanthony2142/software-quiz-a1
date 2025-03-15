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
#### add misstakes NATHANN

def earth_questions(questions):
    global score
    global question_number
    global question_amount
    global number
    global wrong_answers

    os.system('cls' if os.name == 'nt' else 'clear')
    # clear the screen
    from earth import questions
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
            print(option)

        answer = input("What do you choose? ")
        while answer.lower() != "a" and answer.lower() != "b" and answer.lower() != "c" and answer.lower() != "d":
            typewriter("Invalid anwser. Please type a valid option ")
            typewriter("\n\n")
            answer = input("What do you choose? ")

        if answer.lower() == question["Answer"]:
            print("That is...")
            time.sleep(1.5)
            print("CORRECT!")
            print(question["Explanation"])
            question_number = question_number + 1
            score = score + 1
            print("Your current score is {}/{}\n".format(score, question_number))
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            number = number + 1

        else:
            print("That is...")
            time.sleep(1.5)
            print("INCORRECT!")
            print(question["Explanation"])
            question_number = question_number + 1
            wrong_answers.append(question)
            print("Your current score is {}/{}\n".format(score, question_number))
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            number = number + 1

    percentage = score / question_amount * 100

    print("You got {:.2f}%".format(percentage))
    print("Your rank is...")
    time.sleep(3)
    if percentage <= 20:
        print("Talc!")
        time.sleep(1.5)
        print("You crumble under the slightest pressure. A mere touch can wear you down, ")
        print("and even a fingernail is too much for you. You’re soft, flaky, and honestly,")
        print("no one’s picking you first for the team. But hey, at least you're useful in baby powder. ")
        
    elif percentage <= 40:
        print("Gypsum!")
        time.sleep(1.5)
        print("You try, but you're still easily scratched, a simple copper coin can still leave a mark on you.")
        print("At least you're useful in drywall and plaster, holding houses together.")
        print("Just don’t expect to be the foundation.")
        

    elif percentage <= 60:
        print("Apatite!")
        time.sleep(1.5)
        print("You’re no pushover, but you’re not indestructible either. Harder than your weaker cousins, ")
        print("you’re tough enough to resist everyday wear but still won’t last against the real heavyweights.") 
        print("You help build bones and teeth, so at least you're part of the reason people can actually chew their food.")


    elif percentage <= 80:
        print("Quartz!")
        time.sleep(1.5)
        print("Now we’re talking! You’re tough, durable, and versatile. You make up sand, glass, and even tech components.")
        print("You might not be the hardest, but people rely on you for watches, buildings, and even some beautiful gemstones.")
        print("You’ve earned your place.")


    else:
        print("Diamond!")
        time.sleep(1.5)
        print("You’ve been under immense pressure, and instead of breaking, ")
        print("you became the toughest mineral on Earth.")
        print("No one scratches you, and you shine bright, whether in industry or in luxury. ")
        print("You’re the ultimate performer, proving that pressure makes diamonds!")

    

    if wrong_answers:
        print("\nYou got the following questions wrong:")
        print("\n")
        for wrong in wrong_answers:
            print(wrong["Question"])
            print("\n")
            print("Answer: {}\n".format(wrong["Explanation"]))
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
        earth_questions(questions)
    if decision.lower() == "no":
        input("Would you like to try another quiz or exit? Type: | quiz | exit | ")  
        typewriter("\n\n")
        while decision.lower() != "quiz" and decision.lower() != "exit":
            typewriter("Invalid choice. Please type a valid option ")
            typewriter("\n\n")
            decision = input("Would you like to try another quiz? Type: | yes | no | ")
        

        if decision.lower() == "quiz":
            ####NATHAN
            pass

        if decision.lower() == "exit":
            ending()
            


            
def filter_topic(questions):
    topics = []
    for question in questions:
        topics.append(question["Topic"])
    unique_topics = list(set(topics))

    typewriter("The following science quizzes are available: \n")
    for topic in unique_topics:
        print(topic)

    decision = input("What science quiz are you wanting to try? ") # first of all get the input
    typewriter("\n\n")
    # check if the input is valid
    while decision.lower() != (topic):
    # repeat the question with a warning
        typewriter("Invalid choice. Please type a valid topic ")
        typewriter("\n\n")
        decision = input("What science quiz are you wanting to try? ") 
        typewriter("\n\n")

    # if security said
    if decision.lower() == "earth":
        earth_questions(questions)
        # goes to earth questions





def intro():
    typewriter("Hello!\n")
    filter_topic(questions)

def main():
    intro()

def ending():
    pass

os.system('cls' if os.name == 'nt' else 'clear')
main()
