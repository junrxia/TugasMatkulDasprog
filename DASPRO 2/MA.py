def analisis_lampu_lalu_lintas(m, n, t):
    siklus = 85
    mobil_per_siklus = 12
    siklus_penuh = t // siklus
    sisa_waktu = t % siklus
    total_mobil_melewati = siklus_penuh * mobil_per_siklus
    waktu_hijau = max(0, sisa_waktu - 25) 
    tambahan_mobil = waktu_hijau // 5
    total_mobil_melewati += tambahan_mobil
    total_mobil = m + n
    if total_mobil_melewati >= total_mobil:
        return f"YES! 0"
    else:
        mobil_tertinggal = total_mobil - total_mobil_melewati
        return f"NO! {mobil_tertinggal}"

m, n, t = map(int, input("Masukkan jumlah mobil di depan, mobil di belakang, dan waktu (pisahkan dengan spasi): ").split())

print(analisis_lampu_lalu_lintas(m, n, t))
