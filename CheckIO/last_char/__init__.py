import re
def checkio(words_set):
    for word1 in words_set:
        nwords_set = words_set.copy()
        nwords_set.remove(word1)
        for word2 in nwords_set:
            if len(word1) == len(word2):
                if word1 == word2:
                    return True
            else:
                match = re.search(word2,word1)
                if match:
                    if word2[-1] == word1[-1]:
                        return True
                
    return False
#These "asserts" using only for self-checking and not necessary for auto-testing

if __name__ == '__main__':
    assert checkio({"hello", "lo", "he"}) == True, "helLO"
    assert checkio({"hello", "la", "hellow", "cow"}) == False, "hellow la cow"
    assert checkio({"walk", "duckwalk"}) == True, "duck to walk"
    assert checkio({"one"}) == False, "Only One"
    assert checkio({"helicopter", "li", "he"}) == False, "Only end"
   
