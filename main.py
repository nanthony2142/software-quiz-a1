# allows time in code
import time
# interacts with operating system 
import os
# commands specific functions
import sys

import random

from earth import questions
from earth import ranks


def typewriter(words): # allows type writting effect
    for char in words:
        time.sleep(0.05) # time for letters to apear
        sys.stdout.write(char)
        sys.stdout.flush()

def quiz_questions(filtered_questions, score, question_number, question_amount, number_of_questions, wrong_answers):

    os.system('cls' if os.name == 'nt' else 'clear')
    random.shuffle(filtered_questions)
    length_quiz = input("What length of quiz are you wanting to do? Type: | short | medium | long | >> ") # first of all get the input
    while length_quiz.lower() != ("short") and length_quiz.lower() != ("medium") and length_quiz.lower() != ("long"): # check if the input is valid
        typewriter("Invalid choice. Please type a valid length\n\n") # repeat the question with a warning
        length_quiz = input("What length of quiz are you wanting to do? Type: | short | medium | long | >> ") 
 
    if length_quiz.lower() == "short":
        question_amount = 5
    elif length_quiz.lower() == "medium":
        question_amount = 10
    elif length_quiz.lower() == "long":
        question_amount = 15
    
    while number_of_questions < question_amount:
        question = filtered_questions[number_of_questions]  # Select the question based on the current number
        typewriter(question["Question"])
        print("\n")
        for option in question["Options"]:
            typewriter(option)

        print("\n")
        answer = input("What do you choose? ")
        while answer.lower() != "a" and answer.lower() != "b" and answer.lower() != "c" and answer.lower() != "d":
            typewriter("Invalid anwser. Please type a valid option\n\n")
            answer = input("What do you choose? ")

        if answer.lower() == question["Answer"]:
            typewriter("That is... ")
            time.sleep(1.5)
            typewriter("CORRECT! \n\n")
            typewriter(question["Explanation"])
            print("\n")
            question_number = question_number + 1
            score = score + 1
            typewriter("Your current score is {}/{}\n".format(score, question_number))
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            number_of_questions = number_of_questions + 1

        else:
            typewriter("That is... ")
            time.sleep(1.5)
            typewriter("INCORRECT! \n\n")
            typewriter(question["Explanation"])
            print("\n")
            question_number = question_number + 1
            wrong_answers.append(question)
            typewriter("Your current score is {}/{}\n".format(score, question_number))
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            number_of_questions = number_of_questions + 1

    return score, question_number, question_amount, number_of_questions, wrong_answers

def quiz_results(filtered_ranks, score, question_amount, wrong_answers):
    os.system('cls' if os.name == 'nt' else 'clear')
    percentage = score / question_amount * 100

    typewriter("You got {:.2f}% on this test.\n".format(percentage))
    typewriter("Your rank is... ")
    time.sleep(1.5)

    for rank in filtered_ranks:
        if percentage <= rank["Test_Percentage"]:
                typewriter("{}\n".format(rank["Rank"]))
                typewriter(rank["Description"])
                time.sleep(1.5)
                print("hi")
                break
                

    # if percentage <= 20:
    #     print[(filtered_ranks[0]["Rank"])]
    #     time.sleep(1.5)
        

    # elif percentage <= 40:
    #     typewriter("Gypsum!\n")
    #     time.sleep(1.5)
    #     typewriter("You try, but you're still easily scratched, a simple copper coin can still leave a mark on you.\n")
    #     typewriter("At least you're useful in drywall and plaster, holding houses together.\n")
    #     typewriter("Just don’t expect to be the foundation.\n")
        

    # elif percentage <= 60:
    #     typewriter("Apatite!\n")
    #     time.sleep(1.5)
    #     typewriter("You’re no pushover, but you’re not indestructible either. Harder than your weaker cousins, \n")
    #     typewriter("you’re tough enough to resist everyday wear but still won’t last against the real heavyweights.\n") 
    #     typewriter("You help build bones and teeth, so at least you're part of the reason people can actually chew their food.\n")


    # elif percentage <= 80:
    #     typewriter("Quartz!\n")
    #     time.sleep(1.5)
    #     typewriter("You’re tough, durable, and versatile. You make up sand, glass, and even tech components.\n")
    #     typewriter("You might not be the hardest, but people rely on you for watches, buildings, and even some beautiful gemstones.\n")
    #     typewriter("You’ve earned your place.\n")


    # else:
    #     typewriter("Diamond!\n")
    #     time.sleep(1.5)
    #     typewriter("You’ve been under immense pressure, and instead of breaking, \n")
    #     typewriter("you became the toughest mineral on Earth.\n")
    #     typewriter("No one scratches you, and you shine bright, whether in industry or in luxury. \n")
    #     typewriter("You’re the ultimate performer, proving that pressure makes diamonds!\n")


    # if wrong_answers:
    #     typewriter("\nYou got the following questions wrong:")
    #     print("\n")
    #     for wrong in wrong_answers:
    #         typewriter(wrong["Question"])
    #         print("\n")
    #         typewriter("Answer: {}\n".format(wrong["Explanation"]))
    # else:
    #     typewriter("\nYou got all the questions right!")

    # decision = input("Would you like to try the test again? Type: | yes | no | ")
    # print("\n\n")
    # while decision.lower() != "yes" and decision.lower() != "no":
    #     typewriter("Invalid choice. Please type a valid option ")
    #     print("\n\n")
    #     decision = input("Would you like to try the test again? Type: | yes | no | ")
    
    # if decision.lower() == "yes":
    #     os.system('cls' if os.name == 'nt' else 'clear')
    #     chemistry_questions(questions)

    # if decision.lower() == "no":
    #     decision = input("Would you like to try a different quiz or exit? Type: | quiz | exit | ")  
    #     print("\n\n")
    #     while decision.lower() != "quiz" and decision.lower() != "exit":
    #         typewriter("Invalid choice. Please type a valid option ")
    #         print("\n\n")
    #         decision = input("Would you like to try a different quiz or exit? Type: | quiz | exit | ")
        

    #     if decision.lower() == "quiz":
    #         decision = input("What science quiz are you wanting to try? Type: | Earth | Chemistry | Biology | ")
    #         print("\n\n")
    #         while decision.lower() != "earth" and decision.lower() != "chemistry" and decision.lower() != "biology":
    #             typewriter("Invalid choice. Please type a valid topic ")
    #             print("\n\n")
    #             decision = input("What science quiz are you wanting to try? Type: | earth | chemistry | biology | ")
            
    #         if decision.lower() == "earth":
    #             earth_questions(questions)

    #         elif decision.lower() == "chemistry":
    #             chemistry_questions(questions)
            
    #         elif decision.lower() == "biology":
    #             biology_questions(questions)

    #     if decision.lower() == "exit":
    #         ending()
    return filtered_ranks, score, question_amount, wrong_answers

def display_topics(questions):
    topics = []
    for question in questions:
        topics.append(question["Topic"])
    unique_topics = list(set(topics))

    typewriter("The following science quizzes are available: \n\n")
    for topic in unique_topics:
        typewriter(topic)
        print("\n")
        

    topic_choice = input("What science quiz are you wanting to try? ") # first of all get the input
    typewriter("\n\n")
    # check if the input is valid
    while topic_choice.lower() not in [topic.lower() for topic in unique_topics]:
        # repeat the question with a warning
        typewriter("Invalid choice. Please type a valid topic ")
        typewriter("\n\n")
        topic_choice = input("What science quiz are you wanting to try? ") 
        typewriter("\n\n")

    return topic_choice

def filter_topic(questions, topic_choice):
    
    filtered_questions = [question for question in questions if question["Topic"].lower() == topic_choice.lower()]
    filtered_ranks = [rank for rank in ranks if rank["Topic"].lower() == topic_choice.lower()]
    return filtered_questions, filtered_ranks
        
def intro():
    os.system('cls' if os.name == 'nt' else 'clear')
    typewriter("Hello!\n")
    typewriter("Welcome to my series of quizzes!\n")
    

def main():
    # variables used in quiz
    score = 0
    question_number = 0
    question_amount = 0 
    number_of_questions = 0
    wrong_answers = []
    percentage = 0

    # main functions used in the program
    intro() 
    topic_choice = display_topics(questions)
    filtered_questions, filtered_ranks = filter_topic(questions, topic_choice)
    score, question_number, question_amount, number_of_questions, wrong_answers = quiz_questions(filtered_questions, score, question_number, question_amount, number_of_questions, wrong_answers)
    filtered_ranks, score, question_amount, wrong_answers = quiz_results(filtered_ranks, score, question_amount, wrong_answers)
    ending()

    


def ending():
    os.system('cls' if os.name == 'nt' else 'clear')
    typewriter("Thank you for doing my series of quizzes. I hope you now have an idea of which science interests you.")

os.system('cls' if os.name == 'nt' else 'clear')
# informs player to open terminal
typewriter("Please open the terminal as much as you can. \n\n")
# question
start_program = input("Are you ready to begin? Type:| ready | >> ") # first of all get the input
# check if the input is valid
while start_program.lower() != "ready":
    # repeat the question with a warning
    typewriter("Invalid choice. Please type a valid option\n\n")
    start_program = input("Are you ready to begin? Type:| ready | >> ") 

# if read said
if start_program.lower() == "ready":
    main()