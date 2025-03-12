import time
import os
import random

questions = [
    {"Topic": "earth", "Question":"How was the moon created?","Options":["a) Accretion from elements of a once Nebula star\n formed into a moon like structure.\n","b) Dairy factories created a huge sphere of cheese\n and sent it to space.\n","c) A planet the size of Mars hit Earth\n forming a moon structure from Earths rubble.\n","d) A comet from a nearby galaxy got caught\n in Earth's gravitational pull and became the moon.\n"],"Answer": "c"},
    {"Topic": "earth", "Question":"Which of these materials is soil NOT made of?","Options":["a) Clay\n","b) Charcoa\n", "c) Silt\n", "d) Sand\n"],"Answer": "b"},
    {"Topic": "earth", "Question":"Which of these minerals is the LEAST hard?","Options":["a) Quartz\n","b) Diamond\n","c) Calcite\n","d) Fluorite\n"],"Answer": "c"},
    {"Topic": "earth", "Question":"Which of these is NOT a law of stratigraphy?", "Options": ["a) Law of Sedimentary Progression \n(sedimentary layers become more complex over time.)\n",	"b) Law of Superposition \n(Older layers are at the bottom, younger on top.)\n",	"c) Law of Original Horizontality \n(Layers are originally deposited horizontally.)\n",	"d) Law of Cross-Cutting Relationships \n(A rock or fault cutting through another is younger than the rock it cuts.)\n"],"Answer": "a"},
    {"Topic": "earth", "Question":"Which of these is the oldest period of time shown?","Options":["a) Jurassic\n","b) Triassic\n","c) Cretaceous\n","d) Paleogene\n"],"Answer": "b"},
    {"Topic": "earth", "Question":"What is the first horizon of soil called?","Options":["a) O-horizion\n","b) A-horizon\n","c) B-horizon\n","d) P-horizon\n"],"Answer": "a"},
    {"Topic": "earth", "Question":"Which of these animal's was the first to exist?","Options":["a) Bee\n","b) Tyrannosaurus rex\n","c) Arthropleura\n","d) Megalodon\n"],"Answer": "c"},
    {"Topic": "earth", "Question":"Which great extinction event wiped out the most life on Earth?","Options":["a) Permian–Triassic extinction event \n(Massive volcanic eruptions in Siberia caused climate changes and loss of oxygen.)\n","b) Cretaceous–Paleogene extinction \n(Wiped out the dinosaurs and allowed mamals to dominate.)\n","c) Late Devonian extinction \n(Caused by climate changes \nwiping out many reef-building organisms.)\n","d) Triassic–Jurassic extinction \n(Volcanic activity paved the way for dinosaurs to dominate.)\n"],"Answer": "a"},
    {"Topic": "earth", "Question":"Which layer of Earth is made of liquid?","Options":["a) the Crust","b) the Mantle","c) the Outer Core","d) the Inner Core"],"Answer": "c"},
    {"Topic": "earth", "Question":"How are we able to date how old rocks are?","Options":["a) Fossil Frequency Analysis \n(The number of fossils in a rock layer is counted, \nand more fossils mean an older rock.)\n","b) Radiometric Dating \n(Scientists measure the decay of radioactive isotopes, \nlike uranium turning into lead, to determine a rock’s age.)\n","c) Crystal Vibration Timing \n(By measuring how fast the tiny crystals inside the rock vibrate, scientists can calculate its age.)\n","d) Rock Hardness Progression \n(Rocks get harder over time, so geologists test how difficult they are to scratch to determine their age.)\n"],"Answer": "b"},
    {"Topic": "earth", "Question":"What are the main two elements that are used in Radiometric Dating?","Options":["a) Iron and Hydrogen\n","b) Iron and Carbon\n","c) Lead and Uranium\n","d) Uranium and Carbon\n"],"Answer": "d"},
    {"Topic": "earth", "Question":"What is NOT a real rock type?","Options":["a) Metamorphic\n","b) Cryllic\n","c) Igneous\n","d) Sedimentary\n"],"Answer": "b"},
    {"Topic": "earth", "Question":"Which piece of evidence is NOT used to help identify Earth's layers?","Options":["a) Seismic Waves\n","b) Meteorites\n","c) Volcanos\n","d) Mining\n"],"Answer": "d"},
    {"Topic": "earth", "Question":"Which of these is NOT part of the rock cycle?","Options":["a) Magma cools and hardens to form igneous rock.\n","b) Sediments are compressed and bonded together to form sedimentary rock.\n","c) Existing rocks undergo heat and pressure, transforming into metamorphic rock.\n","d) Water evaporates from minerals, causing them to fuse into solid rock over time.\n"],"Answer": "d"},
    {"Topic": "earth", "Question":"In 1912, Alfred Wegener proposed that the continents were once part of a single massive landmass called Pangaea. \nHowever, his theory wasn't widely accepted until the early 1960s. \nWhich of these is NOT a piece of evidence that supports Wegeners claim?","Options":["a) Glacial deposits in regions now near the equator \nindicated that continents were once \npositioned closer to the poles.\n","b) Radiometric dating suggested that rocks were \nformed at similar times on mutiple continents.\n","c) The coastlines of continents like South America and Africa \nseem to fit together like a jigsaw puzzle, \nsuggesting they were once connected.\n","d) Similar fossils found on continents now separated by oceans \nsuggest they were once connected.\n"],"Answer": "b"}
]



# os.system('cls' if os.name == 'nt' else 'clear')
# for question in questions:
#     random.shuffle(questions)
#     print(question["Question"])
#     print(f"Your options are:")
#     for option in question["Options"]:
#         print(option)

#     answer = input("What do you choose? ")
#     if answer == question["Answer"]:
#         print("Well done!!!")
#         time.sleep(1)
#         os.system('cls' if os.name == 'nt' else 'clear')
#     else:
#         print("Wrong")
#         time.sleep(1)
#         os.system('cls' if os.name == 'nt' else 'clear')