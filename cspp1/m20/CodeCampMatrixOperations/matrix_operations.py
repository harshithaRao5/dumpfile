def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    mul_matrix = [[0 for row in range(len(m2[0]))] for column in range(len(m1))]
    if len(m1[0]) == len(m2):
        for i in range(len(m1)):
            for k in range(len(m2[0])):
                for j in range(len(m2)):
                    mul_matrix[i][k] += int(m1[i][j]) * int(m2[j][k])
        return mul_matrix
    else:
        print("Error: Matrix shapes invalid for mult")
        return None
    

def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        sum_matrix = [[0 for row in range(len(m1))] for column in range(len(m1[0]))]
        for i in range(len(m1)):
            for j in range(len(m1[0])):
                sum_matrix[i][j] = int(m1[i][j]) + int(m2[i][j])
        return sum_matrix
    else:
        print("Error: Matrix shapes invalid for addition")
        return None
   
def read_matrix(m1, m2):
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''

    


def main():
    # read matrix 1
    rows_columns = []
    for i in range(1):
        rows_columns += input().split(',')
    n_1 = int(rows_columns[0])
    matrix_1 = []
    for _ in range(n_1):
        matrix_1.append(list(map(int, input().rstrip().split())))
    #print(matrix_1)
    # read matrix 2
    rows_columns1 = []
    for i in range(1):
        rows_columns1 += input().split(',')
    n_2 = int(rows_columns1[0])
    matrix_2 = []
    for _ in range(n_2):
        matrix_2.append(list(map(int, input().rstrip().split())))
    #print(matrix_2)

    # add matrix 1 and matrix 2
    print(add_matrix(matrix_1, matrix_2))

    # multiply matrix 1 and matrix 2
    print(mult_matrix(matrix_1, matrix_2))
    

if __name__ == '__main__':
    main()
