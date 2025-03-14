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
            print("That is CORRECT!")
            print(question["Explanation"])
            question_number = question_number + 1
            score = score + 1
            print("Your current score is {}/{}\n".format(score, question_number))
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            number = number + 1

        else:
            print("That is INCORRECT!")
            print(question["Explanation"])
            question_number = question_number + 1
            print("Your current score is {}/{}\n".format(score, question_number))
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            number = number + 1

    percentage = score / question_amount * 100

    if percentage <= 20:
        print("rock")
    elif percentage <= 40:
        print("pebble")
    elif percentage <= 60:
        print("stone")
    elif percentage <= 80:
        print("boulder")
    else:
        print("mountain")
    


            
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

os.system('cls' if os.name == 'nt' else 'clear')
main()
