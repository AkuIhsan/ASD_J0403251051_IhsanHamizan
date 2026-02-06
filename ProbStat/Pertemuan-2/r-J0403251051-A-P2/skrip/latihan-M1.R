##-----------------------
## R sebagai kalkulator
## 4 02 2026
## Ihsan Hamizan | J0403251051
##-----------------------

100.1 + 234.9 + 12.01
a <- 100.1 + 234.9 + 12.01
print(a)
b <- 2+2
print(b)
c <- sqrt(256)
print(c)
d <- log10(100)*cos(pi)
print(d)
e <- cumsum(c(2,3,4,5,6))
print(e)
f <- 170166719 %% 31079
print(f)
g <- 48/(14*3)
print(g)
h <- log(100)
print(h)
i <- 48:14*3
print(i)
j <- log(10)
print(j)
k <- log10(10)
print(k)
l <- exp(2)
print(l)
m <- abs(-4)
print(m)


# Perhitungan SPLDV menggunakan  matriks
matriksA <- matrix(c(5,4,-1,1),2,2, byrow=TRUE)
matriksB <- c(-10,2)
print(matriksA)
print(matriksB)
print(solve(matriksA,matriksB))


# Perhitungan SPLTV menggunakan rbind
matriksC <- rbind(c(1, 2, 3),
             c(2, 2, 3),
             c(3, 2, 8))
matriksD <- c(20, 100, 200)
print(solve(matriksC, matriksD))


