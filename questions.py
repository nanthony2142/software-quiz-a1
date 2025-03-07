questions = [

# {"Topic": "Soccer","Question":"Who is fifa's boy?","Answer":"Messi"},
# {"Topic": "Soccer","Question":"Who is fifa's boy?","Answer":"Messi"},

# {"Topic": "Soccer","Question":"Who is fifa's boy?","Answer":"Messi"},

# {"Topic": "Soccer","Question":"Who is fifa's boy?","Answer":"Messi"},
{"Topic": "Soccer","Question":"Who is fifa's boy?","Options":["Messi","Ronaldo","Salah","Anthony"],"Answer": 0},

{"Topic": "Soccer","Question":"What is nathans surname","Options":["Messi","Dickson","Salah","Onana"],"Answer": 1},

]


for question in questions:
    print(question["Question"])
    print(f"Your options are:")
    for option in question["Options"]:
        print(option)

    answer = input("What do you choose?") #Anthony
    if answer == question["Options"][question["Answer"]]:
        print("Well done!!!")
    else:
        print("Wrong")

        