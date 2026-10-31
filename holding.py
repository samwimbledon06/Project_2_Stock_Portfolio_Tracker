# Creating a class to represent a holding in a portfolio
class Holding:
    def __init__(self, ticker, date_bought, purchase_price, quantity, current_price = None): # Initialize the holding with ticker, date bought, purchase price, quantity, and current price
        self.ticker = ticker
        self.date_bought = date_bought
        self.purchase_price = purchase_price
        self.current_price = current_price if current_price is not None else purchase_price  # Initialize current price to purchase price if not provided
        self.quantity = quantity

    def gain_loss(self): # Calculate the gain or loss for a given holding
        return (self.current_price - self.purchase_price) * self.quantity # difference between current price and the purchase price per share multiplied by the number of shares held

    def market_value(self): # Calculate the market value of a given holding
        return self.current_price * self.quantity # current price per share multiplied by the number of shares held

    def cost_basis(self): # Calculate the cost basis of a given holding
        return self.purchase_price * self.quantity # purchase price per share multiplied by the number of shares held

if __name__ == "__main__":
    holding = Holding("AAPL", "2024-01-01", 100.00, 10, 110.00) # Create a sample holding for testing
    print(f"Gain/Loss: {holding.gain_loss()}") # Print the gain or loss for the holding
    print(f"Market Value: {holding.market_value()}") # Print the market value of the holding
    print(f"Cost Basis: {holding.cost_basis()}") # Print the cost basis of the holding

    holding2 = Holding("GOOGL", "2024-01-01", 100.0, 5)   
    print(f"The current price of {holding2.ticker} is {holding2.current_price}.")

    holding3 = Holding("NVDA", "2024-01-06", 100, 5, 0.00) 
    print(f"The current price of {holding3.ticker} is {holding3.current_price}.") # Current price should show as 0.00