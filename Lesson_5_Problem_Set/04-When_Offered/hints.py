# Please write HINTS here

# From the README:
# We do NOT accept pull requests that have deleted another contributer's hint or solution without a very clear reason
# ONLY use concepts covered in the class so far
# Do NOT give solutions here - ONLY hints



#When looking at problems using dictionaries, you might find it useful to print out the different elements to understand where you are in the code.

#For example:

#Print out courses:
def when_offered(courses,course):
    return courses

print when_offered (courses, 'cs101')

#Print out elements inside courses:
def when_offered(courses,course):
    for hexamester in courses:
        print hexamester

when_offered (courses, 'cs101')

#Print out hashes inside courses:
def when_offered(courses,course):
    for hexamester in courses:
        print courses[hexamester]

when_offered (courses, 'cs101')

