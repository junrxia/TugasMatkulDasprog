# Input
kecepatan_km_jam = float(input("Masukkan kecepatan lepas landas jet (km/jam): "))
jarak = float(input("Masukkan jarak yang ditempuh oleh katapel (meter): "))

# Mengubah kecepatan dari km/jam ke m/s
kecepatan_m_s = kecepatan_km_jam * (5/18)

# Percepatan a = v^2 / (2 * s)
percepatan = (kecepatan_m_s ** 2) / (2 * jarak)

# Waktu menggunakan rumus t = v / a
waktu = kecepatan_m_s / percepatan

# Hasil
print(f"Percepatan yang diperlukan adalah {percepatan:.2f} m/s²")
print(f"Waktu yang diperlukan untuk mencapai kecepatan lepas landas adalah {waktu:.2f} detik")
