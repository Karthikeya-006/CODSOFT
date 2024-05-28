def add(a,b):
    return a+b;
def sub(a,b):
    return a-b;
def multiply(a,b):
    return a*b;
def division(a,b):
    return a/b;
while(True):
    print("Arithmetic operations:-\n"
          "1.Add\n"
          "2.Subtraction\n"
          "3.Multiplication\n"
          "4.Division\n"
          "5.exit")
    num1=int(input("enter a number:-"))
    num2=int(input("enter another number:-"))
    choose=int(input("choose the arithmetic operation:-"))
    if choose==1:
        print(num1,"+",num2,"=", add(num1,num2))
    elif choose==2:
        print(num1,"-",num2,"=", sub(num1,num2));
    elif choose==3:
        print(num1,"*",num2,"=", multiply(num1,num2));
    elif choose==4:
        print(num1,"/",num2,"=", division(num1,num2));
    elif choose==5:
        break;
else:
    print("please choose an opertion")
