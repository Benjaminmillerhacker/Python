# Function with Arguments
a= input("what is value of a?")
B= input("what is value of b?")
def Addition(a, b):
    Sum = a + b
    return Sum
# Aftermath calling the same var outside the Function Definition
print("Aftermath calling the Function:", Addition(a, b))
