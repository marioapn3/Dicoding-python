print(float(5))

"""
Output:
5.0
"""

print(int(5.6))
print(int(-5.6)) 

""" 
Output:
5
-5
"""

print(int("25"))
print(str(25))
print(float("25"))
print(str(25.6))

"""
Output:
25
25
25.0
25.6
"""


# print(int("1p"))

# """
# Output:
# ValueError: invalid literal for int() with base 10: '1p
# """

print(set([1,2,3]))
print(tuple({5,6,7}))
print(list('hello'))

"""
Output:
{1,2,3}
(5,6,7)
['h','e','l','l','o']
"""

print(dict([[1,2],[3,4]]))

"""
Output:
{1:2, 3:4}
"""

print(dict([(3,26),(4,44)]))

"""
Output:
{3:26, 4:44}
"""