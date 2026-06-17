import mainwindow
import os.path
import csv

# creates data folder if it doesn't exist
if not os.path.exists("data"):
    os.makedirs("data")

customer_data_path = "data\customer_data.csv"
customer_data_headers = ["Customer ID", "First Name", "Last Name", "Phone", "Email", "Communication Preference",
                         "Street Address", "City", "State", "Zip Code", "Company Name"]

# creates customer_data.csv file if it doesn't exist
if not os.path.exists(customer_data_path):
    with open(customer_data_path, mode="w", newline="") as customer_data:
        writer = csv.writer(customer_data)
        writer.writerow(customer_data_headers)

main_window = mainwindow.MainWindow()
main_window.mainloop()
