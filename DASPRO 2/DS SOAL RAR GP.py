def apakah_bisa_lompat(n, jarak):
    for j in jarak:
        if j > n:
            return "NO HE CAN'T"
    return "YES HE CAN"
n = int(input("Masukkan jarak lompatan maksimum: ")) 
jarak = list(map(int, input("Masukkan jarak antar pilar (pisahkan dengan spasi): ").split()))
print(apakah_bisa_lompat(n, jarak))
