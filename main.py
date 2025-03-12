# allows time in code
import time
# interacts with operating system 
import os
# commands specific functions
import sys

import random

from earth import questions


def typewriter(words): # allows type writting effect
    for char in words:
        time.sleep(0.05) # time for letters to apear
        sys.stdout.write(char)
        sys.stdout.flush()


def earth_questions(earth):
    os.system('cls' if os.name == 'nt' else 'clear')
    # clear the screen
    from earth import questions
    random.shuffle(questions)
    for question in questions:
        print(question["Question"])
        print("\n")
        for option in question["Options"]:
            print(option)

        answer = input("What do you choose? ")
        while answer.lower() != "a" and answer.lower() != "b" and answer.lower() != "c" and answer.lower() != "d":
            typewriter("Invalid choice. Please type a valid option ")
            typewriter("\n\n")
            answer = input("What do you choose? ")
        if answer.lower() == question["Answer"]:
            print("Well done!!!")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print("Wrong")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')

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
