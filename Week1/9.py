def factorial_it(a):
    j=1
    for i in range(1,(a+1),1):
        j = j*i
    print("Factorial Iterative: %d" %j)

def factorial_rec(a):
    if(a <=0):
        return 1
    return a * factorial_rec(a-1)

print("TOPL Lab")
print("Vaibhav Gutpa")
print("Enroll - 9917103128")
print("Batch F4")
print("Quest - WAP to calculate factorial of an integer number. Write both iterative and recursive solutions.\n")

while(1):
    contin = 0
    a = int(input("Enter the number upto which Fibonacci has to be calculated: "))

    factorial_it(a)

    print("Facorial Recursive: %d" %(factorial_rec(a)))

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
