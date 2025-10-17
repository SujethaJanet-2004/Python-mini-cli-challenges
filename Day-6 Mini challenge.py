# Built-in Functions

print("Welcome to Mini Function Playground App")

while True:
    print("\nEnter an option of your choice")
    print("1. Sum the elements")
    print("2. To find maximum of elements")
    print("3. To find minimum of elements")
    print("4. To sort the elements")
    print("5. To find length of elements")
    print("6. Exit")  # Added exit option
    
    op = input("Enter option number: ")

    # Input the list only once per loop
    numbers = input("Enter numbers separated by space: ")
    user = [int(x) for x in numbers.split()]

    # Define functions correctly
    def add(nums):
        return sum(nums)
    
    def maximum(nums):
        return max(nums)
    
    def minimum(nums):
        return min(nums)
    
    def sorting(nums):
        return sorted(nums)
    
    def length(nums):
        return len(nums)

    # Execute based on user choice
    if op == '1':
        print("Sum:", add(user))
    elif op == '2':
        print("Maximum:", maximum(user))
    elif op == '3':
        print("Minimum:", minimum(user))
    elif op == '4':
        print("Sorted:", sorting(user))
    elif op == '5':
        print("Length:", length(user))
    elif op == '6':
        print("Exiting Mini Function Playground. Goodbye!")
        break
    else:
        print("Invalid option! Please enter 1-6.")