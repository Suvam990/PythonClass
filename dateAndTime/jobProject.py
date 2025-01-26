import datetime

jobs =[
    {'tittle1':'python developer', 'salary':20000, 'exp_date':'2025-5-21'},
    {'tittle':'java developer', 'salary':30000, 'exp_date':'2024-5-21'},
    {'tittle':'php developer', 'salary':40000, 'exp_date':'2025-5-21'},
    {'tittle':'web developer', 'salary':50000, 'exp_date':'2022-6-21'},
]

job_tittle = ['pyhton_developer','java_developer','php_developer','web_developer']
now_date = datetime.datetime.now()



job_list = int(input("enter a job type form(1-4):\n 1.pyhton developer 2.java developer 3.php developer 4.we developer: "))
 

for job in jobs:
   job_exp_date = datetime.datetime.strptime(job['exp_date'], "%Y-%m-%d")
   if job_list == 1:
        if job_exp_date < now_date:
            print(f"the {job['tittle']} job has expired")
   else:
      print("The job is avilable")    
    