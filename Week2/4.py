def rec_rev(a,b,c):
    if c == 0:
        b += a[c]
        print(b)
        return

    b += a[c]
    rec_rev(a,b,c-1)


print("TOPL Lab")
print("Vaibhav Gutpa")
print("Enroll - 9917103128")
print("Batch F4")
print("Quest - Write a function using recursion that takes in a string and returns a reversed copy of the string. (Without using string library support)\n")

while(1):
    contin = 0
    
    a = str(input("Enter the string: "))

    a = list(a)
    b = ""

    rec_rev(a,b, len(a)-1)


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
