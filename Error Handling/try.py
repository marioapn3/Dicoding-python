z=0
try:
    print(1/z)
except ZeroDivisionError:
    print("Anda tidak bisa membagi angka dengan nilai nol.")

"""
Output:
Anda tidak bisa membagi angka dengan nilai nol.
"""

# try:
#      # kode yang mungkin menimbulkan exception
# except:
#      # kode yang akan dijalankan jika terjadi exception
# else:
#      # kode yang akan dijalankan jika tidak terjadi exception
# finally:
#      # kode yang akan dijalankan setelah blok try selesai, terlepas dari exception atau tidak

var_dict = {"rata_rata": "1.0"}

try:
    print(f"rata-rata adalah {var_dict['rata_rata']}")
except KeyError:
    print("Key tidak ditemukan.")
except TypeError:
    print("Anda tidak bisa membagi nilai dengan tipe data string")
else:
    print("Kode ini dieksekusi jika tidak ada exception.")
finally:
    print("Kode ini dieksekusi terlepas dari ada atau tidaknya exception.")
    
"""
Output:
rata-rata adalah 1.0
Kode ini dieksekusi jika tidak ada exception.
Kode ini dieksekusi terlepas dari ada atau tidaknya exception.
"""

var = -1
if var < 0:
    raise ValueError("Bilangan negatif tidak diperbolehkan")
else:
    for i in range(var):
        print(i+1)
    

"""
Traceback (most recent call last):
  File "/home/glot/main.py", line 3, in <module>
    raise ValueError("Bilangan negatif tidak diperbolehkan")
ValueError: Bilangan negatif tidak diperbolehkan
"""