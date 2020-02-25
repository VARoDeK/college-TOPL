def rec_max(a, maxx):
    del a[0]
    if len(a) == 0:
        print("The max number is: %d"%maxx)
        return

    if(maxx < a[0]):
        maxx = a[0]
    
    rec_max(a, maxx)

print("TOPL Lab")
print("Vaibhav Gutpa")
print("Enroll - 9917103128")
print("Batch F4")
print("Quest - Write a recursive function that has a parameter representing a list of integers and returns the maximum stored in the list.(Without using library support)\n")

while(1):
    contin = 0
    
    a = int(input("Enter the number of elements: "))
    b = []

    for i in range(a):
        b.append(int(input("Enter the elemets %d: "%(i+1))))

    maxx = b[0]

    rec_max(b, maxx)


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
