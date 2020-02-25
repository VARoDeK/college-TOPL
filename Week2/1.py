def rec_mult(a,b):
    if(a == 1):
        return b
    
    b += rec_mult(a-1, b)
    return b

print("TOPL Lab")
print("Vaibhav Gutpa")
print("Enroll - 9917103128")
print("Batch F4")
print("Quest - Write a function that takes in two numbers and recursively multiplies them together.\n")

while(1):
    contin = 0

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if(a<b):
        x = rec_mult(a,b)
    else:
        x = rec_mult(b,a)

    print("The product is: %d"%x)

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
