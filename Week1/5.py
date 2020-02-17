print("TOPL Lab")
print("Vaibhav Gutpa")
print("Enroll - 9917103128")
print("Batch F4")
print("Quest - WAP to check a number is power of 2\n")

while(1):
    contin = 0

    a = int(input("Enter the number: "))
    i = 1;
    j = 0;

    while(1):
        i = 1<<j
        if( i == a):
            print("The number is 2^%d." %j)
            break
        if( i > a ):
            print("It is not a power of 2.")
            break;
        j = j+1

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
