# Create a list containing four fruits
fruits = ["apple", "banana", "mango", "orange"]

# Print the first and last item using indexes
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Append a fifth fruit and print the whole list
fruits.append("pineapple")
print("After appending:", fruits)

# Remove one fruit and print the list again
fruits.remove("banana")
print("After removing:", fruits)

# Print how many fruits remain using len()
print("Number of remaining fruits:", len(fruits))
