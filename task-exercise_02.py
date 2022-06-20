#FAULTY CALCULATOR

print("Enter first number")
num1=int(input())

print("Enter second number")
num2= int(input())

print("Which operation would you like to perform?")
ab=input("Enter any of these for specific operation +, -, +, /: ")

result= 0 

if ab=='+':
    result= num1 + num2 
elif ab=='-':
    result=num1 - num2 
elif ab=='*':
    result=num1 *num2 
elif ab=='/' :
   result=num1/num2
else:
    print("Input character not recognized")

print(num1,ab,num2, "=" ,result)



if  num1 == 56:
    num2==9
    ab=='+'
    result= num1 + num2
    print("77")
elif num1== 45:
     num2==3
     ab=='*'
     result=45 * 3
     print("555")
else:
     num1==56
     num2==6
     ab=='/'
     result= 56 / 6
     print("4")
