# Numeration of the string
import re


def check_brackets(string):
    ''' check if there are any brackets in the string ==> True or False'''
    match = re.search(r'\([\w.+-/^.*]+\)',string)
    if match:
        return True
    else:
        return False

def check_powers_roots(string):
    ''' check if there are any powers or roots in the string ==> True or False
    Caution: the powers and roots operator assigned is (^) '''
    match = re.search(r'([\w.]+)\^([\w.]+)',string)
    if match:
        return True
    else:
        return False

def check_mul_div(string):
    ''' check if there are any multiplications or division operations in the string ==> True or False'''
    match_mul = re.search(r'([\w.]+)\*([\w.]+)',string)
    match_div = re.search(r'([\w.]+)\/([\w.]+)',string)
    if match_mul or match_div :
        return True
    else:
        return False

def check_add_sub(string):
    ''' check if there are any additions or subtractions in the string ==> True or False'''
    match_add = re.search(r'([\w.]+)\+([\w.]+)',string)
    match_sub = re.search(r'([\w.]+)\-([\w.]+)',string)
    if match_add or match_sub:
        return True
    else:
        return False


def add_sub(string):
    if type(string) == type('string'):
        add_result = 0.0
        m_string = string
        
        while check_add_sub(m_string):
            match_add = re.search(r'([\w.]+)\+([\w.]+)',m_string)
            match_sub = re.search(r'([\w.]+)\-([\w.]+)',m_string)
            if match_add:
                print('adding ',match_add.group(1),'and ',match_add.group(2))
                mn = float(match_add.group(1))+float(match_add.group(2))
                m_string = m_string[:m_string.find(match_add.group(0))]+str(mn)+m_string[len(match_add.group(0))+m_string.find(match_add.group(0)):]
            elif match_sub:
                print('subtracting ',match_sub.group(2),'from ',match_sub.group(1))
                mn = float(match_sub.group(1))- float(match_sub.group(2))
                m_string = m_string[:m_string.find(match_sub.group(0))]+str(mn)+m_string[len(match_sub.group(0))+m_string.find(match_sub.group(0)):]
        try:
            add_result =float(m_string)     
            return add_result
        except:
            return m_string
    elif type(string) == type(1.0) or type(string) == type(1):
        return string
    else:
        IOError('invalid input')

def mul_div(string):
    if type(string) == type('string'):
        mul_result = 0.0
        m_string = string
        while check_mul_div(m_string):
            match_mul = re.search(r'([\w.]+)\*([\w.]+)',m_string)
            match_div = re.search(r'([\w.]+)\/([\w.]+)',m_string)
            if match_mul:
                print('multiplying ',match_mul.group(1),'by ',match_mul.group(2))
                mn = round(float(match_mul.group(1)) * float(match_mul.group(2)),3)
                m_string = m_string[:m_string.find(match_mul.group(0))]+str(mn)+m_string[len(match_mul.group(0))+m_string.find(match_mul.group(0)):]
            elif match_div:
                print('Dividing ',match_div.group(1),'by ',match_div.group(2))
                mn = round(float(match_div.group(1))/ float(match_div.group(2)),3)
                m_string = m_string[:m_string.find(match_div.group(0))]+str(mn)+m_string[len(match_div.group(0))+m_string.find(match_div.group(0)):]  
        try:
            add_result =float(m_string)     
            return add_result
        except:
            return m_string
             
    elif type(string) == type(1.0) or type(string) == type(1):
        return string
    else:
        IOError('invalid input')
        

def powers(string):
    if type(string) == type('string'):
        power_result = 0.0
        m_string = string
        while check_powers_roots(m_string):
            match_powers = re.search(r'([\w.]+)\^([\w.]+)',m_string)
            if match_powers:
                print('raising ',match_powers.group(1),'by power ',match_powers.group(2))
                mn = round(float(match_powers.group(1)) ** float(match_powers.group(2)),3)
                m_string = m_string[:m_string.find(match_powers.group(0))]+str(mn)+m_string[len(match_powers.group(0))+m_string.find(match_powers.group(0)):]

        try:
            power_result =float(m_string)     
            return power_result
        except:
            return m_string
             
    elif type(string) == type(1.0) or type(string) == type(1):
        return string
    else:
        IOError('invalid input')

def Brackets(string):
    if type(string) == type('string'):
        brackets_result = 0.0
        m_string = string
        while check_brackets(m_string):
            match_brackets = re.search(r'\([\w.+-/^.*]+\)',m_string)
            if match_brackets:
                expr_to_calculate = match_brackets.group()[1:-1]
                print('Calculating ',match_brackets.group())
                mn = round(float(add_sub(mul_div(powers(expr_to_calculate)))),3)
                m_string = m_string[:m_string.find(match_brackets.group())]+str(mn)+m_string[len(match_brackets.group())+m_string.find(match_brackets.group()):]

        try:
            brackets_result =float(m_string)     
            return brackets_result
        except:
            return m_string
             
    elif type(string) == type(1.0) or type(string) == type(1):
        return string
    else:
        IOError('invalid input')
        
def Numerate(string):
    ''' it takes some string input ===> return the numerical value of that string
    the periorties of performing operations are
    1- the brackets
    2- the powers and roots
    3- the multiplication and division
    4- the addition and subtraction'''
    try:
        value = add_sub(mul_div(powers(Brackets(string))))
    except:
        print('Error!')
    return value 
