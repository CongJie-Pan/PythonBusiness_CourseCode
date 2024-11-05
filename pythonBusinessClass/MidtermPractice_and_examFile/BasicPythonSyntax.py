# 1. ------------------
print("1.")
def findEvens(numList):
    for num in numList:
        if num%2 == 0:
            print(num)

numList = [10, 20, 33, 46, 55]
print("Finding Even Numbers: " )
findEvens(numList)

print("---")
# 2. ------------------
print("2.")

for i in range(5, 0, -1):
    for j in range(i):
        print(i,end=" ")
    print()

print("---")
# 3. ---------------------
print("3.")

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

# Ask the user to input number
try:
    user_input = int(input("Enter a number: "))

    if is_prime(user_input):
        print(f"{user_input} is a prime number")
    else:
        print(f"{user_input} is not a prime number")
except ValueError:
   print("The invalid input , please enter again")

print("---")
#4. ----------------------------------
print("4.")

def read_names_from_file(file_name):
    """Read the file and return a list of names"""
    with open(file_name, "r") as file:
        return file.read().splitlines()  # Return the list directly

def count_girls_names(names, girl_names):
    """Count and return matching girl names"""
    matched_names = [name for name in names if name in girl_names]
    return matched_names

# Read the names from "names.txt" and "GirlNames.txt"
names = read_names_from_file('names.txt')
girl_names = read_names_from_file('GirlNames.txt')

# Count and get the matching girl names
matched_names = count_girls_names(names, girl_names)

# Output the result
print(f"Number of matching girl names: {len(matched_names)}")
print("The matching girl names are:")
for i, name in enumerate(matched_names, start=1):
    print(f"({i}) {name}")  # Print each name on a new line and adding the sequence number


