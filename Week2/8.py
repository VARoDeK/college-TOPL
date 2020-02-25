def rec_triangle(a,b):
    if(len(a) <= 1):
        b.append(1)
        return b

    b.append(a[0] + a[1])
    del a[0]
    c = rec_triangle(a,b)
    return c

print("TOPL Lab")
print("Vaibhav Gutpa")
print("Enroll - 9917103128")
print("Batch F4")
print("Quest - Write a function which implements the Pascal's triangle:\n")

while(1):
    contin = 0

    x = int(input("Enter number of lines in triangle: "))
    
    a = [1]
    for i in range(x):
        print(a, sep=" ")
        a = rec_triangle(a,[1])

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
