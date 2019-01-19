#!/usr/local/bin/python3
import fractions
import math

def C(n,k):
    return fractions.Fraction(math.factorial(n), (math.factorial(n-k) * math.factorial(k)))

def binom(n,p,k):
    return C(n,k) * p**k * (1-p)**(n-k)

def binom_exp(n, p):
    return sum(k * binom(n,p,k) for k in range(n))

def p2():  # CORRECT
    print('Webwork Ch7a P2:')
    n = 35
    p = 0.4
    N = n - 1
    P = 2 * p * ( 1 - p )
    print(binom_exp(N,P))

def p3():  # CORRECT
    print('Webwork Ch7a P3:')
    n = 120
    p = 1/365
    print('total exp=',binom_exp(n,p))
    x = 3
    print(f'E(x={x})=', 365 * binom(n,p,x)) 
    print('E{distinct birthdays}=', 365 * (1-(364/365)**n))

def p7():
    print('Webwork Ch7a P7:')
    N=120
    k=30
    n=10
    mu = n * k / N
    print('mean:',mu)
    var = n * k/N * (N-k)/N * (N-n)/(N-1)
    print('variance:', var)

def c7bp1():
    c1=0.3
    c2=0.9 # first 4 flips -> 3 heads
    n=4
    k=3
    p1 = binom(n,c1,k) / (binom(n,c2,k)+binom(n,c1,k))
    p2 = binom(n,c2,k) / (binom(n,c2,k)+binom(n,c1,k))
    print(f'P(C1|2H of 3): {p1}\tP(C2|2H of 3): {p2}')
    ph = c1*p1+c2*p2
    ex=3+ 6*ph
    print(f'P(H): {ph}\tE[X]={ex}')

def main():
    c7bp1()

if __name__ == "__main__":
    main()
