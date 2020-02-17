print("TOPL Lab")
print("Vaibhav Gutpa")
print("Enroll - 9917103128")
print("Batch F4")
print("Quest - WAP to check a number is palindrome or not.\n")

while(1):
    contin = 0
    a = str(int(input("Enter the number: ")))

    b = a[::-1]
    if(a==b):
        print("It is a plaindrome.")
    else:
        print("It is not a palindrome.")


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
