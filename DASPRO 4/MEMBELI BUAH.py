# Baca input
N, K = map(int, input().split())
harga_buah = list(map(int, input().split()))
harga_buah.sort()
jumlah_buah = 0
total_uang = 0
for harga in harga_buah:
    if total_uang + harga <= K:
        total_uang += harga
        jumlah_buah += 1
    else:
        break
if K in harga_buah:
    jumlah_buah += 1
print(jumlah_buah)