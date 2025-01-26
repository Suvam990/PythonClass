import datetime

user_date = input("Enter a your birth date(yyyy-mm-dd):")
user_date = datetime.datetime.strptime(user_date, "%Y-%m-%d")
date = datetime.datetime.now()
b_date = date - user_date


if  date>user_date:
    day = date - user_date
    print("your birthday is ", day.days, "days ago")  
else:
    day = user_date - date
    print("your birthday is", day.days,  "yet to come")      

