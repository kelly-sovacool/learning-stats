#!/usr/local/bin/python3
import fractions
import math

def C(n,k):
    return fractions.Fraction(math.factorial(n), (math.factorial(n-k) * math.factorial(k)))

def binom(n,p,k):
    return C(n,k) * p**k * (1-p)**(n-k)

def main():
    print('Webwork Ch4a Q4:', C(51,27) * fractions.Fraction(1,2)**51)

if __name__ == "__main__":
    main()
