x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }

print(type(x))

"""
Output:
<class 'dict'>
"""

# x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }

# print(x[0])

# """ 
# Output:
# KeyError: 0
# """

x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }

print(x ['name'])

""" 
Output:
Perseus Evans
"""

# 1 Menambah Data pada Dictionary

x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }
x ['Job'] = "Web Developer"

print(x)

"""
Output:
{'name': 'Perseus Evans', 'age': 20, 'isMarried': False, 'Job': 'Web Developer'}
"""

# 2 Menghapus Data pada Dictionary

x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }
del x['isMarried']

print(x)

"""
Output:
{'name': 'Perseus Evans', 'age': 20}
"""

# 3 Mengubah Data pada Dictionary
x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }
x ['name'] = "Dicoding"

print(x)

"""
Output:
{'name': 'Dicoding', 'age': 20, 'isMarried': False}
"""

