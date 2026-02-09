import math

print("===== Scientific Calculator =====")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Square")
print("6. Square Root")
print("7. Power")
print("8. Logarithm (base 10)")
print("9. Sine")
print("10. Cosine")
print("11. Tangent")

choice = int(input("Enter your choice (1-11): "))

if choice in [1, 2, 3, 4, 7]:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

if choice == 1:
    print("Result:", a + b)

elif choice == 2:
    print("Result:", a - b)

elif choice == 3:
    print("Result:", a * b)

elif choice == 4:
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: Division by zero")

elif choice == 5:
    a = float(input("Enter number: "))
    print("Result:", a * a)

elif choice == 6:
    a = float(input("Enter number: "))
    print("Result:", math.sqrt(a))

elif choice == 7:
    print("Result:", math.pow(a, b))

elif choice == 8:
    a = float(input("Enter number: "))
    print("Result:", math.log10(a))

elif choice == 9:
    a = float(input("Enter angle in degrees: "))
    print("Result:", math.sin(math.radians(a)))

elif choice == 10:
    a = float(input("Enter angle in degrees: "))
    print("Result:", math.cos(math.radians(a)))

elif choice == 11:
    a = float(input("Enter angle in degrees: "))
    print("Result:", math.tan(math.radians(a)))

else:
    print("Invalid choice")
