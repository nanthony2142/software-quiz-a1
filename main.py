#Imports
import time 
import os
import sys
import random
from quiz_questions_ranks import questions
from quiz_questions_ranks import ranks

def typewriter(words): # allows type writting effect
    for char in words:
        time.sleep(0.05) # time for letters to apear
        sys.stdout.write(char)
        sys.stdout.flush()

def length_quiz_questions(question_amount): #determines the length of the quiz
        
    os.system('cls' if os.name == 'nt' else 'clear')
    length_quiz = input("What length of quiz are you wanting to do? Type: | short | medium | long | >> ") # first of all get the input
    while length_quiz.lower() != ("short") and length_quiz.lower() != ("medium") and length_quiz.lower() != ("long"): # check if the input is valid
        typewriter("Invalid choice. Please type a valid length\n\n") # repeat the question with a warning
        length_quiz = input("What length of quiz are you wanting to do? Type: | short | medium | long | >> ") 
 
    # all posible lengths of the quiz
    if length_quiz.lower() == "short":
        question_amount = 5
    elif length_quiz.lower() == "medium":
        question_amount = 10
    elif length_quiz.lower() == "long":
        question_amount = 15
    
    return question_amount # return variables

def quiz_questions(filtered_questions, score, number_of_question_answered, question_amount, wrong_answers): #quiz questions

    os.system('cls' if os.name == 'nt' else 'clear')
    random.shuffle(filtered_questions) # shuffle the questions
    
    typewriter("To answer the questions, type the letter of the option you think is correct.\n\n")
    time.sleep(1.5)
    os.system('cls' if os.name == 'nt' else 'clear')
    while number_of_question_answered < question_amount: # while loop to ask the questions
        # if number of questions answered is less than the amount of questions
        question = filtered_questions[number_of_question_answered]  # Select the question based on the current number
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
            number_of_question_answered = number_of_question_answered + 1 # add 1 to the number of questions answered
            score = score + 1  # add 1 to the score
            typewriter("Your current score is {}/{}\n".format(score, number_of_question_answered))
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')

        else:
            typewriter("That is... ")
            time.sleep(1.5)
            typewriter("INCORRECT! \n\n")
            typewriter(question["Explanation"])
            print("\n")
            number_of_question_answered = number_of_question_answered + 1 # add 1 to the number of questions answered
            wrong_answers.append(question) # add the question to the wrong answers
            typewriter("Your current score is {}/{}\n".format(score, number_of_question_answered))
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')

    return score, question_amount, number_of_question_answered, wrong_answers # return variables

def quiz_results(filtered_ranks, score, question_amount, wrong_answers): # quiz results
    os.system('cls' if os.name == 'nt' else 'clear')
    percentage = score / question_amount * 100 # calculate the percentage

    typewriter("You got {:.2f}% on this test.\n".format(percentage)) # print the percentage
    typewriter("Your rank is... ")
    time.sleep(1.5)

    for rank in filtered_ranks: # check the rank
        if percentage <= rank["Test_Percentage"]:
                typewriter("{}\n".format(rank["Rank"]))
                typewriter(rank["Description"])
                time.sleep(1.5)
        
                typewriter("\nWhat questions did you get wrong?\n\n")
                for wrong in wrong_answers:
                    print("\n\n")
                    if wrong_answers:
                        typewriter("Question: ")
                        typewriter(wrong["Question"])
                        print("\n")
                        typewriter("Answer: {}\n".format(wrong["Explanation"])) # print the wrong answer
                        print("\n\n")
                    else:
                        typewriter("You got all the questions correct!\n")
                        print("\n\n")
                time.sleep(3)
                os.system('cls' if os.name == 'nt' else 'clear')
                break # exit the loop
    return filtered_ranks, score, question_amount, wrong_answers # return variables
    
def may_restart_quiz(): # ask if the user wants to restart the quiz
    os.system('cls' if os.name == 'nt' else 'clear')
    restart_quiz = input("Would you like to restart the quiz? Type: | yes | no | >> ") # first of all get the input
    while restart_quiz.lower() != "yes" and restart_quiz.lower() != "no": # check if the input is valid
        typewriter("Invalid choice. Please type a valid option\n\n") # repeat the question with a warning
        restart_quiz = input("Would you like to restart the quiz? Type: | yes | no | >> ") 

    if restart_quiz.lower() == "yes":
        display_topics(questions) # restart the quiz

def display_topics(questions): # display the topics
    os.system('cls' if os.name == 'nt' else 'clear')
    topics = []
    for question in questions:
        topics.append(question["Topic"]) # get the topics
    unique_topics = list(set(topics))

    typewriter("The following science quizzes are available: \n\n")
    for topic in unique_topics:
        typewriter(topic)
        print("\n")
        

    topic_choice = input("What science quiz are you wanting to try? ") # first of all get the input
    typewriter("\n\n")
    # check if the input is valid
    while topic_choice.lower() not in [topic.lower() for topic in unique_topics]: # check if the input is valid
        # repeat the question with a warning
        typewriter("Invalid choice. Please type a valid topic ")
        typewriter("\n\n")
        topic_choice = input("What science quiz are you wanting to try? ") 
        typewriter("\n\n")

    return topic_choice # return the topic choice

def filter_topic(questions, topic_choice): # filter the topic
    
    filtered_questions = [question for question in questions if question["Topic"].lower() == topic_choice.lower()]
    filtered_ranks = [rank for rank in ranks if rank["Topic"].lower() == topic_choice.lower()]
    return filtered_questions, filtered_ranks

def pre_quiz(): # pre quiz
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

def intro(): # intro
    os.system('cls' if os.name == 'nt' else 'clear')
    typewriter("Hello!\n")
    typewriter("Welcome to my series of quizzes!\n")
    typewriter("This program will help you decide what sciences you're interested\nin and what you may want to do for year 11 and 12.\n")
    typewriter("You will be asked a series of questions and based on your answers,\n")
    typewriter("you will be given a score and rank to help determine your aptitude for that science.\n")
    time.sleep(3)

def ending(): # ending
    os.system('cls' if os.name == 'nt' else 'clear')
    typewriter("Thank you for doing my series of quizzes.\nI hope you now have an idea of which science interests you\n and which science subjects you have an aptitude for, to help you decide your year 11 and 12 subjects.\n")
    time.sleep(1.5)
    os.system('cls' if os.name == 'nt' else 'clear')

def main(): # main function
    # main functions used in the program
    pre_quiz()
    intro()
    while True: # main loop
        # variables used in quiz
        score = 0
        number_of_question_answered = 0
        question_amount = 0 
        wrong_answers = []

        topic_choice = display_topics(questions)
        filtered_questions, filtered_ranks = filter_topic(questions, topic_choice)
        question_amount = length_quiz_questions(question_amount)
        score, number_of_question_answered, question_amount, wrong_answers = quiz_questions(filtered_questions, score, number_of_question_answered, question_amount, wrong_answers)
        quiz_results(filtered_ranks, score, question_amount, wrong_answers)

        restart_quiz = input("Would you like to restart the quiz or do a different one? Type: | yes | no | >> ")
        while restart_quiz.lower() != "yes" and restart_quiz.lower() != "no":
            typewriter("Invalid choice. Please type a valid option\n\n")
            restart_quiz = input("Would you like to restart the quiz or do a different one? Type: | yes | no | >> ")

        if restart_quiz.lower() == "no": # if the user wants to exit the program
            break  # Exit the loop to end the program
    ending()

main() # call the main function