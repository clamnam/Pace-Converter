# Calculator (Calc.py) README

### Running the GUI Application

1. Create an instance of CalcApp.
2. Call the `main` method to start the GUI application.

``` 
app = CalcApp()
app.main()
```

## Description

The `Calc.py` file contains a Python class named `Calculator`, which is designed to perform various distance and time-related calculations. The calculations include converting between miles and kilometers, calculating pace, and converting pace units. The class is intended for use in a graphical user interface (GUI) application.

## Class: Calculator

### Methods

#### `__init__(self, dist: int, time: str)`

- Constructor for the Calculator class.
- Initializes the distance (`dist`) and time (`time`) attributes.

#### `split_time(self) -> Union[Tuple[int, int], str]`

- Splits the time input (in the format 'min:sec') into minutes and seconds.
- Returns a tuple of minutes and seconds if successful, or an error message if the input is invalid.

#### `miles_kilometers(self) -> Union[float, str]`

- Converts distance from miles to kilometers.
- Returns the converted distance in kilometers or an error message if unsuccessful.

#### `kilometers_miles(self) -> Union[float, str]`

- Converts distance from kilometers to miles.
- Returns the converted distance in miles or an error message if unsuccessful.

#### `pace(self) -> Union[Tuple[int, int], str]`

- Calculates pace based on the input time and distance.
- Returns a tuple of minutes and seconds per kilometer or an error message if unsuccessful.

#### `user_pace(self) -> Tuple[int, str]`

- Calls the `pace` method and formats the result for user-friendly display.
- Returns a tuple representing the pace in minutes and seconds.

#### `km_to_miles(self) -> Union[Tuple[int, str], str]`

- Converts pace from minutes per kilometer to minutes per mile.
- Returns a tuple representing the converted pace or an error message if unsuccessful.

#### `miles_to_km(self) -> Union[Tuple[int, str], str]`

- Converts pace from minutes per mile to minutes per kilometer.
- Returns a tuple representing the converted pace or an error message if unsuccessful.

## GUI Application (gui.py)

The `gui.py` file contains a GUI application built using the `tkinter` library. It allows users to input distance and time values, select a specific calculation, and view the result.

### Class: CalcApp

#### Methods

#### `__init__(self)`

- Constructor for the CalcApp class.
- Initializes the main window, labels, entries, and an instance of the Calculator class.

#### `radio_array(self) -> List[ttk.Radiobutton]`

- Creates radio buttons for selecting calculator commands.
- Returns a list of radio buttons.

#### `radio(self, allRadios: List[ttk.Radiobutton])`

- Packs the radio buttons into the GUI.

#### `submit(self)`

- Retrieves input values from the GUI, updates the Calculator instance, and performs the selected calculation.
- Displays the result in the GUI.

#### `main(self)`

- Packs and displays the UI elements, including radio buttons, entry fields, and buttons.
- Runs the main event loop.


