import itertools

N, M = map(int, input().split())  
harga_barang = list(map(int, input().split()))  
pecahan_uang = list(map(int, input().split()))  
max_hutang = None
for i in range(1, N+1):
    for subset_barang in itertools.combinations(harga_barang, i):
        total_harga = sum(subset_barang)  
        for j in range(1, M+1):
            for subset_uang in itertools.combinations(pecahan_uang, j):
                total_uang = sum(subset_uang) 
                hutang = total_uang - total_harga
                if max_hutang is None or hutang < max_hutang:
                    max_hutang = hutang
print(max_hutang)
