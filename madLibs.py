import subprocess

# Parts of Speech
n = []
v = []
adj = []
adv = []
num = 0


def welcomeMessage():
    print("\nMax's Mad Libs")
    print("Please fill in the parts of speech to create your own story!\n")
 


def getNoun():
    print("Please input 4 nouns (singular and present tense: ")
    print("\n")

    for i in range(4):
        n.append(input("Input noun " + str(i+1) + ": "))

    subprocess.run("clear")
    
def getVerb():
    print("Please input 4 verbs")
    print("\n")

    for i in range(4):
        v.append(input("Input verb " + str(i+1) + ": "))

    subprocess.run("clear")

def getAdjective():
    print("Please input 4 adjectives")
    print("\n")

    for i in range(4):
        adj.append(input("Input adjective " + str(i+1) + ": "))

    subprocess.run("clear")

def getAdverb():
    print("Please input 4 adverbs")
    print("\n")

    for i in range(4):
        adv.append(input("Input adverb " + str(i+1) + ": "))

    subprocess.run("clear")

def getNumber(num):
    if num <= 5:
        num = num*10
    else:
        num = 30

    return int(num)
    
# Story by me

def story():
    print("\nI " + adv[2] + " rose from my bed")
    print("My head was spinning. The party last night was " + adj[3] + ".")
    print("I lost my " + n[0] + ", which put me in a " + adj[2] + " mood.")
    print("I picked up my " + n[3] + " to check the time. Yikes! I was already " + str(getNumber(num)) + " minutes late!")
    print("I " + adv[0] + " threw on some clothes and ran to the bathroom to " + v[3] + " my " + n[1])
    print("Suddenly, the hangover hit.")
    print("My brain felt " + adj[0] + ". I slumped to the floor like a bag of " + n[2] + "(e)s.")
    print("Just then, as if to rescue itself, my brain had a burst of pure " + adj[1] + "! My JUUL was on my nightstand!")
    print("It would give me the dopamine rush I needed to power through and " + adv[1] + " " + v[2] + " to school.")
    print("I " + v[1] + "ed over to my nightstand, grabbed it and dipped with the JUUL " + v[0] + " between my teeth.")
    print("Finally, I was out the door. I sprinted " + adv[3] + " down the block.")
    print("Just as I turned the corner, the JUUL flew out of my mouth and into the street drain.")
    print("Eh, I should probably quit anyways\n")

welcomeMessage()
getNoun()
getVerb()
getAdjective()
getAdverb()

num = int(input("Please enter an integer 1-5: "))

story()
