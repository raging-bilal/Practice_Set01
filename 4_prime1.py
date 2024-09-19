# def checkPrime(n):
#     if n<=1:
#         print("INVALID INPUT! Please enter positive integers: !")
#     else:
#         for i in range(2,n):
#             if n%i==0:   
#                 print("Not Prime!")
#                 break
#         else:
#             print("Prime")
# n=int(input("Enter the number to check if the given number is Prime or Not: "))
# checkPrime(n)










# else clause with Loop
# when iteration is exhausted

a=12
for i in range(2,a):
    if a%i==0:
        print("Not Prime------")
        break
else:
    print("Prime------")
