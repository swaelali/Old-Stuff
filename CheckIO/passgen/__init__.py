from random import randint
def generate(size):
    password =""   
    digit_pat ="0123456789"
    lower_pat ="abcdefghijklmnopqrstuvwxyz"
    upper_pat = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(size):
        pat_pointer = randint(1,3)
        if pat_pointer ==1:
            password = password+digit_pat[randint(0,9)]
        elif pat_pointer ==2:
            password = password+lower_pat[randint(0,25)]
        else:
            password = password+upper_pat[randint(0,25)]
    return password

if __name__ == '__main__':
    print generate(12)