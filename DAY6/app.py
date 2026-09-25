print("=" * 40)
print("       MULTIPLICATION TABLE")
print("=" * 40)

# Accept input from the user
number = int(input("Enter the number: "))
limit = int(input("Enter the multiplication limit: "))

print("\n" + "-" * 40)
print(f"Multiplication Table of {number}")
print("-" * 40)

# Generate multiplication table
for i in range(1, limit + 1):
    result = number * i
    print(f"{number} × {i} = {result}")

print("-" * 40)
print("Table generated successfully!")