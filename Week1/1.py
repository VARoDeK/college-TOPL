print("TOPL Lab")
print("Vaibhav Gutpa")
print("Enroll - 9917103128")
print("Batch F4")
print("Quest - Write a program (WAP) to read a number and check it is even or odd.\n")

while(1):
    contin = 0
    
    x = int(input("Enter the Number: "))
    if( x & 0x1 == 0 ):
        print("The number is Even")
    else:
        print("The number is Odd")

    while(1):
        a = str(input("\nDo you want to continue checking numbers? (y/n)"))
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
