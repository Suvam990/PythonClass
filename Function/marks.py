# def total(num):
#     x=0
#     for y in num:
#         x +=y

#     print(x)


# total([10,20,30,40])        

def marks():
    math = int(input("math: "))
    computer = int(input("computer: "))
    science = int(input("science: "))
    english = int(input("english: "))
    nepali = int(input("nepali: "))

    sum = math+computer+science+english+nepali

    percentage  = (sum/500)*(100)
     
    if percentage <=100 and percentage >=80:
        print("you got A+")
    elif percentage <=80 and percentage >=70:
        print("you got B+")
    elif percentage <=70 and percentage>=60:
        print("you got c+")
    elif percentage <=60 and percentage>=50:
        print("you got D+")      
    else:
        print("you failed")

    print("Total: ",sum)
    print(f"Percentage: ",percentage)  



print("====ENTER YOUR MARKS OF SUBJECT====")
Student_markes = marks()
print(Student_markes)                
