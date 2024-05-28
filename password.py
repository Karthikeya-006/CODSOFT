import random
import string
l=string.ascii_lowercase
L=list(l)
u=string.ascii_uppercase
U=list(u)
d=string.digits
D=list(d)
s=string.punctuation
S=list(s)
p_len=int(input("enter the length of the password\n"))
p=[]
p.extend(L)
p.extend(U)
p.extend(D)
p.extend(S)
password=("".join(random.sample(p,p_len)))
while password[0] in S or password[0] in D:
    password=("".join(random.sample(p,p_len)))
print("password is :\t")
print(password)
