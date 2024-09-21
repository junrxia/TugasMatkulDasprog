def pecahkan_pesan():
    pesan = input()
    n = int(input())
    indeks = list(map(int, input().split()))
    hasil = ''.join(pesan[i] for i in indeks)
    print(hasil)
pecahkan_pesan()