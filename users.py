username = input("Enter your name:")
userage = int(input("Enter your age:"))

def Age(userage):
    use = 100-userage+2022
    return use
use = Age(userage)
msg = "Hello %s!!! your age is %d and you will turn 100 in the year %d"  %(username,userage,use)  
print(msg)
