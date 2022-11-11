#python code to roll a dice 1000 times and dispaly frequency and percentage
#author
#Francis wanjagi


# import rnadom module for generating random values
import random
import math

#Create a list of the faces of a die
faces = [1, 2, 3, 4, 5, 6]

#This line creates a list of six zeros. This list will be used to store the number of times each face is rolled.
counts = [0, 0, 0, 0, 0, 0]

#This loop generates a random number from 1 to 6 1000 times. For each number, it
#increments the count for that face in the counts list.
for i in range(1000):
    face = random.choice(faces)
    counts[face-1] += 1

#This loop prints the results. The enumerate function gives us the index and value of each
#element in the counts list.
print("Face", " ", "Frequency", " ", "Percentage")
totalF = 0
totalP = 0
for i, count in enumerate(counts):
    print(i+1, "|   ", count, " |   ", round((count/1000)*100, 2), "%")
    totalF += count
    totalP += round((count/1000)*100, 2)
print("________________________")
print("Total", totalF, "     ", round(totalP), "%")