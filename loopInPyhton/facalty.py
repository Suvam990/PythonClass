faculty=[
    {'fid':1,'name':'Science'},
    {'fid':2,'name':'Management'},
    {'fid':3,'name':'Humanities'}
]


students =[
    {'sid':1,'name':'ram','fid':1},
    {'sid':2,'name':'sita','fid':2},
    {'sid':3,'name':'gita','fid':3},
    {'sid':4,'name':'gopal','fid':1},
    {'sid':5,'name':'hari','fid':2},
    {'sid':6,'name':'nabin','fid':3},
    {'sid':7,'name':'sabin','fid':1},
    {'sid':8,'name':'abinash','fid':2},
    {'sid':9,'name':'anil','fid':3},
    {'sid':10,'name':'santosh','fid':1}
]

faculty_name = input("Enter a faculty name: ")

for faculty_id in faculty:
    if faculty_id['name'] == faculty_name:
        for student in students:
             if student['fid'] == faculty_id['fid']:
                print(f"Name:{student['name']}")
