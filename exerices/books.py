users = [
        {'username':'admin','password':'admin002'},
        {'username':'ram','password':'ram002'}

]

books = [
    {'title':'python', 'author':'ram','price':'2000'},
    {'title':'jave', 'author':'shyam','price':'4000'}
]

username = input('Enter user name: ')
password = input('enter password: ')
is_login = False

for user in users:
    uname = user['username']
    upass = user['password']
    if username==uname and password==upass:
        is_login = True


if is_login:
    print('Title\tAuthor\tPrice')
    for book in books:
        print(f"{book['title']}\t{book['author']}\t{book['price']}")
else:
    print("invalid password and username")        