#!/usr/bin/env python3
arr = [9, 8, 2, 3, 9, 4, 1, 0, 3]
arr1 = arr[:2]  # First two elements (0 to index 1, excluding 2) - Slicing the array using colon (:) operator
arr2 = arr[-5:]  # Last five elements (from index -5 to the end)
arr3 = arr[1:6]  # From index 1 (inclusive) to 6 (exclusive)
print("The first two numbers of the array are: {}".format(arr1))
print("The last five numbers of the array are: {}".format(arr2))
print("The 2nd through 6th numbers of the array are: {}".format(arr3))
