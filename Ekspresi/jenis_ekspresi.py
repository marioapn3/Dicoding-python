# Ekspresi Menurut Arity dari Operator
# Jenis	Contoh
# Biner

# (x + y), (x - y), (x * y), (x / y), (x ** y), (x < y), (x <= y), (x > y), (x >= y), (x % y), (x == y), (x != y).

# Uner

# (x += 1), (x-=1), (not x).


a = True
a = not a
print(a)

b = 6
b -= 1
print(b)

c = 6
c += 1
print(c)

d = 10
print(-d)

"""
Output:
False
5
7
-10
"""

print(2+2)
print(3<10)
print(True or False)

"""
Output:
4
True
True
"""

x = 11
y = 5

print(x + y)
print(x - y)
print(x * y)
print(x // y)
print(x / y)
print(x % y)
print(x ** y)

"""
Output:

16
6
55
2
2.2
1
161051
"""


x = 5
y = 10

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

"""
Output:

False
True
False
True
False
True
"""


x = "Dicoding"
y = "Indonesia"

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

"""
Output:

False
True
False
True
False
True
"""