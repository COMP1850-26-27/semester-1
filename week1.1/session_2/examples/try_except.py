try:
    num1 = int(input("Enter your number: "))
    num2 = int(input("Enter your number: "))
    answer = num1 + num2
    print(f"{num1} + {num2} = {answer}")
except:
    print("Please enter numbers only.")
    