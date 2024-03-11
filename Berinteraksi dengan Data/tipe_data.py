x = 6
print(type(x))

x = 6.0
print(type(x))

x = 1+2j
print(type(x))


"""
Output:
<class 'int'>
<class 'float'>
<class 'complex'>
"""


var = 10
print(var)
print(id(var))
var = 11
print(var)
print(id(var))

"""
Output:
10
<memory address>
11
<memory address>
"""


x = True
print(type(x))

x = False
print(type(x))

"""
Output:
<class 'bool'>
<class 'bool'>
"""

# String

x = 'Dicoding'
print(type(x))

"""
Output: 
<class 'str'>
"""

# Multi Line

multi_line = """Halo!
Kapan terakhir kali kita bertemu?
Kita bertemu hari Jum’at yang lalu."""

print(multi_line)

"""
Output:
Halo!
Kapan terakhir kali kita bertemu?
Kita bertemu hari Jum’at yang lalu.
"""

# Print Indekks String

x = 'Dicoding'
print(x[0])

""" 
Output:
D
"""

# Print Indexing dan Slicing

x = 'Dicoding'
print(x[2:])

"""
Output:
coding
"""

# Formatted String

name = "Perseus Evans"
print(f"Hello, nama saya {name}")
 
"""
Output: 
Hello, nama saya Perseus Evans
"""

# str.format()

name = "Perseus Evans"
print("Nama saya {}".format(name))
 
"""
Output: 
Nama saya Perseus Evans
"""
