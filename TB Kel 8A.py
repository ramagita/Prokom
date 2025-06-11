def tampilkan_cover():
    import os

    os.system('cls' if os.name == 'nt' else 'clear')
    lebar = 80

    def center(text):
        return text.center(lebar)

    putih_background = '\033[47m' 
    hitam_foreground = '\033[30m' 
    reset = '\033[0m'     

    cover_lines = [
        "",
        "TUGAS BESAR",
        "PEMROGRAMAN KOMPUTER",
        "(Sistem Pendukung Keputusan Dalam Proses Penilaian Dan",
        "Penentuan Siswa Terbaik)",
        "",
        "Oleh:",
        "Kelompok 8A",
        "",
        "Anggota:",
        " Ramagita Aghni      2410932001",
        " Afif Gardana        2410932009",
        " Rayhan Lubis        2410932045",
        "",
        "Asisten Pembimbing:",
        "Dwi Ramadhani",
        "",
        "Dosen Pengampu:",
        "(Dr.Eng Ardhian Agung Yulianto S.Kom, M.T)",
        "",
        "",
        "LABORATORIUM SISTEM INFORMASI DAN KEPUTUSAN",
        "DEPARTEMEN TEKNIK INDUSTRI",
        "FAKULTAS TEKNIK",
        "UNIVERSITAS ANDALAS",
        "2025",
        ""
    ]

    print(putih_background + hitam_foreground)

    for line in cover_lines:
        print(center(line))

    print(reset) 
    input("Tekan ENTER untuk melanjutkan ke program utama...")

class Siswa:
    def __init__(self, nama, nisn, uts, uas, tugas, ekskul, sikap):
        self.nama = nama.lower()
        self.nisn = nisn
        self.uts = uts
        self.uas = uas
        self.tugas = tugas
        self.ekskul = ekskul
        self.sikap = sikap
        self.nilai_akhir = 0
        self.status = ""

    def hitung_nilai(self, bobot):
        self.nilai_akhir = (
            self.uts * bobot['uts'] +
            self.uas * bobot['uas'] +
            self.tugas * bobot['tugas'] +
            self.ekskul * bobot['ekskul'] +
            self.sikap * bobot['sikap']
        )
        self.status = "Lulus" if self.nilai_akhir >= 80 else "Tidak Lulus"

class Sistem:
    def __init__(self):
        self.data_siswa = []
        self.bobot = {
            'uts': 0.2,
            'uas': 0.3,
            'tugas': 0.2,
            'ekskul': 0.15,
            'sikap': 0.15
        }
        self.buat_data_awal()

    def validasi_nama(self, nama):
        return all(c.isalpha() or c.isspace() for c in nama) and len(nama) > 0

    def validasi_nisn(self, nisn):
        return nisn.isdigit()

    def input_valid(self):
        while True:
            nama = input("Nama siswa: ")
            if not self.validasi_nama(nama):
                print("Input nama tidak valid.")
                continue

            nisn = input("NISN: ")
            if not self.validasi_nisn(nisn):
                print("Input NISN tidak valid.")
                continue

            try:
                uts = float(input("Nilai UTS: "))
                uas = float(input("Nilai UAS: "))
                tugas = float(input("Nilai Tugas: "))
                ekskul = float(input("Nilai Ekskul: "))
                sikap = float(input("Nilai Sikap: "))
            except ValueError:
                print("Input nilai harus berupa angka.")
                continue

            return nama.lower(), nisn, uts, uas, tugas, ekskul, sikap

    def buat_data_awal(self):
        data_awal = [
            ("apip", "1001", 85, 88, 90, 80, 85),
            ("gita", "1002", 78, 82, 76, 70, 80),
            ("lubis", "1003", 90, 91, 93, 85, 88),
            ("fira", "1004", 65, 70, 72, 60, 70),
            ("dika", "1005", 88, 87, 85, 90, 92),
            ("kalista", "1006", 75, 78, 77, 76, 74),
            ("kirana", "1007", 92, 95, 94, 88, 90),
            ("aryl", "1008", 70, 68, 72, 65, 66),
            ("ghayyas", "1009", 80, 82, 79, 78, 81),
            ("ivan", "1010", 85, 86, 84, 83, 80),
            ("kywat", "1011", 78, 77, 75, 70, 73),
            ("anadel", "1012", 89, 91, 90, 87, 88),
            ("habib", "1013", 60, 65, 64, 58, 60),
            ("faiz", "1014", 95, 94, 96, 92, 94),
            ("zahra", "1015", 82, 80, 83, 85, 84),
        ]

        for d in data_awal:
            siswa = Siswa(*d)
            siswa.hitung_nilai(self.bobot)
            self.data_siswa.append(siswa)

    def tambah_siswa(self):
        data = self.input_valid()
        siswa = Siswa(*data)
        siswa.hitung_nilai(self.bobot)
        self.data_siswa.append(siswa)
        print("Data berhasil ditambahkan.")

    def tampilkan_data(self):
        if not self.data_siswa:
            print("Data kosong.")
            return
        self.cetak_tabel(self.data_siswa)

    def cari_siswa(self):
        keyword = input("Masukkan nama siswa: ").lower()
        hasil = [s for s in self.data_siswa if keyword in s.nama]
        if hasil:
            self.cetak_tabel(hasil)
        else:
            print("Data tidak ditemukan.")

    def hapus_siswa(self):
        nama = input("Masukkan nama siswa yang ingin dihapus: ").lower()
        for s in self.data_siswa:
            if s.nama == nama:
                self.data_siswa.remove(s)
                print("Data berhasil dihapus.")
                return
        print("Siswa tidak ditemukan.")

    def ubah_data(self):
        nama = input("Masukkan nama siswa yang ingin diubah: ").lower()
        for s in self.data_siswa:
            if s.nama == nama:
                data = self.input_valid()
                s.nama, s.nisn, s.uts, s.uas, s.tugas, s.ekskul, s.sikap = data
                s.hitung_nilai(self.bobot)
                print("Data berhasil diubah.")
                return
        print("Siswa tidak ditemukan.")

    def olah_data_tu(self):
        print("== Atur Bobot Penilaian (total harus 100%) ==")
        total = 0
        temp_bobot = {}
        for k in self.bobot:
            try:
                bobot_baru = float(input(f"Bobot {k.upper()} (%): "))
                temp_bobot[k] = bobot_baru / 100
                total += bobot_baru
            except ValueError:
                print("Input tidak valid.")
                return
        if abs(total - 100) > 0.01:
            print("Total bobot harus 100%. Bobot tidak diterapkan.")
            return
        self.bobot = temp_bobot
        for s in self.data_siswa:
            s.hitung_nilai(self.bobot)
        print("Nilai akhir diperbarui.")

    def tampilkan_peringkat(self):
        if not self.data_siswa:
            print("Data kosong.")
            return
        urut = sorted(self.data_siswa, key=lambda x: x.nilai_akhir, reverse=True)
        self.cetak_tabel(urut, peringkat=True)

    def cetak_tabel(self, daftar, peringkat=False):
        lebar_kolom = 15
        if peringkat:
            headers = ["Peringkat", "Nama", "NISN", "Nilai Akhir", "Status"]
        else:
            headers = ["Nama", "NISN", "UTS", "UAS", "Tugas", "Ekskul", "Sikap", "Nilai Akhir", "Status"]
        print("\n" + "-" * (lebar_kolom * len(headers)))
        print("".join(h.center(lebar_kolom) for h in headers))
        print("-" * (lebar_kolom * len(headers)))
        for i, s in enumerate(daftar, 1):
            if peringkat:
                print(
                    str(i).center(lebar_kolom) +
                    s.nama.center(lebar_kolom) +
                    s.nisn.center(lebar_kolom) +
                    f"{s.nilai_akhir:.2f}".center(lebar_kolom) +
                    s.status.center(lebar_kolom)
                )
            else:
                print(
                    s.nama.center(lebar_kolom) +
                    s.nisn.center(lebar_kolom) +
                    f"{s.uts:.1f}".center(lebar_kolom) +
                    f"{s.uas:.1f}".center(lebar_kolom) +
                    f"{s.tugas:.1f}".center(lebar_kolom) +
                    f"{s.ekskul:.1f}".center(lebar_kolom) +
                    f"{s.sikap:.1f}".center(lebar_kolom) +
                    f"{s.nilai_akhir:.2f}".center(lebar_kolom) +
                    s.status.center(lebar_kolom)
                )
        print("-" * (lebar_kolom * len(headers)))

akun = {
    "siswa": {"username": "siswa", "password": "siswaakt24"},
    "guru": {"username": "guru", "password": "guruakt24"},
    "tu": {"username": "tu", "password": "tuakt24"}
}

def login(role):
    print(f"\n--- Login sebagai {role.upper()} ---")
    for attempt in range(3):
        username = input("Username: ")
        password = input("Password: ")
        data = akun.get(role)
        if data and username == data["username"] and password == data["password"]:
            print("Login berhasil.")
            return True
        else:
            print(f"Login gagal ({attempt + 1}/3). Username atau password salah.")
    print("Percobaan login melebihi batas. Program dihentikan.")
    exit()

def konfirmasi_keluar():
    while True:
        jawaban = input("Apakah Anda yakin ingin keluar? (ya/tidak): ").lower()
        if jawaban in ["ya", "tidak"]:
            return jawaban
        else:
            print("Pilihan tidak valid. Harap masukkan 'ya' atau 'tidak'.")

def menu():
    tampilkan_cover()
    sistem = Sistem()
    while True:
        print("\n=== SISTEM PENDUKUNG KEPUTUSAN DALAM PROSES PENILAIAN DAN PENENTUAN SISWA TERBAIK ===")
        print("\n=== Login sebagai ===")
        print("1. Siswa\n2. Guru\n3. Tata Usaha\n4. Selesai")
        pilihan = input("Pilih (1-4): ")

        if pilihan == "1":
            if login("siswa"):
                while True:
                    print("\n--- MODE SISWA ---")
                    print("1. Tampilkan Nilai Akhir")
                    print("2. Keluar")
                    pil = input("Pilih menu: ")
                    if pil == "1":
                        sistem.tampilkan_peringkat()
                    elif pil == "2":
                        if konfirmasi_keluar() == "ya":
                            break
                    else:
                        print("Pilihan tidak valid.")

        elif pilihan == "2":
            if login("guru"):
                while True:
                    print("\n--- MODE GURU ---")
                    print("1. Tambah Siswa")
                    print("2. Tampilkan Data")
                    print("3. Cari Siswa")
                    print("4. Ubah Data")
                    print("5. Hapus Data")
                    print("6. Keluar")
                    pil = input("Pilih menu: ")
                    if pil == "1":
                        sistem.tambah_siswa()
                    elif pil == "2":
                        sistem.tampilkan_data()
                    elif pil == "3":
                        sistem.cari_siswa()
                    elif pil == "4":
                        sistem.ubah_data()
                    elif pil == "5":
                        sistem.hapus_siswa()
                    elif pil == "6":
                        if konfirmasi_keluar() == "ya":
                            break
                    else:
                        print("Pilihan tidak valid.")

        elif pilihan == "3":
            if login("tu"):
                while True:
                    print("\n--- MODE TATA USAHA ---")
                    print("1. Ubah Persentase Bobot Nilai Akhir")
                    print("2. Keluar")
                    pil = input("Pilih menu: ")
                    if pil == "1":
                        sistem.olah_data_tu()
                    elif pil == "2":
                        if konfirmasi_keluar() == "ya":
                            break
                    else:
                        print("Pilihan tidak valid.")

        elif pilihan == "4":
            print("Keluar dari program.")
            if konfirmasi_keluar() == "ya":
                print("Program selesai, Terima kasih")
                break

        else:
            print("Pilihan tidak valid.")

menu()