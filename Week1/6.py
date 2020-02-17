print("TOPL Lab")
print("Vaibhav Gutpa")
print("Enroll - 9917103128")
print("Batch F4")
print("Quest - WAP to check a number is Armstrong number or not\n")

while(1):
    contin = 0
    a = int(input("Enter the number: "))

    b = list(str(a))
    x=0
    for i in b:
        x += int(i)**3

    if( a==x ):
        print("It is an Armstrong number.")
    else:
        print("It is not an Armstrong number.")

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
