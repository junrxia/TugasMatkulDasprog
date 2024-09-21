def kuadrat_sempurna(x):
    sqrt_x = int(x ** 0.5)
    return sqrt_x * sqrt_x == x

def jumlah_kuadrat(n):
    for i in range(int(n ** 0.5) + 1):
        for j in range(int((n - i * i) ** 0.5) + 1):
            for k in range(int((n - i * i - j * j) ** 0.5) + 1):
                l_square = n - i * i - j * j - k * k
                if kuadrat_sempurna(l_square):
                    return True
    return False

n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))

for number in numbers:
    if jumlah_kuadrat(number):
        print("LEAVE")
    else:
        print("ERASE")
