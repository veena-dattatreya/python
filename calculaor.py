import os


def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
symbol={'+':add,'-':sub,'*':mul,'/':div}
def calculator():
    first=eval(input("enter first number:"))
    flag=True
    while flag:
        sym=input("enter operater")
        second=eval(input("enter second number:"))
        cal_fun=symbol[sym]
        output=cal_fun(first,second)
        print(f"{output}")
        continue_1=input("do u want to continue y or n:").lower()
        if continue_1=="y":
            first=output
        elif continue_1==("n"):
            flag=False
            os.system('cls')
        else:
            flag=False
            print('bye')
            os.system('cls')

calculator()




