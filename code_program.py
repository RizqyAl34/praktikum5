# List untuk menyimpan data mahasiswa
data_mahasiswa = []

while True:
    # Meminta masukan data mahasiswa
    nama = input("Masukkan nama mahasiswa: ")
    tugas = float(input("Masukkan nilai tugas: "))
    uts = float(input("Masukkan nilai UTS: "))
    uas = float(input("Masukkan nilai UAS: "))
    
    # Menghitung nilai akhir berdasarkan bobot
    nilai_akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)
    
    # Menyimpan data ke dalam list
    data_mahasiswa.append({
        "Nama": nama,
        "Tugas": tugas,
        "UTS": uts,
        "UAS": uas,
        "Nilai Akhir": nilai_akhir
    })
    
    # Menanyakan apakah ingin menambah data lagi
    tambah_data = input("Tambah data lagi? (y/t): ")
    if tambah_data.lower() == 't':
        break  # Keluar dari loop jika pengguna memasukkan 't'

# Menampilkan daftar data mahasiswa
print("\nDaftar Data Mahasiswa:")
print("="*40)
print("Nama\tTugas\tUTS\tUAS\tNilai Akhir")
print("="*40)

for mahasiswa in data_mahasiswa:
    print(f"{mahasiswa['Nama']}\t{mahasiswa['Tugas']}\t{mahasiswa['UTS']}\t{mahasiswa['UAS']}\t{mahasiswa['Nilai Akhir']:.2f}")