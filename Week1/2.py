def percentage():
    a = 0.0
    for i in range(5):
        a += float(input("Enter the marks of subject (out of 100) %d: " %(i+1)))
    print("The sum of marks is %f." %a)
    a = a/5
    print("The percentage is: %f." %a)
    grade( a )

def grade( a ):
    if ( a >= 60.0 ):
        print("First Division.")
    elif( a<60.0 and a>=50.0 ):
        print("Second Division")
    elif( a<50.0 and a>=40.0 ):
        print("Third Division")
    else:
        print("FAIL")

print("TOPL Lab")
print("Vaibhav Gutpa")
print("Enroll - 9917103128")
print("Batch F4")
print("Quest - WAP to find the sum and percentage of marks of five subjects. \
\n\tIf the percentage is =60 then print FIRST division\
\n\telse If the percentage is <60 and >=50 then print SECOND division\
\n\telse If the percentage is <50 and >=40 then print THIRD division\
\n\telse If the percentage is <40 then print FAIL.\n")

while(1):
    contin = 0
    percentage()

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
