import os
def main():
    print("Simple Calculator\n")
    print("Enter \'a\' for addition.")
    print("Enter \'s\' for subtraction.")
    print("Enter \'m\' for multiplication.")
    print("Enter \'d\' for division.")
    print("Enter \'q\' to quit.\n")
    options=[ "a", "s", "m", "d", "q"]
    num1, num2= 1, 2
    option={"a": addition, "s":subtraction, "m": multiplication, "d": division, "q": None}
    while True:
        choice=input("Enter your choice: ").lower()
        if choice not in option.keys():
            print("Invalid Input!")
        else:
            break
    if choice == "q":
        exit()
    while True:
        num1=input("Enter a number: ")
        num2=input("Enter a number: ")
        if not(check_int_float(num1) and check_int_float(num2)):
            print("Invalid Input!")
        else:
            break        
    num1, num2=float(num1), float(num2) 
    ans=option[choice](num1, num2)   
    print(f"Current result: {ans}")
    while True:
            more=input("Enter more (y/n): ").lower()
            if more == "y":
                num2=input("Enter another number: ")
                if not(check_int_float(num2)):
                    print("\nInvalid Input!")
                    continue
                num2=float(num2)
                num1=ans
                ans=option[choice](num1, num2)
                print(f"Result: {ans}") 
            else:
                os.system("clear")
                main()
                break 
def check_int_float(n):
    if "." in n:
        n=n.replace(".", "")
    if n.isdigit():
        return True
    else:
        return False                            
def addition(num1, num2):
    return num1+num2                
def subtraction(num1, num2):
    return num1-num2              
def multiplication(num1, num2):
    return num1*num2                
def division(num1, num2):
    if num2 == 0.0:
        print("Zero Division Error! Try again")
        main()
    else:
        return num1/num2                                                                                 
    
main()    