#AMOUNT TO BE PAID IS FIXED FOR THE RANGE 1-100 PRICE=$4/UNIT
#AMOUNT TO BE PAID FOR THE UNIT RANGE 100-200, PRICE=$5.50/UNIT
#AMOUNT TO BE PAID FOR THE UNIT RANGE 200-300, PRICE=$7.5/UNIT
#AMOUNT TO BE PAID FOR THE UNIT RANGE ABOVE-300, PRICE=$10/UNIT
a=int(input("enter your units"))
b=0 #payable amount
c=0 #variable to help in unit calculations
if a>0 and a<101:
     b=a*4
     print("your total payable amount is=" ,b)
elif a>100 and a<201:
    c=a-100
    b=(c*5.50)+400
    print("your total payable amount is=",b)
elif a>200 and a<301:
     c=a-200
     b=(c*7.5)+950
     print("your total payable amount is=",b)
elif a>300:
     c=a-300
     b=(c*10)+1700
     print("your total payable amount is=",b)