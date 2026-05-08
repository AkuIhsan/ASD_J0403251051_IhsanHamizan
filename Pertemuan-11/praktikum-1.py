#################################################
# Nama : Ihsan Hamizan                          #
# NIM  : J0403251051                            #
# Kelas : TPL A2                                #
#################################################

#Fungsi adjencecy matrix undirected
def createGraph(V, edges) :
    mat = [[0 for _ in range(V)] for _ in range(V)]

    #  Tambahkan hubungan antara vertex
    for it in edges :
        u = it[0]
        v = it[1]
        mat[u][v] = 1

        # Karena graph nya tidak terarah
        mat[v][u] = 1
    return mat

if __name__ == "__main__" :
    V = 4

    # Himpunan hubungan antara setiap vertex
    edges = [[0,1],[0,2],[2,3],[1,2]]

    # Membangun graph dengan vertex yang sudah ditentukan dan edges yang sudah ditentukan
    mat = createGraph(V, edges)

    print("Adjacency Matrix Representation")
    for i in range(V) :
        for j in range(V) :
            print(mat[i][j], end=" ")
        print()