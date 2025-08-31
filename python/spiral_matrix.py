"""
Given an m x n matrix, return all elements of the matrix in spiral order.
"""

from typing import List


def spiralOrder(matrix: List[List[int]]):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)

    while left < right and top < bottom:
        for i in range(left, right):
            print(matrix[top][i])
        top += 1
        for i in range(top, bottom):
            print(matrix[i][right - 1])

        right -= 1
        print("top: ", top, " bottom: ", bottom, " right: ", right, " left: ", left)
        if not (left < right and top < bottom):
            break
        for i in range(right - 1, left - 1, -1):
            print(matrix[bottom - 1][i])
        bottom -= 1

        for i in range(bottom - 1, top - 1, -1):
            print(matrix[i][left])
        left += 1

        print("top: ", top, " bottom: ", bottom, " right: ", right, " left: ", left)
    # i = j = 0
    # for i in range(len(matrix)):
    #     for j in range(len(matrix[0])):
    #         print(matrix[i][j])
    #         if j == len(matrix[0]):
    #             i += 1


matrix = [
    [1, 2, 3, 4]
    # [5, 6, 7, 8]
]
spiralOrder(matrix)
