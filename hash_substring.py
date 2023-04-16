# python3


def read_input():
    choice = input()

    if "F" in choice:
        useFile = 'tests/06'
        file1 = open(useFile, 'r')
        lines = file1.readlines()

        pattern = lines[0].rstrip()
        text = lines[1].rstrip()

    elif "I" in choice:
        # input from keyboard
        pattern = input().rstrip()
        text = input().rstrip()

    return (pattern, text)


def print_occurrences(output):
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
        if pattern_hash_val == text_hash_val:
            for j in range(pattern_len):
                if text[i + j] != pattern[j]:
                    break
                else:
                    j += 1

            if j == pattern_len:
                indexes.append(str(i))

        if i < text_len - pattern_len:
            text_hash_val = (alphabet_len * (text_hash_val - ord(text[i]) * h) + ord(text[i + pattern_len])) % q

            if text_hash_val < 0:
                text_hash_val = text_hash_val + q

    return indexes


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))