# Slicing
# sequence[start:stop:step]

# Start merupakan indeks pertama yang Anda ambil. 
# Stop merupakan indeks terakhir yang ingin Anda ambil.
# Step merupakan jumlah elemen yang ingin Anda lewati di antara setiap elemen slice. 
# Secara default, nilai step adalah 1.

x = ["laptop", "monitor", "mouse", "mousepad", 
"keyboard", "webcam", "microphone"]

# Mulai dari index ke 0 berhenti di index ke 5 dan step 2
print(x[0:5:2])
# Mulai dari index ke 1 berhenti di index ke 6 
print(x[1:]) 
# step 3
print(x[:3])

"""
Output:
['laptop', 'mouse', 'keyboard']
['monitor', 'mouse', 'mousepad', 'keyboard', 'webcam', 'microphone']
['laptop', 'monitor', 'mouse']

"""