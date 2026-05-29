# Nama : Ihsan Hamizan
# NIM : J0403251051
# Kelas : A2
# Praktikum 13 - Graph III: Spanning Tree


# ==========================================================
# Implementasi Sederhana Algoritma Kruskal
# ==========================================================

# Daftar edge: (bobot, node1, node2)
edges = [
    (5, 'BOGOR', 'JAKARTA'),
    (2, 'BOGOR', 'DEPOK'),
    (3, 'DEPOK', 'JAKARTA'),
    (6, 'JAKARTA', 'BANDUNG'),
    (4, 'DEPOK', 'BANDUNG')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()
# Mebuat daftar MST dengan list Kosong
mst = []
total_weight = 0 # membuat variabel untuk menghitung total bobot
connected = set() # membuat set kosong untuk melihat node apa saja yang sudah terhubung
for weight, u, v in edges:
    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected: # Lakukan pengecekan apakah nodenya sudah terkoneksi atau belum
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


# ==========================================================
# Implementasi Sederhana Algoritma Prim
# ==========================================================

import heapq

# Graph dalam bentuk dictionary
graph = {
 'BOGOR': {'JAKARTA': 5, 'DEPOK': 2},
 'JAKARTA': {'BOGOR': 5, 'BANDUNG': 6, 'DEPOK' : 3},
 'DEPOK': {'JAKARTA': 3, 'BOGOR': 2, 'BANDUNG': 4},
 'BANDUNG': {'DEPOK': 4, 'JAKARTA': 6}
}

# Fungsi algoritma prim
def prim(graph, start):
    visited = set([start]) # variabel untuk node yang sudah pernah di kunjungi
    edges = [] # variabel untuk daftar edge dari graph
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))  # mendaftarkan edge yang ada di node yang sedang dikunjungi atau yang sudah pernah dikunjungi
    mst = []
    total_weight = 0 # Variabel untuk menghitung total bobot MST

    while edges:
        weight, u, v = heapq.heappop(edges)
        if v not in visited: # Jika node V belum pernah dikunjungi maka memenuhi kondisi ini
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
    return mst, total_weight

# Insiasi algoritma dengan node pertama yaitu "A"
mst, total = prim(graph, 'BOGOR')
# Menampilkan hasil MST
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)
# Menampilkan total bobot
print("Total bobot =", total)


# Jawaban Analisis:
# 1. Kasus apa yang dipilih?
# 2. Algoritma apa yang digunakan?
# 3. Edge mana saja yang dipilih dalam MST?
# 4. Berapa total bobot MST?
# 5. Mengapa edge tertentu tidak dipilih?

# Jawaban :
# 1. Kasus 1 . Jaringan Jalan Antar Kota.
# 2. Keduanya baik Frim maupun Kruskal.
# 3. BOGOR-DEPOK dengan bobot 2, DEPOK-JAKARTA dengan bobot 3, dan  DEPOK-BANDUNG dengan bobot 4
# 4. 9
# 5. dikarenakan beberapa edge mengandung cycle atau siklus sehingga tidak dapat dipilih dan ada kemungkinan edge yang tidak terpilih tidak mengandung cycle atau siklus tetapi bobot edge nya lebih besar dibantingkan dengan edge yang terpilih