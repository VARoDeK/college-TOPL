def rec_count(a):
    if(a<10):
        return 1

    return 1+rec_count(a/10)

print("TOPL Lab")
print("Vaibhav Gutpa")
print("Enroll - 9917103128")
print("Batch F4")
print("Quest - Find number of digits in a number\n")

while(1):
    contin = 0
    
    a= int(input("Enter the number: "))

    b = rec_count(a)

    print("The number of digits is: %d"%b)

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
