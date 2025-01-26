# data=[]

# num = int(input("Enter a number of student: "))

# for i in range(1,num+1):
#    name = input(f"{i} Enter your name: ")
#    if name not in data:
#       data.append(name)


# print("the unique names are: ",data)


data= [
       [10,20,30,40,50],
      [60,70,80,90,100] 
]

total_sum = 0
 
for i in data:
    for j in i:
        total_sum += j
        
      
new_data = []
for i in range(len(data[0])):
    new_data.append(data[0][i] + data[1][i])
    


print('the total sum is: ',total_sum)
print('the rusle: ',new_data)





   




