import numpy as np


def demoTest():
    i = 3
    x = 2

    array = [13, 22, 15]

    j = i + x

    k = i * x

    sum = 0
    for item in range(0, j):  # runs from 0-4
        sum += item

    print("sum :" + str(sum))
    print()


def matrixMultiplication():
    # 3x3 matrix
    X = [[12, 7, 3],
         [4, 5, 6],
         [7, 8, 9]]
    # 3x4 matrix
    Y = [[5, 8, 1, 2],
         [6, 7, 3, 0],
         [4, 5, 9, 1]]
    # result is 3x4
    result = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]

    print(np.array(X).shape)
    print()

    len(X)
    np.array(X).shape
    np.array(X).shape

    # iterate through rows of X
    for i in range(len(X)):
        # iterate through columns of Y
        for j in range(len(Y[0])):
            # iterate through rows of Y
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]

    for r in result:
        print(r)


#demoTest()
matrixMultiplication()
