# Validator functions for input validation

# Validating user input for the value they input e.g. price or quantity. This function checks if the input is a valid float and returns None if it is not valid. It also checks if the input is a positive number and returns None if it is not.
import math # Importing the math module to use the isfinite function for checking if the value is finite

def convert_valid_input_to_float(user_input):
    try:
        float_value = float(user_input) # This converts the string that is automatically parsed from the input into a float

    except ValueError: # If the conversion to float fails, it means the input was not a valid value (e.g. a string that cannot be converted to a float)
        return None # Return None to indicate that the input was invalid
    
    if float_value <= 0 : # Checks if the value is negative or zero, which is not valid for a purchase price
        return None # Return None to indicate that the input was invalid.

    if not math.isfinite(float_value): # Checks to see if float_value is a finite number 
        return None

    return float_value


# Testing different inputs for convert_valid_input_to_float function
if __name__ == "__main__":
    test_inputs = ["12.50", "abc", "", "-5", "nan", "inf", "0", "0.0", "-inf"]
    for input_value in test_inputs:
        print(convert_valid_input_to_float(input_value)) # Print the result of convert_valid_input_to_float for each test inputs