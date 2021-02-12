# Importing the real expresions package
import re
# Opening file and creating a handle
handle = open('Actual_Data.txt')
# Empty list for values throughout text
numlist = list()
# Code parsing out lines
for line in handle:
    line = line.strip()
    # Expression to extract num values
    y = re.findall('[0-9]+', line)
    # If we do not find any values we will continue through loop
    if len(y) == 0 : continue
    # Add values extracted from y into numlist
    numlist += y
print(numlist)

# Adding values of the list
sum = 0
for num in numlist:
    sum += int(num)
print(sum)
