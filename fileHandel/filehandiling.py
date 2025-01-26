# handle = open('record.txt','a')
# name  = input('enter your  a name: ')
# address = input("enter a address: ")
# phone = input("enter a phone num: ")
# handle.write(F"{name},{address},{phone}")
# handle.close


# handle = open('record.txt','a')
# name  = input('enter your  a name: ')
# address = input("enter a address: ")
# phone = input("enter a phone num: ")

# def marks():
#     math = int(input("math: "))
#     computer = int(input("computer: "))
#     science = int(input("science: "))
#     english = int(input("english: "))
#     nepali = int(input("nepali: "))

#     total = math+computer+science+english+nepali

#     percentage  = (total/500)*(100)
     
#     if percentage <=100 and percentage >=80:
#         grade = "A+"
#     elif percentage <=80 and percentage >=70:
#         grade = "B+"
#     elif percentage <=70 and percentage>=60:
#         grade = "C"
#     elif percentage <=60 and percentage>=50:
#         grade = "D+"    
#     else:
#         print("you failed")

#     return (f"Total: {total}, Percentage: {percentage}%, Grade: {grade}")
  



# print("====ENTER YOUR MARKS OF SUBJECT====")
# Student_markes = marks()
# print(Student_markes)  

# handle.write(f"{name}, {address}, {phone}, {Student_markes} \n")
# handle.close

handle = open('record.txt','r')
# print(handle.read())
print(handle.readlines())


# regex
# oops
# mysql, sqlite database

