# Please write SOLUTIONS here
# From the README:
# We do NOT accept pull requests that have deleted another contributer's hint or solution without a very clear reason
# ALL solutions must be clearly documented
# ALL solutions must actually work
# ONLY use concepts covered in the class so far

def count_words(str):

    if str=="" or str==" ": # Account for the case where there are no words in the string
        return 0
    else:
        count=1 #If the string isn't empty, or just a space, then there will be at least one word, so start count at 1
        for i in str:
        	# Go through the string, and every time you find a space, add to count.
            if i ==" ":
               count+=1
        return count

