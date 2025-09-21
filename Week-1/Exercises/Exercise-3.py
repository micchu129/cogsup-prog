################################################################################
"""
Recommended readings: 
  Chapter on lists: https://automatetheboringstuff.com/3e/chapter6.html 
  List comprehension: https://www.pythonforbeginners.com/basics/list-comprehensions-in-python
"""
################################################################################

"""
Exercise 3.1

Task:
------
Write code that prints the sum of the elements in the following list.
[1, 4, -6, 7, 2, 3, 9, 11, 6]
"""

lst = [1, 4, -6, 7, 2, 3, 9, 11, 6] # In all exercises in this script, you will work with this list

print("Exercise 3.1")

sum = 0

for i in lst:
    sum = sum+i
print(sum)

pass

print("---")

"""
Exercise 3.2

Task:
------
Print the product of the elements in the list.
"""

print("Exercise 3.2")

product = 1

for i in lst:
    product = product*i
print(product)

pass

print("---")

"""
Exercise 3.3

Task:
------
Print the sum of the squares of the list.
"""

print("Exercise 3.3")

sq_sum = 0

for i in lst:
    sq_sum = sq_sum+i**2

print(sq_sum)

pass

print("---")

"""
Exercise 3.4

Task:
------
Print the largest element of the list.
"""

print("Exercise 3.4")

print(max(lst))

pass

print("---")

"""
Exercise 3.5

Task:
------
Print the largest element of the list.
"""

print("Exercise 3.5")

#assuming a typo, print smallest?

print(min(lst))

pass

print("---")