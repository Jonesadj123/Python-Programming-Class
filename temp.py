"""
File: temperatureconverter.py
A GUI program that converts temperatures
between Fahrenheit and Celsius.
"""

import sys

# Allow IDLE to find BreezyPythonGUI
sys.path.append(
    r"C:\Users\jones\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages"
)

from breezypythongui import EasyFrame


class TemperatureConverter(EasyFrame):

    def __init__(self):
        """Set up the temperature converter window."""

        EasyFrame.__init__(
            self,
            title="Temperature Converter",
            width=350,
            height=150
        )

        # Row 0: Labels
        self.addLabel(
            text="Fahrenheit",
            row=0,
            column=0
        )

        self.addLabel(
            text="Celsius",
            row=0,
            column=1
        )

        # Row 1: Temperature entry fields
        self.fahrenheitField = self.addFloatField(
            value=32.0,
            row=1,
            column=0,
            width=15
        )

        self.celsiusField = self.addFloatField(
            value=0.0,
            row=1,
            column=1,
            width=15
        )

        # Row 2: Command buttons
        self.addButton(
            text=">>>>",
            row=2,
            column=0,
            command=self.convertToCelsius
        )

        self.addButton(
            text="<<<<",
            row=2,
            column=1,
            command=self.convertToFahrenheit
        )

    def convertToCelsius(self):
        """Convert Fahrenheit to Celsius."""

        fahrenheit = self.fahrenheitField.getNumber()

        celsius = (fahrenheit - 32) * 5 / 9

        self.celsiusField.setNumber(celsius)

    def convertToFahrenheit(self):
        """Convert Celsius to Fahrenheit."""

        celsius = self.celsiusField.getNumber()

        fahrenheit = celsius * 9 / 5 + 32

        self.fahrenheitField.setNumber(fahrenheit)


def main():
    """Run the temperature converter."""

    TemperatureConverter().mainloop()


if __name__ == "__main__":
    main()
