def fibonacci_it(a):
    j=0
    i=1
    while ( j<a ):
        print(j, end=" ")
        j = i+j
        i = j-i

def fibonacci_rec(a,i,j):
    if( j > a ):
        return
    print(j, end=" ")
    j = i+j
    i = j-i
    fibonacci_rec(a,i,j)

print("TOPL Lab")
print("Vaibhav Gutpa")
print("Enroll - 9917103128")
print("Batch F4")
print("Quest - WAP to print Fibonacci series up to given number. Write both iterative and recursive solutions.\n")

while(1):
    contin = 0
    a = int(input("Enter the number upto which Fibonacci has to be calculated: "))

    print("Fibonacci Series Iterative: ", end="")
    fibonacci_it(a)

    print("\nFibonacci Series Recursive: ", end="")
    fibonacci_rec(a,1,0)

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
