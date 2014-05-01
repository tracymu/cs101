# Please write SOLUTIONS here

# From the README:
# We do NOT accept pull requests that have deleted another contributer's hint or solution without a very clear reason
# ALL solutions must be clearly documented
# ALL solutions must actually work
# ONLY use concepts covered in the class so far

def cached_execution(cache, proc, proc_input):
    if not proc_input in cache:
        cache[proc_input] = proc(proc_input)
    return cache[proc_input]