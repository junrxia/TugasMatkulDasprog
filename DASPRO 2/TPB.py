def cek_bilangan_prima(n):
    if n < 2:
        return "IT IS NOT A PRIME"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return "IT IS NOT A PRIME"
    return "IT IS A PRIME"
n = int(input("Masukkan angka: "))

print(cek_bilangan_prima(n))
