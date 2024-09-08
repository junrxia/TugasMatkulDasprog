def kabisat(tahun):
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return 1
    else:
        return 0

def hari_ke_tahun(bulan, hari, tahun):
    hari_bulan = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if kabisat(tahun):
        hari_bulan[1] = 29
    nomor_hari = sum(hari_bulan[:bulan - 1]) + hari
    return nomor_hari
bulan = int(input("Masukkan bulan (1-12): "))
hari = int(input("Masukkan hari (1-31): "))
tahun = int(input("Masukkan tahun: "))
nomor_hari = hari_ke_tahun(bulan, hari, tahun)
print(f"Hari untuk tanggal {bulan}/{hari}/{tahun} adalah: {nomor_hari}")
