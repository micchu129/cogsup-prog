################################################################################
"""
Recommended readings: 
  Chapter on dictionaries: https://automatetheboringstuff.com/3e/chapter7.html 
  Iterating through dictionaries: https://realpython.com/iterate-through-dictionary-python/
"""
################################################################################

"""
Exercise 4.1

Task:
------
Print the sum of the values in the dictionary.
"""

dct = {'a': 3, 'b': 7, 'c': -2, 'd': 10, 'e': 5}

print("Exercise 4.1")

print(sum(dct.values()))
pass

print("---")

"""
Exercise 4.2

Task:
------
Print the key that has the largest value in dct.
"""

print("Exercise 4.2")

largest_val = 0
largest_key = str
for keys in dct:
      if dct[keys] > largest_val:
            largest_val = dct[keys]
            largest_key = keys
      else:
            pass
print(largest_key)

pass

print("---")

"""
Exercise 4.3

Task:
------
Create a new dictionary with the squares of all the values in dct.
"""

print("Exercise 4.3")

sq_dct = {}
for key, value in dct.items():
      sq_dct[(key+"_squared")] = value**2

print(sq_dct)

pass

print("---")

"""
Exercise 4.4

Task:
------
Print only the keys in dct whose values are even numbers.
"""

print("Exercise 4.4")

for key, value in dct.items():
      if value % 2 == 0:
            print(key)
      else: pass
#or alternatively if we want a list of even-keys
even_keys = []
for key, value in dct.items():
      if value % 2 == 0:
            even_keys.append(key)
      else: pass
print(even_keys)

pass

print("---")

"""
Exercise 4.5

Task:
------
Create a new dictionary that swaps the keys and values in dct.
"""
print("Exercise 4.5")

flip_dct = {}

for key, value in dct.items():
      flip_dct[value] = key

print(flip_dct)

pass

print("---")

"""
Exercise 4.6

Task:
------
Count the number of times each letter appears in the string 'ccctcctttttcc'
and print the resulting dictionary.
"""

s = 'ccctcctttttcc'

print("Exercise 4.6")

count_s = {}
for i in list(s):
     # print(i)
      if i not in count_s:
            #print("Key not present, initializing " + i)
            count_s[i] = 1
      elif i in count_s:
            #print("Key Exists, adding 1 to " + i)
            count_s[i] += 1
      #print(count_s)
      

print(count_s)


pass

print("---")

"""
Exercise 4.7

Task:
------
Given the dictionary of responses_mapping = {'j':'jazz', 'p':'pop'},
and the string responses = 'jjjpjjpppppjj',
print the list of corresponding words.
"""

responses_mapping = {'j':'jazz','p':'pop'}
responses = 'jjjpjjpppppjj'

print("Exercise 4.7")

mapped_reponses = []
for i in list(responses):
      mapped_reponses.append(responses_mapping[i])

print(mapped_reponses)

pass

print("---")

"""
Exercise 4.8

Task:
------
Merge the following two dictionaries into one:
{'a': 1, 'b': 2} and {'c': 3, 'd': 4}
"""

print("Exercise 4.8")

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}

d1.update(d2)
print(d1)

pass

print("---")

"""
Exercise 4.9

Task:
------
Starting from the dictionary {'zebra': 10, 'dolphin': 25, 'alligator': 3, 'monkey': 5, 'pig': 9},
create a new one whose keys are sorted alphabetically.
"""
animals = {'zebra': 10, 'dolphin': 25, 'alligator': 3, 'monkey': 5, 'pig': 9}

print("Exercise 4.9")

alphabetical_animals = {}
for key in sorted(animals.keys()):
      alphabetical_animals[key] = animals[key]

print(alphabetical_animals)

pass

print("---")

"""
Exercise 4.10

Task:
------
Starting from the dictionary {'zebra': 10, 'dolphin': 25, 'alligator': 3, 'monkey': 5, 'pig': 9},
create a new one whose values appear in increasing order.
"""

print("Exercise 4.10")

numerical_animals = {}
for key, value in sorted(animals.items(), key=lambda item: item[1]):
      numerical_animals[key] = value

print(numerical_animals)

pass

print("---")