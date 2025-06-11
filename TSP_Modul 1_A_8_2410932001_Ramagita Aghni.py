nim = input("Masukkan NIM : ")
AB = int(nim[6: 8])
CD = int (nim[8: 10])

# Menentukan total biaya parkir AB motor dan CD mobil
# Menentukan biaya parkir 1 motor dan biaya parkir 1 mobil.

Determinan = 3 * 3 - 5 * 2
Motor = 3 * 16000 - 2 * 25000
Mobil = 3 * 25000 - 5 * 16000
Motor = Motor / Determinan
Mobil = Mobil / Determinan
total = Motor * AB + Mobil * CD

# Menampilkan Hasil
print("Jumlah Motor = ", AB)
print("Jumlah Mobil = ", CD)
print("Biaya Parkir 1 motor = ", Motor)
print("Biaya Parkir 1 mobil = ", Mobil)
print("Biaya parkir AB motor dan CD mobil = ", total)
