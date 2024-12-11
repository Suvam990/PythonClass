# # a= 20
# # b=40
# # # if a>b:
# # #     print('a is greater then b')

# # # else: print('b is greater then a')
# # print('a') if a<b else print('b')

# # x = 41

# # if x < 10 or x == 41:
# #   print("Above ten,")
# #   if x > 20:
# #     print("and also above 20!")
# #   else:
# #     print("but not above 20.")



# # if a <20:
# #     print('your are fail')
# #     if a<10:
# #         print('you are mark is to low please attend a extra class')
# # else:
# #     print('your are pass')

# # mark = input("enter a your mark: ")

# # if mark < 40:
# #     print('your are fail')
# #     # if mark <10:
# #     #     print('your mark is to low please attend a extra class')
# # else:
# #     print('congratulation you are pass')

# # x=10
# # y=20

# # if x>y:
# #     print('x is large')
# # else:
# #     print('y is large')


# a=5
# b=10
# c=20

# if a>b>c:
#     print('a is grater then b and c')
# if b>a>c:
#     print('b is grater then a and c')
# else:
#     print('c is gater then a and b')        

# uname='admin'
# upass ='admin002'

# username = input('enter your name: ')
# passwrod = input('enter a password: ')

# if uname == username and upass==passwrod:
#     print('welcome back')
# else:
#     print('your username and password does not match') 



# age = int(input('enter your age: ')) 

# if age >= 18:
#     print('your eligible for vote')
# else:
#     print('your are not eligible for vote')    

user_pin = 1234
balance = 10000
a=1
b=2

pin = int(input('enter your pin: '))

if user_pin == pin:
    a = int(input('do your want ot see your balance prss 1 or prss 2 ro wothdraw: '))
    if a == 1:
        print(balance)
    if b == 2:
        new =int(input("enter a amount you want to withdraw: "))
        if new>balance:
            print("insufficent amount")
        else:
            print('you have withdraw', new)     
else:
    print('your pin is in correct')       


