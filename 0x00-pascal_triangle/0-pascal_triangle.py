#!/usr/bin/python3
"""Create a pascal triangle based on input (n)"""


def pascal_triangle(n):
    """Create a 2D list of pascal triangle"""
    triangle = []

    if n <= 0:
        return triangle

    ind = 0
    inner_triangle = []
    while ind < n:
        if ind == 0:
            inner_triangle.append(1)
            triangle.append(inner_triangle)
            ind += 1
            continue

        temp = []
        start = 0

        while start <= len(inner_triangle):
            if start == 0:
                temp.append(1)
                start += 1
                continue
            if start == len(inner_triangle):
                temp.append(1)
                start += 1
                continue
            temp.append(inner_triangle[start] + inner_triangle[start - 1])
            start += 1

        inner_triangle = temp
        triangle.append(inner_triangle)
        ind += 1

    return triangle
