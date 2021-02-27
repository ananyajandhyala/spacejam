#RANDOM CODE GENERATOR FOR OTP FOR SPACEJAM
from datetime import date,datetime
import random
today=date.today()
d1 = today.strftime("%d")
d2=  today.strftime("%d/%m/%Y")
print("Date", d2)
now=datetime.now()
current_time = now.strftime("%H")
end_time=int(current_time)+1
d=int(d1)

otp=random.randint(1000,5000)
print(otp)
user=int(input("Enter code sent to you by resident"))
today=date.today()
d1 = today.strftime("%d")
current_time = now.strftime("%H")
if(int(d1)==d and int(current_time)<=end_time):
    if(user==otp ):
        print("Access granted")
    else:
        print("Access denied")
else:
    print("Code is Invalid")

