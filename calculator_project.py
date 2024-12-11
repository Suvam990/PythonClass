print("See your grade, Total and Percentage")
# Enter a number of subject
math = int(input('math: '))
science = int(input('science: '))
english= int(input('english: '))
computer = int(input('computer: '))
Nepali = int(input('nepali: '))

# Calculate the total marks
total = math + science + english + computer + Nepali

# Calculate the percentage
percentage = total / 5

# Print the total and percentage
print('Total:', total)
print('Percentage:', percentage)

if percentage > 80 and percentage < 100:
    print('grade: A+')
elif percentage > 70 and percentage < 80:
    print('grade: B+')
elif percentage > 60 and percentage < 70:
    print('grade: B')    
elif percentage > 50 and percentage < 60:
    print('grade: C+')
elif percentage > 40 and percentage < 50:
    print('grade: C')   
else:
 print("your grade is to low")