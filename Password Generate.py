import random
passlen = int(input("Enter the length of Password : "))
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*?"
p = "".join(random.sample(s,passlen ))
print(p)