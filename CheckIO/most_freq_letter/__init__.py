def checkio(text):

    chars = "abcdefghijklmnoqrstuvwxyz"
    freqs={}
    text = text.lower()
    text = text.strip()

    for char in chars:
        freqs[char] = text.count(char)
    f_chars = sorted(freqs.keys())
    f_vals = sorted(freqs.values())
    max_freq = f_vals.pop()
    for s_char in f_chars:
        if freqs[s_char] == max_freq:
            return s_char

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")