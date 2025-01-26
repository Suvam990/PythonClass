# WAP to enter five suject  arks and find the total and percentage grade
# def marks():
#     math = int(input("math: "))
#     computer = int(input("computer: "))
#     science = int(input("science: "))
#     english = int(input("english: "))
#     nepali = int(input("nepali: "))

#     sum = math+computer+science+english+nepali

#     percentage  = (sum/500)*(100)
     
#     if percentage <=100 and percentage >=80:
#         print("you got A+")
#     elif percentage <=80 and percentage >=70:
#         print("you got B+")
#     elif percentage <=70 and percentage>=60:
#         print("you got c+")
#     elif percentage <=60 and percentage>=50:
#         print("you got D+")      
#     else:
#         print("you failed")

#     print("Total: ",sum)
#     print(f"Percentage: ",percentage)  



# print("====ENTER YOUR MARKS OF SUBJECT====")
# Student_markes = marks()
# print(Student_markes)

# WAP a program for eligible to paty
# age = int(input("Enter your age to go in party: "))

# if age>=18 and age<=40:
#     print("Enjoy your party")
# else:
#     print("Your are not eligible gor paty")


#WAP t enter three number and print descending order
# a = int(input('Enter 1st number: '))
# b= int(input('enter 2nd number:'))
# c = int(input('enter 3rd number:'))

# if a >b>c:
#     print(a , b , c)
#     if a>c>b:
#         print(a,c,b)
# elif b>a>c:
#     print(b, a, c)
#     if b>c>a:
#         print(b,c,a)
# elif c>a>b:
#     print(c,a,b)
#     if c>b>c:
#         print(c,b,a)


print("=============computer Bazar=============")

print("1)Dell  2)Asus  3)Mack")
dell_price = 0
asus_price = 0
mack_price = 0
total_amount = 0
delivery_price = 0
packing_price  = 0
tax_amount = 0
delivery_option = 0
packing_option = 0
location=0


option = int(input("Enater your option: "))

if option ==   1:
    prodcut_name = "Dell"
    qunatity = int(input("enter you qunatity: "))
    if qunatity <=10:
        mack_price = 20000 * qunatity
        print("Delivary Option")
        print("1. Home Delivery(1000)  2.Pick up(free)")

        delivery_price=0
        delivery_option = int(input("Enter your choice: "))
        if delivery_option == 1:
            delivery_price = 1000
        elif delivery_option == 2:
            delivery_price = 0
        else:
            print("Invalid")    


            print("Packing 1. Normal(rs1000) 2.Gift Packing(rs5000)")
            packing_price = 0 
            packing_option = int(input("Enter your choice: "))
        if packing_option == 1:
            packing_price = 1000
        elif packing_option == 2:
            packing_price = 5000


        print("Choice loction")
        print("1.Kathmandu(13%)  2.Lalitpur(0)  3.Bhatapur(0)")
        tax_amount = 0
        location = int(input("Enter your loction: "))
        total_amount = dell_price + asus_price + mack_price
        if location == 1:
            tax_amount = total_amount * 0.13
        
        else:
            print("Invalid choice")
    else:
        print("Your quntity reach to limite")




elif option == 2:
    prodcut_name = "Asus"
    qunatity = int(input("enter you qunatity: "))
    if qunatity <=10:
        mack_price = 30000 * qunatity
        print("Delivary Option")
        print("1. Home Delivery(1000)  2.Pick up(free)")

        delivery_price=0
        delivery_option = int(input("Enter your choice: "))
        if delivery_option == 1:
            delivery_price = 1000
        elif delivery_option == 2:
            delivery_price = 0
        else:
            print("Invalid")    


            print("Packing 1. Normal(rs1000) 2.Gift Packing(rs5000)")
            packing_price = 0 
            packing_option = int(input("Enter your choice: "))
        if packing_option == 1:
            packing_price = 1000
        elif packing_option == 2:
            packing_price = 5000


        print("Choice loction")
        print("1.Kathmandu(13%)  2.Lalitpur(0)  3.Bhatapur(0)")
        tax_amount = 0
        location = int(input("Enter your loction: "))
        total_amount = dell_price + asus_price + mack_price
        if location == 1:
            tax_amount = total_amount * 0.13
        else:
            print("Your quntity reach to limite")
    else:
        print("Your quntity reach to limite")
    
elif option == 3:
    prodcut_name = "Mack"
    
    qunatity = int(input("enter you qunatity: "))
    if qunatity <=10:
        mack_price = 40000 * qunatity
        print("Delivary Option")
        print("1. Home Delivery(1000)  2.Pick up(free)")

        delivery_price=0
        delivery_option = int(input("Enter your choice: "))
        if delivery_option == 1:
            delivery_price = 1000
        elif delivery_option == 2:
            delivery_price = 0
        else:
            print("Invalid")    


            print("Packing 1. Normal(rs1000) 2.Gift Packing(rs5000)")
            packing_price = 0 
            packing_option = int(input("Enter your choice: "))
        if packing_option == 1:
            packing_price = 1000
        elif packing_option == 2:
            packing_price = 5000


        print("Choice loction")
        print("1.Kathmandu(13%)  2.Lalitpur(0)  3.Bhatapur(0)")
        tax_amount = 0
        location = int(input("Enter your loction: "))
        total_amount = dell_price + asus_price + mack_price
        if location == 1:
            tax_amount = total_amount * 0.13
        
        else:
            print("Invalid choice")
    else:
            print("Your quntity reach to limite")         
            


gran_total = total_amount + delivery_price + packing_price + tax_amount


print("==========Invoice===========")
print(f"product name:{prodcut_name}")
print(f"Quntity:{qunatity}")
print(f"Delivery option:{delivery_price}")
print(f"packing Price:{packing_price}")
print(f"Tax amount:{tax_amount}")
print(f"Grand total:{gran_total}")






