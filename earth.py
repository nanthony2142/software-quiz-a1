import time
import os
import random



#############INTROOOOOOOO########
#please open the terminal as much as you can etccccccc



#Hello 

#############INTROOOOOOOO########




questions = [
    {"Topic": "Earth", "Question":"How was the moon created?","Options":["a) Accretion from elements of a once Nebula star\n formed into a moon like structure.\n","b) Dairy factories created a huge sphere of cheese\n and sent it to space.\n","c) A planet the size of Mars hit Earth\n forming a moon structure from Earths rubble.\n","d) A comet from a nearby galaxy got caught\n in Earth's gravitational pull and became the moon.\n"],"Answer": "c","Explanation": "The moon was actually created when a planet the size of Mars hit Earth, forming a moon structure from Earths rubble."},
    {"Topic": "Earth", "Question":"Which of these materials is soil NOT made of?","Options":["a) Clay\n","b) Charcoa\n", "c) Silt\n", "d) Sand\n"],"Answer": "b","Explanation": "Soil is not made of charcoal."},
    {"Topic": "Earth", "Question":"Which of these minerals is the LEAST hard?","Options":["a) Quartz\n","b) Diamond\n","c) Calcite\n","d) Fluorite\n"],"Answer": "c","Explanation": "Calcite is the least hard mineral with a hardness raiting of 3."},
    {"Topic": "Earth", "Question":"Which of these is NOT a law of stratigraphy?", "Options": ["a) Law of Sedimentary Progression \n(sedimentary layers become more complex over time.)\n",	"b) Law of Superposition \n(Older layers are at the bottom, younger on top.)\n",	"c) Law of Original Horizontality \n(Layers are originally deposited horizontally.)\n",	"d) Law of Cross-Cutting Relationships \n(A rock or fault cutting through another is younger than the rock it cuts.)\n"],"Answer": "a","Explanation": "The Law of Sedimentary Progression is not a law in any science."},
    {"Topic": "Earth", "Question":"Which of these is the oldest period of time shown?","Options":["a) Jurassic\n","b) Triassic\n","c) Cretaceous\n","d) Paleogene\n"],"Answer": "b","Explanation": "The Triassic period is the oldest of the four periods shown and that is when dinosaurs first existed."},
    {"Topic": "Earth", "Question":"What is the first horizon of soil called?","Options":["a) O-horizion\n","b) A-horizon\n","c) B-horizon\n","d) P-horizon\n"],"Answer": "a","Explanation": "The O-horizon is the first horizon of soil and is made up of ORGANIC matter, which is why it's called the O-horizon."},
    {"Topic": "Earth", "Question":"Which of these animal's was the first to exist?","Options":["a) Bee\n","b) Tyrannosaurus rex\n","c) Arthropleura\n","d) Megalodon\n"],"Answer": "c","Explanation": "Arthropleura was the first animal of these to exist and was a giant millipede."},
    {"Topic": "Earth", "Question":"Which great extinction event wiped out the most life on Earth?","Options":["a) Permian–Triassic extinction event \n(Massive volcanic eruptions in Siberia caused climate changes and loss of oxygen.)\n","b) Cretaceous–Paleogene extinction \n(Wiped out the dinosaurs and allowed mamals to dominate.)\n","c) Late Devonian extinction \n(Caused by climate changes \nwiping out many reef-building organisms.)\n","d) Triassic–Jurassic extinction \n(Volcanic activity paved the way for dinosaurs to dominate.)\n"],"Answer": "a","Explanation": "The Permian–Triassic extinction event wiped out 96% of all marine species and 70% of all land species. it is known as the Great Dying."},
    {"Topic": "Earth", "Question":"Which layer of Earth is made of liquid?","Options":["a) The Crust\n","b) The Mantle\n","c) The Outer Core\n","d) The Inner Core\n"],"Answer": "c","Explanation": "The Outer Core is made of liquid iron and nickel. This was discovered by studying seismic waves as secondary waves can't travel through liquids."},
    {"Topic": "Earth", "Question":"How are we able to date how old rocks are?","Options":["a) Fossil Frequency Analysis \n(The number of fossils in a rock layer is counted, \nand more fossils mean an older rock.)\n","b) Radiometric Dating \n(Scientists measure the decay of radioactive isotopes, \nsuch as uranium turning into lead, to determine a rock’s age.)\n","c) Crystal Vibration Timing \n(By measuring how fast the tiny crystals inside the rock vibrate, scientists can calculate its age.)\n","d) Rock Hardness Progression \n(Rocks get harder over time, so geologists test how difficult they are to scratch to determine their age.)\n"],"Answer": "b","Explanation": "Radiometric Daiting is the process of measuring the decay of radioactive isotopes. From this we have been able to determine the age of the Earth to be 4.54 billion years old."},
    {"Topic": "Earth", "Question":"What are the main two elements that are used in Radiometric Dating?","Options":["a) Iron and Hydrogen\n","b) Iron and Carbon\n","c) Lead and Uranium\n","d) Uranium and Carbon\n"],"Answer": "d","Explanation": "Uranium and Carbon are the two main elements used in Radiometric Dating. Uranium is used to date rocks and Carbon is used to date organic material."},
    {"Topic": "Earth", "Question":"What is NOT a real rock type?","Options":["a) Metamorphic\n","b) Cryllic\n","c) Igneous\n","d) Sedimentary\n"],"Answer": "b","Explanation": "Cryllic is not a real rock type."},
    {"Topic": "Earth", "Question":"Which piece of evidence is NOT used to help identify Earth's layers?","Options":["a) Seismic Waves\n","b) Meteorites\n","c) Volcanos\n","d) Mining\n"],"Answer": "d","Explanation": "Mining is not used to help identify Earth's layers."},
    {"Topic": "Earth", "Question":"Which of these is NOT part of the rock cycle?","Options":["a) Magma cools and hardens to form igneous rock.\n","b) Sediments are compressed and bonded together to form sedimentary rock.\n","c) Existing rocks undergo heat and pressure, transforming into metamorphic rock.\n","d) Water evaporates from minerals, causing them to fuse into solid rock over time.\n"],"Answer": "d","Explanation": "Water evaporating from minerals is not part of the rock cycle."},
    {"Topic": "Earth", "Question":"In 1912, Alfred Wegener proposed that the continents were once part of a single massive landmass called Pangaea. \nHowever, his theory wasn't widely accepted until the early 1960s. \nWhich of these is NOT a piece of evidence that supports Wegeners claim?","Options":["a) Glacial deposits in regions now near the equator \nindicated that continents were once \npositioned closer to the poles.\n","b) Radiometric dating suggested that rocks were \nformed at similar times on mutiple continents.\n","c) The coastlines of continents like South America and Africa \nseem to fit together like a jigsaw puzzle, \nsuggesting they were once connected.\n","d) Similar fossils found on continents now separated by oceans \nsuggest they were once connected.\n"],"Answer": "b","Explanation": "Radiometric dating was not used as evidence to support Wegeners claim."},
    {"Topic": "Chemistry", "Question":"What is the most reactive element on the periodic table?","Options":["a) Francium\n","b) Fluorine\n","c) Oxygen\n","d) Hydrogen\n"],"Answer": "a","Explanation": "Francium a Alkaline Earth Metal that is the most reactive element in the universe."},
    {"Topic": "Chemistry", "Question":"How many naturally occurring elements are there?","Options":["a) 92\n","b) 118\n","c) 50\n","d) 78\n"],"Answer": "a","Explanation": "There are 92 naturally occurring elements. The other 26 remaining elements on the periodic table are man-made."},
    {"Topic": "Chemistry", "Question":"Which is NOT a real category on the periodic table?","Options":["a) Alkali metals\n","b) Earth metals\n","c) Actinides\n","d) Noble gases\n"],"Answer": "b","Explanation": "Earth metals is not a real category on the periodic table, however Alkali Earth metals is a real category"},
    {"Topic": "Chemistry", "Question":"How many elements are humans made up of?","Options":["a) 30\n","b) 26\n","c) 12\n","d) 58\n"],"Answer": "b","Explanation": "Humans are made up of 26 unique elements."},
    {"Topic": "Chemistry", "Question":"What two factors determine the density of a substance?","Options":["a) Mass and temperature\n","b) Volume and temperature\n","c) weight and volume\n","d) Mass and volume\n"],"Answer": "d","Explanation": "Density is determined by mass and volume."},
    {"Topic": "Chemistry", "Question":"What naturally occurring metal is the most dense?","Options":["a) Uranium\n","b) Iron\n","c) Francium\n","d) Copper\n"],"Answer": "a","Explanation": "Uranium is the most dense naturally occurring metal."},
    {"Topic": "Chemistry", "Question":"What metal is NOT magnetic?","Options":["a) Cobalt\n","b) Iron\n","c) Copper\n","d) Nickel\n"],"Answer": "c","Explanation": "Copper is not magnetic."},
    {"Topic": "Chemistry", "Question":"Which of the following is NOT a separation technique?","Options":["a) Filtration\n","b) Evaporation\n","c) Combustion\n","d) Distillation\n"],"Answer": "c","Explanation": "Combustion is not a separation technique."},
    {"Topic": "Chemistry", "Question":"What is the chemical formula for the ammonium ion?","Options":["a) NH₃\n","b) NH₄⁺\n","c) NO₃⁻\n","d) NH₂⁻\n"],"Answer": "b","Explanation": "The chemical formula for the ammonium ion is NH₄⁺."},
    {"Topic": "Chemistry", "Question":"Which of the following is NOT a real type of radiation?","Options":["a) Alpha radiation\n","b) Beta radiation\n","c) Gamma radiation\n","d) Delta radiation\n"],"Answer": "d","Explanation": "Delta radiation is not a real type of radiation."},
    {"Topic": "Chemistry", "Question":"Which type of beta radiation has the highest penetration power?","Options":["a) Gamma radiation\n","b) Alpha radiation\n","c) Beta-minus (β⁻)\n","d) Beta-plus (β⁺)\n"],"Answer": "c","Explanation": "Gamma has the highest penetration power."},
    {"Topic": "Chemistry", "Question":"What is a metalloid?","Options":["a) An element that only conducts electricity in extreme conditions.\n","b) An element that has properties of both metals and non-metals.\n","c) An element that is highly conductive and malleable.\n","d) An element that cannot conduct electricity at all.\n"],"Answer": "b","Explanation": "A metalloid has properties of both metals and non-metals."},
    {"Topic": "Chemistry", "Question":"Which of the following is NOT a type of chemical reaction?","Options":["a) Synthesis\n","b) Decomposition\n","c) Replication\n","d) Combustion\n"],"Answer": "c","Explanation": "Replication is not a type of chemical reaction."},
    {"Topic": "Chemistry", "Question":"What is an atom?","Options":["a) A type of molecule made up of only protons.\n","b) A charged particle found in the nucleus of an element.\n","c) A substance made up of two or more different elements chemically bonded.\n","d) The smallest unit of an element that retains its chemical properties.\n"],"Answer": "d","Explanation": "An atom is the smallest unit of an element that retains its chemical properties."},
    {"Topic": "Chemistry", "Question":"Which of the following is NOT a part of an atom?","Options":["a) Proton\n","b) Neuron\n","c) Electron\n","d) Neutron\n"],"Answer": "b","Explanation": "A neuron is a part in the brain not a part of an atom."},
    {"Topic": "Biology", "Question": "Which of the following is NOT alive?", "Options": ["a) animals\n", "b) fungi\n", "c) virus\n", "d) bacteria\n"], "Answer": "c", "Explanation": "Viruses are not considered alive because they cannot reproduce on their own."},
    {"Topic": "Biology", "Question": "Which of these is NOT a real animal species?", "Options": ["a) Naked Mole Rat\n", "b) Panther\n", "c) Tartigrade\n", "d) Headless Chicken Monster\n"], "Answer": "b", "Explanation": "Panther's are not a real animal species. However Panthera is a genus which includes big cats such as lions and tigers."},
    {"Topic": "Biology", "Question": "Which of these is NOT a membrane bound organelle?", "Options": ["a) Ribosome (A small structure that synthesizes proteins)\n", "b) Mitochondria (Responsible for cellular respiration)\n", "c) Vacuole (A sac that stores nutrients)\n", "d) Nucleus (Stores DNA of the cell)\n"], "Answer": "a", "Explanation": "Ribosomes are not membrane bound organelles."},
    {"Topic": "Biology", "Question": "Which of the following is NOT a requirement of MRS GREN, the acronym that represents the characteristics that all living things must have?", "Options": ["a) Movement\n", "b) Respiration\n", "c) Growth\n", "d) Equilibrium\n"], "Answer": "d", "Explanation": "Equilibrium is not a requirement of MRS GREN."},
    {"Topic": "Biology", "Question": "What is the name of the diagram that illustrates the evolutionary connections between all living organisms?", "Options": ["a) The Evolutionary Ladder\n", "b) The Tree of Life\n", "c) The Organism Web\n", "d) The Food Web\n"], "Answer": "b", "Explanation": "The Tree of Life is the diagram that illustrates the evolutionary connections between all living organisms."},
    {"Topic": "Biology", "Question": "What is the largest living organism on Earth?", "Options": ["a) Blue Whale\n", "b) Honey Mushroom\n", "c) The Great Barrier Reef\n", "d) African Elephant\n"], "Answer": "b", "Explanation": "The Honey Mushroom is the largest living organism on Earth as it's roots reach out 10.36 square kilometers. The Great Barrier Reef is bigger but is made up of many individual organisms."},
    {"Topic": "Biology", "Question": "What is the process by which an organism maintains a stable internal environment?", "Options": ["a) Metabolism\n", "b) Respiration\n", "c) Homeostasis\n", "d) Reproduction\n"], "Answer": "c", "Explanation": "Homeostasis is the process by which an organism maintains a stable internal environment, such as someones body temperature."},
    {"Topic": "Biology", "Question": "Which kingdom is most closely related to humans, besides Animalia?", "Options": ["a) Plantae\n", "b) Protista\n", "c) Bacteria\n", "d) Fungi\n"], "Answer": "d", "Explanation": "Fungi is the kingdom most closely related to humans, besides Animalia. Because we share a common ancestor."},
    {"Topic": "Biology", "Question": "What does DNA stand for?", "Options": ["a) Deoxyribonucleic Acid\n", "b) Dynamic Nucleic Acid\n", "c) Deoxynucleotide Acid\n", "d) Double Nucleic Acid\n"], "Answer": "a", "Explanation": "DNA stands for Deoxyribonucleic Acid."},
    {"Topic": "Biology", "Question": "An animal that is not eaten by any other animals on a food web is known as what?", "Options": ["a) Primary consumer\n", "b) Detritivore\n", "c) Apex predator\n", "d) Delta consumer\n"], "Answer": "c", "Explanation": "An animal that is not eaten by any other animals on a food web is known as an Apex predator."},
    {"Topic": "Biology", "Question": "Which is NOT a part of cell theory?", "Options": ["a) All living organisms are composed of cells.\n", "b) All cells are from pre-existing cells.\n", "c) The cell is the basic unit of life.\n", "d) The function of a cell is determined by its size.\n"], "Answer": "d", "Explanation": "The function of a cell is determined by its size is NOT a part of cell theory."},
    {"Topic": "Biology", "Question": "Which of the following is an example of mutualism symbiosis?", "Options": ["a) A lion hunting a zebra\n", "b) Bees pollinating flowers\n", "c) A bird flying past a dog\n", "d) tree absorbing sunlight\n"], "Answer": "b", "Explanation": "Bees pollinating flowers is an example of mutualism symbiosis as both the bee and flower are benefited from this symbiosis."},
    {"Topic": "Biology", "Question": "Dinosaurs are most closely related to which group of modern animals?", "Options": ["a) Birds\n", "b) Reptiles\n", "c) Amphibians\n", "d) Mammals\n"], "Answer": "a", "Explanation": "Dinosaurs are most closely related to birds."},
    {"Topic": "Biology", "Question": "Which of the following is a unique characteristic of fungi?", "Options": ["a) They produce their own food through photosynthesis.\n", "b) They have chloroplasts like plants.\n", "c) They decompose organic matter and absorb nutrients.\n", "d) They are all multi-celled organisms.\n"], "Answer": "c", "Explanation": "Fungi decompose organic matter and absorb nutrients."},
    {"Topic": "Biology", "Question": "What is the equivalent of an egg cell in a flower?", "Options": ["a) Pollen grain\n", "b) Seeds\n", "c) Ovule\n", "d) Anther\n"], "Answer": "c", "Explanation": "The equivalent of an egg cell in a flower is the ovule. And a sperm cell is the pollen grain."},
]




# os.system('cls' if os.name == 'nt' else 'clear')

# chemistry_questions = [question for question in questions if question["Topic"].lower() == "chemistry"]
# for question in chemistry_questions:
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
