name = input("Enter Student Name: ")
age = int(input("Enter Age: "))
percentage = float(input("Enter Percentage: "))
income = float(input("Enter Family Income: "))
rural_input = input("Is the student from a rural area? (True/False): ")

is_rural = True if rural_input == "True" else False

eligible = (percentage > 90) or (percentage > 85 and income < 300000)

print("\n----- Student Details -----")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Percentage: {percentage}%")
print(f"Family Income: {income}")
print(f"From Rural Area: {is_rural}")

if eligible:
    print("\nEligible for scholarship")
else:
    print("\nNot eligible")
