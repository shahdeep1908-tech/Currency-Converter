# Currency Converter Project

This is a simple currency converter project written in Python. It uses exchange rates from a predefined dictionary for demonstration purposes. For a real-world implementation, you can use an API to fetch the latest exchange rates.

## How to Run

1. Clone the repository to your local machine:


    git clone https://github.com/your-username/currency_converter_project.git


2. Navigate to the project directory:

    cd currency_converter_project


3. Create a virtual environment (optional but recommended):

    python -m venv venv



4. Activate the virtual environment:

   - On Windows:
     - venv\Scripts\activate
   
   - On macOS and Linux:
     - source venv/bin/activate



5. Install the required dependencies:


    pip install -r requirements.txt
    


6. Run the currency converter script:


    python main.py



The script will prompt you to enter the source currency code, target currency code, and the amount to convert. It will then display the converted amount.

## Additional Functionalities

The `currency_converter.py` file contains a `CurrencyConverter` class with some additional functionalities. You can explore and extend this class to add more features to your currency converter.

Feel free to modify and expand the project as per your requirements!

## Note

The exchange rates used in this example are predefined for simplicity. For a more accurate currency conversion, you should replace them with real-time rates fetched from an API.

