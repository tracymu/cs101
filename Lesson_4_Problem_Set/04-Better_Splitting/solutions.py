# Solution by: Nadia Vu

def split_string(source,splitlist):
    words = []
    idx = 0
    word_begin = 0
    for char in source:
        # if the char is a separator
        if char in splitlist:
            # then if there are REAL char (aka non separator items) this handles the case when word_begin lands on a separator.
            if idx != word_begin:
                words.append(source[word_begin:idx])
            # update word begin to be the next character
            word_begin = idx+1
        idx+=1 # increment index regardless to move along the source.

    if idx != word_begin:
        words.append(source[word_begin:idx]) #this handles the case where there is no separator at the end

    return words

# Do you have another solution? Please add it here