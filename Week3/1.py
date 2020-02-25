from os import getcwd

print("TOPL Lab")
print("Vaibhav Gutpa")
print("Enroll - 9917103128")
print("Batch F4")
print("Quest - Write a function to concatenate the contents of two files into another.n")

while(1):
    contin = 0
    a = getcwd()
    a += "/"
    f1 = open(a+"file1.txt", "rt")
    f2 = open(a+"file2.txt", "rt")
    f3 = open(a+"file3.txt", "wt")

    b = f1.read()
    print("Content of file1: ", b)
    f3.write(b)
    b = f2.read()
    print("Content of file2: ", b)
    f3.write(b)

    f1.close()
    f2.close()
    f3.close()

    f3 = open(a+"file3.txt", "rt")
    b = f3.read()
    f3.close()
    print("Content of file3: ", b)

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
