# Nama : Ihsan Hamizan
# NIM : J0403251051
# Kelas : A2
# Praktikum 13 - Graph III: 

# ==========================================================
# Implementasi Kruskal
# ==========================================================
# Daftar edge: (bobot, node1, node2)
edges = [
 (1, 'C', 'D'),
 (2, 'A', 'C'),
 (3, 'B', 'D'),
 (4, 'A', 'B'),
 (5, 'A', 'D')
]
# Mengurutkan edge berdasarkan bobot
edges.sort()
mst = [] # variabel untuk daftar edge yang sudah terhubung
total_weight = 0 # Variabel untuk menghitung total bobot
# Set sederhana untuk node yang sudah dipilih
connected = set() # variabel untuk daftar node yang sudah terhubung
for weight, u, v in edges:
    # Jika edge tidak membentuk cycle sederhana
    if u not in connected or v not in connected: # Jika salah satu node nya belum terhubung maka masuk ke kondisi ini
        mst.append((u, v, weight)) # Menambahkan node ke dalam list mst
        total_weight += weight # Menambahkan nilai bobot dari node yang sudah dipilih
        connected.add(u)
        connected.add(v)

# Menampilkan hasil node
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)
print("Total bobot =", total_weight)