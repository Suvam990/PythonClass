# handle = open("record/db.text","a")
# handle.write("hello world!")
# name = input("Enter a name: ")
# age = input("Enter a age: ")
# address = input("Enter a address: ")
# handle.write(f"{name} \n")
# handle.write(age)
# handle.write( f"\n {address}")
# handle.close

print("==================Mobile Bazar==============")
print("1. Mi(Rs:20000) 2. Samsung(Rs:30000) 3. Iphone(Rs:50000)")

mi_price =0
samsung_price =0
iphone_price =0
product_name=""
quantity = 0
option = int(input("Enter your choice: "))
if option==1:
    product_name = "Mi"
    quantity = int(input("Enter the quantity: "))
    mi_price = 20000 * quantity

elif option==2:
    product_name = "Samsung"
    quantity = int(input("Enter the quantity: "))
    samsung_price = 30000 * quantity

elif option==3:
    product_name = "Iphone"
    quantity = int(input("Enter the quantity: "))
    iphone_price = 50000 * quantity
else:
    print("Invalid choice")

print("Delivey Option")
print("1. Home Delivery(Rs:1000) 2. Pick up(Free)")
delivery_price =0
delivery_option = int(input("Enter your choice: "))
if delivery_option==1:
    delivery_price = 1000


print("Packing: 1. Normal(Rs:1000) 2. Gift Packing(Rs:5000)")
packing_price =0
packing_option = int(input("Enter your choice: "))
if packing_option==1:
    packing_price = 1000
elif packing_option==2:
    packing_price = 5000

print("Location: 1.KTM(13%) 2. Lalitpur(0%) 3. Bhaktapur(0%)")
tax_amount =0
location_option = int(input("Enter your choice: "))
total = mi_price + samsung_price + iphone_price
if location_option==1:
    tax_amount = total * 0.13

grand_total = total + delivery_price + packing_price + tax_amount
print("======== Invoice =========")
print(f"Product Name: {product_name}")
print(f"Quantity: {quantity}")
print(f"Total: {total}")
print(f"Delivery Price: {delivery_price}")
print(f"Packing Price: {packing_price}")
print(f"Tax Amount: {tax_amount}")
print(f"Grand Total: {grand_total}")


handle = open("record/db.text", "a")
handle.write(f"Product Name: {product_name} \n")
handle.write(f"Quantity: {quantity} \n")
handle.write(f"Total: {total} \n")
handle.write(f"Delivery Price: {delivery_price} \n")
handle.write(f"Packing Price: {packing_price} \n")
handle.write(f"Tax Amount: {tax_amount} \n")
handle.write(f"Grand Total: {grand_total} \n")
handle.close


with open("record/db.text") as my_file:
    print(my_file.read())