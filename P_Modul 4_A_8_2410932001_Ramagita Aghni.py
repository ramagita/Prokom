print ("Ramagita Aghni, 2410932001, 8A")

# Data Pemain Penyerang
Data_Pemain = [["Vinicius Junior", 24, "3 Tahun", "Rp 3.476,33 M"],
               ["Rodrygo", 24, "4 Tahun","Rp 1.738,16 M"],
               ["Arda Guler", 19, "5 Tahun", "Rp 782,17 M"],
               ["Brahim Diaz", 25, "3 Tahun", "Rp 608,36 M"],
               ["Kylian Mbappe", 26, "5 Tahun", "Rp 2.781,06 M"]]

while True:
    print("/nMenu utama:")
    print("1. Tampilkan Data Pemain")
    print("2. Menghapus Data")
    print("3. Menambah Data")
    print("4. Mengganti Data")
    pilihan = input("Pilih mrnu (1/2/3/4): ")

    if pilihan == "1":
        print("/nData Pemain Penyerang:")
        for data in Data_Pemain:
            print(f"Nama: {data[0]}, umur: {data[1]}, durasi kontrak: {data[2]}, Nilai Pasar: {data[3]}" )

    elif pilihan == "2":
        nama_pemain = input("Nama pemain yang akan dihapus: ")
        ditemukan = False
        for data in Data_Pemain:
            if data[0].lower() == nama_pemain.lower():
                Data_Pemain.remove(data)
                print(f"Data Pemain {nama_pemain} berhasil dihapus")
                ditemukan = True
                break
            if not ditemukan:
                print("Pemain tidak ditemukan")

    elif pilihan == "3":
        nama_pemain = input("Nama pemain yang akan ditambah: ")

    elif pilihan == "4":
        nama_pemain = input("Nama pemain yang akan diganti: ")


