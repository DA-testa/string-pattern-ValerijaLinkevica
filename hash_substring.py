# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    choice = input()

    if "F" in choice:
        filename = input()

        if "a" in filename:
            return("Incorrect file name")

        useFile = 'tests/' + filename
        file1 = open(useFile, 'r')
        lines = file1.readlines()

        pattern = lines[0]
        text = lines[1]

    elif "I" in choice:
        # input from keyboard
        pattern = input().rstrip()
        text = input().rstrip()
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return (pattern, text)

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    indexes = []
    alphabet_len = 256
    pattern_len = len(pattern)
    text_len = len(text)
    pattern_hash_val = 0
    text_hash_val = 0
    i = 0
    j = 0
    q = 7
    h = 1

    for i in range(pattern_len - 1):
        h = (h * alphabet_len) % q

    for i in range(pattern_len):
        pattern_hash_val = (alphabet_len * pattern_hash_val + ord(pattern[i])) % q
        text_hash_val = (alphabet_len * text_hash_val + ord(text[i])) % q
 
    for i in range(text_len - pattern_len + 1):
        if pattern_hash_val == t:
            for j in range(pattern_len):
                if text[i + j] != pattern[j]:
                    break
                else:
                    j += 1

            if j == pattern_len:
                indexes.add(str(i))

        if i < text_len - pattern_len:
            text_hash_val = (alphabet_len * (text_hash_val - ord(text[i]) * h) + ord(text[i + pattern_len])) % q

            if text_hash_val < 0:
                text_hash_val = text_hash_val + q

    return indexes


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

