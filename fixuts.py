'''UTS ALPRO PROGRAM PARKIR
Muhammad Reyhandhani 1204230011
Daffa Yusuf M 1204230015
Achmad Zaki 1204230042
Nindyandha Sekar Prameswari 1204230069
Ario veisa rayanda utomo 1204230086'''


print("Selamat datang di program parkir Cak Boyo")
print("=========================================")
print()

# Data login
db_login_user = [
    ["cakboyo","pangerantampan"],
    ["konoha","selaludihati"],
    ["cakjukir","ahlinyahali"],]

# Tarif parkir
tarif_motor = 2000
tarif_mobil = 5000
tarif_bus = 10000

#jumlah
jumlah_mobil = 0
jumlah_motor = 0
jumlah_bus = 0

# Data parkiran
parkiran_motor = {
    "Lantai 1": [(i, j) for i in "JIHGFEDCBA" for j in range(3)],
    "Lantai 2": [(i, j) for i in "CBA" for j in range(9)],
    "Lantai 3": [(i, j) for i in "JIHGFEDCBA" for j in range(6, 9)]
}

parkiran_mobil = {

    "Lantai 3": [(i, j) for i in "GFEDCBA" for j in range(6)],
    "Lantai 2": [(i, j) for i in "JIHGFEDCBA" for j in range(9)],
    "Lantai 1": [(i, j) for i in "JIHGFEDCBA" for j in range(3, 9)],
}

parkiran_bus = {
    "Lantai 3": [(i, j) for i in "JIH" for j in range(6)]
}
# Fungsi untuk melakukan login
def login():
    attempt = 0
    while attempt < 3:
        username = input("Username: ")
        password = input("Password: ")

        if [username, password] in db_login_user:
            print("Login berhasil!")
            return True
        else:
            print("Login gagal. Coba lagi.")
            attempt += 1

    print("Anda sudah mencoba 3 kali. Program berhenti.")
    return False

# fungsi laporan
def generate_laporan():
    income = (jumlah_mobil*tarif_mobil) + (jumlah_motor*tarif_motor ) + (jumlah_bus*tarif_bus)
    print("Rincian Pemasukan")
    print()
    print(f"Jumlah motor adalah {jumlah_motor} dan mendapatkan pendapatan {jumlah_motor*tarif_motor}")
    print(f"Jumlah mobil adalah {jumlah_mobil} dan mendapatkan pendapatan {jumlah_mobil*tarif_mobil}")
    print(f"Jumlah bus adalah {jumlah_bus} dan  mendapatkan pendapatan {jumlah_bus*tarif_bus}")
    print(f"total pendapatan adakah {income}")
    
# fungsi koordinat
def get_parkir(jenis_kendaraan):
    if jenis_kendaraan == "motor":
        for lantai, koordinat in parkiran_motor.items():
            if koordinat:
                return lantai, koordinat.pop()
    elif jenis_kendaraan == "mobil":
        for lantai, koordinat in parkiran_mobil.items():
            if koordinat:
                return lantai, koordinat.pop()
    elif jenis_kendaraan == "bus":
        for lantai, koordinat in parkiran_bus.items():
            if koordinat:
                return lantai, koordinat.pop()
            return None
        
# fungsi cek posisi
def cek_posisi():
    get_parkir(parkiran_motor)
    findPlat=input("masukan nomer plat kendaraan : ")
    if platNomer == findPlat:
        print(f"Kendaraan dengan nomer {platNomer} parkir di {lantai}, Koordinat lokasi: ({baris}, {kolom})")
    else:
        print("Kendaraan Tidak di temukan") 

# fungsi cek parkiran
def cek_ketersedian():
    if jumlah_motor < 87:
        print("Tersedia tempat parkir untuk motor")
    else:
        print("Tidak ada tempat parkir untuk kendaraan jenis motor")
    if jumlah_mobil < 165:
        print("Tersedia tempat parkir untuk mobil")
    else:
        print("Tidak ada tempat parkir untuk kendaraan jenis mobil")
    if jumlah_bus < 18:
        print("Tersedia tempat parkir untuk bus")
    else:
        print("Tidak ada tempat parkir untuk kendaraan jenis mobil")
        
        
        
#progam utama
if login():
    while True:
        print("\nMenu:")
        print("1. Parkir kendaraan")
        print("2. Generate laporan")
        print("3. Cek posisi kendaraan")
        print("4. Cek ketersediaan parkir")
        print("5. Keluar")
        choice = input("masukan pilihan : ")

        if choice == "1":
            print()
    
            for i in parkiran_motor:
                jenis_kendaraan = input("masukan jenis kendaraan (motor/mobil/bus) = ")
                platNomer = input("masukan plat nomer anda : ")
                
                if jenis_kendaraan == "motor":
                    if jumlah_motor < 87:
                        jumlah_motor = jumlah_motor + 1
                        lokasi_parkir = get_parkir(jenis_kendaraan)
                        if lokasi_parkir:
                            lantai, (baris, kolom) = lokasi_parkir
                            print(f"Motor dengan nomer plat {platNomer} parkir di {lantai}, Koordinat: ({baris}, {kolom})") 
                        break
                    else:
                        print("Parkiran Motor Tidak Tersedia")
                        
                elif jenis_kendaraan == "mobil":
                    if jumlah_mobil < 165:
                        jumlah_mobil = jumlah_mobil + 1
                        lokasi_parkir = get_parkir(jenis_kendaraan)
                        if lokasi_parkir:
                            lantai, (baris, kolom) = lokasi_parkir
                            print(f"Mobil dengan nomer plat {platNomer} parkir di {lantai}, Koordinat: ({baris}, {kolom})") 
                        break
                    else:
                        print("parkiran Mobil Tidak Tersedia")

                elif jenis_kendaraan == "bus":
                    if jumlah_bus < 18:
                        jumlah_bus = jumlah_bus + 1
                        lokasi_parkir = get_parkir(jenis_kendaraan)
                        if lokasi_parkir:
                            lantai, (baris, kolom) = lokasi_parkir
                            print(f"Bus dengan nomer plat {platNomer} parkir di {lantai}, Koordinat: ({baris}, {kolom})") 
                        break
                    else:
                        print("Parkiran Bus Tidak Tersedia")
                else:
                    print('Jenis Kendaraan Anda Tidak Ada')
                    break

        if choice == "2":
           generate_laporan()


        if choice == "3":
           cek_posisi()
           
        if choice == "4":
           cek_ketersedian()

        if choice == "5":
            print("program selesai")
            break