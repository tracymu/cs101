# Please write SOLUTIONS here

# From the README:
# We do NOT accept pull requests that have deleted another contributer's hint or solution without a very clear reason
# ALL solutions must be clearly documented
# ALL solutions must actually work
# ONLY use concepts covered in the class so far

def cached_execution(cache, proc, proc_input):
  if not proc_input in cache:    # Check for the proc_input in the cache (dictionary)
      cache[proc_input]= proc(proc_input) #If it isn't in there, add a new entry to the dictionary 'cache'
  return cache[proc_input] # Whether it was already in there, or just added, you can now return the value for that key 'proc_input'

