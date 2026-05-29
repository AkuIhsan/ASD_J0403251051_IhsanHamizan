# Nama : Ihsan Hamizan
# NIM : J0403251051
# Kelas : A2
# Praktikum 13 - Graph III: Spanning Tree

# Daftar edge graph
edges = [
 ('A', 'B'),
 ('A', 'C'),
 ('A', 'D'),
 ('C', 'D'),
 ('B', 'D')
]

# Contoh spanning tree
spanning_tree = [
 ('A', 'C'),
 ('C', 'D'),
 ('D', 'B')
]

# Menampilkan daftar edge pada graph
print("Edge pada graph:")
for edge in edges:
    print(edge)

# Menampilkan hasil spanning tree pada graph
print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)

print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))

# Jawaban Analisis:
# 1. Apa perbedaan graph awal dan spanning tree?
# 2. Mengapa spanning tree tidak boleh memiliki cycle?
# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?

# Jawaban :
# 1. Pada graph awal jumlah edges nya 5 sedangkan di spanning tree hanya ada 3.
# 2. Untuk meminimalisir jumlah edge yang ada sehingga efisien.
# 3. Karena dari namanya sendiri terdapat kata "Minimum" yang artinya sedikit, sehingga tujuannya adalah untuk menghemat biaya