#!/usr/bin/python3

def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = []

        row.append(1)

        if i > 1:
            for j in range(1, i):
                value = triangle[i - 1][j - 1] + triangle[i - 1][j]
                row.append(value)

        if i > 0:
            row.append(1)

        triangle.append(row)
    return triangle