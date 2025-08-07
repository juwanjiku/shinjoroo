# Question 1: Create the calculate_discount function
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price

# Question 2: Use the function with user input
# Prompt the user for the original price and discount percentage
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    # Call the function with user inputs
    final_price = calculate_discount(original_price, discount_percentage)

    # Check if a discount was applied and print the result
    if final_price < original_price:
        print(f"The final price after a {discount_percentage}% discount is: ${final_price:.2f}")
    else:
        print("No discount was applied.")
        print(f"The original price remains: ${original_price:.2f}")

except ValueError:
    print("Invalid input. Please enter a number for price and discount percentage.")