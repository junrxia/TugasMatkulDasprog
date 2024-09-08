def last_man_standing(n, c):

    if n % 2 == 0:
        return "Lili" if c == 1 else "Lala"
    else:
        return "Lala" if c == 1 else "Lili"

n, c = map(int, input("Masukkan jumlah bola dan pemain yang mulai (pisahkan dengan spasi): ").split())

print(last_man_standing(n, c))
