s1="Khushn#!#!#$873128oo#@#@kwdbehj#@#@#CAdejhTXEDHI"

u=""
l=""
d=""
s=""

for i in s1:
    if i.isupper():
        u=u+i

    elif i.islower():
        l=l+i

    elif i.isdigit():
        d=d+i

    else:
        s=s+i

res=u+l+d+s

print("The final result is: ",res) 