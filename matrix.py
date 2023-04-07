# def reshape_matrix(matrix, r, c):
#     '''
#     INPUT: Two dimensional list, and number of rows and columns of reshaped matrix
#     OUTPUT: Reshaped matrix
#     '''
#     if r*c != len(matrix)*len(matrix[0]):
#         return matrix
        
#     reshaped = []
#     new_row = []
#     for row in matrix:
#         for item in row:
#             new_row.append(item)
#             if len(new_row) == c:
#                 reshaped.append(new_row)
#                 new_row = []
#     return reshaped

def one_list_to_matrix(target_list, c):
    if len(target_list) == c:
        return target_list
    new_list = target_list[0:c]

    return new_list, one_list_to_matrix(target_list[c:], c)

def reshape_matrix(matrix, r, c):
    '''
    INPUT: Two dimensional list, and number of rows and columns of reshaped matrix
    OUTPUT: Reshaped matrix
    '''
    orig_c = 0 
    orig_r = 0
    for column in matrix[0]: #n
        orig_c+=1
    for row in matrix: #m --> n
        orig_r +=1

    if orig_c*orig_r != r*c:
        return matrix

    target_list = [] #space n
    
    for row in matrix: #m*n --> n^2
        for element in row: #(the n in the line above)
            target_list.append(element)
    
    new_matrix = list(one_list_to_matrix(target_list, c)) #n #space n^2

    if not isinstance(new_matrix[0], list):
        return [new_matrix]
        
    return new_matrix


print(reshape_matrix(
    [[7, 2, 1],
     [4, 3, 5],
     [6, 9, 8]], 9, 1))