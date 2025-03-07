questions = [
    {"Question":"How was the moon created?","Options":["a) Accretion from elements of a once Nebula star formed into a moon like structure.","b) Dairy factories created a huge sphere of cheese and sent it to space.","c) A planet the size of Mars hit Earth forming a moon strcutre from Earths rubble.","d) A commit from a nearby galaxy got caught in Earth's gravitational pull and became the moon."],"Answer": "c"},

]

for question in questions:
    print(question["Question"])
    print(f"Your options are:")
    for option in question["Options"]:
        print(option)

    answer = input("What do you choose? ") #y=
    if answer == question["Answer"]:
        print("Well done!!!")
    else:
        print("Wrong")
