'''program for checking various conditions in game'''
def Tic_Tac_Toe(matrix):
    '''function for playing TicTacToe game'''
    result = []
    for i in range(0, 3):
        if matrix[i][0] == matrix[i][1] == matrix[i][2]:
            result.append(matrix[i][0])
    for i in range(0, 3):
        if matrix[0][i] == matrix[1][i] == matrix[2][i]:
           result.append(matrix[0][i])
    if matrix[0][0] == matrix[1][1] == matrix[2][2]:
           result.append(matrix[0][0])
    if matrix[2][0] == matrix[1][1] == matrix[0][2]:
        result.append(matrix[0][2])
    if len(result) == 0:
        print('draw')
        return None
    if len(result) == 1:
        if result[0] == 'x' or result[0] == 'o':
           print(result[0])
        else:
           print("invalid input")
        return result[0]
    else:
        print("invalid game")
        return None
       
def main():
    '''main function '''
    matrix = []
    for i in range(0, 3):
        matrix.append(input().split())
    Tic_Tac_Toe(matrix)
if __name__ == '__main__':
    main()
