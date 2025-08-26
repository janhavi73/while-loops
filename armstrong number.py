num=int(input("please enter a number:"))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum +=digit**3
    temp//=10
if sum == num:
    print("the number is an armstrong number")
else:
    print("it isn't an armstrong number")        
