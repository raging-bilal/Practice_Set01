# s1="Khushnood"
# l=len(s1)
# rev=""

# for i in range(l-1,-1,-1):

#     rev=rev+s1[i]
# print('The reverse string are as follows:')
# print(rev,end="")




s1="Tenet"

# s1="Khushnood Bilal"
s2=s1[::-1]

if s1==s2:
    print("{0} is palindrome! ".format(s1))

else:
    print("{0} is NOT palindrome! ".format(s1))
