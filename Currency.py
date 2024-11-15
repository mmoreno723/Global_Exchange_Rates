class CurrencyConverter:
    """A class that stores multiple functions to get a single currency, add a currency,
    and get a single item in the index"""
    def __init__(self, currencies_file):
        """ A constructor that opens the text file and stores currency information in a
        dictionary, along with currency names and exchange rates."""
        self.currencies_dict = {}
        self.currency_names = {}
        self._exchange_rates = {}
        with open(currencies_file, 'r') as input_file:
            for index, line in enumerate(input_file, start=1):
                iso_code, currency_name, exchange_rate = line.strip().split(", ")
                self.currencies_dict[index] = (iso_code, currency_name, float(exchange_rate))
                self.currency_names[iso_code] = currency_name
                self._exchange_rates[iso_code] = float(exchange_rate)

    def __repr__(self):
        """A repr method to return the items in the dictionary as a string"""
        return "\n".join([f"{key}: {iso_code}, {currency_name}" for key, (iso_code, currency_name, _) in
                          self.currencies_dict.items()])

    def get_currency(self, iso_code):
        """A method that takes in an ISO code and returns the exchange rate of the corresponding currency"""
        if iso_code in self.currency_names:
            return self.currency_names[iso_code], self._exchange_rates[iso_code]
        return None, None

    def add_currency(self, iso_code, currency_name, exchange_rate):
        """A method that takes three arguments and adds the new currency to the dictionary"""
        index = max(self.currencies_dict.keys()) + 1
        self.currencies_dict[index] = (iso_code, currency_name, float(exchange_rate))

    def _get_exchange_rate(self, iso_code):
        """ A private method that returns the exchange rate"""
        if iso_code in self._exchange_rates and iso_code in self.currency_names:
            return self.currency_names[iso_code], self._exchange_rates[iso_code]
        return None, None

    def __getitem__(self, item):
        """A magic method that gets a specific item in the currencies dictionary"""
        return self.currencies_dict[item]
