# import datetime

# jobs = [
#     {'S.N': 1, 'types': 'engineering', 'post': 'manager'},
#     {'S.N': 2, 'types': 'dataEntry', 'post': 'specialist'}
# ]

# for job in jobs:
#     # print(f"{job}")
#     time = da

# # print("hellow world")
users = [
    {'username':'admin','password':'admin001'},
    {'username':'ram','password':'ram001'}
]
category = [
    {'cid':1,'name':'Electronics'},
    {'cid':2,'name':'Clothing'},
    {'cid':3,'name':'Grocery'},
]

products = [
    {'pid':1,'name':'Mobile','price':20000,'quantity':2,'cid':1},
    {'pid':2,'name':'Laptop','price':50000,'quantity':1,'cid':1},
    {'pid':3,'name':'T-shirt','price':500,'quantity':3,'cid':2},
    {'pid':4,'name':'Jeans','price':1500,'quantity':2,'cid':2},
    {'pid':5,'name':'Rice','price':50,'quantity':5,'cid':3},
    {'pid':6,'name':'Dal','price':100,'quantity':2,'cid':3},
]

username = input("Enter your username: ")
  

for data in users:
    if data['username'] == username:
        
        password = input("Enter your password: ")
        if data['password'] == password:
            print("Welcome to the system!")
            name = input(f"Enter the category name: ")
            for cat in category:
                if cat['name'] == name:
                    for product in products:
                        if product['cid'] == cat['cid']:
                            total = product['price'] * product['quantity']
                            print(f"Product Name: {product['name']} Price: {product['price']} Quantity: {product['quantity']} Total: {total}")
              
        else:
            print("Your password is incorrect")
    else:
        print("your username is incorrect")    


   
 


