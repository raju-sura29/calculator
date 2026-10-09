num1=int(input("give num1; "))
num2=int(input("give num2; "))
conditon=input("give condition; ")

def calculator():
    if conditon=="+":
        print(f"addtion is:{num1+num2}")
    elif conditon=="-":
        print(f"subraction is:{num1-num2}")
    elif conditon=="*":
        print(f"multiplication is:{num1*num2}")
    try:
        if conditon=="/" and num2==0:
            print(f"division is:{num1/num2}")
        elif conditon=="/":
            print(f"division is:{num1/num2}")
    except ZeroDivisionError:
        print(f"undefind, {num1} can't divide by 0")
calculator()
