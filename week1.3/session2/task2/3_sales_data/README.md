# Sales Data Statistics


1. We want to analyse a set of sales data in `sales.csv`.

2. Edit `sales_data.py` and add lines to:

    - Open the file and read the data
    
    - find the:
        - largest sale day (highest sale amount)
        - average sale amount
        - the widget which has been sold the most
    - and print these out in a nice, human-readable format

3. Additional work: You can calculate other sales statistics such as:

    - total sales for each region
    - most sold widget for each region
    - total sales for each widget


Hints:
- Remember to handle file errors
- The first row contains headers: Date, Product, Sales_Amount, Units_Sold, Region
- Sales amounts are stored as strings - you'll need to convert to integer using `int()` for arithmetic operation
- For finding the highest selling widget, use a dictionary to count units sold per product
- For average, sum all sales amounts and divide by number of rows