import csv
import tkinter as tk
from tkinter import messagebox
import mainwindow
import string
import random
import pandas as pd

class NewCustomer(tk.Tk):
    """creates new customer window in order to add new customers to database"""
    def __init__(self):
        super().__init__()
        self.customer_data_path = "data\customer_data.csv"

        ##################################### WINDOW SET-UP #########################################################
        self.window_size = "970x575"
        self.geometry(self.window_size)
        self.title("New Customer")

        ###################################### WINDOW HEADER ########################################################
        self.header_font = ("Arial", 50)
        self.header_label = tk.Label(self, text="Customer Details", pady=50, font=self.header_font)
        self.header_label.grid(row=0, column=1, columnspan=6)

        ######################### LABELS, ENTRY FORMS, ERROR MESSAGES, AND CHECKBOX GUI #############################
        self.label_font = ("Arial", 12)
        self.entry_font = ("Arial", 11)
        self.entry_border_size = 2
        self.entry_padx = (0, 15)  # padding size to add 15px on right side of entry fields
        self.error_pady = (0, 14)  # adds 14px padding to the bottom of error messages

        self.first_name_label = tk.Label(self, text="First Name: ", font=self.label_font)
        self.first_name_label.grid(row=1, column=1, sticky="E")
        self.first_name_entry = tk.Entry(self, bd=self.entry_border_size, font=self.entry_font)
        self.first_name_entry.grid(row=1, column=2, sticky="W", padx=self.entry_padx)
        # error labels will display only when the user doesn't enter valid data in entry fields
        self.first_name_error = tk.Label(self, text="Enter First Name", fg="red")

        self.last_name_label = tk.Label(self, text="Last Name: ", font=self.label_font)
        self.last_name_label.grid(row=1, column=3, sticky="E")
        self.last_name_entry = tk.Entry(self, bd=self.entry_border_size, font=self.entry_font)
        self.last_name_entry.grid(row=1, column=4, sticky="W", padx=self.entry_padx)
        self.last_name_error = tk.Label(self, text="Enter Last Name", fg="red")

        self.phone_label = tk.Label(self, text="Phone: ", font=self.label_font)
        self.phone_label.grid(row=3, column=1, sticky="E")
        self.phone_entry = tk.Entry(self, bd=self.entry_border_size, font=self.entry_font)
        self.phone_entry.grid(row=3, column=2, sticky="W", padx=self.entry_padx)
        self.phone_error = tk.Label(self, text="Enter #'s no symbols, 8054826248", fg="red")

        self.email_label = tk.Label(self, text="E-mail: ", font=self.label_font)
        self.email_label.grid(row=3, column=3, sticky="E")
        self.email_entry = tk.Entry(self, bd=self.entry_border_size, font=self.entry_font, width=25)
        self.email_entry.grid(row=3, column=4, sticky="W", padx=self.entry_padx)
        self.email_error = tk.Label(self, text="Enter Email Address", fg="red")

        self.communication_preference_label = tk.Label(self, text="Communication: ", font=self.label_font)
        self.communication_preference_label.grid(row=3, column=5, columnspan=2, sticky="NW")
        self.communication_preference = tk.StringVar() # a string variable will be used for the checkboxes
        self.phone_checkbox = tk.Checkbutton(self, text="Phone", variable=self.communication_preference,
                                             onvalue="Phone", offvalue="")
        self.phone_checkbox.grid(row=3, column=5, columnspan=2, sticky="NW", padx=(120,0))
        self.email_checkbox = tk.Checkbutton(self, text="Email", variable=self.communication_preference,
                                             onvalue="Email", offvalue="")
        self.email_checkbox.grid(row=4, column=5, sticky="NW", columnspan=2, padx=(120,0))
        self.communication_preference_error = tk.Label(self, text="Select Preference", fg="red")

        self.address_label = tk.Label(self, text="Street Address: ", font=self.label_font)
        self.address_label.grid(row=5, column=1, sticky="E")
        self.address_entry = tk.Entry(self, bd=self.entry_border_size, font=self.entry_font, width=25)
        self.address_entry.grid(row=5, column=2, sticky="W", padx=self.entry_padx)
        self.address_error = tk.Label(self, text="Enter Street Address", fg="red")

        self.city_label = tk.Label(self, text="City: ", font=self.label_font)
        self.city_label.grid(row=5, column=3, sticky="E")
        self.city_entry = tk.Entry(self, bd=self.entry_border_size, font=self.entry_font)
        self.city_entry.grid(row=5, column=4, sticky="W", padx=self.entry_padx)
        self.city_error = tk.Label(self, text="Enter City", fg="red")

        self.state_label = tk.Label(self, text="State: ", font=self.label_font)
        self.state_label.grid(row=5, column=5, columnspan=2, sticky="W")
        self.state_entry = tk.Entry(self, bd=self.entry_border_size, font=self.entry_font)
        self.state_entry.grid(row=5, column=5, columnspan=2, sticky="W", padx=(50, 0))
        self.state_error = tk.Label(self, text="Enter Full State Name", fg="red")

        self.zip_code_label = tk.Label(self, text="Zip Code: ", font=self.label_font)
        self.zip_code_label.grid(row=7, column=1, sticky="E")
        self.zip_code_entry = tk.Entry(self, bd=self.entry_border_size, font=self.entry_font)
        self.zip_code_entry.grid(row=7, column=2, sticky="W", padx=self.entry_padx)
        self.zip_code_error = tk.Label(self, text="Enter Zip Code", fg="red")

        self.company_label = tk.Label(self, text="Company: ", font=self.label_font)
        self.company_label.grid(row=7, column=3, sticky="E")
        self.company_entry = tk.Entry(self, bd=self.entry_border_size, font=self.entry_font)
        self.company_entry.grid(row=7, column=4, sticky="W", padx=self.entry_padx)
        self.company_optional = tk.Label(self, text="(Optional)")
        self.company_optional.grid(row=8, column=4, sticky="W")

        # error label will display only when customer already exists in database
        self.customer_exists_error = tk.Label(self, text="Customer Already Exists", fg="red")

        ####################################### GUI BUTTONS ###########################################################
        self.button_font = ("Arial", 14)
        self.home_btn = tk.Button(self, text="Home", width=8, font=self.button_font, command=self.home)
        self.home_btn.grid(row=10, column=1, columnspan=2, padx=(0, 170))
        self.save_btn = tk.Button(self, text="Save", width=8, font=self.button_font, command=self.save_data)
        self.save_btn.grid(row=10, column=3, columnspan=2, padx=(0,110))

        ###################################### GRID CELL SPACE CONFIGURATION #########################################
        # configures .grid() column 0 to take up as much room on the left side as column 7 on the
        # right side weight=1 on both columns
        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=7, weight=1)
        self.error_row_size = 35 # size of row where error messages are displayed
        self.rowconfigure(index=2, minsize=self.error_row_size) # error label rows
        self.rowconfigure(index=4, minsize=self.error_row_size)
        self.rowconfigure(index=6, minsize=self.error_row_size)
        self.rowconfigure(index=8, minsize=self.error_row_size)
        self.rowconfigure(index=9, minsize=70)

    def save_data(self):
        """handles saving data to customer database"""
        ################################## GETS DATA FROM ENTRIES AND STORES IN VARIABLES ############################
        customer_id = self.create_id() # creates unique Customer ID
        first_name = self.first_name_entry.get().title() # .title() converts entry string into titlecase
        last_name = self.last_name_entry.get().title()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        communication = self.communication_preference.get()
        address = self.address_entry.get().title()
        city = self.city_entry.get().title()
        state = self.state_entry.get().title()
        zip_code = self.zip_code_entry.get().title()
        company_name = self.company_entry.get()

        # runs data validation
        valid_data = self.check_data(first_name, last_name, phone, email, communication, address, city,
                            state, zip_code)
        if valid_data: # if valid data is entered it will be saved to customer_data.csv
            with open(self.customer_data_path, "a", newline='') as customer_data:
                writer = csv.writer(customer_data)

                # write new line of data
                new_customer = [customer_id, first_name, last_name, phone, email, communication, address, city,
                                state, zip_code, company_name]
                # new_customer = ["0000", "jerry", "meza", "0000000000", "gmjerryg@gmail.com", "email", "325 Casey Rd.",
                #             "Moorpark", "California", "93021", "Tech Insider Deals"]

                writer.writerow(new_customer)

            messagebox.showinfo("Success", "New customer successfully added.")

    def create_id(self):
        """creates a customer ID which consists of 9 upper case letters and numbers"""
        duplicate_id = True
        while duplicate_id:
            # creates string which consists of all upper case letters and numbers
            letters_and_numbers = string.ascii_uppercase + string.digits
            id_length = 9
            # .choices() creates a list of 9 random characters from the letters_and_numbers string
            id_list = random.choices(letters_and_numbers, k=id_length)
            customer_id = "".join(id_list)

            # checks if customer_id is a duplicate ID
            customer_data_df = pd.read_csv(self.customer_data_path)
            existing_ids_list = customer_data_df["Customer ID"].tolist()

            if customer_id not in existing_ids_list:
                duplicate_id = False

        return customer_id

    def check_data(self, first_name, last_name, phone, email, communication, address, city, state, zip_code):
        """Runs data validaiton and dislays error messages in for entry fields which need correcting. Returns
        True if all data is valid."""
        # removes all error labels displayed if any are displayed
        self.first_name_error.grid_forget()
        self.last_name_error.grid_forget()
        self.phone_error.grid_forget()
        self.email_error.grid_forget()
        self.communication_preference_error.grid_forget()
        self.address_error.grid_forget()
        self.city_error.grid_forget()
        self.state_error.grid_forget()
        self.zip_code_error.grid_forget()
        self.customer_exists_error.grid_forget()

        valid_data = True
        # if any condition is met it will display the appropriate error label
        if first_name == "" or first_name.isspace(): # checks if first_name is blank or just a space
            self.first_name_error.grid(row=2, column=2, pady=self.error_pady, sticky="W")
            valid_data=False
        if last_name == "" or last_name.isspace():
            self.last_name_error.grid(row=2, column=4, pady=self.error_pady, sticky="W")
            valid_data=False
        if not phone.isdigit(): # .isdigit() checks if string is only numbers
            self.phone_error.grid(row=4, column=2, pady=self.error_pady, sticky="W")
            valid_data = False
        if email == "" or email.isspace():
            self.email_error.grid(row=4, column=4, pady=self.error_pady, sticky="W")
            valid_data = False
        if communication == "": # makes sure a checkbox has been marked for communication preference
            self.communication_preference_error.grid(row=4, column=5, columnspan=2, sticky="NW")
            valid_data = False
        if address == "" or address.isspace():
            self.address_error.grid(row=6, column=2, pady=self.error_pady, sticky="W")
            valid_data = False
        if city == "" or city.isspace():
            self.city_error.grid(row=6, column=4, pady=self.error_pady, sticky="W")
            valid_data = False
        if state == "" or state.isspace() or len(state) <=2: # checks for full state name
            self.state_error.grid(row=6, column=5, pady=self.error_pady, sticky="W", padx=(50, 0))
            valid_data = False
        if not zip_code.isdigit():
            self.zip_code_error.grid(row=8, column=2, pady=self.error_pady, sticky="W")
            valid_data = False

        # checks if customer already exists in customer_data.csv
        customer_data_df = pd.read_csv(self.customer_data_path)
        if valid_data:
            for index, row in customer_data_df.iterrows():
                # if a user with the same first name, last name, phone number, and email is found in database
                # the customer won't be added to database and display error message
                if row["First Name"] == first_name and row["Last Name"] == last_name and str(row["Phone"]) == phone \
                        and row["Email"] == email:
                    valid_data = False
                    self.customer_exists_error.grid(row=9, columnspan=7, sticky="SW", padx=(471, 0))
                    break

        return valid_data

    def home(self):
        """returns user to the main window"""
        self.destroy()
        main_window = mainwindow.MainWindow()
        main_window.mainloop()

if __name__ == "__main__":
    new_customer = NewCustomer()
    new_customer.mainloop()

