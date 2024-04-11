from chempy import balance_stoichiometry  # Import the balance_stoichiometry function


# Define a function to balance a chemical equation
def balance_chemical_equation(reactants, products):
    try:
        # Balance the stoichiometry
        balanced_reactants, balanced_products = balance_stoichiometry(reactants, products)
        # Return the balanced equation
        return balanced_reactants, balanced_products
    except ValueError as e:
        # Handle the case where reactants or products are missing
        return f"Error: {e}. Please ensure all reactants and products are correctly entered."


# Get user input for reactants and products
user_reactants = set(input("Enter the reactants (separated by space): ").split())
user_products = set(input("Enter the products (separated by space): ").split())

# Call the function to balance the equation
result = balance_chemical_equation(user_reactants, user_products)

# Check if the result is an error message or a tuple of balanced equations
if isinstance(result, tuple):
    balanced_reactants, balanced_products = result
    # Print the balanced equation
    print('Balanced reactants:', balanced_reactants)
    print('Balanced products:', balanced_products)
else:
    # Print the error message
    print(result)
