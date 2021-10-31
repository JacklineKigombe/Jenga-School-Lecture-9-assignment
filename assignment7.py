#Sum of numbers
#Input from the user

def main():
    fi = int(input("Enter the first number: "))
    se = int(input("Enter the second number: "))
    thi = int(input("Enter the third number: "))
    fou = int(input("Enter the fourth number: "))
    fif = int(input("Enter the fifth number: "))
    list = [fi,se,thi,fou,fif]
    sum = 0
    for i in list:
        sum = sum + i
    print ("The sum of the numbers is",sum)

main()

    

