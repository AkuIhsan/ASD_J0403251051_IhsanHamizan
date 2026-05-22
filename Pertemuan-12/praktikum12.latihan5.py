# Nama : Ihsan Hamizan
# NIM : J0403251051
# Kelas : A2
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 5: Studi Kasus dengan Program Shortest Path 
# Algoritma: Dijkstra
# ==========================================================

import heapq
# Graph lokasi kota
graph = {
 'Bogor': {'Jakarta': 5, 'Depok': 2},
 'Depok': {'Jakarta': 2, 'Bandung' : 6},
 'Jakarta': {'Bandung': 7},
 'Bandung' : {}
}
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

hasil = dijkstra(graph, 'Bogor')
print("Jarak terpendek dari Kota Bogor")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak)


# Jawaban Analisis:
# 1. Node awal yang digunakan apa?
# 2. Node mana yang memiliki jarak paling kecil dari node awal?
# 3. Node mana yang memiliki jarak paling besar dari node awal?
# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat.

# Jawaban
# 1. Bogor
# 2. Depok
# 3. Bandung
# 4. Tujuan Akhir Jakarta, Pertama dari Node Bogor melakukan pengecekan terhadap tetangganya yang memiliki jarak terkecil, sebagai contoh, Bogor ke Jakarta langsung = 5, Bogor ke Depok = 2, maka Bogor Ke Depok memiliki nilai jarak terkecil. pindah ke node Depok dan lakukan pengecekan kembali terhadap tetangganya Depok ke Jakarta = 2, Depok ke Bandung = 6, Maka Depok ke Jakarta lebih kecil jadi total dari Bogor ke Jakarta melalui Depok adalah 4. jarak ini lebih kecil dari pada Bogor ke Jakarta langsung