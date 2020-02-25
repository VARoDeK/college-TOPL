def rec_print(a):
    if(a == 0):
        print("%d"%a)
        return

    print("%d"%a, end=", ")
    rec_print(a-1)

print("TOPL Lab")
print("Vaibhav Gutpa")
print("Enroll - 9917103128")
print("Batch F4")
print("Quest - Write a function using recursion to print numbers from n to 0.\n")

while(1):
    contin = 0
    
    a = int(input("Enter the number: "))

    print("Patter: ", end="")
    rec_print(a)

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
