# Validator functions for input validation

# Validating user input for the value they input e.g. price or quantity. This function checks if the input is a valid float and returns None if it is not valid. It also checks if the input is a positive number and returns None if it is not.
import math # Importing the math module to use the isfinite function for checking if the value is finite
from datetime import datetime # Importing the datetime module to use the strptime function for checking if the date is valid

MAX_YEARS_BACK = 100 # This is a constant that defines the maximum number of years back that a date can be. This is used to check if the date input is valid.

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

def validate_ticker_input(user_input): # This function is used to validate the ticker symbol input by the user.
    if not isinstance(user_input, str) or user_input.strip() == "": # Checks if the input is empty or just whitespace and the input is not a string, which is not valid for a ticker symbol
        return None # Return None to indicate that the input was invalid.

    user_input = user_input.strip() # This removes any whitespace from the beginning and end of the string. This is done to standardize the input and make it easier to compare with other ticker symbols.  

    letter_count = 0 # This initializes a variable to count the number of letters in the input string. This is done to check if the there is at least one letter for a ticker symbol.
    for char in user_input: # This loops through each character in the input string and checks if it is a valid character for a ticker symbol. Ticker symbols can only contain letters, hyphens, and dots. If any character is not valid, the function returns None to indicate that the input was invalid.
        if not char.isalpha() and char not in (".", "-"): # Checks if the character is not a letter and not a dot or hyphen, which is not valid for a ticker symbol
            return None # Return None to indicate that the input was invalid.

        if char.isalpha(): # Checks if the character is a letter, which is valid for a ticker symbol
            letter_count += 1 # This increments the letter count by 1 for each letter in the input string. This is done to check that the input should have at least one letter.
        

    if letter_count == 0: # Checks if the letter count is zero, which means the input was just a dot or hyphen and not a valid ticker symbol
        return None # Return None to indicate that the input was invalid.
    
    if len(user_input) > 7: # Checks if the length of the input is greater than 7, which is not valid for a ticker symbol
        return None # Return None to indicate that the input was invalid.

    user_input = user_input.upper() # This converts the input to uppercase. This is done to standardize the input and make it easier to compare with other ticker symbols.

    return user_input # Return the validated and standardized ticker symbol input.

def validate_date_input(user_input): # This function is used to validate the date input by the user.
    if not isinstance(user_input, str): # Checks if the user input is not a string, which is not valid for date input
        return None # Return None which indicates that the date is not valid

    user_input = user_input.strip() # This removes any whitespace from the beginning and end of the string. This is done to standardize the input and make it easier to compare with other date inputs.

    if user_input == "": # Checks if the input is empty or just whitespace, which is not valid for a date input
        return None # Return None to indicate that the input was invalid.
    
    try:
        date_value = datetime.strptime(user_input, "%Y-%m-%d") # This converts the string that is automatically parsed from the input into a datetime object. The format is specified as "%Y-%m-%d" which means the date should be in the format of "YYYY-MM-DD".
    
    except ValueError: # If the conversion to datetime fails, it means the input was not a valid date format
        return None # Return None to indicate that the input was invalid.

    if date_value > datetime.now() or date_value.year < datetime.now().year - MAX_YEARS_BACK: # Checks if the date is in the future or more than of the 1st of the year from 100 years in the past, which is not valid for a date input
        return None # Return None to indicate that the input was invalid.

    string_date = datetime.strftime(date_value, "%Y-%m-%d") # This converts the datetime object back into a string in the format of "YYYY-MM-DD". This is done to standardize the input and make it easier to compare with other date inputs.
    return string_date # Return the validated and standardized date input.

validate_ticker_input(None)
# Testing different inputs for convert_valid_input_to_float function
if __name__ == "__main__":
    test_inputs = ["12.50", "abc", "", "-5", "nan", "inf", "0", "0.0", "-inf"]
    for input_value in test_inputs:
        print(convert_valid_input_to_float(input_value)) # Print the result of convert_valid_input_to_float for each test inputs.

    test_inputs_str = ["AAPL", "aapl", " aapl ", "GOOGL", "BRK.B", "", "123", "A B", None, 123, ".", "-", "A.B.C", "GOOGL.L", "TOOLONG1"]
    for input_value in test_inputs_str:
        print(validate_ticker_input(input_value)) # Print the result of validate_ticker_input for each test inputs.

    test_inputs_date = ["2026-10-08", "2026-13-45", "08/10/2026", "2026-02-30", "", None, "yesterday", "2026-1-5", "2026-12-31"]
    for input_value in test_inputs_date:
        print(validate_date_input(input_value)) # Print the result of validate_date_input for each test inputs.

    
    