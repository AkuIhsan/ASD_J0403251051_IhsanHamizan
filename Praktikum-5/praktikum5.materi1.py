# ==========================================================
# Contoh Rekursi 1: Faktorial
# Nama : IHSAN HAMIZAN
# Nim : J0403251051
# Kelas : TPL A2
# ==========================================================
def faktorial(n):
    # Base case: berhenti ketika n = 0
    if n == 0:
        return 1
    # Recursive case: masalah diperkecil menjadi faktorial(n-1)
    return n * faktorial(n - 1)
    print(faktorial(5)) # Output: 120

print(faktorial(8))