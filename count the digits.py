num=int(input("please enter a number: "))
if num ==0:
    count=1
else:
    if num < 0:
        num=num * -1
    count=0
    while num >0:
        num //=10
        count +=1
print("the number has", count,"digits")        
