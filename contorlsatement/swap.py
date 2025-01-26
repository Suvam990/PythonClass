# Value in accending order

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

# Value in decending order


# WAP to enter three nimber and find the greates number
def greates_nimber():
    a = int(input('Enter 1st number: '))
    b= int(input('enter 2nd number:'))
    c = int(input('enter 3rd number:'))

    if a <b<c:
     print(a , b , c)
    if a<c<b:
        print(a,c,b)
    elif b<a<c:
        print(b, a, c)
    if b<c<a:
        print(b,c,a)
    elif c<a<b:
        print(c,a,b)
        if c<b<c:
            print(c,b,a)   


# wap to enter a number and check ehether it is even or odd

def even_odd():
    num1 = int(input("enter a number 1: "))
    num2 = int(input("Enter a number 2: "))

    if num1%2 == 0:
        print("The 1st number is even")
    elif num2%2 == 1:
        print("The 2nd number is odd")
    else:
        print("Invalid number")  

#wap to enter age and chjeck whether the person is eligible t vote or not
def vote_system():
    age = int(input("Enter your age: "))
    if age>=18:
        print("you are eligible for vote") 
    else:
         print("you are not eligible for vote")   

    return age

GretesNumber = greates_nimber()
print(GretesNumber)           
EvenOdd = even_odd()
print(EvenOdd)
VoteSystem = vote_system()
print(VoteSystem)

# enrter amount , total with