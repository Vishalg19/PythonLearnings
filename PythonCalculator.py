''' ...Calculator using Python...'''
First = int(input("Enter first number: "))
Operator = input("Enter Operator(+,-,*,/,%,//: ")
Second = int(input("Enter second number: "))

if Operator == '+':
    print(First+Second)
elif Operator == '-':
    print(First-Second)
elif Operator == '*':
    print(First*Second)
elif Operator == '/':
    print(First / Second)
elif Operator == '%':
    print(First % Second)
elif Operator == '//':
    print(First // Second)
else:
    Print("Operator Invalid")