s=float(input("Enter the Salary : "))
gen=input("Enter the Gender : ")
if(gen=='M'or gen=='m'):
    bonus=0.1
    bonus_amount=bonus*s
    print("Bonus : ",bonus_amount)
    Total_amount=s+bonus_amount
    print("Total amount : ",Total_amount)
elif(gen=='F'or gen=='f'):
    bonus=12/100
    Bonus_amount=bonus*s
    print("Bonus : ",Bonus_amount)
    Total_amount=s+Bonus_amount
    print("Total amount : ",Total_amount)
