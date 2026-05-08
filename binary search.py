data=[11,22,33,66,55,44,99,88,77]
num=int(input('enter a number to find in the data:'))
min=0
temp=0
max=len(data)-1
while min<=max:
    mid=(min+max)//2
    if data[mid]==num:
        temp=1
        break
    elif data[mid]>num:
        max=mid-1
    else:
        min=mid+1
if temp==1:
    print("match found",)
else:
    print("match is not found")