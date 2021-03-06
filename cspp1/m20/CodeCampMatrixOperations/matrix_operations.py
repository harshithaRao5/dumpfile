'''matrix operations'''
def mult_matrix(matrix_1, matrix_2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    mul_matrix = [[0 for row in range(len(matrix_2[0]))] for column in range(len(matrix_1))]
    if len(matrix_1[0]) == len(matrix_2):
        for i in range(len(matrix_1)):
            for k in range(len(matrix_2[0])):
                for j in range(len(matrix_2)):
                    mul_matrix[i][k] += int(matrix_1[i][j]) * int(matrix_2[j][k])
        return mul_matrix
    else:
        print("Error: Matrix shapes invalid for mult")
        return None
def add_matrix(matrix_1, matrix_2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    if len(matrix_1) == len(matrix_2) and len(matrix_1[0]) == len(matrix_2[0]):
        sum_matrix = [[0 for row in range(len(matrix_1[0]))] for column in range(len(matrix_1))]
        for i in range(len(matrix_1)):
            for j in range(len(matrix_1[0])):
                sum_matrix[i][j] = int(matrix_1[i][j]) + int(matrix_2[i][j])
        return sum_matrix
    else:
        print("Error: Matrix shapes invalid for addition")
        return None
def read_matrix(rows_columns):
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    matrix_1 = []
    for _ in range(0, int(rows_columns[0])):
        column = input().split()
        if len(column) == int(rows_columns[1]):
            matrix_1.append(column)
        else:
            print("Error: Invalid input for the matrix")
            return None
    return matrix_1
def main():
    '''main function'''
    # read matrix 1
    num_rows_columns = input()
    rows_columns = num_rows_columns.split(',')
    matrix_1 = read_matrix(rows_columns)
    # read matrix 2
    num_rows_columns = input()
    rows_columns1 = num_rows_columns.split(',')
    matrix_2 = read_matrix(rows_columns1)
    if matrix_1 != None and matrix_2 != None:
    # add matrix 1 and matrix 2
        print(add_matrix(matrix_1, matrix_2))
    # multiply matrix 1 and matrix 2
        print(mult_matrix(matrix_1, matrix_2))
if __name__ == '__main__':
    main()
