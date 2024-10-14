t = int(input())
ans = []
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    q = int(input())

    window_sum = sum(a[:k])
    max_sum = window_sum
    min_sum = window_sum
    for i in range(1, k + 1):
        window_sum = sum(a[:i])
        max_sum = max(max_sum, window_sum)
        min_sum = min(min_sum, window_sum)
        for j in range(1, n - i + 1):
            window_sum = window_sum - a[j - 1] + a[j + i - 1]
            max_sum = max(max_sum, window_sum)
            min_sum = min(min_sum, window_sum)

    if q == 1:
        ans.append(max_sum)
    elif q == 2:
        ans.append(min_sum)

for i in ans:
    print(i)