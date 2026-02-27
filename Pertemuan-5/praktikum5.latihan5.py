# ==========================================================
# Studi Kasus: Generator PIN
# Nama : IHSAN HAMIZAN
# Nim : J0403251051
# Kelas : TPL A2
# ==========================================================
def buat_pin(panjang, hasil=""):
    if len(hasil) == panjang:
        if "0" in hasil and "1" in hasil and "2" in hasil:
            print("PIN:", hasil)
            return
        return
    for angka in ["0", "1", "2"]:
        buat_pin(panjang, hasil + angka)

buat_pin(3)
