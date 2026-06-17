import tkinter as tk
import mainwindow

class ReadMe(tk.Tk):
    def __init__(self):
        super().__init__()
        #########################################WINDOW SET-UP####################################################
        self.window_size = "700x400"
        self.geometry(self.window_size)
        self.title("Read Me")

        ####################################### TEXT BOX #########################################################
        self.description_text = tk.Text(self, width=75, height=16, wrap="word", font=("Verdana", 10))
        self.description_text.grid(row=1, column=1)
        self.message = "To Display All Current Customers In Database Search Phone: 1234567890\n\n" \
                       "Users can add, search, or delete customers from the database. Uses the pandas module to " \
                       "store data in the customer_data.csv file located in the data folder. Program runs data " \
                       "validation to make sure data is properly entered before it's written to the " \
                       "customer_data.csv file.\n\n" \
                       "It prevents customer duplicates in the database by checking no two customers have the same " \
                       "first name, last name, phone number, and email. First name, last name, phone number, " \
                       "and emails can be shared, but all 4 previously mention data cannot be the same.\n\n" \
                       "Users can search for a customer by first and last name, phone number, or email. Customers " \
                       "can be edited or deleted from the database."

        self.description_text.insert(index="end", chars=self.message)
        self.description_text.config(state="disabled") # sets Text widget to read-only mode

        ############################################### HOME BUTTON #################################################
        self.button_font = ("Arial", 14)
        self.home_btn = tk.Button(self, text="Home", font=self.button_font, width=10, command=self.home)
        self.home_btn.grid(row=2, column=1, pady=(20, 0))

        ####################################### EMPTY GRID CELLS CONFIGURATION ######################################
        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=2, weight=1)
        self.rowconfigure(index=0, weight=1)
        self.rowconfigure(index=3, weight=1)

        self.mainloop()

    def home(self):
        """returns user to the main window"""
        self.destroy()
        main_window = mainwindow.MainWindow()
        main_window.mainloop()


if __name__ == "__main__":
    read_me = ReadMe()
    read_me.mainloop()