def cat_jumps(a, b, c, indices):
    # Simulasikan lompatan sebanyak c kali
    for _ in range(c):
        # Pindahkan b angka terakhir ke depan
        a = a[-b:] + a[:-b]
    
    # Ambil angka-angka sesuai indeks yang diminta
    result = [a[i] for i in indices]
    return result

# Input daftar angka
a = list(map(int, input("Masukkan 7 angka dipisahkan dengan spasi: ").split()))

# Input jumlah kucing yang melompat dari belakang ke depan (b)
b = int(input("Masukkan jumlah kucing yang melompat dari belakang ke depan: "))

# Input jumlah kali lompatan (c)
c = int(input("Masukkan jumlah kali lompatan: "))

# Input tiga indeks yang ingin diambil (d, e, f)
indices = list(map(int, input("Masukkan tiga indeks dipisahkan dengan spasi: ").split()))

# Output hasil
output = cat_jumps(a, b, c, indices)
print("Output:", output)
