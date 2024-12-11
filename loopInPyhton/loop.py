# x=10

# while x>=1:
#     print(x)
#     x=x-1
    
a=1
# num = 5

# while a<=10:
#     print(f"{num}x{a}={num*a}")
#     a+=1


# a=1
# total=0

# while a<=100:
   
#    total+=a
#    a+=1
#    print(total)


# data = ['ram', 'sita', 'hari', 'gita']

# x=0

# while x<len(data):
#     print(data[x])
#     x+=1


# x=1

# while x<=10:
#     c= x % 2
    
#     if c == 0:
#         print(x)
        
#     x +=1  



data = [
    [12, 34, 55, 65, 75],
    [98, 76, 54, 32, 12],
    [12, 43, 56, 78, 90]
]

# Initialize a variable to store the sum
total_sum = 0

# Iterate through each row and each element in the row
for row in data:
    for element in row:
        total_sum += element

print(total_sum)
        
    
  