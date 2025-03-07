from questions import questions




def print_questions(questions):
    for question in questions:
        print(question["Question"])

def intro():
    print("Hello!")
    print_questions(questions)

def main():
    intro()

main()