import sys

from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QMessageBox, QInputDialog, QApplication, QStackedWidget
from PyQt5.uic import loadUi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import math


class NinePage(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("physics_p9.ui", self)

        self.label_22.hide()
        self.label_16.hide()
        self.label_17.hide()
        self.label_18.hide()

        self.label_19.hide()
        self.label_20.hide()
        self.label_21.hide()

        # self.lineEdit_3.textChanged.connect(self.calculate_missing_value)  # Hypotenuse
        # self.lineEdit_4.textChanged.connect(self.calculate_missing_value)  # Base
        # self.lineEdit_5.textChanged.connect(self.calculate_missing_value)  # Perpendicular

        # sin
        self.lineEdit_14.textChanged.connect(self.calculate_sin)
        self.lineEdit_20.textChanged.connect(self.calculate_theta)

        # cos
        self.lineEdit_15.textChanged.connect(self.calculate_cos)
        self.lineEdit_21.textChanged.connect(self.calculate_theta_cos)

        # tan
        self.lineEdit_16.textChanged.connect(self.calculate_tan)
        self.lineEdit_22.textChanged.connect(self.calculate_theta_tan)

        #  (csc)
        self.lineEdit_17.textChanged.connect(self.calculate_cosec)
        self.lineEdit_23.textChanged.connect(self.calculate_theta_cosec)

        # (sec)
        self.lineEdit_18.textChanged.connect(self.calculate_sec)
        self.lineEdit_24.textChanged.connect(self.calculate_theta_sec)

        # (cot)
        self.lineEdit_19.textChanged.connect(self.calculate_cot)
        self.lineEdit_25.textChanged.connect(self.calculate_theta_cot)

        self.pushButton.clicked.connect(self.choose_graph)

        # side
        self.lineEdit.textChanged.connect(self.degree)
        self.lineEdit_2.textChanged.connect(self.radian)

        self.pushButton_2.clicked.connect(self.pytho)

        import math
        if len(self.lineEdit_14.text()) != 0:
            self.sin = self.lineEdit_14.text()
        else:
            self.sin = "None"

        if len(self.lineEdit_15.text()) != 0:
            self.cos = self.lineEdit_15.text()
        else:
            self.cos = "None"
        if len(self.lineEdit_16.text()) != 0:
            self.tan = self.lineEdit_16.text()
        else:
            self.tan = "None"


        if len(self.lineEdit_17.text()) != 0:
            self.csc = self.lineEdit_17.text()
        else:
            self.csc = "None"

        if len(self.lineEdit_18.text()) != 0:
            self.sec = self.lineEdit_18.text()
        else:
            self.sec = "None"

        if len(self.lineEdit_19.text()) != 0:
            self.cot = self.lineEdit_19.text()
        else:
            self.cot = "None"

        # HOME
        



    def pytho(self):
        if self.pushButton_2.text() == "BACK":
            # Reset to initial state when "BACK" is pressed
            self.pushButton_2.setText("CALCULATE")

            # Hide result labels
            self.label_22.hide()
            self.label_16.hide()
            self.label_17.hide()
            self.label_18.hide()
            self.label_19.hide()
            self.label_20.hide()
            self.label_21.hide()

            self.label_15.show()  # triangle diagram
            self.lineEdit_3.show()  # hypote
            self.lineEdit_4.show()  # base
            self.lineEdit_5.show()  # perpe

            # Clear the input fields
            self.lineEdit_3.clear()
            self.lineEdit_4.clear()
            self.lineEdit_5.clear()

            # Clear the result labels
            self.label_19.setText("")
            self.label_20.setText("")
            self.label_21.setText("")

        else:
            self.pushButton_2.setText("BACK")

            # Show
            self.label_22.show()
            self.label_16.show()
            self.label_17.show()
            self.label_18.show()
            self.label_19.show()
            self.label_20.show()
            self.label_21.show()

            # Hide input field
            self.label_15.hide()
            self.lineEdit_3.hide()
            self.lineEdit_4.hide()
            self.lineEdit_5.hide()


            h = self.lineEdit_3.text()  # Hypo
            b = self.lineEdit_4.text()  # Base
            p = self.lineEdit_5.text()  # Perpe

            try:
                h = float(h) if h else None
                b = float(b) if b else None
                p = float(p) if p else None
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
                return

            # Calculate missing side using Pythagoras theorem
            if b is not None and p is not None and h is None:
                h = math.sqrt(b ** 2 + p ** 2)  # Calculate hypotenuse
                print(f"Calculated Hypotenuse (h): {h:.2f}, Base (b): {b:.2f}, Perpendicular (p): {p:.2f}")
            elif h is not None and p is not None and b is None:
                if h > p:
                    b = math.sqrt(h ** 2 - p ** 2)  # Calculate base
                    print(f"Calculated Base (b): {b:.2f}, Hypotenuse (h): {h:.2f}, Perpendicular (p): {p:.2f}")
                else:
                    print("Invalid input: Hypotenuse must be greater than the Perpendicular.")
                    return
            elif h is not None and b is not None and p is None:
                if h > b:
                    p = math.sqrt(h ** 2 - b ** 2)  # Calculate perpendicular
                    print(f"Calculated Perpendicular (p): {p:.2f}, Hypotenuse (h): {h:.2f}, Base (b): {b:.2f}")
                else:
                    print("Invalid input: Hypotenuse must be greater than the Base.")
                    return
            else:
                print("Please provide exactly two values.")
                return

            # Display results in labels
            self.label_19.setText(f'{b:.2f}' if b is not None else "")
            self.label_20.setText(f'{p:.2f}' if p is not None else "")
            self.label_21.setText(f'{h:.2f}' if h is not None else "")

    def degree(self):
        try:
            degree_value = float(self.lineEdit.text())
            radian_value = degree_value * (math.pi) / 180

            # Block signal to prevent recursive update
            self.lineEdit_2.blockSignals(True)
            self.lineEdit_2.setText(f"{radian_value:.5f}")
            self.lineEdit_2.blockSignals(False)
        except ValueError:
            self.lineEdit_2.clear()  # Clear the output if input is invalid



    def radian(self):
        try:
            radian_value = float(self.lineEdit_2.text())
            degree_value = radian_value * 180 / (math.pi)

            # Block signal to prevent recursive update
            self.lineEdit.blockSignals(True)
            self.lineEdit.setText(f"{degree_value:.5f}")
            self.lineEdit.blockSignals(False)
        except ValueError:
            self.lineEdit.clear()  # Clear the output if input is invalid


    def calculate_sin(self):  # 14=theta 20=val
        self.lineEdit_20.blockSignals(True)
        try:
            degree_value = eval(self.lineEdit_14.text())
            radian = math.radians(float(degree_value))
            sin_value = math.sin(radian)
            self.lineEdit_20.setText(f"{sin_value:.2f}")
        except Exception as e:
            print(f"Error : {e}")
            self.lineEdit_20.setText("")
        self.lineEdit_20.blockSignals(False)

    def calculate_theta(self):  # 14=theta 20=val
        try:
            self.lineEdit_14.blockSignals(True)
            sin_value = eval(self.lineEdit_20.text())
            if -1 <= sin_value <= 1:
                try:
                    sin_theta = math.asin(float(sin_value))
                    degree_val = math.degrees(sin_theta)
                    self.lineEdit_14.setText(f"{degree_val:.2f}")
                except Exception as e:
                    print(f"Error : {e}")
                    self.lineEdit_20.lineEdit.setText("")
            self.lineEdit.blockSignals(False)
        except Exception as e:
            print(f"Error : {e}")

    def calculate_cos(self):  # 15=theta 21=val
        self.lineEdit_21.blockSignals(True)
        try:
            degree_value = eval(self.lineEdit_15.text())
            radian = math.radians(float(degree_value))
            cos_value = math.cos(radian)
            self.lineEdit_21.setText(f"{cos_value:.2f}")
        except Exception as e:
            print(f"Error : {e}")
            self.lineEdit_21.setText("")
        self.lineEdit_21.blockSignals(False)



    def calculate_theta_cos(self):
        cos_text = self.lineEdit_21.text()
        if cos_text:  # Avoid errors if input is empty
            try:
                cos_theta = float(cos_text)
                if -1 <= cos_theta <= 1:
                    theta = math.degrees(math.acos(cos_theta))
                    self.lineEdit_15.blockSignals(True)
                    self.lineEdit_15.setText(f'{theta:.1f}')
                    self.lineEdit_15.blockSignals(False)
                else:
                    self.lineEdit_15.setText('Out of range')
            except ValueError:
                self.lineEdit_15.setText('Invalid input')



    def calculate_tan(self):
        theta_text = self.lineEdit_16.text()
        if theta_text:
            try:
                theta = float(theta_text)
                tan_theta = math.tan(math.radians(theta))
                self.lineEdit_22.blockSignals(True)
                self.lineEdit_22.setText(f'{tan_theta:.4f}')
                self.lineEdit_22.blockSignals(False)
            except ValueError:
                self.lineEdit_22.setText('Invalid input')

    def calculate_theta_tan(self):
        tan_text = self.lineEdit_22.text()
        if tan_text:
            try:
                tan_theta = float(tan_text)
                # Use atan to calculate theta, converting back to degrees
                theta = math.degrees(math.atan(tan_theta))
                self.lineEdit_16.blockSignals(True)
                self.lineEdit_16.setText(f'{theta:.1f}')
                self.lineEdit_16.blockSignals(False)
            except ValueError:
                self.lineEdit_16.setText('Invalid input')


    # Cosec (csc)
    def calculate_cosec(self):  # 17=theta 23=val
        self.lineEdit_23.blockSignals(True)
        try:
            degree_val = eval(self.lineEdit_17.text())
            radian = math.radians(float(degree_val))
            csc_value = 1 / math.sin(radian)
            self.lineEdit_23.setText(f"{csc_value:.2f}")
        except Exception as e:
            print(f"Error : {e}")
            self.lineEdit_23.setText("")
        self.lineEdit_23.blockSignals(False)

    def calculate_theta_cosec(self):  # 17=theta 23=val
        self.lineEdit_17.blockSignals(True)
        try:
            degree_val = eval(self.lineEdit_23.text())
            radian = math.radians(float(degree_val))
            csc_value = 1 / math.sin(radian)
            self.lineEdit_17.setText(f"{csc_value:.2f}")
        except Exception as e:
            print(f"Error : {e}")
            self.lineEdit_17.setText("")
        self.lineEdit_17.blockSignals(False)

    def calculate_sec(self):  # 18=theta 24=val
        self.lineEdit_24.blockSignals(True)
        try:
            degree_val = eval(self.lineEdit_18.text())
            if float(degree_val) == 90:
                self.lineEdit_24.setText("")
            else:
                radian = math.radians(float(degree_val))
                sec_value = 1 / math.cos(radian)
                self.lineEdit_24.setText(f"{sec_value:.2f}")
        except Exception as e:
            print(f"Error: {e}")
            self.lineEdit_24.setText("")
        self.lineEdit_24.blockSignals(False)

    def calculate_theta_sec(self):  # 18=theta 24=val
        self.lineEdit_18.blockSignals(True)
        try:
            sec_value = eval(self.lineEdit_24.text())
            radian = math.acos(1 / float(sec_value))
            degree_val = math.degrees(radian)
            self.lineEdit_18.setText(f"{degree_val:.2f}")
        except Exception as e:
            print(f"Error: {e}")
            self.lineEdit_18.setText("")
        self.lineEdit_18.blockSignals(False)

    def calculate_cot(self):  # 19=theta 25=val
        self.lineEdit_25.blockSignals(True)
        try:
            degree_val = eval(self.lineEdit_19.text())
            radian = math.radians(float(degree_val))
            cot_value = 1 / math.tan(radian)
            self.lineEdit_25.setText(f"{cot_value:.2f}")
        except Exception as e:
            print(f"Error: {e}")
            self.lineEdit_25.setText("")
        self.lineEdit_25.blockSignals(False)

    def calculate_theta_cot(self):  # 19=theta 25=val
        self.lineEdit_19.blockSignals(True)
        try:
            cot_value = eval(self.lineEdit_25.text())
            radian = math.atan(1 / float(cot_value))
            degree_val = math.degrees(radian)
            self.lineEdit_19.setText(f"{degree_val:.2f}")
        except Exception as e:
            print(f"Error: {e}")
            self.lineEdit_19.setText("")
        self.lineEdit_19.blockSignals(False)


    def choose_graph(self):

        sin_value = self.lineEdit_20.text() or "None"
        cos_value = self.lineEdit_21.text() or "None"
        tan_value = self.lineEdit_22.text() or "None"
        csc_value = self.lineEdit_23.text() or "None"
        sec_value = self.lineEdit_24.text() or "None"
        cot_value = self.lineEdit_25.text() or "None"
        print("310")
        print(sin_value, cos_value, tan_value, csc_value, sec_value, cot_value)

        self.call_window = NineGraph(sin_value, cos_value, tan_value, csc_value, sec_value, cot_value)
        widget.addWidget(self.call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class NineGraph(QMainWindow):
    def __init__(self, sin_theta, cos_theta, tan_theta, csc_theta, sec_theta, cot_theta):
        super().__init__()
        loadUi("physics_p9_g_i.ui", self)
        print("NG 2134", sin_theta, cot_theta, tan_theta, csc_theta, sec_theta, cot_theta)
        for i in ("NG 2134", sin_theta, cot_theta, tan_theta, csc_theta, sec_theta, cot_theta):
            print(f"{i} -> type -> {type(i)}")
        self.trig_values = {
            "sin": sin_theta,
            "cos": cos_theta,
            "tan": tan_theta,
            "csc": csc_theta,
            "sec": sec_theta,
            "cot": cot_theta
        }

        self.pushButton_2.clicked.connect(self.sin_btn_function)
        self.pushButton_3.clicked.connect(self.cos_btn_function)
        self.pushButton_4.clicked.connect(self.tan_btn_function)
        self.pushButton_5.clicked.connect(self.csc_btn_function)
        self.pushButton_6.clicked.connect(self.sec_btn_function)
        self.pushButton_7.clicked.connect(self.cot_btn_function)

        self.pushButton.clicked.connect(self.back_button)
        




    def back_button(self):
        print("Back Button Pressed")
        self.call_window = NinePage()
        widget.addWidget(self.call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def sin_btn_function(self):
        if self.trig_values['sin'] != "None":
            self.call_window = NineGraphPlot(self.trig_values['sin'], "sin")
            widget.addWidget(self.call_window)
            widget.setCurrentIndex(widget.currentIndex() + 1)
        else:
            msg = QMessageBox(self)
            msg.setWindowTitle("Choose Option")
            msg.setText("Select an option:")


            theta_btn = msg.addButton("Theta", QMessageBox.AcceptRole)
            value_btn = msg.addButton("Value", QMessageBox.AcceptRole)
            msg.exec_()


            option = "Theta" if msg.clickedButton() == theta_btn else "Value"


            if option == "Theta":
                data, ok = QInputDialog.getText(self, "Enter the Theta", "Enter the Value:")
                if ok:
                    print(f"Theta: {data}")
                    self.call_window = NineGraphPlot(math.sin(math.radians(float(data))), "sin")
                    widget.addWidget(self.call_window)
                    widget.setCurrentIndex(widget.currentIndex() + 1)
            elif option == "Value":
                while True:
                    data, ok = QInputDialog.getText(self, "Enter Value", "Enter the Value (between -1 and 1):")
                    if ok:
                        try:
                            value = float(data)
                            if -1 <= value <= 1:
                                print(f"Value: {value}")
                                self.call_window = NineGraphPlot(value, "sin")
                                widget.addWidget(self.call_window)
                                widget.setCurrentIndex(widget.currentIndex() + 1)
                                break
                            else:
                                print("Invalid input. Please enter a value between -1 and 1.")
                        except Exception as e:
                            print(f"Error : {e}")
                    else:
                        break

    def cos_btn_function(self):
        if self.trig_values['cos'] != "None":
            self.call_window = NineGraphPlot(self.trig_values['cos'], "cos")
            widget.addWidget(self.call_window)
            widget.setCurrentIndex(widget.currentIndex() + 1)
        else:
            msg = QMessageBox(self)
            msg.setWindowTitle("Choose Option")
            msg.setText("Select an option:")

            theta_btn = msg.addButton("Theta", QMessageBox.AcceptRole)
            value_btn = msg.addButton("Value", QMessageBox.AcceptRole)
            msg.exec_()

            option = "Theta" if msg.clickedButton() == theta_btn else "Value"

            if option == "Theta":
                while True:  # Loop until a valid theta is provided
                    data, ok = QInputDialog.getText(self, "Enter the Theta", "Enter the Value:")
                    if ok:
                        try:
                            theta = float(data)
                            print(f"Valid Theta: {theta}")
                            self.call_window = NineGraphPlot(math.cos(math.radians(theta)), "cos")
                            widget.addWidget(self.call_window)
                            widget.setCurrentIndex(widget.currentIndex() + 1)
                            break  # Exit the loop on valid Theta
                        except Exception as e:
                            print(f"Error: {e}")
                    else:
                        break
            elif option == "Value":
                data, ok = QInputDialog.getText(self, "Enter Value", "Enter the Value:")
                if ok:
                    try:
                        value = float(data)
                        print(f"Value: {value}")
                        self.call_window = NineGraphPlot(value, "cos")
                        widget.addWidget(self.call_window)
                        widget.setCurrentIndex(widget.currentIndex() + 1)
                    except Exception as e:
                        print(f"Error: {e}")

    def tan_btn_function(self):
        if self.trig_values['tan'] != "None":
            self.call_window = NineGraphPlot(self.trig_values['tan'], "tan")
            widget.addWidget(self.call_window)
            widget.setCurrentIndex(widget.currentIndex() + 1)
        else:
            msg = QMessageBox(self)
            msg.setWindowTitle("Choose Option")
            msg.setText("Select an option:")

            theta_btn = msg.addButton("Theta", QMessageBox.AcceptRole)
            value_btn = msg.addButton("Value", QMessageBox.AcceptRole)
            msg.exec_()

            option = "Theta" if msg.clickedButton() == theta_btn else "Value"

            if option == "Theta":
                while True:
                    data, ok = QInputDialog.getText(self, "Enter the Theta", "Enter the Value:")
                    if ok:
                        try:
                            theta = float(data)
                            if theta % 90 == 0 and theta % 180 != 0:
                                print("Invalid Theta for tan function. Please enter a non-multiple of 90.")
                            else:
                                print(f"Valid Theta: {theta}")
                                self.call_window = NineGraphPlot(math.tan(math.radians(theta)), "tan")
                                widget.addWidget(self.call_window)
                                widget.setCurrentIndex(widget.currentIndex() + 1)
                                break
                        except Exception as e:
                            print(f"Error: {e}")
                    else:
                        break
            elif option == "Value":
                data, ok = QInputDialog.getText(self, "Enter Value", "Enter the Value:")
                if ok:
                    try:
                        value = float(data)
                        print(f"Value: {value}")
                        self.call_window = NineGraphPlot(value, "tan")
                        widget.addWidget(self.call_window)
                        widget.setCurrentIndex(widget.currentIndex() + 1)
                    except Exception as e:
                        print(f"Error: {e}")

    def csc_btn_function(self):
        if self.trig_values['csc'] != "None":
            self.call_window = NineGraphPlot(self.trig_values['csc'], "csc")
            widget.addWidget(self.call_window)
            widget.setCurrentIndex(widget.currentIndex() + 1)
        else:
            msg = QMessageBox(self)
            msg.setWindowTitle("Choose Option")
            msg.setText("Select an option:")

            theta_btn = msg.addButton("Theta", QMessageBox.AcceptRole)
            value_btn = msg.addButton("Value", QMessageBox.AcceptRole)
            msg.exec_()

            option = "Theta" if msg.clickedButton() == theta_btn else "Value"

            if option == "Theta":
                while True:
                    data, ok = QInputDialog.getText(self, "Enter the Theta", "Enter the Value:")
                    if ok:
                        try:
                            theta = float(data)
                            if theta % 180 == 0:
                                print("Invalid Theta for csc function. Please enter a non-multiple of 180.")
                            else:
                                print(f"Valid Theta: {theta}")
                                self.call_window = NineGraphPlot(1 / math.sin(math.radians(theta)), "csc")
                                widget.addWidget(self.call_window)
                                widget.setCurrentIndex(widget.currentIndex() + 1)
                                break
                        except Exception as e:
                            print(f"Error: {e}")
                    else:
                        break
            elif option == "Value":
                while True:
                    data, ok = QInputDialog.getText(self, "Enter Value", "Enter any value except 0:")
                    if ok:
                        try:
                            value = float(data)
                            if value != 0:
                                print(f"Value: {value}")
                                self.call_window = NineGraphPlot(value, "csc")
                                widget.addWidget(self.call_window)
                                widget.setCurrentIndex(widget.currentIndex() + 1)
                                break
                            else:
                                print("Invalid input. Value cannot be zero for csc.")
                        except Exception as e:
                            print(f"Error: {e}")
                    else:
                        break

    def sec_btn_function(self):
        if self.trig_values['sec'] != "None":
            self.call_window = NineGraphPlot(self.trig_values['sec'], "sec")
            widget.addWidget(self.call_window)
            widget.setCurrentIndex(widget.currentIndex() + 1)
        else:
            msg = QMessageBox(self)
            msg.setWindowTitle("Choose Option")
            msg.setText("Select an option:")

            theta_btn = msg.addButton("Theta", QMessageBox.AcceptRole)
            value_btn = msg.addButton("Value", QMessageBox.AcceptRole)
            msg.exec_()

            option = "Theta" if msg.clickedButton() == theta_btn else "Value"

            if option == "Theta":
                while True:
                    data, ok = QInputDialog.getText(self, "Enter the Theta", "Enter the Value:")
                    if ok:
                        try:
                            theta = float(data)
                            if theta % 90 == 0 and theta % 180 != 0:
                                print("Invalid Theta for sec function. Please enter a non-multiple of 90.")
                            else:
                                print(f"Valid Theta: {theta}")
                                self.call_window = NineGraphPlot(1 / math.cos(math.radians(theta)), "sec")
                                widget.addWidget(self.call_window)
                                widget.setCurrentIndex(widget.currentIndex() + 1)
                                break
                        except Exception as e:
                            print(f"Error: {e}")
                    else:
                        break
            elif option == "Value":
                data, ok = QInputDialog.getText(self, "Enter Value", "Enter the Value:")
                if ok:
                    try:
                        value = float(data)
                        print(f"Value: {value}")
                        self.call_window = NineGraphPlot(value, "sec")
                        widget.addWidget(self.call_window)
                        widget.setCurrentIndex(widget.currentIndex() + 1)
                    except Exception as e:
                        print(f"Error: {e}")

    def cot_btn_function(self):
        if self.trig_values['cot'] != "None":
            self.call_window = NineGraphPlot(self.trig_values['cot'], "cot")
            widget.addWidget(self.call_window)
            widget.setCurrentIndex(widget.currentIndex() + 1)
        else:
            msg = QMessageBox(self)
            msg.setWindowTitle("Choose Option")
            msg.setText("Select an option:")

            theta_btn = msg.addButton("Theta", QMessageBox.AcceptRole)
            value_btn = msg.addButton("Value", QMessageBox.AcceptRole)
            msg.exec_()

            option = "Theta" if msg.clickedButton() == theta_btn else "Value"

            if option == "Theta":
                while True:
                    data, ok = QInputDialog.getText(self, "Enter the Theta", "Enter the Value:")
                    if ok:
                        try:
                            theta = float(data)
                            if theta % 180 == 0:
                                print("Invalid Theta for cot function. Please enter a non-multiple of 180.")
                            else:
                                print(f"Valid Theta: {theta}")
                                self.call_window = NineGraphPlot(1 / math.tan(math.radians(theta)), "cot")
                                widget.addWidget(self.call_window)
                                widget.setCurrentIndex(widget.currentIndex() + 1)
                                break
                        except Exception as e:
                            print(f"Error: {e}")
                    else:
                        break
            elif option == "Value":
                data, ok = QInputDialog.getText(self, "Enter Value", "Enter the Value:")
                if ok:
                    try:
                        value = float(data)
                        print(f"Value: {value}")
                        self.call_window = NineGraphPlot(value, "cot")
                        widget.addWidget(self.call_window)
                        widget.setCurrentIndex(widget.currentIndex() + 1)
                    except Exception as e:
                        print(f"Error: {e}")


from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import math
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from PyQt5.uic import loadUi


import matplotlib.pyplot as plt
import numpy as np
import math
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget

class NineGraphPlot(QMainWindow):
    def __init__(self, value, trig_type):
        super().__init__()
        loadUi("physics_p9_g_ii.ui", self)  # Assuming you have loaded the UI
        self.widget = QWidget(self)
        self.widget.setGeometry(110, 80, 761, 381)

        self.theta=self.calculate_inverse_trig(trig_type,value)
        print(self.theta,type(self.theta))

        if trig_type == "sin":
            self.sin_plot(self.theta)
        elif trig_type == "cos":
            self.cos_plot(self.theta)
        elif trig_type == "tan":
            self.tan_plot(self.theta)
        elif trig_type == "cot":
            self.cot_plot(self.theta)
        elif trig_type == "sec":
            self.sec_plot(self.theta)
        elif trig_type == "csc":
            self.csc_plot(self.theta)
        else:
            print("Invalid trigonometric function. Please use 'sin', 'cos', 'tan', 'cot', 'sec', or 'csc'.")

    def calculate_inverse_trig(self, trig_type, value):
        if trig_type == "sin":
            return math.degrees(math.asin(value))
        elif trig_type == "cos":
            return math.degrees(math.acos(value))
        elif trig_type == "tan":
            return math.degrees(math.atan(value))
        elif trig_type == "csc":
            if value == 0:
                raise ValueError("Cosecant value cannot be zero.")
            return math.degrees(math.asin(1 / value))
        elif trig_type == "sec":
            if value == 0:
                raise ValueError("Secant value cannot be zero.")
            return math.degrees(math.acos(1 / value))
        elif trig_type == "cot":
            if value == 0:
                raise ValueError("Cotangent value cannot be zero.")
            return math.degrees(math.atan(1 / value))
        else:
            raise ValueError(f"Invalid trigonometric type: {trig_type}")

    def sin_plot(self, theta):
        """Plot the sine function."""
        x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
        y_val = [math.sin(i) for i in x]
        sin_val = math.sin(math.radians(theta))

        plt.plot(x, y_val, color="red", label=f"sin(⊖)", linewidth=1.2)
        plt.scatter(math.radians(theta), sin_val, color="blue", label=f"sin(⊖)={sin_val:.2f} \n ⊖={theta}°")
        plt.axvline(math.radians(theta), color="orange", linestyle="--")
        plt.axhline(0, color="black", linewidth=0.8)
        plt.axvline(0, color="black", linewidth=0.8)
        plt.grid(True)
        plt.legend()
        plt.title("Sine Function")
        plt.savefig(f"physics_p9_sin.png", transparent=True)
        plt.close()
        print(f"sin(⊖) for ⊖={theta}° = {sin_val:.2f}")

    def cos_plot(self, theta):
        """Plot the cosine function."""
        x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
        y_val = [math.cos(i) for i in x]
        cos_val = math.cos(math.radians(theta))

        plt.plot(x, y_val, color="green", label=f"cos(⊖)", linewidth=1.2)
        plt.scatter(math.radians(theta), cos_val, color="blue", label=f"cos(⊖)={cos_val:.2f} \n ⊖={theta}°")
        plt.axvline(math.radians(theta), color="orange", linestyle="--")
        plt.axhline(0, color="black", linewidth=0.8)
        plt.axvline(0, color="black", linewidth=0.8)
        plt.grid(True)
        plt.legend()
        plt.title("Cosine Function")
        plt.savefig(f"physics_p9_cos.png", transparent=True)
        plt.close()
        print(f"cos(⊖) for ⊖={theta}° = {cos_val:.2f}")

    def tan_plot(self, theta):
        """Plot the tangent function."""
        x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
        y_val = [math.tan(i) if abs(math.tan(i)) < 10 else None for i in x]
        tan_val = math.tan(math.radians(theta)) if abs(math.tan(math.radians(theta))) < 10 else None

        plt.plot(x, y_val, color="blue", label=f"tan(⊖)", linewidth=1.2)
        if tan_val is not None:
            plt.scatter(math.radians(theta), tan_val, color="red", label=f"tan(⊖)={tan_val:.2f} \n ⊖={theta}°")
        plt.axvline(math.radians(theta), color="orange", linestyle="--")
        plt.axhline(0, color="black", linewidth=0.8)
        plt.axvline(0, color="black", linewidth=0.8)
        plt.grid(True)
        plt.legend()
        plt.title("Tangent Function")
        plt.savefig(f"physics_p9_tan.png", transparent=True)
        plt.close()
        print(f"tan(⊖) for ⊖={theta}° = {tan_val:.2f}" if tan_val else f"tan(⊖) for ⊖={theta}° is undefined")

    def csc_plot(self, theta):
        """Plot the cosecant function."""
        x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
        y_val = [1 / math.sin(i) if math.sin(i) != 0 and abs(1 / math.sin(i)) < 10 else None for i in x]
        csc_val = 1 / math.sin(math.radians(theta)) if math.sin(math.radians(theta)) != 0 else None

        plt.plot(x, y_val, color="cyan", label=f"csc(⊖)", linewidth=1.2)
        if csc_val is not None:
            plt.scatter(math.radians(theta), csc_val, color="blue", label=f"csc(⊖)={csc_val:.2f} \n ⊖={theta}°")
        plt.axvline(math.radians(theta), color="orange", linestyle="--")
        plt.axhline(0, color="black", linewidth=0.8)
        plt.axvline(0, color="black", linewidth=0.8)
        plt.grid(True)
        plt.legend()
        plt.title("Cosecant Function")
        plt.savefig(f"physics_p9_csc.png", transparent=True)
        plt.close()
        print(f"csc(⊖) for ⊖={theta}° = {csc_val:.2f}" if csc_val else f"csc(⊖) for ⊖={theta}° is undefined")

    def sec_plot(self, theta):
        """Plot the secant function."""
        x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
        y_val = [1 / math.cos(i) if math.cos(i) != 0 and abs(1 / math.cos(i)) < 10 else None for i in x]
        sec_val = 1 / math.cos(math.radians(theta)) if math.cos(math.radians(theta)) != 0 else None

        plt.plot(x, y_val, color="orange", label=f"sec(⊖)", linewidth=1.2)
        if sec_val is not None:
            plt.scatter(math.radians(theta), sec_val, color="blue", label=f"sec(⊖)={sec_val:.2f} \n ⊖={theta}°")
        plt.axvline(math.radians(theta), color="orange", linestyle="--")
        plt.axhline(0, color="black", linewidth=0.8)
        plt.axvline(0, color="black", linewidth=0.8)
        plt.grid(True)
        plt.legend()
        plt.title("Secant Function")
        plt.savefig(f"physics_p9_sec.png", transparent=True)
        plt.close()
        print(f"sec(⊖) for ⊖={theta}° = {sec_val:.2f}" if sec_val else f"sec(⊖) for ⊖={theta}° is undefined")

    def cot_plot(self, theta):
        """Plot the cotangent function."""
        x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
        y_val = [1 / math.tan(i) if math.tan(i) != 0 and abs(1 / math.tan(i)) < 10 else None for i in x]
        cot_val = 1 / math.tan(math.radians(theta)) if math.tan(math.radians(theta)) != 0 else None

        plt.plot(x, y_val, color="purple", label=f"cot(⊖)", linewidth=1.2)
        if cot_val is not None:
            plt.scatter(math.radians(theta), cot_val, color="blue", label=f"cot(⊖)={cot_val:.2f} \n ⊖={theta}°")
        plt.axvline(math.radians(theta), color="orange", linestyle="--")
        plt.axhline(0, color="black", linewidth=0.8)
        plt.axvline(0, color="black", linewidth=0.8)
        plt.grid(True)
        plt.legend()
        plt.title("Cotangent Function")
        plt.savefig(f"physics_p9_cot.png", transparent=True)
        plt.close()
        print(f"cot(⊖) for ⊖={theta}° = {cot_val:.2f}" if cot_val else f"cot(⊖) for ⊖={theta}° is undefined")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QStackedWidget()
    main_wind = NinePage()
    widget.addWidget(main_wind)
    widget.setFixedSize(main_wind.size())
    widget.show()
    sys.exit(app.exec())

