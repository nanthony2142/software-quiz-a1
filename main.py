# interacts with operating system 
import os

from earth import questions


def earth_questions(earth):
    # clear the screen
    from earth import questions
    for question in earth:
        print(question["Question"])

def filter_topic(questions):
    topics = []
    for question in questions:
        topics.append(question["Topic"])
    unique_topics = list(set(topics))

    print("The topics are.....:")
    for topic in unique_topics:
        print(topic)

def intro():
    print("Hello!")
    filter_topic(questions)

def main():
    intro()

os.system('cls' if os.name == 'nt' else 'clear')
main()
