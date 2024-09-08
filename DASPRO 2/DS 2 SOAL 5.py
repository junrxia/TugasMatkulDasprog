def hitung_biaya(data):
    if data < 0:
        return "Data tidak valid."
    if 0 < data <= 1.0:
        biaya = 250
    elif 1.0 < data <= 2.0:
        biaya = 500
    elif 2.0 < data <= 5.0:
        biaya = 1000
    elif 5.0 < data <= 10.0:
        biaya = 1500
    elif data > 10.0:
        biaya = 2000
    else:
        return "Data tidak valid."
    return f"Biaya yang harus dibayar: Rp {biaya}"
try:
    data_penggunaan = float(input("Masukkan jumlah data yang digunakan (dalam GB): "))
    print(hitung_biaya(data_penggunaan))
except ValueError:
    print("Masukan tidak valid, harap masukkan angka.")
