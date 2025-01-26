# from studentId import StudentId
# import math
# from calculator import add,sub

# print(info)

# print(add(4,3))
# print(dir(math))

import datetime

today = datetime.datetime.today()
print(today)

b_date=datetime.datetime(1993,5,12)
print(today-b_date)


jobs=[
    {'title':'pyhton Developer','exp_data':'2024-12-25'},
    {'title':'java Developer','exp_data':'2024-11-25'}
]


for job in jobs:
    expdata = job['exp_data']
    date_string = datetime.datetime.strptime(expdata, "%Y-%m-%d")
   
    if date_string >= today:
        print(f"the'{job['title']}' is avilable")
    else:
        print(f"the '{job['title']}'is not avilable")    



for job in jobs:
    expdata = job['exp_data']
    Ajob = int(input('chooice listed job 1)Python 2)java: '))
    if Ajob == 1:
        for Ajob in jobs:
            print(job[0])



            # data time stringh formate
