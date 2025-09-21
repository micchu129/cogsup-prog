"""
Write a script that lists all the prime numbers between 1 and 10000.
(A prime number is an integer greater or equal to 2 which has no divisors except 1 and itself). 
Hint: Write an is_factor helper function.
"""

def is_factor(d, n):
    """True iff (if and only if) d is a divisor of n."""
    return n % d == 0
    
def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
                if is_factor(i, n):
                    return False
        return True

list_of_primes = []

for i in range(0,10001):
    if is_prime(i):
         list_of_primes.append(i)

     
     

print(list_of_primes)