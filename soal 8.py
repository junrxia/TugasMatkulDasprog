# Konstanta
toilet_per_orang = 1 / 3  
liter_flush_lama = 15  
liter_flush_baru = 2  
flush_per_hari = 14  
biaya_per_toilet = 150  

# Input
populasi = int(input("Masukkan populasi komunitas: "))

# Perhitungan
jumlah_toilet = populasi * toilet_per_orang
air_digunakan_lama = jumlah_toilet * liter_flush_lama * flush_per_hari
air_digunakan_baru = jumlah_toilet * liter_flush_baru * flush_per_hari
air_dihemat_per_hari = air_digunakan_lama - air_digunakan_baru
total_biaya = jumlah_toilet * biaya_per_toilet

# Hasil
print(f"Air yang dihemat per hari: {air_dihemat_per_hari:.2f} liter")
print(f"Total biaya pemasangan toilet baru: ${total_biaya:.2f}")
