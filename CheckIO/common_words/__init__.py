def checkio(first, second):
    first_list = first.split(',')
    second_list = second.split(',')
    common = [word for word in first_list if word in second_list]
    common = sorted(common)
    common = str(common)
    common = common.replace("[", "")
    common = common.replace("]", "")
    common = common.replace("'", "")
    common = common.replace(" ", "")
    return common
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
