from colorama import Fore, Style, init

init()
def laporan_isi_tabung(warna):
    warna = warna.lower()
    isi_gas = {
        'o': ('amonia', Fore.MAGENTA),         # Orange
        'b': ('karbon monoksida', Fore.RED),   # Brown
        'y': ('hidrogen', Fore.YELLOW),        # Yellow
        'g': ('oksigen', Fore.GREEN)           # Green
    }
    
    if warna in isi_gas:
        isi, warna_teks = isi_gas[warna]
        return f"{warna_teks}Isi tabung: {isi}{Style.RESET_ALL}"
    else:
        return f"{Fore.WHITE}Isi tidak diketahui.{Style.RESET_ALL}"

warna_tabung = input("Masukkan huruf pertama warna tabung gas: ")
print(laporan_isi_tabung(warna_tabung))
