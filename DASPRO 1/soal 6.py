# Input
nilai_diinginkan = input("Masukkan nilai yang diinginkan (contoh: A, B, C, dll): ")
rata_rata_minimum = float(input("Masukkan rata-rata minimum yang diperlukan: "))
rata_rata_saat_ini = float(input("Masukkan rata-rata saat ini dalam mata kuliah: "))
persentase_final = float(input("Masukkan berapa persen ujian akhir dari total nilai mata kuliah: "))

# Menghitung nilai 
nilai_diperlukan = (rata_rata_minimum - (1 - persentase_final / 100) * rata_rata_saat_ini) / (persentase_final / 100)

# Hasil
print(f"Anda memerlukan nilai {nilai_diperlukan:.2f} pada ujian akhir untuk mendapatkan nilai {nilai_diinginkan}.")
