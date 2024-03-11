kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort()

print(kendaraan)

"""
Output:
 ['helikopter', 'mobil', 'motor', 'pesawat']
"""

kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort(reverse=True)

print(kendaraan)

"""
Output:
 ['pesawat', 'motor', 'mobil', 'helikopter']

"""

urutan = ['Dicoding', 1, 2, 'Indonesia', 3]
urutan.sort()

print(urutan)

"""
Output:
TypeError: '<' not supported between instances of 'int' and 'str'
"""

# Metode sort menggunakan urutan ASCII sehingga nilai huruf kapital (uppercase) akan lebih dahulu dibandingkan huruf kecil (lowercase).
kendaraan = ['motor', 'mobil', 'helikopter', 'Pesawat']
kendaraan.sort()

print(kendaraan)

"""
Output:
['Pesawat', 'helikopter', 'mobil', 'motor']
"""