import tkinter as tk
import mainwindow
import pandas as pd
import vieweditcustomer

class SearchResults(tk.Frame):
    """Creates a tkinter.Frame to display the search results"""
    def __init__(self, parent):
        super().__init__(parent)
        # parent is the tkinter widget in which SearchResults() class is used.
        # In this program the parent is the SearchCustomer() class/window.
        self.parent = parent
        self.customer_data_path = "data\customer_data.csv"
        self.button_font = ("Arial", 14)

        ######################################FRAME, SCROLLBAR, CANVAS SET-UP##########################################
        self.width= 920
        self.height = 400
        self.configure(width=self.width, height=self.height)

        # creates scrollbar with vertical scroll position
        self.scrollbar = tk.Scrollbar(self, orient="vertical")
        # "NS" specifies scrollbar should stick to top and bottom of cell
        self.scrollbar.grid(row=0, column=1, sticky="NS")

        # yscrollcommand links scrollbar to scroll vertically on canvas
        # use .set to make the scrollbar be the proper size and have proper functionality
        self.canvas = tk.Canvas(self, width=self.width, height=self.height, yscrollcommand=self.scrollbar.set)
        # "NSEW" specifies canvas to expand to all four edges of the grid cell
        self.canvas.grid(row=0, column=0, sticky="NSEW")

        # configures scrollbar to be used to scroll the canvas vertically. The canvas.yview method is called
        # to update the visible portion of the canvas and make sure it matches the current position of the scrollbar.
        self.scrollbar.config(command=self.canvas.yview)

        self.inner_frame = tk.Frame(self.canvas, width=self.width) # frame is created inside the canvas

        # makes self.inner_frame into a child widget of canvas.
        # places frame at upper left corner of canvas (0,0) x,y coordinate
        # anchor="n" places widget at the top edge of the canvas
        self.canvas.create_window((0,0), window=self.inner_frame, anchor="n")

        # updates canvas widget to adjust it's scrolling region based on the size of its child widget self.inner_frame
        self.inner_frame.update_idletasks() # ensures all drawing and layout of self.inner_frame are completed
        # sets the scrollregion to the bounding box of all it's contents in any direction
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

        # binds "<Configure>" event to the canvas widget. Event is triggered whenever the size or position of the
        # canvas changes. callback function self.on_configure is called whenever the event is triggered.
        self.canvas.bind("<Configure>", self.on_configure)
        # binds the <MouseWheel> whenever it's used at any position in the window.
        # lambda event: allows it to pass an event object to that specifies the amount of scroll with mouse wheel
        self.canvas.bind_all("<MouseWheel>", lambda event: self.canvas.yview_scroll(int(-1*(event.delta/120)), "units"))

        ################################# LABELS ########################################################
        self.label_font = ("Arial", 12, "bold")
        self.first_name_label = tk.Label(self.inner_frame, text="First Name", font=self.label_font)
        self.first_name_label.grid(row=0, column=1, sticky="S")

        self.last_name_label = tk.Label(self.inner_frame, text="Last Name", font=self.label_font)
        self.last_name_label.grid(row=0, column=2, sticky="S")

        self.phone_label = tk.Label(self.inner_frame, text="Phone", font=self.label_font)
        self.phone_label.grid(row=0, column=3, sticky="S")

        self.email_label = tk.Label(self.inner_frame, text="Email", font=self.label_font)
        self.email_label.grid(row=0, column=4, sticky="S")

        #######################################EMPTY GRID CELL SPACE###################################################
        self.inner_frame.columnconfigure(index=0, weight=1)
        self.inner_frame.columnconfigure(index=6, weight=1)

    def search_results(self, search_results_df):
        """Will display the search results in the frame"""
        results_font =("Arial", 12)

        # iterates through each row in the search results dataframe and displays it in the self.inner_frame
        for i, row in search_results_df.iterrows():
            first_name = row["First Name"]
            last_name = row["Last Name"]
            phone = str(row["Phone"])
            email = row["Email"]
            identification = row["Customer ID"]

            x_padding = 20 # x padding size between result labels

            first_name_result =  tk.Label(self.inner_frame, text=first_name, font=results_font)
            first_name_result.grid(row=i+1, column=1, padx=x_padding)
            last_name_result = tk.Label(self.inner_frame, text=last_name, font=results_font)
            last_name_result.grid(row=i+1, column=2, padx=x_padding)
            phone_result = tk.Label(self.inner_frame, text=phone, font=results_font)
            phone_result.grid(row=i+1, column=3, padx=x_padding)
            email_result = tk.Label(self.inner_frame, text=email, font=results_font)
            email_result.grid(row=i+1, column=4, padx=x_padding)

            # command=lambda allows you to call method self.view_edit_result() and pass argument customer_id
            # lambda is a function in itself that calls the self.view_edit_result()
            # customer_id=identification must be used with lambda to capture the current value of the
            # identification variable through each iteration of the for loop ensures the correct Customer ID
            # is passed to the view_edit_result() method
            view_edit_btn = tk.Button(self.inner_frame, text="View/Edit", font=self.button_font,
                                      command=lambda customer_id=identification:self.view_edit_result(customer_id))
            view_edit_btn.grid(row=i+1, column=5, padx=x_padding)

    def view_edit_result(self, customer_id):
        """handles the view/edit buttons, ensures parent is destroyed and view/edit window is created"""
        self.parent.destroy() # destroys the parent tkinter window where this frame class is created
        view_edit_customer = vieweditcustomer.ViewEditCustomer()
        view_edit_customer.prefill_entries(customer_id) # prefills entries in view/edit window with use of Customer ID

    def on_configure(self, event):
        """updates the scroll region of canvas to ensure that all its contents are visible"""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def home(self):
        """returns user to the main window"""
        self.destroy()
        main_window = mainwindow.MainWindow()
        main_window.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    df = pd.read_csv("data\\customer_data.csv")
    search_results = SearchResults(root)
    search_results.search_results(df)
    search_results.pack()
    root.mainloop()
