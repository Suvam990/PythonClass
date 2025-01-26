# def add(x,y):
#     return x+y

# def total(a,b):
#     print(add(a,b))

# total(20,60)  


# def take_marks():
#     english = int(input("English: "))
#     math = int(input("Math: "))
#     science = int(input("Science: "))
#     nepali = int(input("Nepali: "))
#     return [english,math,science,nepali]


# def total():
   
#     total_marks = 0
#     for mark in take_marks():
#         total_marks += mark
#     return total_marks

# def percentage():
#     a = total_marks
   
#     percen = (total_marks/500)*100
#     print(f"Persentage:{percen}%")
#     print(a)
#     return percen



# take_marks()
# total()
    
def take_mark():
   neplai =int(input("enter nepali marks: "))
   english =int(input("enter english marks: "))
   science = int(input("enter a science: "))
   math = int(input("enter a Math: "))
   return[neplai,english,math,science]
    

def total():
    total_mark =0
    for a in take_mark():
        total_mark += a
    print(f"Total Mark:{total_mark}")    
    return total_mark

def per():
    a=total()
    per = (a/500)*100
    print(f"percentage:{per}% ")

per()