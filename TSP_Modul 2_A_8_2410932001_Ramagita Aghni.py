# pemesanan tiket pesawat

kota_tujuan= str(input("Masukkan kota tujuan anda :"))
jenis_tiket= str(input("Apa jenis tiket yang akan anda beli? :"))

if kota_tujuan == "Medan":
    harga = 1002600
    if jenis_tiket == "PP":
        harga_total= harga * 2 * 0.8
        print("harga tiket yang akan dipesan:", harga_total)
    elif jenis_tiket == "sekali" :
        harga_total = harga
        print("harga tiket yang akan dipesan:", harga_total)
    else :
        print("Pilihan Anda Tidak tersedia")
    
elif kota_tujuan == "Jakarta" :
    harga= 2142900
    if jenis_tiket == "PP" :
        harga_total= harga * 2 * 0.8
        print("harga tiket yang akan dipesan:", harga_total)
    elif jenis_tiket == "sekali" :
        harga_total = harga
        print("harga tiket yang akan dipesan:", harga_total)
    else :
            print("Pilihan Anda Tidak tersedia")
    

elif kota_tujuan == "Batam" :
    harga= 665400
    if jenis_tiket == "PP" :
        harga_total= harga * 2 * 0.8
        print("harga tiket yang akan dipesan:", harga_total)
    elif jenis_tiket == "sekali" :
        harga_total = harga
        print("harga tiket yang akan dipesan:", harga_total)
    else :
        print("Pilihan Anda Tidak tersedia")

else :
    print("Pilihan anda tidak tersedia")


     