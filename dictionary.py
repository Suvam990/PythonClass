# # data = {
# #     'name': 'subham lama',
# #     'age':21,
# #     'city':'kathmandu',
# #     'contact':{
# #         'phone':987436378,sus
# #         'email':'subhamalama13@gamil.com',
# #     }
# # }

# # print(data['name'])
# # print(data['age'])
# # print(data['contact']['email'])
# # print(data['contact']['phone'])


# data = []

# name = input('Enater a name: ')
# email = input('Enter a email: ')
# address = input('Enter an addresss: ')

# new_data={
#     'name':name,
#     'email':email,
#     'address':address,
# }

# data.append(new_data)
# print(data)

data =[
    {
        'name':'ram',
        'country':[
            {'name':'Nepal', 'capital':'Kathmandu'},
        ]
    }
]



# print('My name '+ data[0]['name'])
# print('I live in '+ data[0]['country'][0]['name'])
# print()
name = data[0]['name']
country = data[0]['country'][0]['name']

print('my name is' + name)
print('i live in ' + country)


# operators 
# control statement

