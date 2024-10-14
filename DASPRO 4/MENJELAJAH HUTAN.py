r, c, N = map(int, input().split())
peta_emas = [list(map(int, input().split())) for _ in range(r)]
langkah = input()
x, y = 0, 0  
total_emas = peta_emas[x][y]  
peta_emas[x][y] = 0  

# Dictionary 
gerakan = {
    'L': (0, -1),
    'R': (0, 1),
    'U': (-1, 0),
    'D': (1, 0)
}

# Fungsi 
def valid(nx, ny, r, c):
    return 0 <= nx < r and 0 <= ny < c
# Proses setiap langkah
for arah in langkah:
    dx, dy = gerakan[arah]
    nx, ny = x + dx, y + dy
    if valid(nx, ny, r, c):
        x, y = nx, ny  
        if arah in ['L', 'D']:
            total_emas -= 2  
        elif arah in ['R', 'U']:
            total_emas += 3  
        total_emas += peta_emas[x][y]  
        peta_emas[x][y] = 0  
    else:
        print(total_emas)
        print("gerakanmu salah bung!")
        exit()

print(total_emas)

# Koordinat (nx, ny) = (2, 3):

# 0 <= 2 < 3 → True (baris valid).
# 0 <= 3 < 4 → True (kolom valid).
# Hasil: True (posisi valid).
# Koordinat (nx, ny) = (3, 2):

# 0 <= 3 < 3 → False (baris tidak valid, karena 3 tidak kurang dari r = 3).
# Hasil: False (posisi tidak valid).
# Koordinat (nx, ny) = (1, 4):

# 0 <= 1 < 3 → True (baris valid).
# 0 <= 4 < 4 → False (kolom tidak valid, karena 4 tidak kurang dari c = 4).
# Hasil: False (posisi tidak valid)