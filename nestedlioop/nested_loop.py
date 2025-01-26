# for i in range(1,6):
#     for j in range(1,11):
#         print(f"{i}*{j}={i*j}")
#     print()




# for i in range(1,6):
#     print("*")
#     for j in range(1,i+1):
#         print("*", end='')

data = [
    {'name': 'ram', 'gender': 'male','status':True},
    {'name': 'sita', 'gender': 'femal','status':False },
    {'name': 'hari', 'gender': 'male','status':True},
    {'name': 'gita', 'gender': 'femal','status':False},
    {'name': 'mohan', 'gender': 'male','status':True}
    
]

# total ctive user
# total inactive user
# total active male 
# toal incative male 
# total active femal 
# total inactive femal 


total_users = len(data)
print(f"Total users: {total_users}")

total_male = 0
total_femal = 0
total_active_user = 0
total_Inactive_user = 0
toal_male_active =0
toal_Inmale_active = 0
toal_femal_active =0
toal_femal_Inactive =0


for user in data:
    if user['gender'] == 'male':
        total_male +=1
    else:
        total_femal +=1

    if user['status'] == True:
        total_active_user +=1
    else:
        total_Inactive_user +=1 

    if user['gender'] == 'male' and user['status'] == True:
        toal_male_active +=1
    elif user['gender'] == 'male' and user['status']==False:
        toal_Inmale_active +=1  

    if user['gender'] == 'femal' and user['status'] == True:
       toal_femal_active +=1
    elif user['gender'] == 'femal' and user['status']==False:
     toal_femal_Inactive  +=1         

print(f"total male: {total_male}")
print(f"total femal: {total_femal}") 
print(f"total active user: {total_active_user}") 
print(f"total active user: {total_Inactive_user}")
print(f"total male active user: {toal_male_active}") 
print(f"total male Inactive user: {toal_Inmale_active}")
print(f"total femal active user: {toal_femal_active}")
print(f"total femal Inactive user: {toal_femal_Inactive}")           

