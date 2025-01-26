# # print("Hello python")

# # x=10
# # y=20
# # print(x+y)


# # int,float,complex,string,boolean
# # data = [
# #     ['ram', 'shyam', 'hari', 'gita'],
# #     ['laxmi', 'sita', 'rita' 'gopal'],
# #     ['sophia',[[[['madan']], 'sontosh']]]
# # ]
# # print(data[2][1][0][0][0])

# # data=[
# #     [
# #          ['ram', 'shyam', 'hari', 'gita'],
# #     ],
# #     [
# #         [
# #             ['gopal','madan']
# #         ]
# #     ]
# # ]
# data=['ram', 'shyam', 'hari', 'gita']
# data.append('nirajan')
# # print(data)

# # clear remove all data
# # data.clear()
# # print(data)


# # name = data.copy()
# # print(name)


# # x=data.count('gopal')
# # print(x)

# # data.extend(name)
# print(data)
# x=data.index("gita")
# print(x)
# data.insert(2,'subham')
# print(data)
# data.pop(3)
# print(data)
# tuple in disnatory

print("================mobile bazar=====================")

print("1.Vivo(Rs1000) 2.OnePlus(Rs2000) 3.IPhone(Rs3000)")
option = int(input("Enter your choice: "))
Vivo_price = 0
onePlus_price = 0
Iphone_price = 0
product_name = ""
quantity = 0
discount = 0
total_price = 0

if option == 1:
    product_name = "Vivo"
    price_per_unit = 1000
elif option == 2:
    product_name = "OnePlus"
    price_per_unit = 2000
elif option == 3:
    product_name = "IPhone"
    price_per_unit = 3000
else:
    print("Invalid product")
    exit()

# Get quantity
quantity = int(input(f"Enter the quantity of {product_name}: "))
total_price = price_per_unit * quantity

# Get discount and calculate discounted price
discount = int(input("Enter a discount from (1-10): "))

if 1 <= discount <= 10:
    discount_amount = total_price * discount / 100
    price_with_discount = total_price - discount_amount
    print(f"Total price before discount: Rs {total_price}")
    print(f"Discount applied: Rs {discount_amount}")
    print(f"Total price after discount: Rs {price_with_discount}")
else:
    print("Invalid discount percentage! Please enter a discount between 1 and 10.")



