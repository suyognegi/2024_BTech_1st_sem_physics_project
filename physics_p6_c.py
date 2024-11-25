# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow
# from PyQt5.uic import loadUi
# from decimal import Decimal, getcontext, InvalidOperation
#
# # Setting decimal precision
# getcontext().prec = 18
#
# class LengthConversion(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         loadUi("physics_p6_c_i.ui", self)
#         self.pushButton_3.clicked.connect(self.convert_button)
#
#         # Speed of light in m/s
#         self.c = Decimal("2.998e8")  # meters per second
#
#
#     def cm_to(self, convert_to):
#         cms = {
#             "cm/s": Decimal("1"),
#             "m/s": Decimal("1e-2"),
#             "km/s": Decimal("1e-5"),
#             "km/hr": Decimal("3.6e-2"),
#             "AU/day": Decimal("5.775e-9"),
#             "pc/Myr": Decimal("9.775e-18"),
#             "ly/yr": Decimal("3.16888e-11")
#         }
#         try:
#             value = Decimal(self.lineEdit_5.text()) * cms[convert_to]
#             self.label_5.setText(self.format_scientific(value))
#             print(self.format_scientific(value))
#         except InvalidOperation:
#             self.label_5.setText("Error")
#         except KeyError:
#             self.label_5.setText("Conversion not supported")
#
#     def ms_to(self, convert_to):
#         ms = {
#             "m/s": Decimal("1"),
#             "cm/s": Decimal("1e2"),
#             "km/s": Decimal("1e-3"),
#             "km/hr": Decimal("3.6"),
#             "AU/day": Decimal("5.775e-7"),
#             "pc/Myr": Decimal("9.775e-16"),
#             "ly/yr": Decimal("3.16888e-9")
#         }
#         try:
#             value = Decimal(self.lineEdit_5.text()) * ms[convert_to]
#             self.label_5.setText(self.format_scientific(value))
#             print(self.format_scientific(value))
#         except InvalidOperation:
#             self.label_5.setText("Error")
#         except KeyError:
#             self.label_5.setText("Conversion not supported")
#
#     def km_s_to(self, convert_to):
#         km_s = {
#             "km/s": Decimal("1"),
#             "cm/s": Decimal("1e5"),
#             "m/s": Decimal("1e3"),
#             "km/hr": Decimal("3.6e3"),
#             "AU/day": Decimal("5.775e-4"),
#             "pc/Myr": Decimal("9.775e-13"),
#             "ly/yr": Decimal("3.16888e-6")
#         }
#         try:
#             value = Decimal(self.lineEdit_5.text()) * km_s[convert_to]
#             self.label_5.setText(self.format_scientific(value))
#             print(self.format_scientific(value))
#         except InvalidOperation:
#             self.label_5.setText("Error")
#         except KeyError:
#             self.label_5.setText("Conversion not supported")
#
#     def km_hr_to(self, convert_to):
#         km_hr = {
#             "km/hr": Decimal("1"),
#             "cm/s": Decimal("2.77778e-3"),
#             "m/s": Decimal("0.277778"),
#             "km/s": Decimal("2.77778e-4"),
#             "AU/day": Decimal("1.598e-7"),
#             "pc/Myr": Decimal("2.654e-15"),
#             "ly/yr": Decimal("9.713e-9")
#         }
#         try:
#             value = Decimal(self.lineEdit_5.text()) * km_hr[convert_to]
#             self.label_5.setText(self.format_scientific(value))
#             print(self.format_scientific(value))
#         except InvalidOperation:
#             self.label_5.setText("Error")
#         except KeyError:
#             self.label_5.setText("Conversion not supported")
#
#     def AU_day_to(self, convert_to):
#         AU_day = {
#             "AU/day": Decimal("1"),
#             "cm/s": Decimal("1.5778e+8"),
#             "m/s": Decimal("1.5778e+6"),
#             "km/s": Decimal("1.5778e+3"),
#             "km/hr": Decimal("5.6788e+6"),
#             "pc/Myr": Decimal("5.915e+14"),
#             "ly/yr": Decimal("1.711e+8")
#         }
#         try:
#             value = Decimal(self.lineEdit_5.text()) * AU_day[convert_to]
#             self.label_5.setText(self.format_scientific(value))
#             print(self.format_scientific(value))
#         except InvalidOperation:
#             self.label_5.setText("Error")
#         except KeyError:
#             self.label_5.setText("Conversion not supported")
#
#     def pc_Myr_to(self, convert_to):
#         pc_Myr = {
#             "pc/Myr": Decimal("1"),
#             "cm/s": Decimal("1.022e+24"),
#             "m/s": Decimal("1.022e+22"),
#             "km/s": Decimal("1.022e+19"),
#             "km/hr": Decimal("3.679e+20"),
#             "AU/day": Decimal("1.694e+14"),
#             "ly/yr": Decimal("3.262e+6")
#         }
#         try:
#             value = Decimal(self.lineEdit_5.text()) * pc_Myr[convert_to]
#             self.label_5.setText(self.format_scientific(value))
#             print(self.format_scientific(value))
#         except InvalidOperation:
#             self.label_5.setText("Error")
#         except KeyError:
#             self.label_5.setText("Conversion not supported")
#
#     def ly_yr_to(self, convert_to):
#         ly_yr = {
#             "ly/yr": Decimal("1"),
#             "cm/s": Decimal("3.154e+17"),
#             "m/s": Decimal("3.154e+15"),
#             "km/s": Decimal("3.154e+12"),
#             "km/hr": Decimal("1.136e+14"),
#             "AU/day": Decimal("1.711e+8"),
#             "pc/Myr": Decimal("3.068e-7")
#         }
#         try:
#             value = Decimal(self.lineEdit_5.text()) * ly_yr[convert_to]
#             self.label_5.setText(self.format_scientific(value))
#             print(self.format_scientific(value))
#         except InvalidOperation:
#             self.label_5.setText("Error")
#         except KeyError:
#             self.label_5.setText("Conversion not supported")
#
#     def c_to(self, convert_to):
#         c = {
#             "m/s": self.c,
#             "cm/s": self.c * Decimal("1e2"),
#             "km/s": self.c * Decimal("1e-3"),
#             "km/hr": self.c * Decimal("3.6e3"),
#             "AU/day": self.c * Decimal("1.5778e-9"),
#             "pc/Myr": self.c * Decimal("1.022e-17"),
#             "ly/yr": self.c * Decimal("1.057e-12")
#         }
#         try:
#             value = Decimal(self.lineEdit_5.text()) * c[convert_to]
#             self.label_5.setText(self.format_scientific(value))
#             print(self.format_scientific(value))
#         except InvalidOperation:
#             self.label_5.setText("Error")
#         except KeyError:
#             self.label_5.setText("Conversion not supported")
#
#     def format_scientific(self, value):
#         # Format the number in scientific notation with superscript
#         exponent = int(value.log10().to_integral_value())  # Get the exponent
#         mantissa = value / Decimal("10")**exponent  # Get the mantissa
#
#         # Format mantissa with two decimal places and create scientific notation in HTML
#         if mantissa == Decimal("1.0"):
#             return f"10<sup>{exponent}</sup>"
#         elif mantissa == Decimal("0.1"):
#             return f"1<sup>{exponent-1}</sup>"
#         else:
#             return f"{mantissa:.2f} x 10<sup>{exponent}</sup>"
#     def more_precise(self):
#         self.label_5.hide()
#         self.label_6.show()
#     def convert_button(self):
#         print("Button Clicked !!")
#         self.conv_from = self.comboBox.currentText()
#         self.conv_to = self.comboBox_2.currentText()
#         print(self.conv_to)
#
#         if self.conv_from == "cm/s":
#             print("function called")
#             self.cm_to(self.conv_to)
#         elif self.conv_from == "m/s":
#             print("function called")
#             self.ms_to(self.conv_to)
#         elif self.conv_from == "km/s":
#             print("function called")
#             self.km_s_to(self.conv_to)
#         elif self.conv_from == "km/hr":
#             print("function called")
#             self.km_hr_to(self.conv_to)
#         elif self.conv_from == "AU/day":
#             print("function called")
#             self.AU_day_to(self.conv_to)
#         elif self.conv_from == "pc/Myr":
#             print("function called")
#             self.pc_Myr_to(self.conv_to)
#         elif self.conv_from == "ly/yr":
#             print("function called")
#             self.ly_yr_to(self.conv_to)
#         elif self.conv_from == "c":
#             print("function called")
#             self.c_to(self.conv_to)
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     main_window = LengthConversion()
#     main_window.show()
#     sys.exit(app.exec())



import sys
from cmath import sqrt

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.uic import loadUi
from decimal import Decimal, getcontext, InvalidOperation

from delete import widget

# Setting decimal precision
getcontext().prec = 18


class LengthConversion(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("physics_p6_c_i.ui", self)

        # Connect the text and combo box changes to real-time conversion
        self.lineEdit_5.textChanged.connect(self.convert_button)
        self.comboBox.currentIndexChanged.connect(self.convert_button)
        self.comboBox_2.currentIndexChanged.connect(self.convert_button)

        # Speed of light in m/s
        self.c = Decimal("2.998e8")  # meters per second
        self.comboBox.raise_()
        self.comboBox_2.raise_()
        self.label_4.raise_()
        self.lineEdit_5.raise_()
        self.label_6.raise_()
        self.label_5.raise_()
        # Connect the combo box changes to the synchronization methods
        self.comboBox_3.currentIndexChanged.connect(self.same_box)
        self.comboBox_4.currentIndexChanged.connect(self.same_box2)
        self.pushButton_2.clicked.connect(self.solve_button_function)

    def same_box(self):
        # Set the text of comboBox_4 to match comboBox_3
        current_text = self.comboBox_3.currentText()
        if self.comboBox_4.currentText() != current_text:
            self.comboBox_4.setCurrentText(current_text)

    def same_box2(self):
        # Set the text of comboBox_3 to match comboBox_4
        current_text = self.comboBox_4.currentText()
        if self.comboBox_3.currentText() != current_text:
            self.comboBox_3.setCurrentText(current_text)

    def cm_to(self, convert_to):
        cms = {
            "cm/s": Decimal("1"),
            "m/s": Decimal("1e-2"),
            "km/s": Decimal("1e-5"),
            "km/hr": Decimal("3.6e-2"),
            "AU/day": Decimal("5.775e-9"),
            "pc/Myr": Decimal("9.775e-18"),
            "ly/yr": Decimal("3.16888e-11")
        }
        self.perform_conversion(cms, convert_to)

    def ms_to(self, convert_to):
        ms = {
            "m/s": Decimal("1"),
            "cm/s": Decimal("1e2"),
            "km/s": Decimal("1e-3"),
            "km/hr": Decimal("3.6"),
            "AU/day": Decimal("5.775e-7"),
            "pc/Myr": Decimal("9.775e-16"),
            "ly/yr": Decimal("3.16888e-9")
        }
        self.perform_conversion(ms, convert_to)

    def km_s_to(self, convert_to):
        km_s = {
            "km/s": Decimal("1"),
            "cm/s": Decimal("1e5"),
            "m/s": Decimal("1e3"),
            "km/hr": Decimal("3.6e3"),
            "AU/day": Decimal("5.775e-4"),
            "pc/Myr": Decimal("9.775e-13"),
            "ly/yr": Decimal("3.16888e-6")
        }
        self.perform_conversion(km_s, convert_to)

    def km_hr_to(self, convert_to):
        km_hr = {
            "km/hr": Decimal("1"),
            "cm/s": Decimal("2.77778e-3"),
            "m/s": Decimal("0.277778"),
            "km/s": Decimal("2.77778e-4"),
            "AU/day": Decimal("1.598e-7"),
            "pc/Myr": Decimal("2.654e-15"),
            "ly/yr": Decimal("9.713e-9")
        }
        self.perform_conversion(km_hr, convert_to)

    def AU_day_to(self, convert_to):
        AU_day = {
            "AU/day": Decimal("1"),
            "cm/s": Decimal("1.5778e+8"),
            "m/s": Decimal("1.5778e+6"),
            "km/s": Decimal("1.5778e+3"),
            "km/hr": Decimal("5.6788e+6"),
            "pc/Myr": Decimal("5.915e+14"),
            "ly/yr": Decimal("1.711e+8")
        }
        self.perform_conversion(AU_day, convert_to)

    def pc_Myr_to(self, convert_to):
        pc_Myr = {
            "pc/Myr": Decimal("1"),
            "cm/s": Decimal("1.022e+24"),
            "m/s": Decimal("1.022e+22"),
            "km/s": Decimal("1.022e+19"),
            "km/hr": Decimal("3.679e+20"),
            "AU/day": Decimal("1.694e+14"),
            "ly/yr": Decimal("3.262e+6")
        }
        self.perform_conversion(pc_Myr, convert_to)

    def ly_yr_to(self, convert_to):
        ly_yr = {
            "ly/yr": Decimal("1"),
            "cm/s": Decimal("3.154e+17"),
            "m/s": Decimal("3.154e+15"),
            "km/s": Decimal("3.154e+12"),
            "km/hr": Decimal("1.136e+14"),
            "AU/day": Decimal("1.711e+8"),
            "pc/Myr": Decimal("3.068e-7")
        }
        self.perform_conversion(ly_yr, convert_to)

    def c_to(self, convert_to):
        c = {
            "m/s": self.c,
            "cm/s": self.c * Decimal("1e2"),
            "km/s": self.c * Decimal("1e-3"),
            "km/hr": self.c * Decimal("3.6e3"),
            "AU/day": self.c * Decimal("1.5778e-9"),
            "pc/Myr": self.c * Decimal("1.022e-17"),
            "ly/yr": self.c * Decimal("1.057e-12")
        }
        self.perform_conversion(c, convert_to)

    def perform_conversion(self, conversion_dict, convert_to):
        try:
            value = Decimal(self.lineEdit_5.text()) * conversion_dict[convert_to]
            self.label_5.setText(self.format_scientific(value))
        except (InvalidOperation, KeyError):
            self.label_5.setText("Error")

    def format_scientific(self, value):
        exponent = int(value.log10().to_integral_value())
        mantissa = value / Decimal("10") ** exponent

        if mantissa == Decimal("1.0"):
            return f"10<sup>{exponent}</sup>"
        else:
            return f"{mantissa:.2f} x 10<sup>{exponent}</sup>"

    def convert_button(self):
        self.conv_from = self.comboBox.currentText()
        self.conv_to = self.comboBox_2.currentText()

        if self.conv_from == "cm/s":
            self.cm_to(self.conv_to)
        elif self.conv_from == "m/s":
            self.ms_to(self.conv_to)
        elif self.conv_from == "km/s":
            self.km_s_to(self.conv_to)
        elif self.conv_from == "km/hr":
            self.km_hr_to(self.conv_to)
        elif self.conv_from == "AU/day":
            self.AU_day_to(self.conv_to)
        elif self.conv_from == "pc/Myr":
            self.pc_Myr_to(self.conv_to)
        elif self.conv_from == "ly/yr":
            self.ly_yr_to(self.conv_to)
        elif self.conv_from == "c":
            self.c_to(self.conv_to)

    def solve_button_function(self):
        self.error = False
        try:
            self.v = float(self.lineEdit_6.text())
            self.c = float(self.lineEdit_7.text())
            self.ans = (self.v / self.c) ** 2
            print(self.ans, self.error)

            if self.ans > 1:
                self.error = True
                print("Error: Value exceeds 1")
                # Handle the error, possibly showing a message box
                QMessageBox.critical(self, "Error", "The value exceeds 1. Invalid input.")
            else:
                self.ans = sqrt(1 - self.ans)
                self.ans = f"{self.ans:.2f}"
                print("Back Button Clicked !!")
                self.call_window = LengthConversionSolve(self.ans)
                widget.addWidget(self.call_window)
                widget.setCurrentIndex(widget.currentIndex() + 1)

        except ValueError:
            QMessageBox.critical(self, "Error", "Please enter valid numbers.")

class LengthConversionSolve(QMainWindow):
    def __init__(self, x):
        super().__init__()
        loadUi("physics_p6_c_ii.ui", self)
        print(x)
        self.label_6.setText(str(x))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = LengthConversion()
    main_window.setFixedSize(main_window.size())
    main_window.show()
    sys.exit(app.exec())


