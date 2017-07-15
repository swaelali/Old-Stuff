# Light out Puzzle Solution ALGORITHM
# Solution of Light out puzzle up to 3x3

from GF2 import *

def combine(puzz_matrix):
    ''' Return a list of all possible combinations according following constraints:
        - no repeation
        - don't care of the sequence of the numbers'''
    
    buttons = len(puzz_matrix)*len(puzz_matrix[0])
    phase = 1
    main_combination=[]
    combinations = []
    while phase < buttons:
        if phase == 1:
            for x in range(1,buttons +1):
                main_combination.append(x)
                combinations = main_combination.copy()
            phase +=1
        else:
            temp_combinations = combinations.copy()
            for i in range(len(main_combination)):
                for x in range(len(combinations)):
                    temp = int(str(main_combination[i])+str(combinations[x]))
                    temp_combinations.append(temp)


            #Flterations
            repeat = buttons
            while repeat !=0:
                for element in temp_combinations:
                    temp_element= str(element)
                    for x in temp_element:
                        if temp_element.count(x)%2 == 0:
                            temp_combinations.remove(element)
                            break
                repeat -=1

            # inner sorting
            comp_element = ''
            temp_element_list = []
        
            temp_temp_combinations = []
            for element in temp_combinations:
                    temp_element= str(element)
                    for x in temp_element:
                        temp_element_list.append(int(x))
                        temp_element_list.sort()
                    for pointer in range(len(temp_element_list)):
                        comp_element = comp_element+str(temp_element_list[pointer])
                    
                    temp_temp_combinations.append(int(comp_element))
                    comp_element = ''
                    temp_element_list = []
        
            temp_combinations = temp_temp_combinations.copy()                
                                
            combinations = list(set(temp_combinations)).copy()
            combinations.sort()
            phase +=1
    return combinations


def assign_matrix_elements(puzz_matrix):
    ''' Return dictionary with pairs of poisition as key and the corresponding of
        this poistion in matrix_puzz as value'''
    assignment_dic={(x,y):one for x in range(len(puzz_matrix)) for y in range(len(puzz_matrix[0]))} 
    return assignment_dic


def get_buttons_vectors(puzz_matrix):
    ''' Return a dictionary of buttons as keys and corresponding vectors (dictionary) as values'''
    buttons = len(puzz_matrix)*len(puzz_matrix[0])

    buttons_vectors ={}
    
    matrix_pairs = assign_matrix_elements(puzz_matrix)
    button_position_dic={}
    position_corresponding_map_dic = {}
    
    max_row = len(puzz_matrix)
    max_col = len(puzz_matrix[0])
    row = 0
    col = 0
    button = 1
    while button < (buttons +1):
        for row in range(max_row):
            for col in range(max_col):
                button_position_dic[button]=(row,col)
                button +=1
    temp_set =set()
    for x in range(max_row):
        for y in range(max_col):
            temp_set.add((x,y))
            if x+1 < max_row:
                temp_set.add((x+1,y))
            if x-1 >=0:
                temp_set.add((x-1,y))
            if y+1 < max_col:
                temp_set.add((x,y+1))
            if y-1 >=0:
                temp_set.add((x,y-1))
				
            position_corresponding_map_dic[(x,y)]=temp_set
            temp_set = set()
    
    for button in button_position_dic.keys():
        buttons_vectors[button]= {x:matrix_pairs[x] for x in position_corresponding_map_dic[button_position_dic[button]]}
        
    return buttons_vectors



def Check(combination,vectors_dic,puzz_matrix):
    temp_matrix=puzz_matrix.copy()
    extacted_vector ={}
    
    pointing_seq = str(combination)
    for button in pointing_seq:
        button = int(button)
        extracted_vector= vectors_dic[button]
       

        for x in range(len(temp_matrix)):
            for y in range(len(temp_matrix[0])):
                if (x,y) in extracted_vector.keys():
                    temp_matrix[x][y] = temp_matrix[x][y]+extracted_vector[(x,y)]
        

    # Checking 
    for x in range(len(temp_matrix)):
            for y in range(len(temp_matrix[0])):
                if temp_matrix[x][y] == 0:
                    temp_matrix=[]
                    return False
    temp_matrix=[]
    return True
    
    
# Demonstration
original_matrix = [[0,0,one],[one,0,one],[0,one,0]]
print("Combining ...")

combinations = combine(original_matrix)
print(len(combinations)," combinations found!")
print('Solving...')
vectors_dic = get_buttons_vectors(original_matrix)

for combination in combinations:
    
    original_matrix = [[0,0,one],[one,0,one],[0,one,0]]
    
    if Check(combination,vectors_dic,original_matrix):
        print("Solution obtained! use that sequence ",combination)
        break
    


        
    
