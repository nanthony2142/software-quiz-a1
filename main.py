# interacts with operating system 
import os

from earth import questions


def earth_questions(earth):
    # clear the screen
    from earth import questions
    for question in earth:
        print(question["Question"])

def intro():
    print("Hello!")
    earth_questions(questions)

def main():
    intro()

os.system('cls' if os.name == 'nt' else 'clear')
main()
