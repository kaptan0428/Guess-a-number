n= int(input("Enter the no to guess : "))
j= int(input("Max no of attempts to guess no : "))

i= 1
while(i<=j):
    m = int(input("Enter the no : "))
    if (m<n and i<j):
        print("Enter a bigger no ")
        print("No of guesses left = ",j-i)
    elif (m>n and i<j):
        print("Enter a smaller no ")
        print("No of guesses left = ", j - i)
    elif (m==n):
        print("Congrates !! Right ans")
        print("No of guesses to finish = ",i)
        break
    if (i==j):
        print("No attempt left")
        print("Game over !! you loose")
