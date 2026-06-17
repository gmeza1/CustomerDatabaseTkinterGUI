import tkinter as tk
from tkinter import messagebox
import mainwindow
import pandas as pd

class ViewEditCustomer(tk.Tk):
    """Allows you to view and edit the information of an existing customer"""
    def __init__(self):
        super().__init__()
        self.customer_data_path = "data\customer_data.csv"

        ##################################### WINDOW SET-UP #########################################################
        self.window_size = "970x575"
        self.geometry(self.window_size)
        self.title("View/Edit Customer")

        ###################################### WINDOW HEADER ########################################################
        self.header_font = ("Arial", 50)
        self.header_label = tk.Label(self, text="View/Edit Customer", pady=50, font=self.header_font)
        self.header_label.grid(row=0, columnspan=8)

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
        self.first_name_error = tk.Label(self, text="Enter First Name", fg="red")

        self.last_name_label = tk.Label(self, text="Last Name: ", font=self.label_font)
        self.last_name_label.grid(row=1, column=3, sticky="E")
        self.last_name_entry = tk.Entry(self, bd=self.entry_border_size, font=self.entry_font)
        self.last_name_entry.grid(row=1, column=4, sticky="W", padx=self.entry_padx)
        self.last_name_error = tk.Label(self, text="Enter Last Name", fg="red")

        self.customer_id = tk.Label(self, text="ID: ", font=self.label_font)
        self.customer_id.grid(row=1, column=5, sticky="E")
        self.customer_id_entry = tk.Entry(self, bd=self.entry_border_size, font=self.entry_font)
        self.customer_id_entry.grid(row=1, column=6, sticky="W")

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
        self.communication_preference = tk.StringVar()
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

        ####################################### GUI BUTTONS ###########################################################
        self.button_font = ("Arial", 14)
        self.home_btn = tk.Button(self, text="Home", width=7, font=self.button_font, command=self.home)
        self.home_btn.grid(row=10, column=1)
        self.save_edit_btn = tk.Button(self, text="Save", width=7, font=self.button_font, command=self.save_edit)
        self.save_edit_btn.grid(row=10, column=3, columnspan=2, padx=(0, 120))
        self.delete_btn = tk.Button(self, text="Delete", width=8, font=self.button_font, command=self.delete_customer)
        self.delete_btn.grid(row=10, column=6)

        #######################################EMPTY GRID CELL SPACE###################################################
        # configures .grid() column 0 to take up as much room on the left side as column 7 on the
        # right side weight=1 on both columns
        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=7, weight=1)
        self.error_row_size = 35
        self.rowconfigure(index=2, minsize=self.error_row_size)
        self.rowconfigure(index=4, minsize=self.error_row_size)
        self.rowconfigure(index=6, minsize=self.error_row_size)
        self.rowconfigure(index=8, minsize=self.error_row_size)
        self.rowconfigure(index=9, minsize=70)

    def prefill_entries(self, customer_id: str):
        """Prefills all entries with the selected customers information"""
        df = pd.read_csv(self.customer_data_path)
        customer_df = df.loc[df["Customer ID"] == customer_id]

        first_name = customer_df.iloc[0]["First Name"] # obtains only the value at index 0 under column "First Name"
        self.first_name_entry.insert(0, first_name) # prefills entry field with customer name at index 0 in the Entry
        last_name = customer_df.iloc[0]["Last Name"]
        self.last_name_entry.insert(0, last_name)
        self.customer_id_entry.insert(0, customer_id)
        self.customer_id_entry.configure(state="readonly") # makes entry read only can't be edited
        phone = customer_df.iloc[0]["Phone"]
        self.phone_entry.insert(0, phone)
        email = customer_df.iloc[0]["Email"]
        self.email_entry.insert(0, email)
        communication_preference = customer_df.iloc[0]["Communication Preference"]
        self.communication_preference.set(communication_preference) # sets which checkbox is marked
        address = customer_df.iloc[0]["Street Address"]
        self.address_entry.insert(0, address)
        city = customer_df.iloc[0]["City"]
        self.city_entry.insert(0, city)
        state = customer_df.iloc[0]["State"]
        self.state_entry.insert(0, state)
        zip_code = customer_df.iloc[0]["Zip Code"]
        self.zip_code_entry.insert(0, zip_code)
        company = customer_df.iloc[0]["Company Name"]
        self.company_entry.insert(0, company)

    def save_edit(self):
        """saves customer edits to customer database"""
        answer = messagebox.askquestion("Edit Customer", "Are you sure you want to edit customer details?")
        if answer == "yes":
            customer_id = self.customer_id_entry.get()
            first_name = self.first_name_entry.get().title() # .title() converts entry string into titlecase
            last_name = self.last_name_entry.get().title()
            phone = self.phone_entry.get() # converts phone number into a string
            email = self.email_entry.get()
            communication = self.communication_preference.get()
            address = self.address_entry.get().title()
            city = self.city_entry.get().title()
            state = self.state_entry.get().title()
            zip_code = self.zip_code_entry.get().title()
            company_name = self.company_entry.get()

            valid_data = self.check_data(first_name, last_name, phone, email, communication, address, city,
                                state, zip_code)
            if valid_data: # if valid data is entered it will be saved to customer_data.csv
                customers_df = pd.read_csv(self.customer_data_path)
                # obtains index row location of customers data to be edited
                customer_index = customers_df.index[customers_df["Customer ID"] == customer_id]

                # creates pandas series to overwrite the customers data with updated data
                customer_update = pd.Series({"Customer ID": customer_id,
                                             "First Name": first_name,
                                             "Last Name": last_name,
                                             "Phone": phone,
                                             "Email": email,
                                             "Communication Preference": communication,
                                             "Street Address": address,
                                             "City": city,
                                             "State": state,
                                             "Zip Code": zip_code,
                                             "Company Name": company_name
                                             })

                # overwrites the customers index row with the updated data
                # use .iloc to identify row by index
                customers_df.iloc[customer_index] = customer_update
                # index=False excludes the index column from the output file
                # mode='w' overwrites existing file
                customers_df.to_csv(self.customer_data_path, index=False, mode='w')

                messagebox.showinfo("Success", "Customer details have been updated.")

    def check_data(self, first_name, last_name, phone, email, communication, address, city, state, zip_code):
        """Validates all data entered into entry fields"""
        # removes any error methods previously displayed
        self.first_name_error.grid_forget()
        self.last_name_error.grid_forget()
        self.phone_error.grid_forget()
        self.email_error.grid_forget()
        self.communication_preference_error.grid_forget()
        self.address_error.grid_forget()
        self.city_error.grid_forget()
        self.state_error.grid_forget()
        self.zip_code_error.grid_forget()

        valid_data = True
        # if any condition is met it will display the data error
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
        if communication == "":
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

        return valid_data

    def delete_customer(self):
        """handles deleting of customers from database"""
        answer = messagebox.askquestion("DELETE CUSTOMER", "Are you sure you want to delete customer?")
        if answer == "yes":
            customer_id = self.customer_id_entry.get() # obtains customer ID
            customers_df = pd.read_csv(self.customer_data_path)
            # obtains index location for customer in database
            customer_index = customers_df.index[customers_df["Customer ID"] == customer_id]

            customers_df = customers_df.drop(customer_index) # deletes entire row at the customer index location
            # index=False will not save index column to csv file
            customers_df.to_csv(self.customer_data_path, index=False, mode="w")

            messagebox.showinfo("Customer Deleted", "Customer was successfully deleted.")

            self.destroy()
            main_window = mainwindow.MainWindow()
            main_window.mainloop()

    def home(self):
        """returns user to the main window"""
        self.destroy()
        main_window = mainwindow.MainWindow()
        main_window.mainloop()

if __name__ == "__main__":
    view_edit_customer = ViewEditCustomer()
    view_edit_customer.mainloop()

