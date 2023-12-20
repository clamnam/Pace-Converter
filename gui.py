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

        # Labels for the radio buttons
        self.radio_labels = [
            "Pace",
            "Convert Miles to Km",
            "Convert Kms to Miles",
            "Convert min/mile to min/km",
            "Convert min/km to min/mile",
        ]
        # Functions for radio Buttons on submit

        self.function_dict = {
            "Pace": self.calc.user_pace,
            "Convert Miles to Km": self.calc.miles_kilometers,
            "Convert Kms to Miles": self.calc.kilometers_miles,
            "Convert min/mile to min/km": self.calc.miles_to_km,
            "Convert min/km to min/mile": self.calc.km_to_miles,
        }

        # Initialize the main window
        self.window.title("Conversion Calculator")
        self.allRadios = []
        self.selectedValue = (
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
    def radio_array(self):
        # create radio buttons for selecting calculator command
        for label in self.radio_labels:
            radioButton = ttk.Radiobutton(
                self.window, text=label, variable=self.selectedValue, value=label
            )
            self.allRadios.append(radioButton)
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
        selectedLabel = self.selectedValue.get()

        # match radio button selection to desired calc function
        if selectedLabel in self.function_dict:
            selectedFunction = self.function_dict[selectedLabel]
            result = selectedFunction()
        else:
            result = "option not selected"

        # Print the result
        self.output.config(text=result)
        ###verifying data passing through
        # print("Result:", result)
        # print("dist value:", self.dist)
        # print("time value:", self.time)
        # print("Selected value:", selectedLabel)

    def main(self):
        # Pack and display UI
        self.label.pack()
        self.radio(
            self.radio_array()
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
