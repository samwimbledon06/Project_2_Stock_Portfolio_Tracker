from validators import validate_ticker_input, convert_valid_input_to_float # This imports the validate_ticker_input and convert_valid_input_to_float functions from the validators module.

def ask_for_user_input(user_prompt, validation_function, error_message): # This function is used to ask the user for input and validate it using a specified validation fucntion. if the input is not valid, it will print an error message and ask for input again. If the user inputs "quit", the function will return None to indicate that the user wants to quit.
    while True: # This is an infinite loop that will keep asking the user for input until they provide a valid input or choose to quit.
        user_input = input(user_prompt) #  This asks the user for input using the sepcified prompt and stores the input in a variable called user_input.
        if user_input.strip().upper() == "QUIT" or user_input.strip().upper() == "CANCEL": # This chgecksthat the user input is not "quit" or "cancel", which is not a valid input. If the user inpuit is "quit" or "cancel", the function will return None to indicate that the user wants to quit.
            return None # Return None to indicate that the user wants to quit.
        
        validated_input = validation_function(user_input) # This calls the specified validation function with the uiser input and stores the result in a variable called validated_input. If the input is valid, the validation function will return the validated input. If the input is not valid, the validation function will return None.
        
        if validated_input is not None: # This checks if the validated input is not None, which means the input was valid. If the input was valid, the function will return the validated input.
            return validated_input # Return the validated input.

        else: # This checks the validated input is None, which means the input was not valid. If the input was not valid, the function will print an error message and ask for input again.
            print(error_message) # Print the specified error message to inform the user that their input was not valid.

if __name__ == "__main__": # Only run the following code if this file is specified as the main program. This is done to prevent the code from being run when the file is imported as a module in another program.
    # print(ask_for_user_input("Please enter a ticker symbol: ", validate_ticker_input, "Invalid ticker symbol. Please try again.")) # This calls the ask_for_user_input function and passes in a prompt for the user to enter a ticker symbol. The function will keep asking for input until the user provides a valid input or chooses to quit.

    print(ask_for_user_input("What is the name of the ticker symbol: ", validate_ticker_input, "Invalid ticker symbol. Please try again.")) # This calls the ask_for_user_input function and passes in a prompt for the user to enter a purchase price. The function will keep asking for input until the user provides a valid input or chooses to quit.