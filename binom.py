#!/usr/local/bin/python3
import fractions
import math

def C(n,k):
    return fractions.Fraction(math.factorial(n), (math.factorial(n-k) * math.factorial(k)))

def binom(n,p,k):
    return C(n,k) * p**k * (1-p)**(n-k)

def binom_exp(n, p):
    return sum(k * binom(n,p,k) for k in range(n))

def neg_binom(x,r,p):
    return C(x-1,r-1)*(p**r)*(1-p)**(x-r)

def hypergeom(N,n,r,x):
    return (C(r,x) * C(N-r,n-x) / C(N,n))

def main():
    r=3
    p=0.9
    print(neg_binom(5,r,p))
    print(sum(neg_binom(x,r,p) for x in range(3,6)))
    print(binom(8,0.9,3))
    print("hypergeom:", hypergeom(80,5,10,2))

if __name__ == "__main__":
    main()
