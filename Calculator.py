n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

print("Enter the choice of operation: ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice: "))
if choice == 1:
  print("The sum of the two numbers is: ", n1 + n2)
elif choice == 2:
  print("The Subtraction of the two numbers is: ", n1 - n2)
elif choice == 3:
  print("The Multiplication of the two numbers is: ", n1 * n2)
elif choice == 4:
  if n2!= 0:
    print("The Division of the two numbers is: ", n1 / n2)
  else:
      print("The second number cannot be zero")
      print("Error: Division by zero is not allowed.")
else:
  print("Invalid choice. Please enter a valid choice.")