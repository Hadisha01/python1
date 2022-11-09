import random
N = int(input("Enter your number:"))
l = random.randint(0,1)
r = random.randint(1,9)
if N < 1:
    print("vry low")
    print(l)
elif N >1 and N <9:
    print("exactly right")
    print(r)
    
else:
    print("very high")
    print(random.randrange(9,N))
        
        
    
             