#!/usr/bin/python3

"""
    a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """This function iterates through a matrix & divides by div"""
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    elif div == 0:
        raise ZeroDivisionError('division by zero')
    for i in range(len(matrix)):
        if len(matrix[0]) != len(matrix[i]):
            raise TypeError('Each row of the matrix must have the same size')
        for j in range(len(matrix[i])):
            length = len(matrix[i])
            if type(matrix[i][j]) is not int and type(matrix[i][j]) is not float:
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    #generate matrix to list
    temp = [num for elem in matrix for num in elem]
    #divide through by div
    temp = [round(x / div, 2) for x in temp]
    #regenerate list to matrix
    new_list = [temp[p:p+length] for p in range(0,len(temp),length)]
    return new_list
