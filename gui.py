import tkinter as tk
from tkinter import ttk
from Calc import Calculator as calc


class CalcApp:
    def __init__(self):
        self.window = tk.Tk()
        self.distLabel = tk.Label(text="Distance Entry")
        self.distEntry = tk.Entry(self.window, font=("calibre", 10, "normal"))
        self.timeLabel = tk.Label(text="Time Entry *format(min:secs)*")
        self.timeEntry = tk.Entry(self.window, font=("calibre", 10, "normal"))
        self.output = tk.Label()

        # Initialize placholder
        self.dist = 1
        self.time = "5:00"

        # Create an instance of Calculator
        self.calc = calc(self.dist, self.time)

        self.radioLabels = [
            "Pace",
            "Convert Miles to Km",
            "Convert Kms to Miles",
            "Convert min/mile to min/km",
            "Convert min/km to min/mile",
        ]
        self.function_dict = {
            "Pace": self.calc.pace,
            "Convert Miles to Km": self.calc.MilesKilometers,
            "Convert Kms to Miles": self.calc.KilometersMiles,
            "Convert min/mile to min/km": self.calc.MkM,
            "Convert min/km to min/mile": self.calc.KmM,
        }

        # Initialize the main window
        self.window.title("Conversion Calculator")
        self.allRadios = []
        self.selected_value = (
            tk.StringVar()
        )  # Variable to store the selected radio button value

        # Create a submit btton
        self.button = ttk.Button(
            self.window, text="Click to Convert", command=self.submit
        )

        # Create a Title label
        self.label = tk.Label(
            self.window,
            text="Welcome to the conversion calculator",
            pady=30,
            padx=100,
            font=100,
            justify="center",
        )

    # function to create
    def radioArray(self):
        # Labels for the radio buttons

        # create radio buttons for selecting calculator command
        for label in self.radioLabels:
            radio_button = ttk.Radiobutton(
                self.window, text=label, variable=self.selected_value, value=label
            )
            self.allRadios.append(radio_button)
        return self.allRadios

    def radio(self, allRadios):
        # one after another Pack the radio buttons
        for radio in allRadios:
            radio.pack()

    def submit(self):
        self.dist = float(self.distEntry.get())  # Convert to float
        self.time = self.timeEntry.get()

        # Update the Calculator instance with the new values entered in the entry fields
        self.calc.dist = self.dist
        self.calc.time = self.time

        # get label of the selected radio button
        selected_label = self.selected_value.get()

        # match radio button selection to desired calc function
        if selected_label in self.function_dict:
            selected_function = self.function_dict[selected_label]
            result = selected_function()
        else:
            result = "option not selected"

        # Print the result
        self.output.config(text=result)
        print("Result:", result)
        print("dist value:", self.dist)
        print("time value:", self.time)
        print("Selected value:", selected_label)

    def main(self):
        # Pack and display UI
        self.label.pack()
        self.radio(
            self.radioArray()
        )  # Call the method to pack the radio buttons and create the radio buttons contained within
        self.distLabel.pack()
        self.distEntry.pack()
        self.timeLabel.pack()
        self.timeEntry.pack()
        self.button.pack()
        self.output.pack()
        self.window.mainloop()  # Run the main event loop


# Create an instance of CalcApp and run the main method in it
app = CalcApp()
app.main()
