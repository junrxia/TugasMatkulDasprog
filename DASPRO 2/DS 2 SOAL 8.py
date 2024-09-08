# Program layanan gratis dengan menu dan pilihan miles
def tampilkan_menu():
    print("=== Menu Layanan Gratis ===")
    print("(1) Layanan Gratis Pertama")
    print("(2) Layanan Gratis Kedua")
    print("(3) Keluar")

def tampilkan_pilihan_miles():
    print("=== Pilihan Jarak Tempuh (Miles) ===")
    print("(1) 1500")
    print("(2) 2000")
    print("(3) 2500")
    print("(4) 3000")
    print("(5) 3500")
    print("(6) 4000")
    print("(7) 4500")

def pilih_miles():
    tampilkan_pilihan_miles()
    pilihan_miles = int(input("Masukkan nomor jarak tempuh (Miles)>> "))
    
    # Mapping pilihan miles ke nilai sebenarnya
    if pilihan_miles == 1:
        return 1500
    elif pilihan_miles == 2:
        return 2000
    elif pilihan_miles == 3:
        return 2500
    elif pilihan_miles == 4:
        return 3000
    elif pilihan_miles == 5:
        return 3500
    elif pilihan_miles == 6:
        return 4000
    elif pilihan_miles == 7:
        return 4500
    else:
        print("Pilihan miles tidak valid, silakan coba lagi.")
        return pilih_miles()

def cek_layanan_gratis():
    while True:
        tampilkan_menu()
        pilihan = int(input("Masukkan nomor Layanan Gratis (atau 3 untuk keluar)>> "))

        if pilihan == 3:
            print("Terima kasih!.")
            break
        miles = pilih_miles()
        if pilihan == 1:
            if 1500 <= miles <= 3000:
                print("Kendaraan harus diservis untuk Layanan Pertama.")
            else:
                print("Tidak perlu servis untuk Layanan Pertama.")
        elif pilihan == 2:
            if 3001 <= miles <= 4500:
                print("Kendaraan harus diservis untuk Layanan Kedua.")
            else:
                print("Tidak perlu servis untuk Layanan Kedua.")
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

# Menjalankan program
cek_layanan_gratis()
