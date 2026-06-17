import tkinter as tk
import tkinter.messagebox
import mainwindow
import pandas as pd
import searchresults

class SearchCustomer(tk.Tk):
    """creates window to search for customers in database"""
    def __init__(self):
        super().__init__()
        self.customer_data_path = "data\customer_data.csv"

        ##################################### WINDOW SET-UP #########################################################
        self.window_size = "940x889"
        self.geometry(self.window_size)
        self.title("Search Customer")

        ###################################### WINDOW HEADER ########################################################
        self.header_font = ("Arial", 50)
        self.header_label = tk.Label(self, text="Search Customer", pady=50, font=self.header_font)
        self.header_label.grid(row=0, columnspan=7)


        ######################### LABELS, ENTRY FORMS, ERROR MESSAGES, AND BUTTONS #############################
        self.label_font = ("Arial", 12)
        self.entry_font = ("Arial", 11)
        self.button_font = ("Arial", 14)
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

        self.name_button = tk.Button(self, text="Search Name", font=self.button_font, command=self.search_name, padx=10)
        self.name_button.grid(row=1, column=4, sticky="NW", padx=(200, 0))

        self.phone_label = tk.Label(self, text="Phone: ", font=self.label_font)
        self.phone_label.grid(row=3, column=1, sticky="E")
        self.phone_entry = tk.Entry(self, bd=self.entry_border_size, font=self.entry_font)
        self.phone_entry.grid(row=3, column=2, sticky="W", padx=self.entry_padx)
        self.phone_error = tk.Label(self, text="Enter #'s no symbols, 8054826248", fg="red")
        self.phone_button = tk.Button(self, text="Search Phone", font=self.button_font,
                                      command=self.search_phone, padx=10)
        self.phone_button.grid(row=5, column=2, sticky="NW")

        self.email_label = tk.Label(self, text="E-mail: ", font=self.label_font)
        self.email_label.grid(row=3, column=3, sticky="E")
        self.email_entry = tk.Entry(self, bd=self.entry_border_size, font=self.entry_font, width=25)
        self.email_entry.grid(row=3, column=4, sticky="W", padx=self.entry_padx)
        self.email_error = tk.Label(self, text="Enter Email Address", fg="red")
        self.email_button = tk.Button(self, text="Search Email", font=self.button_font,
                                      command=self.search_email, padx=10)
        self.email_button.grid(row=5, column=4, sticky="NW")

        self.home_btn = tk.Button(self, text="Home", padx=40, font=self.button_font, command=self.home)
        self.home_btn.grid(row=6, columnspan=7, pady=(70, 0))

        ###################################### SEARCH RESULTS FRAME###################################################
        self.search_results = searchresults.SearchResults(self)
        self.search_results.grid(row=7, column=0, columnspan=7, pady=(25,0))

        #######################################EMPTY GRID CELL SPACE###################################################
        # configures .grid() column 0 to take up as much room on the left side as column 6 on the
        # right side weight=1 on both columns
        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=6, weight=1)
        self.error_row_size = 35
        self.rowconfigure(index=2, minsize=self.error_row_size)
        self.rowconfigure(index=4, minsize=self.error_row_size)

    def search_name(self):
        """handles searches by customer first and last name"""
        self.first_name_error.grid_forget() # removes error messages if any are displayed
        self.last_name_error.grid_forget()

        first_name = self.first_name_entry.get().title()
        last_name = self.last_name_entry.get().title()

        # displays error messages if any entry data is not valid in first and last name
        if first_name == "" or first_name.isspace(): # checks if first_name is blank or just a space
            self.first_name_error.grid(row=2, column=2, pady=self.error_pady, sticky="W")
        elif last_name == "" or last_name.isspace():
            self.last_name_error.grid(row=2, column=4, pady=self.error_pady, sticky="W")
        else:
            customers_df = pd.read_csv(self.customer_data_path)
            # searches the customers_df for locations for matches with the first_name and last_name
            # must use the & symbol not "and" keyword also use parenthesis around each conditional statement
            search_results_df = customers_df.loc[(customers_df["First Name"] == first_name) &
                                                 (customers_df["Last Name"] == last_name)]

            if search_results_df.empty: # displays message pop-up window if no customers are found
                tk.messagebox.showerror("No Results", "No customers found in database.")
            else:
                # displays search results in search_results frame
                self.search_results.destroy()
                self.search_results = searchresults.SearchResults(self)
                self.search_results.search_results(search_results_df)
                self.search_results.grid(row=7, column=0, columnspan=7, pady=(25,0))

    def search_phone(self):
        """Handles searches by customer phone number"""
        self.phone_error.grid_forget()

        phone = self.phone_entry.get()
        if not phone.isdigit(): # .isdigit() checks if string is only numbers
            self.phone_error.grid(row=4, column=2, pady=self.error_pady, sticky="W")
        else:
            customers_df = pd.read_csv(self.customer_data_path)
            # customers_df["Phone"].astype(str) will compare the value as a string to the variable phone which is
            # also a string type variable. This allows the first digit of a phone number to be 0 otherwise it
            # would be removed, because it's treated as an integer data type by default.
            search_results_df = customers_df.loc[customers_df["Phone"].astype(str) == phone]

            if search_results_df.empty: # displays message pop-up window if no customers are found
                tk.messagebox.showerror("No Results", "No customers found in database.")
            else:
                # displays search results in search_results frame
                self.search_results.destroy()
                self.search_results = searchresults.SearchResults(self)
                self.search_results.search_results(search_results_df)
                self.search_results.grid(row=7, column=0, columnspan=7, pady=(25,0))

    def search_email(self):
        """Handles searches with customer email."""
        self.email_error.grid_forget()

        email = self.email_entry.get()
        if email == "" or email.isspace():
            self.email_error.grid(row=4, column=4, pady=self.error_pady, sticky="W")
        else:
            customers_df = pd.read_csv(self.customer_data_path)
            # searches customers dataframe for any email matches and adds it to search results dataframe
            search_results_df = customers_df.loc[customers_df["Email"] == email]

            if search_results_df.empty: # displays message pop-up window if no customers are found
                tk.messagebox.showerror("No Results", "No customers found in database.")
            else:
                # displays search results in search_results frame
                self.search_results.destroy()
                self.search_results = searchresults.SearchResults(self)
                self.search_results.search_results(search_results_df)
                self.search_results.grid(row=7, column=0, columnspan=7, pady=(25,0))

    def home(self):
        """returns user to the main window"""
        self.destroy()
        main_window = mainwindow.MainWindow()
        main_window.mainloop()

if __name__ == "__main__":
    search_customer = SearchCustomer()
    search_customer.mainloop()
