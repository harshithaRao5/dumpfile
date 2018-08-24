'''program for checking various conditions in game'''
def tic_tac_toe(matrix):
    '''function for playing Tictactoe game'''
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
    if len(result) == []:
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
    for _ in range(0, 3):
        matrix.append(input().split())
    tic_tac_toe(matrix)
if __name__ == '__main__':
    main()
