import subprocess
import random

# Parts of Speech
n = []
v = []
adj = []
adv = []



def welcomeMessage():
    print("\n")
    print("Max's Mad Libs")
    print("Please fill in the parts of speech to create your own crazy story!")
    print("\n")


def getNoun():
    print("Please input 3 nouns")
    print("\n")

    for i in range(1, 4):
        n.append(input("Input noun " + str(i) + ": "))

    subprocess.run("clear")
    
def getVerb():
    print("Please input 3 verbs")
    print("\n")

    for i in range(1, 4):
        v.append(input("Input verb " + str(i) + ": "))

    subprocess.run("clear")

def getAdjective():
    print("Please input 3 adjectives")
    print("\n")

    for i in range(1, 4):
        adj.append(input("Input adjective " + str(i) + ": "))

    subprocess.run("clear")

def getAdverb():
    print("Please input 3 adverbs")
    print("\n")

    for i in range(1, 4):
        adv.append(input("Input adverb " + str(i) + ": "))

    subprocess.run("clear")

def getNumber():
    num = input("Please enter an integer 1-5: ")
    if num <= 5:
        num = num*10
    else:
        num = 30
    return num

def story():
    print("\n")
    print("I " + adv[2] + "rose from my bed")
    print("My head was spinning. The party last night was " + adj[3] + ".")
    print("I lost my " + n[0] + ", which put me in a " + adj[2] + " mood.")
    print("I picked up my " + n[3] + " to check the time. Yikes! I was already " + getNumber() + " minutes late!")
    print("I " + adv[0] + " threw on some clothes and ran to the bathroom to " + v[3] + " my " + n[1])
    print()
