# Fungsi untuk menghitung waktu berdasarkan jenis roti
def waktu_roti(jenis_roti):
    if jenis_roti == 'W':
        return {
            "pemanasan": 15,
            "menguleni": 30,
            "pengembangan": 60,
            "pembentukan": 15,
            "pemanggangan": 45
        }
    elif jenis_roti == 'S':
        return {
            "pemanasan": 20,
            "menguleni": 35,
            "pengembangan": 65,
            "pembentukan": 20,
            "pemanggangan": 50
        }
def tampilkan_instruksi(jenis_roti, ukuran_ganda, manual):
    waktu = waktu_roti(jenis_roti)

    print("\n=== Instruksi Pembuatan Roti Anda ===")
    print("LIAT CARANYA YAAA!")
    print(f"1. Pemanasan awal selama {waktu['pemanasan']} menit. Siapkan bahan-bahan!")
    print(f"2. Proses menguleni adonan selama {waktu['menguleni']} menit. Nikmati aromanya(Seperti BAU ANIME)!")
    print(f"3. Biarkan adonan mengembang selama {waktu['pengembangan']} menit. Sabar adalah kunci!")
    print(f"4. Pembentukan roti akan memakan waktu {waktu['pembentukan']} menit. Bentuk sesuai selera!")
    if manual:
        print("5. Sekarang saatnya untuk pemanggangan manual! Silakan keluarkan adonanmu")
        print("Tips: Panggang adonan Anda di oven hingga keemasan dan nikmati hasilnya!")
    else:
        if ukuran_ganda:
            waktu_pemanggangan = waktu['pemanggangan'] * 1.5
        else:
            waktu_pemanggangan = waktu['pemanggangan']
        
        print(f"5. Pemanggangan berlangsung selama {waktu_pemanggangan:.0f} menit. Roti sudah jadi well, siap untuk dihidangkan well!")
        print("Selamat menikmati roti lezat buatan sendiri! WELL")
def mesin_roti():
    print("Selamat datang di mesin pembuat roti otomatis!")
    jenis_roti = input("Silakan pilih jenis roti: (W untuk Roti Putih, S untuk Roti Manis): ").upper()
    if jenis_roti not in ['W', 'S']:
        print("Maaf, pilihan jenis roti tidak valid (Udah di kasih pilihan malah, milih dia yang gak ada rasa)!")
        return
    ukuran_ganda = input("Apakah ukuran roti yang kamu buat adalah ukuran ganda? (Y/N): ").upper() == 'Y'
    manual = input("Apakah kamu ingin memanggang secara manual? (Y/N): ").upper() == 'Y'
    tampilkan_instruksi(jenis_roti, ukuran_ganda, manual)
mesin_roti()
