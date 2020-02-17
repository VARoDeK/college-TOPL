print("TOPL Lab")
print("Vaibhav Gutpa")
print("Enroll - 9917103128")
print("Batch F4")
print("Quest - WAP to check a number is prime or not.\n")

while(1):
    contin = 0
    a = int(input("Enter the number: "))

    b = a ** 0.5
    b = int(b) +2

    for i in range(2,b,1):
        if( a%i == 0 ):
            print("It is not a prime number. 1st factor is %d" %i)
            break

    else:
        print("It is a prime number.")

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
