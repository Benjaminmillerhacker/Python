#The input numbers
#List understanding/Comprehension
#In certain circumstances flat > better than nested .

input_num = [11,12,13,14,15,16,17,18]
odd_num= []

for number in input_num:
    if number % 2 != 0:
        odd_num.append(number)

print(odd_num)


#revising the code .
# Utilizing list comprehension the previous code could be revised

input_num = [11,12,13,14,15,16,17,18]
odd_num = [x for x in input_num if x%2 != 0]
print (odd_num)
