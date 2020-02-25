def gcd(a,b):
    if(a==0):
        return b

    if(b==0):
        return a

    if( a<b ):
        x = gcd(a, b-a)
    else:
        x = gcd(a-b, b)
    return x

print("TOPL Lab")
print("Vaibhav Gutpa")
print("Enroll - 9917103128")
print("Batch F4")
print("Quest - Write a function to get the least common multiple (LCM) of two positive integers..\n")

while(1):
    contin = 0
    a = int(input("First number: "))
    b = int(input("Second number: "))

    c = gcd(a,b)

    d = a*b/c

    print("The LCM is: %d"%d)

    while(1):
        a = str(input("\nDo you want to continue? (y/n)"))
        if( a == 'y' or a == 'Y' ):
            contin = 1
            break
        elif( a == 'n' or a == 'N' ):
            contin = 0
            break
        else:
            print("Enter correct option.\n")
            continue
    if( contin == 1 ):
        print("\n----------------------\n")
        continue
    else:
        break
