def calculator():
    print("Enter first number:")
    x = int(input())
    print("Enter second number:")
    y = int(input())
    print("Enter + for add, - for subtract")
    z = input()
    if z == "+":
        print("Sum is ",x+y)
    else:
        print("Diff is ",x-y)


