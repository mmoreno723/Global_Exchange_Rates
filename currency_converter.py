"""
Michael Moreno
Class: CS 521 - Spring 1
Date: 03/01/2024
Final Project
Description of Problem: A program that can convert your United States Dollar currency to one of
twenty different currencies. The program will ask the user to enter the amount of money they want
to convert, which currency they want to convert into, and will then perform the calculation. The
program can also list out all the supported currencies, get details about a specific currency, get
a specific exchange rate, and allow the user to add a new currency.
"""
from Currency import CurrencyConverter
CURRENCY_FILE = 'currencies.txt'
# Defines the class that will be used as a variable in the global scope
converter = CurrencyConverter(CURRENCY_FILE)
currencies_dict = {}
# Reads the text file and stores the data into a dictionary with the keys as ISO codes
with open(CURRENCY_FILE, 'r') as file:
    lines = list(file.readlines())
    for line in lines:
        iso_code, currency_name, exchange_rate = line.strip().split(", ")
        currencies_dict[iso_code] = currency_name, float(exchange_rate)


# A function that will get all the currencies from the text file
def all_currencies():
    print("=" * 20)
    print("Here is a list of the supported currencies:")
    all_items = CurrencyConverter("currencies.txt")
    print(all_items)


# A function that performs the calculation of the conversion
def convert_currency(input_amount, currency_code):
    usd_amount = input_amount / currencies_dict["USD"][1]
    output_amount = usd_amount * currencies_dict[currency_code][1]
    formatted_output = "{:,.2f}".format(output_amount)
    return formatted_output


# A function that asks how much the user wants to convert and which currency they want to convert to
def prompt_conversion():
    while True:
        try:
            input_amount = float(input("How much USD you like to convert?: "))
            if input_amount <= 0:
                print("Please enter a positive value.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    while True:
        try:
            output_currency = input("Enter the currency you would like to convert to using "
                                    "the three letter ISO currency code (ex: EUR): ").upper()
            currency_calculation = convert_currency(input_amount, output_currency)
            break
        except KeyError:
            print("Invalid ISO code. Please enter a valid three-letter ISO currency code.")
    # Prints the currency calculation along with the user input
    print(f"{input_amount:.2f} USD is equivalent to {currency_calculation} {output_currency}.")


# A function that gets a specific item based on which index the user inputted
def get_item():
    while True:
        try:
            input_index = input("Enter the index to see which currency is at that index: ")
            index = int(input_index)
            if index in converter.currencies_dict:
                item = converter[index]
                # Prints the currency found at the specific index
                print(f"The currency at index {index} is {item}.")
                break
            else:
                print("Index not found. Please enter a valid index.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# A function that gets a single rate based on which three-letter ISO code the user inputted
def get_single_rate():
    while True:
        iso_input = input("Enter a specific three letter ISO code to see the exchange rate: ").upper()
        single_currency_name, single_rate = converter.get_currency(iso_input)
        if single_rate is None:
            print("Currency not supported. Please enter a valid ISO code.")
        else:
            # Prints the specific exchange rate for a given currency
            print(f"The exchange rate for the {single_currency_name} is 1 USD to {single_rate}.")
            break


# A function that asks the user if they want to return back to the main menu
def ask_again():
    while True:
        answer = input("Would you like to go back to the main menu Y/N?: ")
        if answer.upper() == "Y":
            return True
        elif answer.upper() == "N":
            return False
        else:
            print("Invalid input. Please enter Y or N.")


# A function that allows the user to add a new currency of their choice
def add_new_currency():
    # Declares converter as a global variable
    global converter
    new_code = input("Enter the three-letter ISO code for the new currency: ").upper()
    new_name = input("Enter the name of the new currency: ")
    while True:
        try:
            new_rate = float(input("Enter the exchange rate for 1 USD to the new currency: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid exchange rate.")
    # Adds the user's new currency to the text file
    with open(CURRENCY_FILE, 'a') as file:
        file.write(f"\n{new_code}, {new_name}, {new_rate}")

    converter.add_currency(new_code, new_name, new_rate)
    # Update currencies_dict with the new currency
    currencies_dict[new_code] = (new_name, new_rate)
    # Reload the CurrencyConverter instance with the updated currencies
    converter = CurrencyConverter(CURRENCY_FILE)
    new_currency_name, new_exchange_rate = converter.get_currency(new_code)
    if new_currency_name is not None:
        # Prints a success message if the new currency was added
        print(
            f"The currency '{new_currency_name}' with ISO code '{new_code}' and exchange "
            f"rate '{new_exchange_rate}' was added successfully!")
    else:
        print("Failed to add the new currency. Please try again.")


if __name__ == "__main__":
    welcome_message = "Welcome to the United States Dollar Global Exchange Rates Program."
    print(welcome_message)
    while True:
        print("=" * 20)
        print("What would you like to do?")
        print("1.) View all the currencies supported along with their ISO code.\n"
              "2.) Convert USD to another currency.\n"
              "3.) Get details about a currency from the list.\n"
              "4.) Get the specific rate for a currency.\n"
              "5.) Add a new currency.\n"
              "6.) Exit the program.")
        # A series of input options to see what the user wants to do and then initializes the specific function
        try:
            user_input = int(input("Enter your choice: "))
            if user_input < 1 or user_input > 6:
                raise ValueError("Please enter a number from the choices above.")
            if user_input == 1:
                all_currencies()
            elif user_input == 2:
                prompt_conversion()
            elif user_input == 3:
                get_item()
            elif user_input == 4:
                get_single_rate()
            elif user_input == 5:
                add_new_currency()
            elif user_input == 6:
                print("Thank you for using the Global Exchange Rates program!")
                break
            if not ask_again():
                print("Thank you for using the Global Exchange Rates program!")
                break
        except ValueError as e:
            print(e)
