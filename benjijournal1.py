#Python function to return multiple values/Parmarters are prime_numbers

def prime_numbers(x):
  l=[]
  for i in range(x+1):
    if checkPrime(i):
      l.append(i)
  return len(l), l

no_of_primes, primes_list = prime_numbers(100)
Reference: 
