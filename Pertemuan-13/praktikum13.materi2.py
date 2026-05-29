# Nama : Ihsan Hamizan
# NIM : J0403251051
# Kelas : A2
# Praktikum 13 - Graph III: 

# Mengimpor library heapq untuk menyediakan implementasi algoritma antrian heap
import heapq

# Graph dalam bentuk dictionary
graph = {
 'A': {'B': 4, 'C': 2, 'D': 5},
 'B': {'A': 4, 'D': 3},
 'C': {'A': 2, 'D': 1},
 'D': {'A': 5, 'B': 3, 'C': 1}
}

# Fungsi untuk algoritma prim
def prim(graph, start):
    visited = set([start]) # variabel untuk node yang sudah pernah dikunjungi
    edges = [] # variabel untuk daftar edges
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor)) # Mendaftarkan edge dari node yang sudah di kunjungi atau sedang di kunjungi
    mst = [] 
    total_weight = 0 # variabel untuk menghitung bobot mst

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

# Inisasi algoritma MST dengan node awal yaitu A
mst, total = prim(graph, 'A')

# Menampilkan hasil algoritma
print("Minimum Spanning Tree:")
for edge in mst:
 print(edge)
print("Total bobot =", total)