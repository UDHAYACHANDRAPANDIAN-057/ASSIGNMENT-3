m1=int(input("Enter a mark1:"))
m2=int(input("Enter a mark2:"))
m3=int(input("Enter a mark3:"))
total=m1+m2+m3
avg=total/3
if(avg>90):
    print("Grade O")
elif(90>avg>=80):
    print("Grade A+")
elif(80>avg>=70):
    print("Grade A")
elif(70>avg>=60):
    print("Grade B+")
elif(60>avg>=50):
    print("Grade B")
else:
    print("Grade U")
