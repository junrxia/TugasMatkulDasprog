def apakah_palindrome(s):
    return s == s[::-1]

def palindrome_king(s):
    n = len(s)
    if 0 <= n <= 200:
        if apakah_palindrome(s):
            return "Palindrome King!"
        else:
            return "Bukan King!"
    else:
        return "Panjang input tidak valid"

# Masukan
s = input().strip()

# Keluaran
print(palindrome_king(s))