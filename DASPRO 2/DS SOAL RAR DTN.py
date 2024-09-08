from datetime import datetime, timedelta

def hitung_waktu_tunggu(waktu_acara, waktu_sekarang):
    waktu_acara_dt = datetime.strptime(waktu_acara, "%H:%M:%S")
    waktu_sekarang_dt = datetime.strptime(waktu_sekarang, "%H:%M:%S")
    selisih_zona_waktu = timedelta(hours=5)
    waktu_acara_gmt7 = waktu_acara_dt + selisih_zona_waktu
    waktu_tunggu = waktu_acara_gmt7 - waktu_sekarang_dt

    if waktu_tunggu.total_seconds() < 0:
        print("Sampai jumpa di Pear Event berikutnya!")
    else:
        jam, sisa_detik = divmod(waktu_tunggu.total_seconds(), 3600)
        menit, detik = divmod(sisa_detik, 60)
        print(f"{int(jam):02}:{int(menit):02}:{int(detik):02}")
waktu_acara = input("Masukkan waktu acara (HH:MM:SS): ")
waktu_sekarang = input("Masukkan waktu sekarang (HH:MM:SS): ")
hitung_waktu_tunggu(waktu_acara, waktu_sekarang)
