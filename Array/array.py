
x = [1, 2, 3, 4, 5]
print(x)

"""
Output:
[1, 2, 3, 4, 5]
"""

import array

x = array.array("i",[1, 2, 3, 4, 5])
print(x)
print(type(x))

"""
Output:
array('i', [1, 2, 3, 4, 5])
<class 'array.array'>
"""

siswa = [90, 100, 50, 80, 85, 45, 80, 75, 50, 60]

print(siswa)
print(siswa[0])


"""
Output:
[90, 100, 50, 80, 85, 45, 80, 75, 50, 60]
90
"""

var_list = [1,2,3]
for elemen in var_list:
    print(id(elemen))

var_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(var_arr)

"""
Output:
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
"""

var_arr = [0 for i in range(10)]
print(var_arr)

"""
Output:
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
"""


var_arr = [0 for i in range(10)]

for i in range(10):
    var_arr[i] = i

print(var_arr)


"""
Output:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""


var_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(var_arr[0])

"""
Output:
9
"""