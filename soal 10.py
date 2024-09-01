# Meminta input koordinat dua titik
x1, y1 = map(float, input("Masukkan koordinat titik pertama (x1 y1): ").split())
x2, y2 = map(float, input("Masukkan koordinat titik kedua (x2 y2): ").split())

# Menghitung gradien 
if x1 != x2:
    slope_line = (y2 - y1) / (x2 - x1)
else:
    slope_line = None  

# Titik tengah 
x_mid = (x1 + x2) / 2
y_mid = (y1 + y2) / 2

# Gradien
if slope_line is not None:
    slope_bisector = -1 / slope_line
else:
    slope_bisector = 0 

# Menghitung intersep y dari garis tegak lurus
b = y_mid - slope_bisector * x_mid

# Menampilkan hasil
if slope_bisector is not None:
    print(f"Persamaan garis yang membagi dua segmen garis secara tegak lurus adalah: y = {slope_bisector:.2f}x + {b:.2f}")
else:
    print(f"Garis tegak lurus adalah garis vertikal melalui x = {x_mid:.2f}")

# Menyimpulkan kasus di mana program akan gagal
if slope_line == 0:
    print("Program akan gagal untuk segmen garis horizontal (gradien nol), karena pembagian dengan nol tidak didefinisikan.")
elif x1 == x2 and y1 == y2:
    print("Program akan gagal untuk dua titik yang sama karena tidak ada segmen garis yang bisa dibuat.")
