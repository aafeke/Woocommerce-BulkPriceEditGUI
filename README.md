# Bulk Price Editor for Woocommerce

Built with tkinter, simple GUI program for bulk editing prices of your Woocommerce products. Still under development.

## Usage

Clone the repository and run the main.py file.

```bash
git clone https://github.com/apri44/Woocommerce-BulkPriceEditGUI
```

1- You'll need to export list of your products by using built-in Woocommerce "Export CSV" feature in Wordpress. Make sure the file has the "Price" header as well as product IDs.

2- Import the file you just exported from Woocommerce.

3- Enter a value into "Add a constant value" textbox (Note: You can enter negative values to lower current prices and also specify percentage of the current prices by adding '%' (e.g. '-25%') to the end of the number).

4- Press the "Export" button, you'll be notified with an alert dialog if export was success. You can find the exported "output.csv" file under the working directory in .temp/output.csv

5- Import the output into Woocommerce back, make sure the "update the products that already exist" checkbox is marked.

## Dependencies

-tkinter
```
pip install tk 
```

## Contributing
Pull requests are welcome.
