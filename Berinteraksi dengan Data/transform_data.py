kata = 'dicoding'
kata = kata.upper()
print(kata)

"""
Output:
DICODING
"""


kata = 'DICODING'
kata = kata.lower()
print(kata)

"""
Output:
dicoding
"""


print("Dicoding          ".rstrip())

"""
Output:
Dicoding
"""


print("           Dicoding".lstrip())

"""
Output:
Dicoding
"""



print("         Dicoding          ".strip())

"""
Output:
Dicoding
"""



kata = 'CodeCodeDicodingCodeCode'
print(kata.strip("Code"))

"""
Output:
Dicoding
"""


print('Dicoding Indonesia'.startswith('Dicoding'))

"""
Output:
True
"""


print('Dicoding Indonesia'.endswith('Dicoding'))

"""
Output:
False
"""


print(' '.join(['Dicoding','Indonesia', '!']))

"""
Output:
Dicoding Indonesia !
"""


print('123'.join(['Dicoding','Indonesia']))

"""
Output:
Dicoding123Indonesia
"""


print('Dicoding Indonesia !'.split())

"""
Output:
['Dicoding','Indonesia','!']
"""


print('''Halo,
aku ikan,
aku suka sekali menyelam
aku tinggal di perairan.
Badanku licin dan renangku cepat.
Senang berkenalan denganmu.'''.split('\n'))

"""
Output:
['Halo,', 'aku ikan,', 'aku suka sekali menyelam', 'aku tinggal di perairan.', 'Badanku licin dan renangku cepat.', 'Senang berkenalan denganmu.']
"""


string = "Ayo belajar Coding di Dicoding"
print(string.replace("Coding", "Pemrograman"))

"""
Output:
Ayo belajar Pemrograman di Dicoding
"""


kata = 'DICODING'
print(kata.isupper())

"""
Output:
True
"""


kata = 'dicoding'
print(kata.islower())

"""
Output:
True
"""


kata = 'dicoding'
print(kata.isalpha())

"""
Output:
True
"""

kata = 'dicoding123'
print(kata.isalnum())

"""
Output:
True
"""



print('123'.isdecimal())

"""
Output:
True
"""


print('         '.isspace())

"""
Output:
True
"""


print('Dicoding Indonesia'.istitle())

"""
Output:
True
"""


teks = 'Code'
tambah_number = teks.zfill(5)
print(tambah_number)

"""
Output:
0Code
"""



print('Dicoding'.rjust(20))

"""
Output:
            Dicoding

"""


print('Dicoding'.rjust(20, '!'))

"""
Output:
!!!!!!!!!!!!Dicoding
"""



print('Dicoding'.ljust(20))

"""
Output:
Dicoding            '
"""


print('Dicoding'.center(10, '-'))

"""
Output:
-Dicoding-

"""


