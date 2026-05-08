#################################################
# Nama : Ihsan Hamizan                          #
# NIM  : J0403251051                            #
# Kelas : TPL A2                                #
#################################################

data = {
    "A" : 0,
    "B" : 1,
    "C" : 2,
    "D" : 3
}

data_reversed = {
    0 : "A",
    1 : "B",
    2 : "C",
    3 : "D"
}

#Fungsi adjencecy list undirected
def creteGraph(V, edges) :
    adj = [[] for _ in range(V)]

    
    for it in edges :
        u = data[it[0]]
        v = data[it[1]]
        adj[u].append(v)

        # Karena graphnya berupa (Undirected)
        adj[v].append(u)

    return adj

if __name__ == "__main__" :
    V = 4

    # Himpuninan edges 
    edges = [["A","B"],["A","C"],["C","D"],["B","D"]]

    # Membangun graph dengan 
    adj = creteGraph(V, edges)

    print("Adjacency List Representation")
    for i in range(V) :

        # Print nilai vertex
        print(f"{data_reversed[i]}:", end=" ")
        for j in adj[i] :

            print(data_reversed[j], end=" ")
        print()