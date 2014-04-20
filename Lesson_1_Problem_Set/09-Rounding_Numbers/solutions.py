# Please write SOLUTIONS here

# From the README:
# We do NOT accept pull requests that have deleted another contributer's hint or solution without a very clear reason
# ALL solutions must be clearly documented
# ALL solutions must actually work
# ONLY use concepts covered in the class so far

# Add .5
# ex: 1 -> 1.5
# ex: 103.7 -> 104.2
x = x + .5
# Make x a string (so we can do string manipulation on it)
x = str(x)
# Find the position of the demimal point for your number
# ex: 1.5 -> decimal point is at position 1
# ex: 103.7 -> decimal point is at posiiton 3
point = x.find('.')
# only take the part of the string before the decimal point
# ex: 1
# ex: 104
print x[:point]