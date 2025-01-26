def Ruppes_Dollar():
    Rupess = int(input("Enter a Rupess Amount: "))
    RuppesCovert = Rupess/130
    print("The Exchange is : ",RuppesCovert)
    return RuppesCovert
    

def pasisa_Ruppes():
    Pasisa = int(input("Enter Pasis Amount: "))
    PasisaConvert = Pasisa/50
    print("The Ruppes you have is: ",PasisaConvert)
    return PasisaConvert()

def even_odd():
    num  = int(input("Enter a number: "))
    if num%2==0:
        print("EVEN")
    else:
        print("ODD")    
    return num()

def Vowel_Consonent():
    valwel = {'a','e','i','o','u'}

    alphabat = input("Enter a alphabet: ")

    if alphabat in valwel:
        print("this is vowel latter: ")
    else:
        print("Its a consonent latter")


Chooies = int(input("Waht your want to do(1-3) \n 1) Convert Ruppes into dollar 2)Covert Pasisa into Ruppes 3)Find even or odd 4)Vowel And Consoent: "))
if Chooies == 1:
    RuppesDollar = Ruppes_Dollar()
    print(RuppesDollar)
elif Chooies == 2:
    PasisaRuppes = pasisa_Ruppes()
    print(PasisaRuppes)
elif Chooies == 3:
    EvenOdd = even_odd()
    print(EvenOdd)  
elif Chooies == 4:
    vowelconsonent = Vowel_Consonent()
    print(vowelconsonent)          
else:
    print("Invalid number you type Please Try again")

    