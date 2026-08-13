# ==========================================
#        PROGRAM BELAJAR PYTHON STRING
# ==========================================

print("=" * 45)
print("       PROGRAM DATA DIRI SEDERHANA")
print("=" * 45)

# Input data
nama = input("Masukkan nama  : ")
kelas = input("Masukkan kelas : ")
sekolah = input("Masukkan sekolah: ")

# Mengolah string
nama_besar = nama.upper()
nama_kecil = nama.lower()

# Menampilkan hasil
print("\n" + "=" * 45)
print("             HASIL DATA DIRI")
print("=" * 45)

print(f"Nama lengkap : {Ahmad Fauzan }")
print(f"Huruf besar  : {AHMAD FAUZAN}")
print(f"Huruf kecil  : {Ahmad fauzan}")
print(f"Kelas        : {10 TKJ A}")
print(f"Sekolah      : {bina mandiri}")
print(f"Panjang nama : {len(nama)} karakter")

print("=" * 45)
print("      Terima kasih sudah mencoba!")
print("=" * 45)