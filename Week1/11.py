def gcd(a,b):
    if(a==0):
        print("The GCD is: %d"%b)
        return

    if(b==0):
        print("The GDC is: %d"%a)
        return

    if( a<b ):
        gcd(a, b-a)
    else:
        gcd(a-b, b)

print("TOPL Lab")
print("Vaibhav Gutpa")
print("Enroll - 9917103128")
print("Batch F4")
print("Quest - Write a function to compute the greatest common divisor (GCD) of two positive integers.\n")

while(1):
    contin = 0
    a = int(input("Firstr number: "))
    b = int(input("Firstr number: "))

    gcd(a,b)

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
