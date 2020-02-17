print("TOPL Lab")
print("Vaibhav Gutpa")
print("Enroll - 9917103128")
print("Batch F4")
print("Quest - Print Pattern.\n")

while(1):
    contin = 0
    a = int(input("Max no of stars: "))
    a = a+1

    for i in range(1,a,1):
        print("*"*i)
    a = a-2    
    for i in range(a,0,-1):
        print("*"*i)

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
