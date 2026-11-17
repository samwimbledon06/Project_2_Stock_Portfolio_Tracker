from validators import convert_valid_input_to_float, validate_ticker_input, validate_date_input # This imports the validate_date_input, validate_ticker_input and convert_valid_input_to_float functions from the validators module.
from holding import Holding # This imports the Holding class from the holding module.

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

def buy(holdings): # This function is used to buy a stock and add it to the portfolio. It takes in the holdings dictionary as an argument and returns the updated holdings dictionary. The function will ask the user for input to buy a stock and add it to the portfolio. The function will validate the user input using the specified validation functions. If the user chooses to quit, the function will return the original holdings dictionary.
    ticker = ask_for_user_input("Please enter the ticker symbol of the stock you bought. Reply with quit or cancel to cancel adding the stock purchase to your portfolio: ", validate_ticker_input, "Invalid ticker symbol, please try again.") # This calls the ask_for_valid_input function and passes in the prompt for the user to enter the ticker symbol of the stock they bought. The user input is then validated for a valid ticker symbol using the validate_ticker_input function. If the input is not valid, then the user is reprompted to enter a valid ticker symbol. The validated input is then stored in a variable called ticker.
    if ticker is None:
        print("Cancelling adding the stock purchase to your portfolio")
        return 

    date_bought = ask_for_user_input("Please enter the date you bought the stock (YYYY-MM-DD). Reply with quit or cancel to cancel adding the stock purchase to your portfolio: ", validate_date_input, "Invalid date format, please try again.") # This calls the ask_for_valid_input function and passes in the prompt for the user to enter the date they bought the stock. The user input is then validated for a valid date using the validate_date_input function. If the input is not valid, then the user is reprompted to enter a valid date. The validated input is then stored in a variable called date_bought.
    if date_bought is None: # THis checks if the date_bought variable is None, which means the user chose to quit the program. If the user chose to quit, the function will return the original holdings dictionary.
        print("Cancelling adding the stock purchase to your portfolio")
        return 
    
    purchase_price = ask_for_user_input("Please enter the purchase price of the stock. Reply with quit or cancel to cancel adding the stock purchase to your portfolio: ", convert_valid_input_to_float, "Invalid purchase price, please try again.") # This calls the ask_for_valid_input function and passes in the prompt for the user to enter the purchase price of the stock. The user input is then validated for a valid float using the convert_valid_input_to_float function. If the input is not valid, then the user is reprompted to enter a valid purchase price. The validated input is then stored in a variable called purchase_price.
    if purchase_price is None: # This checks if the purchase_price variable is None, which means the user chose to quit the program. If the user chose to quit, the function will return the original holdings dictionary.
        print("Cancelling adding the stock purchase to your portfolio") 
        return 

    quantity = ask_for_user_input("Please enter the quantity of the stock you bought. Reply with quit or cancel to cancel adding the stock purchase to your portfolio: ", convert_valid_input_to_float, "Invalid quantity, please try again.") # This calls the ask_for_valid_input function and passes in the prompt for the user to enter the quantity of the stock they bought. The user input is then validated for a valid float using the convert_valid_input_to_float function. If the input is not valid, then the user is reprompted to enter a valid quantity. The validated input is then stored in a variable called quantity.
    if quantity is None: # This checks if the quantity variable is None, which means the user chose to quit the program. If the user chose to quit, the function will return the original holdings dictionary.
        print("Cancelling adding the stock purchase to your portfolio")
        return 

    print(f"Ticker: {ticker} \nDate Bought: {date_bought} \nPurchase Price: {purchase_price} \nQuantity: {quantity}") # This prints the ticker, date bought, purchase price, and quantity of the stock that the user entered. This is done to confirm that the user entered the correct information.

    if ticker in holdings: # This checks if the ticker symbol is already in the dictionary of holdings. If the ticker symbol is already in the dictionary of holdings, then the function will print a message to inform the user that they already own this stock and will update the existing holding with the new quantity and purchase price. If the date bought of the second holding of the ticker is at a sooner date then the date_bought variable is updated to the most recent date shares of that ticker were purchased.  If the ticker symbol is not in the dictionary of holdings, then the function will create a new holding and add it to the dictionary of holdings.
        if holdings[ticker].date_bought > date_bought:
            print(f"You already own {ticker} and the date you entered is earlier than the date you bought it. Updating the existing holding with the new information.") # This prints a message to inform the user that they already own this stock and the date they entered is earlier than the date they bought it. The function will update the existing holding with the new information.
            holdings[ticker].purchase_price = ((holdings[ticker].purchase_price * holdings[ticker].quantity) + (purchase_price * quantity)) / (holdings[ticker].quantity + quantity) # This updates the purcahse price of the existing holding by calculating the weighted average of the purchase price and quantity of the existing holding and the new purchase price and quantity. This is done to ensure that the purchase price of the existing holding reflects the average cost of all shares owned.
            holdings[ticker].quantity += quantity # This updates the quantity of the existing holding by adding the quantity of the new purchase to the quantity of the existing holding. This is done to ensure that the quantity of the existing holding reflects the total number of shares owned.

        else:
            print(f"You already own {ticker} and the date you entered is later than or equal to the date you bought it. Updating the existing holding with the new information.") # This prints a message to inform the user that they already own this stock and the date they entered is later than the date they bought it. The function will update the existing holding with the new information.
            holdings[ticker].date_bought = date_bought # This updates the date bought of the existing holding with the new date bought that the user entered. This is done to ensure that the date bought of the existing holding reflects the most recent purchase date.
            holdings[ticker].purchase_price = ((holdings[ticker].purchase_price * holdings[ticker].quantity) + (purchase_price * quantity)) / (holdings[ticker].quantity + quantity) # This updates the prucahse price of the existing holding by calculating the weighted average of the purchase price and quantity of the existing holding and the new purchase price and quantity. This is done to ensure that the purchase price of the existing holding reflects the average cost of all shares owned.
            holdings[ticker].quantity += quantity # This updates the quantity of the existing holding by adding the quantity of the new purchase to the quantity of the existing holding. This is done to ensure that the quantity of the existing holding reflects the total number of shares owned.
            
    else: # This checks if the ticker symbol is not in the dictionary of holdings. If the ticker symbol is not inthe dictionary of holdings, thenthe function will create a new holding and add it tothe dictionary of holdings.

        holding = Holding(ticker, date_bought, purchase_price, quantity) # This creates a new instance of the Holding class with the ticker, date bought, purchase price, and quantity that the user entered. The current price is not provided, so it will be initialized to the purchase price.

        holdings[ticker] = holding # This adds the new holding to the dictionary of holdings with the ticker symbol as the key and the holding object as the value.

if __name__ == "__main__": # Only run the following code if this file is specified as the main program. This is done to prevent the code from being run when the file is imported as a module in another program.
    # print(ask_for_user_input("Please enter a ticker symbol: ", validate_ticker_input, "Invalid ticker symbol. Please try again.")) # This calls the ask_for_user_input function and passes in a prompt for the user to enter a ticker symbol. The function will keep asking for input until the user provides a valid input or chooses to quit.

    # print(ask_for_user_input("What is the name of the ticker symbol: ", validate_ticker_input, "Invalid ticker symbol. Please try again.")) # This calls the ask_for_user_input function and passes in a prompt for the user to enter a purchase price. The function will keep asking for input until the user provides a valid input or chooses to quit.

    holdings = {} # This initializes an empty dictionary to store the holdings in the portfolio.
    buy(holdings) # This calls the buy function and passes in the holdings dictionary. The function will ask the user for input to buy a stock and add it to the portfolio. The updated holdings dictionary will be returned and stored in the variable called holdings.
    buy(holdings) # This calls the buy function again and passes in the updated holdings dictionary. The function will ask the user for input to buy another stock and add it to the portfolio. The updated holdings dictionary will be returned and stored in the variable called holdings.
    print(holdings["AAPL"].quantity, holdings["AAPL"].purchase_price, holdings["AAPL"].date_bought) # This prints the updated holdings dictionary in the portfolio.
