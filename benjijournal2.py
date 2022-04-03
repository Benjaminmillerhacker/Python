# Function with Arguments
def Addition(a, b):
    Sum = a + b
    Sum=x
    return Sum

#Python function to return multiple values/Parmarters are prime_numbers

def prime_numbers(x):
  l=[]
  for i in range(x+1):
    if checkPrime(i):
      l.append(i)
  return len(l), l


#If you want to assign a value to variable named a/b with user input:
a= input("what is value of a?")
B= input("what is value of b?")
Sum = a + b
Sum=x
return Sum


no_of_primes, primes_list = prime_numbers(100)

#Python assignment with expression
x = 2    #Assignment statement
x = x + 2    # Assignment with expression
print(x)        #print function
