import time
import os
import random

questions = [
    {"Topic": "car", "Question":"How was the moon created?","Options":["a) Accretion from elements of a once Nebula star formed into a moon like structure.","b) Dairy factories created a huge sphere of cheese and sent it to space.","c) A planet the size of Mars hit Earth forming a moon structure from Earths rubble.","d) A comet from a nearby galaxy got caught in Earth's gravitational pull and became the moon."],"Answer": "c"},
    {"Topic": "earth", "Question":"Which of these materials is soil NOT made of?","Options":["a) Clay","b) Charcoa", "c) Silt", "d) Sand"],"Answer": "b"},
    {"Topic": "earth", "Question":"Which of these minerals is the LEAST hard?","Options":["a) Quartz","b) Diamond","c) Calcite","d) Fluorite"],"Answer": "c"},
    {"Topic": "earth", "Question":"Which of these is NOT a law of stratigraphy?", "Options": ["a) Law of Sedimentary Progression (sedimentary layers become more complex over time.)",	"b) Law of Superposition (Older layers are at the bottom, younger on top.)",	"c) Law of Original Horizontality (Layers are originally deposited horizontally.)",	"d) Law of Cross-Cutting Relationships (A rock or fault cutting through another is younger than the rock it cuts.)"],"Answer": "a"},
    {"Topic": "earth", "Question":"Which of these is the oldest period of time shown?","Options":["a) Jurassic","b) Triassic","c) Cretaceous","d) Paleogene"],"Answer": "b"},
    {"Topic": "earth", "Question":"What is the first horizon of soil called?","Options":["a) O-horizion","b) A-horizon","c) B-horizon","d) P-horizon"],"Answer": "a"},
    {"Topic": "earth", "Question":"Which of these animal's was the first to exist?","Options":["a) Bee","b) Tyrannosaurus rex","c) Arthropleura","d) Megalodon"],"Answer": "c"},
    {"Topic": "earth", "Question":"Which great extinction event wiped out the most life on Earth?","Options":["a) Permian–Triassic extinction event (Massive volcanic eruptions in Siberia caused climate changes and loss of oxygen.)","b) Cretaceous–Paleogene extinction (Wiped out the dinosaurs and allowed mamals to dominate)","c) Late Devonian extinction (Caused by climate changes wiping out many reef-building organisms.)","d) Triassic–Jurassic extinction (Volcanic activity paved the way for dinosaurs to dominate)"],"Answer": "a"},
    {"Topic": "earth", "Question":"Which layer of Earth is made of liquid?","Options":["a) the Crust","b) the Mantle","c) the Outer Core","d) the Inner Core"],"Answer": "c"},
    {"Topic": "earth", "Question":"How are we able to date how old rocks are?","Options":["a) Fossil Frequency Analysis – The number of fossils in a rock layer is counted, and more fossils mean an older rock.","b) Radiometric Dating – Scientists measure the decay of radioactive isotopes, like uranium turning into lead, to determine a rock’s age.","c) Crystal Vibration Timing – By measuring how fast the tiny crystals inside the rock vibrate, scientists can calculate its age.","d) Rock Hardness Progression – Rocks get harder over time, so geologists test how difficult they are to scratch to determine their age."],"Answer": "b"},
    {"Topic": "earth", "Question":"What are the main two elements that are used in Radiometric Dating?","Options":["a) Iron and Hydrogen","b) Iron and Carbon","c) Lead and Uranium","d) Uranium and Carbon"],"Answer": "d"},
    {"Topic": "earth", "Question":"What is NOT a real rock type?","Options":["a) Metamorphic","b) Cryllic","c) Igneous","d) Sedimentary"],"Answer": "b"},
    {"Topic": "earth", "Question":"Which piece of evidence is NOT used to help identify Earth's layers?","Options":["a) Seismic Waves","b) Meteorites","c) Volcanos","d) Mining"],"Answer": "d"},
    {"Topic": "earth", "Question":"Which of these is NOT part of the rock cycle?","Options":["a) Magma cools and hardens to form igneous rock.","b) Sediments are compressed and bonded together to form sedimentary rock.","c) Existing rocks undergo heat and pressure, transforming into metamorphic rock.","d) Water evaporates from minerals, causing them to fuse into solid rock over time."],"Answer": "d"},
    {"Topic": "earth", "Question":"In 1912, Alfred Wegener proposed that the continents were once part of a single massive landmass called Pangaea. However, his theory wasn't widely accepted until the early 1960s. Which of these is NOT a piece of evidence that supports Wegeners claim?","Options":["a) Glacial deposits in regions now near the equator indicated that continents were once positioned closer to the poles.","b) Radiometric dating suggested that rocks were formed at similar times on mutiple continents.","c) The coastlines of continents like South America and Africa seem to fit together like a jigsaw puzzle, suggesting they were once connected.","d) Similar fossils found on continents now separated by oceans suggest they were once connected."],"Answer": "b"}
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