def find_max_min_subarray(arr, k, is_max):
  n = len(arr)
  if k > n:
    return None  # Subarray panjang k tidak bisa dibuat

  # Inisialisasi jendela pertama
  window_sum = sum(arr[:k])
  result = window_sum if is_max else window_sum

  # Geser jendela
  for i in range(1, n - k + 1):
    window_sum = window_sum - arr[i - 1] + arr[i + k - 1]
    result = max(result, window_sum) if is_max else min(result, window_sum)

  return result

# Contoh penggunaan
arr = [1, 2, -3, 4, 5]
k = 3
is_max = True  # Cari nilai maksimum
result = find_max_min_subarray(arr, k, is_max)
print("Nilai maksimum subarray dengan panjang", k, "adalah:", result)