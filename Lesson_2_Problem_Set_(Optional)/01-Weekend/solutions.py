# From the README:
# We do NOT accept pull requests that have deleted another contributer's hint or solution without a very clear reason
# ALL solutions must be clearly documented
# ALL solutions must actually work
# ONLY use concepts covered in the class so far

# There are two solutions below. 
# The second one is maybe more suited to the material given so far while the first one has less lines
def weekend(day):
    return day =='Saturday' or day == 'Sunday'


# Another method
def weekend(day):
    if (day) == 'Saturday':
        return True
    if (day) == 'Sunday':
        return True
    else:
        return False
