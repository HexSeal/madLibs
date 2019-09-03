import subprocess

# Parts of Speech
n = []
v = []
adj = []
adv = []

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
        n.append(input("Input verb " + str(i) + ": "))

    subprocess.run("clear")

def getAdjective():
    print("Please input 3 adjectives")
    print("\n")

    for i in range(1, 4):
        n.append(input("Input adjective " + str(i) + ": "))

    subprocess.run("clear")

def getAdverb():
    print("Please input 3 adverbs")
    print("\n")

    for i in range(1, 4):
        n.append(input("Input adverb " + str(i) + ": "))

    subprocess.run("clear")

