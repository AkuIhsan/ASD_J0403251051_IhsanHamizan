# Nama : Ihsan Hamizan
# NIM : J0403251051
# Kelas : A2
# Praktikum 13 - Graph III: Spanning Tree


# Mengimpor library heapq untuk menyediakan implementasi algoritma antrian heap
import heapq

# Graph dalam bentuk dictionary
graph = {
 'A': {'B': 4, 'C': 2, 'D': 5},
 'B': {'A': 4, 'D': 3},
 'C': {'A': 2, 'D': 1},
 'D': {'A': 5, 'B': 3, 'C': 1}
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
mst, total = prim(graph, 'A')
# Menampilkan hasil MST
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)
# Menampilkan total bobot
print("Total bobot =", total)


# Jawaban Analisis:
# 1. Algoritma apa yang digunakan?
# 2. Edge mana saja yang dipilih?
# 3. Berapa total biaya minimum?
# 4. Mengapa MST cocok digunakan pada kasus ini?

# Jawaban 
# 1. Algoritma Prim
# 2. A-C dengan bobot 2, C-D dengan bobot 1, D-B dengan bobot 3.
# 3. 6
# 4. Karena terdapat pemborosan edge dan terdapat cycle atau siklus.