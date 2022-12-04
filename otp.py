import random
a=[]
for i in range(5):
    o=random.randrange(0,9)
    o=str(o)
    a.append(o)
otp=''.join(a)
print(otp)
user=input("enter the OTP")
if(user in otp):
    print("authorized access")
else:
    print("unauthorized access")
