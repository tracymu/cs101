# Please write SOLUTIONS here

def count_words(str):
    if str=="" or str==" ":
        return 0
    else:
        count=1
        for i in str:
            if i ==" ":
               count+=1
        return count
# From the README:
# We do NOT accept pull requests that have deleted another contributer's hint or solution without a very clear reason
# ALL solutions must be clearly documented
# ALL solutions must actually work
# ONLY use concepts covered in the class so far
