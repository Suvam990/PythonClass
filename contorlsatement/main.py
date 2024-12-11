
# num = int(input('Enter an number: '))
# new_num3 = num % 3
# new_num5 =  num % 5
# if new_num3 == 0 and new_num5 == 0:
#     print("Its divisiable by 3 and 5 ")
# else:
#     print("Its not divisiable by 3 and 5 ")

print("Computer bazzer")

print('1)Dell(RS20000)  2)Toshiba(Rs30000)  3)Mac(Rs50000)')

Product_option = int(input('Enter Option(1-3): '))
Quantity_option = int(input('Enter Qunatity: '))

Tax_Dell= (13/100)*20000
Tax_Toshiba = (13/100)*30000
Tax_mac = (13/100)*50000

if Product_option ==1:
    deliver=int(input("Delivery Option \n 1) Home(Rs1000) 2)Pickup(free): "))
    if deliver == 1:
        print("Packing \n 1)Pasltic(rs100) 2)Bage(Rs2000) 3)Gift-box(rs3000)")
        Packing = int(input('Chooise packing: '))
        if Packing == 1:
           Location = int(input('Chooies Loction \n 1)KTM(13% tax) 2)BKT(f) 3)LTP(f)')) 
           if Location ==1:
                print('DELL')
                print('amount:Rs.20000')
                print('quntity: ', Quantity_option)
                print('Tax amount: ',  Tax_Dell)
                print('Delivery Charge: RS1000')
                print('Packing bag:Rs1000')
                print('Grand Total: ', 20000+Tax_Dell+1000+1000)
           if Location ==2:
                print('DELL')
                print('amount:Rs.20000')
                print('quntity: ', Quantity_option)
                print('Tax amount: 0',  )
                print('Delivery Charge: RS1000')
                print('Packing bag:Rs1000')
                print('Grand Total: ', 20000+0+1000+1000)
           if Location ==3:
                print('DELL')
                print('amount:Rs.20000')
                print('quntity: ', Quantity_option)
                print('Tax amount: 0')
                print('Delivery Charge: RS1000')
                print('Packing bag:Rs1000')
                print('Grand Total: ', 20000+0+1000+1000)   
        if Packing == 2:
           Location = int(input('Chooies Loction \n 1)KTM(13% tax) 2)BKT(f) 3)LTP(f)')) 
           if Location ==1:
                print('DELL')
                print('amount:Rs.20000') 
                print('quntity: ', Quantity_option)
                print('Tax amount: ',  Tax_Dell)
                print('Delivery Charge: RS1000')
                print('Packing bag:Rs1000')
                print('Grand Total: ', 20000+Tax_Dell+1000+1000)
           if Location ==2:
                print('DELL')
                print('amount:Rs.20000') 
                print('quntity: ', Quantity_option)
                print('Tax amount: 0',  )
                print('Delivery Charge: RS1000')
                print('Packing bag:Rs1000')
                print('Grand Total: ', 20000+0+1000+1000)
           if Location ==3:
                print('DELL')
                print('amount:Rs.20000') 
                print('quntity: ', Quantity_option)
                print('Tax amount: 0')
                print('Delivery Charge: RS1000')
                print('Packing bag:Rs1000')
                print('Grand Total: ', 20000+0+1000+1000)
        if Packing == 3:
           Location = int(input('Chooies Loction \n 1)KTM(13% tax) 2)BKT(f) 3)LTP(f)')) 
           if Location ==1:
                print('DELL')
                print('amount:Rs.20000') 
                print('quntity: ', Quantity_option)
                print('Tax amount: ',  Tax_Dell)
                print('Delivery Charge: RS1000')
                print('Packing bag:Rs1000')
                print('Grand Total: ', 20000+Tax_Dell+1000+1000)
           if Location ==2:
                print('DELL')
                print('amount:Rs.20000') 
                print('quntity: ', Quantity_option)
                print('Tax amount: 0',  )
                print('Delivery Charge: RS1000')
                print('Packing bag:Rs1000')
                print('Grand Total: ', 20000+0+1000+1000)
           if Location ==3:
                print('DELL')
                print('amount:Rs.20000') 
                print('quntity: ', Quantity_option)
                print('Tax amount: 0')
                print('Delivery Charge: RS1000')
                print('Packing bag:Rs1000')
                print('Grand Total: ', 20000+0+1000+1000)                  
    
    elif deliver == 2:
        print("Packing \n 1)Pasltic(rs100) 3)Bage(Rs1000) 3)Gift-box(rs3000)")
        Packing = int(input('Chooise packing: '))
        if Packing == 1:
           Location = int(input('Chooies Loction \n 1)KTM(13% tax) 2)BKT(f) 3)LTP(f)')) 
           if Location ==1:
                print('DELL')
                print('quntity: ', Quantity_option)
                print('Tax amount: ',  Tax_Dell)
                print('Delivery Charge: RS1000')
                print('Packing bag:Rs1000')
                print('Grand Total: ', 20000+Tax_Dell+1000+1000)
           if Location ==2:
                print('DELL')
                print('quntity: ', Quantity_option)
                print('Tax amount: 0',  )
                print('Delivery Charge: RS1000')
                print('Packing bag:Rs1000')
                print('Grand Total: ', 20000+0+1000+1000)
           if Location ==3:
                print('DELL')
                print('quntity: ', Quantity_option)
                print('Tax amount: 0')
                print('Delivery Charge: RS1000')
                print('Packing bag:Rs1000')
                print('Grand Total: ', 20000+0+1000+1000)
        if Packing == 2:
           Location = int(input('Chooies Loction \n 1)KTM(13% tax) 2)BKT(f) 3)LTP(f)')) 
           if Location ==1:
                print('DELL')
                print('quntity: ', Quantity_option)
                print('Tax amount: ',  Tax_Dell)
                print('Delivery Charge: RS1000')
                print('Packing bag:Rs1000')
                print('Grand Total: ', 20000+Tax_Dell+1000+1000)
           if Location ==2:
                print('DELL')
                print('quntity: ', Quantity_option)
                print('Tax amount: 0',  )
                print('Delivery Charge: RS1000')
                print('Packing bag:Rs1000')
                print('Grand Total: ', 20000+0+1000+1000)
           if Location ==3:
                print('DELL')
                print('quntity: ', Quantity_option)
                print('Tax amount: 0')
                print('Delivery Charge: RS1000')
                print('Packing bag:Rs1000')
                print('Grand Total: ', 20000+0+1000+1000) 
        if Packing == 3:
           Location = int(input('Chooies Loction \n 1)KTM(13% tax) 2)BKT(f) 3)LTP(f)')) 
           if Location ==1:
                print('DELL')
                print('quntity: ', Quantity_option)
                print('Tax amount: ',  Tax_Dell)
                print('Delivery Charge: RS1000')
                print('Packing bag:Rs3000')
                print('Grand Total: ', 20000+Tax_Dell+1000+3000)
           if Location ==2:
                print('DELL')
                print('quntity: ', Quantity_option)
                print('Tax amount: 0',  )
                print('Delivery Charge: RS3000')
                print('Packing bag:Rs1000')
                print('Grand Total: ', 20000+0+1000+3000)
           if Location ==3:
                print('DELL')
                print('quntity: ', Quantity_option)
                print('Tax amount: 0')
                print('Delivery Charge: RS3000')
                print('Packing bag:Rs1000')
                print('Grand Total: ', 20000+0+1000+3000)    
   # to show product naem, quantiy , tax amount and grand total
if Product_option ==2:
    deliver=int(input("Delivery Option \n 1) Home(Rs1000) 2)Pickup(free): "))
    if deliver == 1:
        print("Packing \n 1)Pasltic(rs100) 2)Bage(Rs2000) 3)Gift-box(rs3000)")
        Packing = int(input('Chooise packing: '))
        if Packing == 1:
           Location = int(input('Chooies Loction \n 1)KTM(13% tax) 2)BKT(f) 3)LTP(f)')) 
           if Location ==1:
                print('Toshiba')
                print('amount:Rs.30000') 
                print('quntity: ', Quantity_option)
                print('Tax amount: ',  Tax_Toshiba)
                print('Delivery Charge: RS1000')
                print('Packing bag:Rs1000')
                print('Grand Total: ', 30000+Tax_Toshiba+1000+1000)
           if Location ==2:
                print('Toshiba')
                print('amount:Rs.30000') 
                print('quntity: ', Quantity_option)
                print('Tax amount: 0',  )
                print('Delivery Charge: RS1000')
                print('Packing bag:Rs1000')
                print('Grand Total: ', 30000+0+1000+1000)
           if Location ==3:
                print('Toshiba')
                print('amount:Rs.30000') 
                print('quntity: ', Quantity_option)
                print('Tax amount: 0')
                print('Delivery Charge: RS1000')
                print('Packing bag:Rs1000')
                print('Grand Total: ', 30000+0+1000+1000)
        if Packing == 2:
           Location = int(input('Chooies Loction \n 1)KTM(13% tax) 2)BKT(f) 3)LTP(f)')) 
           if Location ==1:
                print('Toshiba')
                print('amount:Rs.30000') 
                print('quntity: ', Quantity_option)
                print('Tax amount: ',  Tax_Toshiba)
                print('Delivery Charge: RS1000')
                print('Packing bag:Rs1000')
                print('Grand Total: ', 30000+Tax_Toshiba+1000+1000)
           if Location ==2:
                print('Toshiba')
                print('amount:Rs.30000') 
                print('quntity: ', Quantity_option)
                print('Tax amount: 0',  )
                print('Delivery Charge: RS1000')
                print('Packing bag:Rs1000')
                print('Grand Total: ', 30000+0+1000+1000)
           if Location ==3:
                print('Toshiba')
                print('amount:Rs.30000') 
                print('quntity: ', Quantity_option)
                print('Tax amount: 0')
                print('Delivery Charge: RS1000')
                print('Packing bag:Rs1000')
                print('Grand Total: ', 30000+0+1000+1000)
        if Packing == 3:
           Location = int(input('Chooies Loction \n 1)KTM(13% tax) 2)BKT(f) 3)LTP(f)')) 
           if Location ==1:
                print('Toshiba')
                print('amount:Rs.30000') 
                print('quntity: ', Quantity_option)
                print('Tax amount: ',  Tax_Toshiba)
                print('Delivery Charge: RS1000')
                print('Packing bag:Rs1000')
                print('Grand Total: ', 30000+Tax_Dell+1000+1000)
           if Location ==2:
                print('Toshiba')
                print('amount:Rs.30000') 
                print('quntity: ', Quantity_option)
                print('Tax amount: 0',  )
                print('Delivery Charge: RS1000')
                print('Packing bag:Rs1000')
                print('Grand Total: ', 20000+0+1000+1000)
           if Location ==3:
                print('Toshiba')
                print('amount:Rs.30000') 
                print('quntity: ', Quantity_option)
                print('Tax amount: 0')
                print('Delivery Charge: RS1000')
                print('Packing bag:Rs1000')
                print('Grand Total: ', 30000+0+1000+1000)                  
    
    elif deliver == 2:
        print("Packing \n 1)Pasltic(rs100) 3)Bage(Rs1000) 3)Gift-box(rs3000)")
        Packing = int(input('Chooise packing: '))
        if Packing == 1:
           Location = int(input('Chooies Loction \n 1)KTM(13% tax) 2)BKT(f) 3)LTP(f)')) 
           if Location ==1:
                print('Toshiba')
                print('amount:Rs.30000') 
                print('quntity: ', Quantity_option)
                print('Tax amount: ',  Tax_Toshiba)
                print('Delivery Charge: RS1000')
                print('Packing bag:Rs1000')
                print('Grand Total: ', 30000+Tax_Toshiba+1000+1000)
           if Location ==2:
                print('Toshiba')
                print('amount:Rs.30000') 
                print('quntity: ', Quantity_option)
                print('Tax amount: 0',  )
                print('Delivery Charge: RS1000')
                print('Packing bag:Rs1000')
                print('Grand Total: ', 30000+0+1000+1000)
           if Location ==3:
                print('Toshiba')
                print('amount:Rs.30000') 
                print('quntity: ', Quantity_option)
                print('Tax amount: 0')
                print('Delivery Charge: RS1000')
                print('Packing bag:Rs1000')
                print('Grand Total: ', 30000+0+1000+1000)
        if Packing == 2:
           Location = int(input('Chooies Loction \n 1)KTM(13% tax) 2)BKT(f) 3)LTP(f)')) 
           if Location ==1:
                print('Toshiba')
                print('amount:Rs.30000') 
                print('quntity: ', Quantity_option)
                print('Tax amount: ',  Tax_Toshiba)
                print('Delivery Charge: RS1000')
                print('Packing bag:Rs1000')
                print('Grand Total: ', 30000+Tax_Toshiba+1000+1000)
           if Location ==2:
                print('Toshiba')
                print('amount:Rs.30000') 
                print('quntity: ', Quantity_option)
                print('Tax amount: 0',  )
                print('Delivery Charge: RS1000')
                print('Packing bag:Rs1000')
                print('Grand Total: ', 30000+0+1000+1000)
           if Location ==3:
                print('Toshiba')
                print('amount:Rs.30000') 
                print('quntity: ', Quantity_option)
                print('Tax amount: 0')
                print('Delivery Charge: RS1000')
                print('Packing bag:Rs1000')
                print('Grand Total: ', 30000+0+1000+1000) 
        if Packing == 3:
           Location = int(input('Chooies Loction \n 1)KTM(13% tax) 2)BKT(f) 3)LTP(f)')) 
           if Location ==1:
                print('Toshiba')
                print('amount:Rs.30000') 
                print('quntity: ', Quantity_option)
                print('Tax amount: ',  Tax_Toshiba)
                print('Delivery Charge: RS1000')
                print('Packing bag:Rs3000')
                print('Grand Total: ', 30000+Tax_Toshiba+1000+3000)
           if Location ==2:
                print('Toshiba')
                print('amount:Rs.30000') 
                print('quntity: ', Quantity_option)
                print('Tax amount: 0',  )
                print('Delivery Charge: RS3000')
                print('Packing bag:Rs1000')
                print('Grand Total: ', 30000+0+1000+3000)
           if Location ==3:
                print('Toshiba')
                print('amount:Rs.30000') 
                print('quntity: ', Quantity_option)
                print('Tax amount: 0')
                print('Delivery Charge: RS3000')
                print('Packing bag:Rs1000')
                print('Grand Total: ', 30000+0+1000+3000) 


if Product_option ==3:
    deliver=int(input("Delivery Option \n 1) Home(Rs1000) 2)Pickup(free): "))
    if deliver == 1:
        print("Packing \n 1)Pasltic(rs100) 2)Bage(Rs2000) 3)Gift-box(rs3000)")
        Packing = int(input('Chooise packing: '))
        if Packing == 1:
           Location = int(input('Chooies Loction \n 1)KTM(13% tax) 2)BKT(f) 3)LTP(f)')) 
           if Location ==1:
                print('Mac')
                print('Amount:Rs.50000')
                print('quntity: ', Quantity_option)
                print('Tax amount: ',  Tax_mac)
                print('Delivery Charge: RS1000')
                print('Packing bag:Rs1000')
                print('Grand Total: ', 50000+Tax_mac+1000+1000)
           if Location ==2:
                print('Mac')
                print('quntity: ', Quantity_option)
                print('Tax amount: 0',  )
                print('Delivery Charge: RS1000')
                print('Packing bag:Rs1000')
                print('Grand Total: ', 50000+0+1000+1000)
           if Location ==3:
                print('Mac')
                print('quntity: ', Quantity_option)
                print('Tax amount: 0')
                print('Delivery Charge: RS1000')
                print('Packing bag:Rs1000')
                print('Grand Total: ', 50000+0+1000+1000)
        if Packing == 2:
           Location = int(input('Chooies Loction \n 1)KTM(13% tax) 2)BKT(f) 3)LTP(f)')) 
           if Location ==1:
                print('Mac')
                print('quntity: ', Quantity_option)
                print('Tax amount: ',  Tax_mac)
                print('Delivery Charge: RS1000')
                print('Packing bag:Rs1000')
                print('Grand Total: ', 50000+Tax_Dell+1000+1000)
           if Location ==2:
                print('Mac')
                print('quntity: ', Quantity_option)
                print('Tax amount: 0',  )
                print('Delivery Charge: RS1000')
                print('Packing bag:Rs1000')
                print('Grand Total: ', 50000+0+1000+1000)
           if Location ==3:
                print('Mac')
                print('quntity: ', Quantity_option)
                print('Tax amount: 0')
                print('Delivery Charge: RS1000')
                print('Packing bag:Rs1000')
                print('Grand Total: ', 50000+0+1000+1000)
        if Packing == 3:
           Location = int(input('Chooies Loction \n 1)KTM(13% tax) 2)BKT(f) 3)LTP(f)')) 
           if Location ==1:
                print('Mac')
                print('quntity: ', Quantity_option)
                print('Tax amount: ',  Tax_mac)
                print('Delivery Charge: RS1000')
                print('Packing bag:Rs1000')
                print('Grand Total: ', 50000+Tax_mac+1000+1000)
           if Location ==2:
                print('Mac')
                print('quntity: ', Quantity_option)
                print('Tax amount: 0',  )
                print('Delivery Charge: RS1000')
                print('Packing bag:Rs1000')
                print('Grand Total: ', 50000+0+1000+1000)
           if Location ==3:
                print('Mac')
                print('quntity: ', Quantity_option)
                print('Tax amount: 0')
                print('Delivery Charge: RS1000')
                print('Packing bag:Rs1000')
                print('Grand Total: ', 50000+0+1000+1000)                  
    
    elif deliver == 2:
        print("Packing \n 1)Pasltic(rs100) 3)Bage(Rs1000) 3)Gift-box(rs3000)")
        Packing = int(input('Chooise packing: '))
        if Packing == 1:
           Location = int(input('Chooies Loction \n 1)KTM(13% tax) 2)BKT(f) 3)LTP(f)')) 
           if Location ==1:
                print('Mac')
                print('quntity: ', Quantity_option)
                print('Tax amount: ',  Tax_mac)
                print('Delivery Charge: RS1000')
                print('Packing bag:Rs1000')
                print('Grand Total: ', 50000+Tax_mac+1000+1000)
           if Location ==2:
                print('Mac')
                print('quntity: ', Quantity_option)
                print('Tax amount: 0',  )
                print('Delivery Charge: RS1000')
                print('Packing bag:Rs1000')
                print('Grand Total: ', 50000+0+1000+1000)
           if Location ==3:
                print('Mac')
                print('quntity: ', Quantity_option)
                print('Tax amount: 0')
                print('Delivery Charge: RS1000')
                print('Packing bag:Rs1000')
                print('Grand Total: ', 50000+0+1000+1000)
        if Packing == 2:
           Location = int(input('Chooies Loction \n 1)KTM(13% tax) 2)BKT(f) 3)LTP(f)')) 
           if Location ==1:
                print('Mac')
                print('quntity: ', Quantity_option)
                print('Tax amount: ',  Tax_mac)
                print('Delivery Charge: RS1000')
                print('Packing bag:Rs1000')
                print('Grand Total: ', 50000+Tax_mac+1000+1000)
           if Location ==2:
                print('Mac')
                print('quntity: ', Quantity_option)
                print('Tax amount: 0',  )
                print('Delivery Charge: RS1000')
                print('Packing bag:Rs1000')
                print('Grand Total: ', 50000+0+1000+1000)
           if Location ==3:
                print('Mac')
                print('quntity: ', Quantity_option)
                print('Tax amount: 0')
                print('Delivery Charge: RS1000')
                print('Packing bag:Rs1000')
                print('Grand Total: ', 50000+0+1000+1000) 
        if Packing == 3:
           Location = int(input('Chooies Loction \n 1)KTM(13% tax) 2)BKT(f) 3)LTP(f)')) 
           if Location ==1:
                print('Mac')
                print('quntity: ', Quantity_option)
                print('Tax amount: ',  Tax_mac)
                print('Delivery Charge: RS1000')
                print('Packing bag:Rs3000')
                print('Grand Total: ', 50000+Tax_mac+1000+3000)
           if Location ==2:
                print('Mac')
                print('quntity: ', Quantity_option)
                print('Tax amount: 0',  )
                print('Delivery Charge: RS3000')
                print('Packing bag:Rs1000')
                print('Grand Total: ', 50000+0+1000+3000)
           if Location ==3:
                print('Mac')
                print('quntity: ', Quantity_option)
                print('Tax amount: 0')
                print('Delivery Charge: RS3000')
                print('Packing bag:Rs1000')
                print('Grand Total: ', 50000+0+1000+3000) 
else:
     print('Their is no any product')                
