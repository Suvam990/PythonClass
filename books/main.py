def register():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    return [username,password]

def login():
    with open("books/users.txt", 'r') as db:
       pass
         
    username = input("enter a user name: ")
   
    # for check in users:
    if username in  db:
      print("user is exites")
      password = input("enter a password: ")
   

login()

# handle=open("record/user.txt","w")
# handle.write("==========register=========\n")
# print("==========register=========")
# uname=input("Enter username:")
# upassword=input("Enter password:")
# handle.write(f"username:{uname},password:{upassword}\n")
# handle.write("==========login=========\n")
# print("==========login=========")
# username=input("Enter username:")
# password=input("Enter password:")
# if username==uname:
#     if password==upassword:
#         print("sucess login")
#         handle.write("sucess login")
#         handle=open("record/book.txt","w")
#         handle.write("ramayan\n")
#         handle.write("munamadan\n")
#         handle.write("sostik\n")
#         print("======book_list=====")
#         print("ramayan")
#         print("munamadan")
#         print("sostik")

#     else:
#         print("wromg password")
#         handle.write("wromg password")
# else:
#     print("wrong username")
#     handle.write("wrong username")


    


