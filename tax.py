"""
File: taxformwithgui.py
Tax Calculator GUI Program
"""

import sys

# Allow IDLE to find BreezyPythonGUI
sys.path.append(
    r"C:\Users\jones\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages"
)

from breezypythongui import EasyFrame


class TaxCalculator(EasyFrame):

    def __init__(self):
        """Set up the tax calculator window."""

        EasyFrame.__init__(
            self,
            title="Tax Calculator",
            width=300,
            height=200
        )

        # Taxable income
        self.addLabel(
            text="Taxable Income:",
            row=0,
            column=0
        )

        self.incomeField = self.addFloatField(
            value=0.0,
            row=0,
            column=1,
            width=15
        )

        # Tax rate
        self.addLabel(
            text="Tax Rate (%):",
            row=1,
            column=0
        )

        self.rateField = self.addFloatField(
            value=15.0,
            row=1,
            column=1,
            width=15
        )

        # Income tax result
        self.addLabel(
            text="Income Tax:",
            row=2,
            column=0
        )

        self.taxField = self.addFloatField(
            value=0.0,
            row=2,
            column=1,
            width=15,
            state="readonly"
        )

        # Calculate button
        self.addButton(
            text="Calculate",
            row=3,
            column=0,
            columnspan=2,
            command=self.calculateTax
        )

    def calculateTax(self):
        """Calculate and display the income tax."""

        income = self.incomeField.getNumber()
        rate = self.rateField.getNumber()

        tax = income * rate / 100

        self.taxField.setNumber(tax)


def main():
    """Start the application."""

    TaxCalculator().mainloop()


if __name__ == "__main__":
    main()
