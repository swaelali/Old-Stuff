def checkio(data):
    data_val = ""
    data = str(data)
    while data !="":
        if len(data) == 4:
            if data[0] in "123":
                data_val = data_val+"M"*int(data[0])
                data = str(int(data) - 1000*int(data[0]))
                if int(data) == 0:
                    return data_val
        elif len(data) == 3:
            if data[0] in "123":
                data_val = data_val +"C"*int(data[0])
            elif data[0] in "4":
                data_val = data_val +"CD"
            elif data[0] in "5":
                data_val = data_val +"D"
            elif data[0] in "678":
                data_val = data_val +"D"+"C"*(int(data[0])-5)
            elif data[0] in "9":
                data_val = data_val +  "CM"
            data = str(int(data) - 100*int(data[0]))
            if int(data) == 0:
                    return data_val
        elif len(data)==2:
            if data[0] in "123":
                data_val = data_val +"X"*int(data[0])
            elif data[0] in "4":
                data_val = data_val +"XL"
            elif data[0] in "5":
                data_val = data_val +"L"
            elif data[0] in "678":
                data_val = data_val +"L"+"X"*(int(data[0])-5)
            elif data[0] in "9":
                data_val = data_val +  "XC"
            data = str(int(data) - 10*int(data[0]))
            if int(data) == 0:
                    return data_val
        elif len(data)==1:
            if data[0] in "123":
                data_val = data_val +"I"*int(data[0])
            elif data[0] in "4":
                data_val = data_val +"IV"
            elif data[0] in "5":
                data_val = data_val +"V"
            elif data[0] in "678":
                data_val = data_val +"V"+"I"*(int(data[0])-5)
            elif data[0] in "9":
                data_val = data_val +  "IX"
            data = str(int(data) - int(data[0]))
            if int(data) == 0:
                    return data_val

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
    print checkio(1335)
    print checkio(3888)