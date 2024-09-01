# Konstanta
konstanta_gravitasi = 9.80  
konstanta_efisiensi = 0.90  
massa_per_meter_kubik = 1000  
konversi_ke_megawatt = 1e-6  

# Input
tinggi_bendungan = float(input("Masukkan tinggi bendungan dalam meter: "))
laju_aliran = float(input("Masukkan laju aliran air dalam meter kubik per detik: "))

# Rumus
daya_dalam_watt = konstanta_efisiensi * laju_aliran * massa_per_meter_kubik * konstanta_gravitasi * tinggi_bendungan
daya_dalam_megawatt = daya_dalam_watt * konversi_ke_megawatt

# Hasil
angka_format = f"Perkiraan daya yang dihasilkan adalah {daya_dalam_megawatt:.2f} MW"
print(angka_format) #Hasil
print("HOREEEEE BERHASILLL")