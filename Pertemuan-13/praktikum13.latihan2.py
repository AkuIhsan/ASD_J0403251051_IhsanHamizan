# Nama : Ihsan Hamizan
# NIM : J0403251051
# Kelas : A2
# Praktikum 13 - Graph III: Spanning Tree

# ==========================================================
# Implementasi Sederhana Algoritma Kruskal
# ==========================================================

# Daftar edge: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()
# Mebuat daftar MST dengan list Kosong
mst = []
total_weight = 0 # membuat variabel untuk menghitung total bobot
connected = set() # membuat set kosong untuk melihat node apa saja yang sudah terhubung
for weight, u, v in edges:
    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight
        connected.add(u)
        connected.add(v)

# Menampilkan hasil MST
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

# Menampilkan total bobot
print("Total bobot =", total_weight)

# Jawaban Analisis:
# 1. Edge mana yang dipilih pertama kali?
# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
# 3. Berapa total bobot MST yang dihasilkan?
# 4. Mengapa edge tertentu tidak dipilih?

# Jawaban
# 1. C-D
# 2. Karena algoritma kruskal mengurutkan edge dari yang terkecil hingga terbesar setelah itu melakukan perhitungan dari yang terkecil.
# 3. 6
# 4. Karena dapat menyebabkan cycle atau siklus.


