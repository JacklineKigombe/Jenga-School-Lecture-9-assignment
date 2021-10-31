#Calculating the sum of 1 to 1000

def main():
    n = int(input("Enter the number of the first natural numbers: "))
    fact = 0
    for i in range (1,n+1):
        fact = fact + i

    print("The sum of the first", n,"natural numbers is ",fact)


main()
