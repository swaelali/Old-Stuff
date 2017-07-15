FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    output_str = ""
    str_no = str(number)
    while str_no != '':
        if len(str_no) == 3:
            output_str = output_str + FIRST_TEN[int(str_no[0])-1]+ ' ' + HUNDRED
            str_no = str(number - int(str_no[0])*100)
            if int(str_no) == 0:
                return output_str
            else:
                output_str = output_str +' '
        elif len(str_no) == 2:
            if int(str_no[0]) ==0:
                str_no = str(int(str_no))
            elif int(str_no[0]) !=1:
                output_str = output_str + OTHER_TENS[int(str_no[0])-2] 
                str_no = str(int(str_no) - int(str_no[0])*10)
                if int(str_no) == 0:
                    return output_str
                else:
                    output_str = output_str +' '
            else:
                output_str = output_str + SECOND_TEN[int(str_no[1])]
                return output_str
        elif len(str_no) ==1:
            if int(str_no) != 0:
                output_str = output_str + FIRST_TEN[int(str_no)-1]
                return output_str
            

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print checkio(4)
    print checkio(133)
    print checkio(12)
    print checkio(40)
    print checkio(101)
    print checkio(212)
    
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(40) == 'forty', "6th example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    
    