print('1) dell   ')
print('2) Mac')
print('3) toshiba')
dell = 20000
mac = 30000
tho = 40000
d=1
num = int(input('enter a num to buy a product: '))
if num == 1:
   q = int(input('you have selected a dell plz enter a quntity: ')) 
   t = q*dell
   print('the total amount is: ', t)
if num == 2:
   q = int(input('you have selected a mac plz enter a quntity: ')) 
   t = q*mac
   print('the total amount is: ', t)
if num == 3:
   q = int(input('you have selected a Toshiba plz enter a quntity: ')) 
   t = q*tho
   print('the total amount is: ', t)    