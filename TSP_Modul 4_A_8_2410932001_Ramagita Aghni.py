print ("Ramagita Aghni, 2410932001, 8A")

# Data Pemain Penyerang Real Madrid FC
Data_Pemain = [
    ["Vinicius Junior", 24, "3 Tahun", "Rp 3.476,33 M"],
    ["Rodrygo", 24, "4 Tahun", "Rp 1.738,16 M"],
    ["Arda Guler", 19, "5 Tahun", "Rp 782,17 M"],
    ["Brahim Diaz", 25, "3 Tahun", "Rp 608,36 M"],
    ["Kylian Mbappe", 26, "5 Tahun", "Rp 2.781,06 M"]
]

while True:
    print("\nMenu utama:")
    print("1. Tampilkan Data Pemain")
    print("2. Menghapus Data Rodrygo")
    print("3. Menambah Data Erling Haaland")
    print("4. Mengganti Data Vinicius Junior")
    print("5. Keluar")

    pilihan = input("Pilih menu (1/2/3/4/5): ")

    if pilihan == "1":
        print("\nData Pemain Penyerang:")
        for data in Data_Pemain:
            print(f"Nama: {data[0]}, Umur: {data[1]}, Durasi Kontrak: {data[2]}, Nilai Pasar: {data[3]}")

    elif pilihan == "2":
        for i, data in enumerate(Data_Pemain):
            if data[0].lower() == "rodrygo":
                del Data_Pemain[i]
                print("Rodrygo berhasil dihapus.")
                break
        else:
            print("Rodrygo tidak ditemukan.")

    elif pilihan == "3":
        Data_Pemain.append(["Erling Haaland", 24, "2 Tahun", "Rp 3.476,33 M"])
        print("Data Erling Haaland berhasil ditambahkan.")

    elif pilihan == "4":
        for data in Data_Pemain:
            if data[0].lower() == "vinicius junior":
                data[2] = "5 Tahun"
                print("Kontrak Vinicius Junior berhasil diperpanjang.")
                break
        else:
            print("Vinicius Junior tidak ditemukan.")

    elif pilihan == "5":
        print("Thank You.")
        break
    
    else :
        print("pilihan tidak valid")