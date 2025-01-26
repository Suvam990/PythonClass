print("================mobile bazar=====================")

print("1.Vivo(Rs1000) 2.OnePlus(Rs2000) 3.IPhone(Rs3000)")
option = int(input("Enter your choice: "))
Vivo_price = 0
onePlus = 0
Iphone = 0
product_name = ""
quntity = 0
discount = 0
if option == 1:
    quntity = int(input("Enter the quntity: "))
    Vivo_price = 1000*quntity
    discount = int(input("enter a discount from(1-10)"))
    discount_amount = Vivo_price * discount /100
    Price_with_discount = Vivo_price - discount_amount
    
   
elif option ==2:
    quntity = int(input("Enter the quntity: "))
    onePlus_price = 2000*quntity
    discount = int(input("enter a discount from(1-10)"))
    discount_amount = onePlus * discount /100
    Price_with_discount = onePlus - discount_amount
elif option ==3:
    quntity = int(input("Enter the quntity: "))
    Iphone = 3000*quntity
    discount = int(input("enter a discount from(1-10)"))
    discount_amount = Iphone * discount /100
    Price_with_discount = Iphone - discount_amount
else:
    print("Invalid product")


name = input("enter your name: ")
address = input("Enter your address: ")
phone = int(input("enter your phone number: "))

print("\n \n =====================Total  Bill====================")
print("Name: ", name)
print("Address: ", address)
print("Phone: ", phone)
print("Total price: ", +Vivo_price+onePlus+Iphone)
print("Discount Amount: ", discount_amount)
print("Price after discount:", Price_with_discount)