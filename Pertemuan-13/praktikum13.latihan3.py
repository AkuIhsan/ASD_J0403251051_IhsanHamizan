# Nama : Ihsan Hamizan
# NIM : J0403251051
# Kelas : A2
# Praktikum 13 - Graph III: Spanning Tree

# ==========================================================
# Implementasi Sederhana Algoritma Frim
# ==========================================================

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
# 1. Node awal apa yang digunakan?
# 2. Edge mana yang dipilih pertama kali?
# 3. Bagaimana Prim menentukan edge berikutnya?
# 4. Berapa total bobot MST yang dihasilkan?
# 5. Apa perbedaan pendekatan Prim dan Kruskal?

# Jawaban :
# 1. A
# 2. A-C
# 3. memilih edge dengan bobot paling kecil yang menghubungkan node yang sudah berada di dalam tree dengan node lain yang belum terhubung. 
# 4. 6
# 5. Kruskal mengurutkan edge yang ada sedangkan Prim tidak mengurutkan edge yang ada dan Kruskal Memilih edge global terkecil sedangkan prim Membesar dari node awal.
