# Please write SOLUTIONS here

# From the README:
# We do NOT accept pull requests that have deleted another contributer's hint or solution without a very clear reason
# ALL solutions must be clearly documented
# ALL solutions must actually work
# ONLY use concepts covered in the class so far


def when_offered(courses,course):
    result = [] # The question asks you to return a list, so you should start with an empty one.
    for hexamester in courses: # Iterate through the first level within the courses
        # Check if course equals the course you are up to in your iteration.
        # Note that you need to say courses[hexamester] not just hexamester.
        # Hexamester will refer only to the top level item you are iterating on , it is just a name(e.g. apr2012)
        # courses[hexamester] is a key, and will return the relevant value, which is the rest of the dictionary.
        if course in courses[hexamester]:
            # Since you want a list of hexamesters as strings for the result, you can simply append hexamester
            result.append(hexamester)
    return result