#################################################
# Nama : Ihsan Hamizan                          #
# NIM  : J0403251051                            #
# Kelas : TPL A2                                #
#################################################

data_user = {
    "Ihsan" : 0,
    "Raihan" : 1,
    "Ivan" : 2,
    "Raffan" : 3,
    "Ibra" : 4
}

data_user_reversed = {
    0 : "Ihsan",
    1 : "Raihan",
    2 : "Ivan",
    3 : "Raffan",
    4 : "Ibra",
}

adjacency_list = {}
adjacency_matrix = []

# fungsi untuk adjacency_matrix
def createGraph(V, edges) :
    mat = [[0 for _ in range(V)] for _ in range(V)]

    #  Tambahkan hubungan antara vertex
    for it in edges :
        u = data_user[it[0]]
        v = data_user[it[1]]
        mat[u][v] = 1

        # Karena graph nya tidak terarah
        mat[v][u] = 1
    return mat

if __name__ == "__main__" :
    V1 = 5

    # Himpunan hubungan antara setiap vertex
    edges = [["Ihsan","Raihan"],["Ihsan","Ivan"],["Ihsan","Raffan"],["Ivan","Raffan"],["Raihan","Ibra"],["Raffan","Ibra"]]

    # Membangun graph dengan vertex yang sudah ditentukan dan edges yang sudah ditentukan
    adjacency_matrix = createGraph(V1, edges)

    print("Adjacency Matrix Representation")
    # print(adjacency_matrix)
    for i in range(V1) :
        for j in range(V1) :
            print(adjacency_matrix[i][j], end=" ")
        print()


# fungsi untuk adjacency_list
def creteGraph(V, edges) :
    adj = [[] for _ in range(V)]

    
    for it in edges :
        u = data_user[it[0]]
        v = data_user[it[1]]
        adj[u].append(v)

        # Karena graphnya berupa (Undirected)
        adj[v].append(u)

    return adj

if __name__ == "__main__" :
    V = 5

    # Himpuninan edges 
    edges = [["Ihsan","Raihan"],["Ihsan","Ivan"],["Ihsan","Raffan"],["Ivan","Raffan"],["Raihan","Ibra"],["Raffan","Ibra"]]

    # Membangun graph dengan 
    adj = creteGraph(V, edges)

    print("Adjacency List Representation")
    for i in range(V) :
        adjacency_list[data_user_reversed[i]] = []
        # Print nilai vertex
        print(f"{data_user_reversed[i]}:", end=" ")
        for j in adj[i] :
            adjacency_list[data_user_reversed[i]].append(data_user_reversed[j])
            print(data_user_reversed[j], end=" ")
        print()

    print(data_user)


