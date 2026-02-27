# ==========================================================
# Latihan 1: Rekursi Pangkat
# Nama : IHSAN HAMIZAN
# Nim : J0403251051
# Kelas : TPL A2
# ==========================================================
def pangkat(a, n):
    # Base case
    if n == 0:
        return 1
    # Recursive case
    return a * pangkat(a, n - 1)
print(pangkat(2, 4)) # Output: 16


# Rangkuman cara kerja alur program
# a = sebagai argumen dari fungsi tersebut untuk bilangan yang akan dipangkatkan
# n = sebagai argumen dari fungsi tersebut untuk nilai pangkat
# Jika n sama dengan angka 0 fungsi tersebut akan berhenti dan mengembalikan nilai yang disimpan sebelumnya
# Jika n tidak dengan angka 0 fungsi tersebut masih berlanjut sampai n = 0
# Gambaran nya seperti ini
# 2*f(x) n = 4
# 2*f(x) n = 3
# 2*f(x) n = 2
# 2*f(x) n = 1
# 1 n = 0

# Jadinya seperti berikut 
# 2*2*2*2*1 n = 4 
# 2*2*2*1 n = 3
# 2*2*1 n = 2
# 2*1 n = 1
# 1 n = 0