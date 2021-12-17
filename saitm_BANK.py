name=input("welcome to saitm BANK\n enter your name: ")
start=int(input("enter your password: "))
amount=45000
while True:
    if (start==1234):
        print("1withdraw money\n2 Update password\n3 exit")
        num=input("choose your Option: ")
        if num=='1':
            withdraw=int(input())
            print('collect your cash')
            amount=amount-withdraw
            ver=input("you want to see your your total balance?(Yes/No)")
            if ver=='yes':
                print("your total amount is",amount)
            else:
                print("enter your option")
        elif num=='2':
            pin=int(input())
            password=1234
            if pin==password:
                p1=int(input("enter you current pic: "))
                p2=int(input("enter new pin: "))
                password=p2
                print("password has been update: " ,password)

        elif num=='3':
            print("tranaction is complete")
            print("thanks for choosing saitm bank")
    else:
        print("enter password is invalid")
        break
