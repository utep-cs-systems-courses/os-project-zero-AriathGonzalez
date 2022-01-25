import sys   # Command line arguments
import os    # Checking if file exists
import re

# Set Input and Output files
if (len(sys.argv) is not 3):
    print("Correct usage: wordCount.py <inputFile> <outputFile")
    
inputFile = sys.argv[1]
outputFile = sys.argv[2]

# Check if programs exist
if not os.path.exists(inputFile):
    print ("Input file does not exist!")
    exit()

if not os.path.exists(outputFile):
    print ("Output file does not exist!")
    exit()
    
# Unique words
words = {}

# Open, Read, and Close file
with open(inputFile, 'r') as file:
    for line in file:
        # Get count for unique words
        for word in re.findall(r"[\w]+",line):
            # Ensure only letters and convert to lowercase
            lowerWord = ''.join(char for char in word if char.isalpha())
            lowerWord = lowerWord.lower()
            
            if (lowerWord not in words):
                words[lowerWord] = 1
            else:
                words[lowerWord] += 1

# Alphabetically sort the unique words
sortedWords = sorted(words.items())

# Write to Output file
file = open(outputFile, 'w')

for word, number in sortedWords:
    strNum = str(number)
    file.write(word + " " + strNum + " \n")
file.close()
