# Importing the real expressions package
import re

# Opening the file
x = open('Sample_Data.txt')

# Empty list
numlist = list()

# Iterating through the lines in the text file
for line in x:
    # Clear whitespace in each line
    line = line.strip()
    # Use real expression function to extract one or more digits
    y = re.findall('[0-9]+', line)
    # If we find nothing in that lines continue
    if len(y) == 0 : continue
    # Add values extracted from y into numlist
    numlist += y
print(numlist)

# Calculating the average
sum = 0
for num in numlist:
    sum += int(num)
print(sum)
