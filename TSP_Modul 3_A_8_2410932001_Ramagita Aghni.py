print ("Program ATM")
pin = "932001"
kesempatan = 3
saldo_awal = "2410932001"

# Proses login
while kesempatan > 0:
    pin_input = input("Masukkan pin: ")
    if pin_input == pin :
        print("Login berhasil!")
        break
    else:
        kesempatan -= 1
        print(f"Salah! Anda memiliki {kesempatan} kesempatan lagi.")
        
if kesempatan == 0:
    print("Kesempatan login habis! Program selesai.")
else:
    while True:
        print ("Saldo anda sebesar Rp.",saldo_awal)
        # Pilih salah satu menu (Tarik, Transfer, dan Setor Tunai )
        print("\nPilihan:")
        print("1. Tarik")
        print("2. Transfer")
        print("3. Setor Tunai")
        
        # Masukkan pilihan menu nya
        pilihan = input("Pilih menu (1/2/3): ")
        
        if pilihan == "1":
            print("Saldo anda:", saldo_awal)
            Tarik = input("Masukkan jumlah uang yang ingin ditarik: ")
            print ("Anda menarik uang sebesar: ", Tarik)
        
        elif pilihan == "2":
            print("Saldo anda:", saldo_awal)
            Transfer= input("Masukkan jumlah uang yang ingin ditransfer: ")
            print ("Anda mentransfer uang sebesar: ", Transfer)
           
        
        elif pilihan == "3":
            print("Saldo anda:", saldo_awal)
            Setor_tunai= input("Masukkan jumlah uang yang ingin disetor: ")
            print ("Anda melakukan setor tunai sebesar: ", Setor_tunai)
        
        else:
            print("Pilihan Anda tidak tersedia, silakan coba lagi.")
            continue  # Mengulang pilihan jika input salah
        
        # Memberikan pertanyaan kepada pengguuna apakah ingin melakukan pilihan lagi
        ulang = input("Apakah Anda ingin melakukan transaksi lagi? (ya/tidak): ").lower()
        if ulang == "Ya":
            continue
        elif ulang == "Tidak":
            exit ()
        else:
            print("pilihan anda tidak tersedia")
