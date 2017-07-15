def no_pig(x):
    result =0
    while x >= 1:
        result = result + x-1
        x -= 1
    return result
def recsum(x):
    if x <= 2:
        return x
    else:
        return x+recsum(x-1)
def stage_adder(stage):
    adder =0
    multplier=0
    while stage >= 2:
        adder = adder + stage*multplier
        multplier +=1
        stage -=1
    return adder

def checkio(number):
    if number ==1:
        return 1
    stage=1
    while True:
        stage +=1 
        n=0
        print "stage: ",stage
        for n in range(recsum(stage)+1): 
            count = stage + stage_adder(stage) +n 
            if count == number:
                if n <= no_pig(stage)-1:
                    return no_pig(stage) 
                else:
                    return no_pig(stage) + n - no_pig(stage)+1
print checkio(27)

    
