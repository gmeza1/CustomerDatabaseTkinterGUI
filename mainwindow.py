import tkinter as tk
import newcustomer
import searchcustomer
import readme

class MainWindow(tk.Tk):
    """Creates the main window/menu when the program starts"""
    def __init__(self):
        super().__init__()  # allows you to use tk.Tk class as part of MainWindow class

        ######################################## WINDOW SET-UP ##################################################
        # button font in main window must be provided in this order
        # (family=, size=, weight=, slant=, underline=, overstrike=)
        self.button_font = ("Arial Rounded MT Bold", 14)
        self.window_size = "400x400"
        self.geometry(self.window_size) # sets window size
        self.title("Customer Data Manager")

        ############################################### BUTTONS #####################################################
        self.search_customer_btn = tk.Button(self, text="Search & Edit\nCustomer", command=self.search_customer)
        self.search_customer_btn.grid(row=1, column=1, pady=10)
        self.search_customer_btn.config(font=self.button_font, height=2, width=15)

        self.new_customer_btn = tk.Button(self, text="New Customer", command=self.new_customer)
        self.new_customer_btn.grid(row=2, column=1, pady=10)
        self.new_customer_btn.config(font=self.button_font, height=2, width=15)

        self.edit_customer_btn = tk.Button(self, text="Read Me", command=self.edit_customer)
        self.edit_customer_btn.grid(row=3, column=1, pady=10)
        self.edit_customer_btn.config(font=self.button_font, height=2, width=15)

        ############################################## GRID SET-UP #################################################
        # configures .grid() column 0 to take up as much room on the left side as column 2 on the
        # right side weight=1 on both
        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=2, weight=1)
        self.rowconfigure(index=0, weight=1)
        self.rowconfigure(index=4, weight=1)

    def search_customer(self):
        self.destroy()  # closes main window and releases resources associated with it
        search_customer = searchcustomer.SearchCustomer()
        search_customer.mainloop()

    def new_customer(self):
        self.destroy()
        new_customer = newcustomer.NewCustomer()
        new_customer.mainloop()

    def edit_customer(self):
        self.destroy()
        read_me = readme.ReadMe()
        read_me.mainloop()

# creates main window object when mainwindow.py is run, but won't when it's imported to other .py files
# this allows for faster testing of the MainWindow() class
if __name__ == "__main__":
    main_window = MainWindow()
    main_window.mainloop()
