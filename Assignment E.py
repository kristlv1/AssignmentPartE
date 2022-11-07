# Importing libaries and setting up necessary variables
import numpy as np
import random
import string
import matplotlib.pyplot as plt
iteration = 0
generation = []
results = []
letters = string.ascii_lowercase + " " + string.ascii_uppercase
highestFitness = []


# User variables (can all be changed)
name = "Genetic Algorithms"       # Key string (the one that will be found)
population = 25                   # number of instances per generation
mRate = 500                       # Mutation chance %
mSize = 4                        # Num of possible mutations
cutoff = 10000                    # Max itterations in while loop

# Creates first generation (random names)
for i in range(population):
    generation.append("".join(random.choice(letters) for j in range(len(name))))


# ---------------
#  All functions
def fitness(input):
    fitnessScore = 0
    for i in range(len(name)):
        if input[i] == name[i]:
            fitnessScore += 1
    return fitnessScore / len(name)

def populate(genlist, x):
    genFoo = [""] * x
    for i in range(1, len(genlist) + 1):
        for j in range(1, x + 1):
            if j % i == 0:
                genFoo[j - 1] = mutation(genlist[i - 1], mRate, mSize)
    return genFoo

def sortgen(gen, res):
    temp = sorted(zip(res, gen))
    return temp[-1], temp[-2]

def mutation(guess, rate, n):
    foo = []
    foo[:0] = guess
    #letters = string.ascii_lowercase + " "
    for i in range(n):
        digit = random.randint(0, len(name) - 1)
        chance = random.randint(1, 100)
        if chance <= rate:
            foo[digit] = "".join(random.choice(letters))
    return "".join(foo)

def scramble(a, b):
    outA = []
    outB = []
    for i in range(len(name)):
        if bool(random.getrandbits(1)):
            outA.append(b[i])
            outB.append(a[i])
        else:
            outA.append(a[i])
            outB.append(b[i])
    return "".join(outA), "".join(outB)

# ----------------------------------------------------------------
# Main loop for running the program (until cutoff or string found)
while iteration < cutoff:
    for i in range(population):
        results.append(fitness(generation[i]))
    best = sortgen(generation, results)

    if best[-1][0] == 1:
        print("Generation: " + str(iteration) + ".   String found: " + str(best[-1][1]))
        highestFitness.append(1)
        iteration += 1
        break

    print("Generation no: " + str(iteration) + ".   Highest fitness: " + f'{best[-1][0]:.3f}' + "  Closest guess this generation: " + str(best[-1][1]))

    maxFitness = round(best[-1][0], 3)
    highestFitness.append(maxFitness)
    scrambled = scramble(best[0][1], best[1][1])
    results = []
    generation = populate(scrambled, population)
    iteration += 1


# --------------------------------------------------------------------------------
# Plots a performance graph showing the highest fitness level for every generation
t = np.arange(0, iteration, 1)
fig, ax = plt.subplots()
ax.plot(t, highestFitness)
ax.set(xlabel='Generations', ylabel='Highest fitness',
       title='Performance graph')
ax.grid()
fig.savefig("Performance.png")
plt.show()




