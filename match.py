operator = input("enter a operator: ")

match operator:
    case "+":
         a = int(input("Enter a 1st num: "))
         b = int(input("enter a 2nd num: "))
         print(a+b)
    case "-":
         a = int(input("Enter a 1st num: "))
         b = int(input("enter a 2nd num: "))
         print(a-b)
    case "*":
        print("2*4: ",2*4)        