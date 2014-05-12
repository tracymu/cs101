### Please write HINTS here
From the README:
- We do NOT accept pull requests that have deleted another contributer's hint or solution thout a very clear reason
- ONLY use concepts covered in the class so far
- Do NOT give solutions here - ONLY hints

### Directions from the question:
Define a procedure, `cached_execution(cache, proc, proc_input)`, that takes in three inputs: a `cache`, which is a Dictionary that maps inputs to `proc` to their previously computed values, a procedure, `proc`, which can be called by just writing `proc(proc_input)`, and `proc_input` which is the input to `proc`. Your procedure should return the value of the `proc` with input `proc_input`, but should only evaluate it if it has not been previously called.


### Hints:
For this question we're going to make our own cache. From [Wikipedia](http://en.wikipedia.org/wiki/Cache_(computing)): "In computing, a cache is a component that transparently stores data so that future requests for that data can be served faster."

Our cache will be used to look up the outputs of a particular function (the `proc` inputs) faster by storing the inputs (`proc_input`) and outputs (`proc(proc_input)`) in a dictonary.

The keys for the dictory should be the `proc_inputs`, the values should the results of `proc(proc_input)`.

The point of the cache is to only compute the result once for a given input. You'll need to check your `cache` for `proc_input` before computing `proc(proc_input)`.
