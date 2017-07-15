def checkio(data):
    digit_pat ="0123456789"
    lower_pat ="abcdefghijklmnopqrstuvwxyz"
    upper_pat = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    flag1=0
    flag2=0
    flag3=0
    for char in data:
        if char in digit_pat:
            flag1 =1
        elif char in lower_pat:
            flag2 =1
        elif char in upper_pat:
            flag3 =1
    if (len(data) >= 10) and (flag1+flag2+flag3 ==3): 
        return True
    else:
        return False

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Done")
