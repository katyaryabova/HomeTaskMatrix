from pprint import pprint
from random import randint

# 6 for entering
m = int(input("Enter Matrix size: "))
matrix_lst = [[randint(1, 50) for k in range(m)] for j in range(m)]
pprint(matrix_lst)


def illustration_matrix(matrix):
    tmp = [0] * len(matrix[0])
    for i in range(len(matrix)):
        for g in range(len(matrix[i])):
            print('{:>5}'.format(matrix[i][g]), end=' ')
            tmp[g] += matrix[i][g]
        print()
    print()

    for i in range(len(tmp)):
        print('{:>5}'.format(tmp[i]), end=' ')
    print()


print()


def sort_matrix(matrix):
    tmp = [0] * len(matrix[0])
    for i in range(len(matrix)):
        for g in range(len(matrix[i])):
            tmp[g] += matrix[i][g]
    for i in range(len(tmp)-1):
        for g in range (len(tmp)-1 - i):
            if tmp[g]>tmp[g+1]:
                tmp[g], tmp[g+1] = tmp[g+1], tmp[g]
                for a in range(len(matrix)):
                    matrix[a][g], matrix[a][g+1] = matrix[a][g+1], matrix[a][g]

    for j in range(len(matrix[0])):
        for a in range(len(matrix) - 1):
            for i in range(len(matrix) - 1 - a):
                if j % 2 == 0:
                    if matrix[i][j] > matrix[i + 1][j]:
                        matrix[i][j], matrix[i + 1][j] = matrix[i + 1][j], matrix[i][j]
                else:
                    if matrix[i][j] < matrix[i + 1][j]:
                        matrix[i][j], matrix[i + 1][j] = matrix[i + 1][j], matrix[i][j]


illustration_matrix(matrix_lst)
sort_matrix(matrix_lst)
illustration_matrix(matrix_lst)
