def prime(low, upper):
    for i in range(low, upper):
        for j in range(2, i):
            if i % j == 0:
                break

        else:
            print(i, end=" ")
low= int(input("Enter the lower range: "))
upper = int(input("Enter the upper range: "))
prime(low, upper)
