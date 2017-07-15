#CheckIO Main Solution of Non-unique elements game
#=================================================
data = [10, 9, 10, 10, 9, 8]
for index in range(len(data)):
    if data.count(data[index]) == 1:
        data[index]="-"
for i in range(len(data)):
    try:
        data.remove("-")
    except:
        pass
print data