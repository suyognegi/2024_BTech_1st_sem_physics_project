import sys
from sympy import symbols,Eq,solve
import vlc
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QComboBox, QLabel, QPushButton, QMessageBox, \
    QInputDialog
from PyQt5.uic import loadUi
from decimal import Decimal, getcontext, InvalidOperation
import math

from PyQt5.uic.properties import QtCore
from sympy import symbols, Eq , solve
#
# # Set precision to 12 decimal places
# getcontext().prec = 12
#

class FirstPage(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("physics_p1.ui", self)
        self.pushButton.clicked.connect(self.button_clicked)

    def button_clicked(self):
        print("Button clicked successfully!")
        self.call_create_window = SecondPage()
        widget.addWidget(self.call_create_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class SecondPage(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("physics_p2.ui",self)

        #pushButton
        self.pushButton.clicked.connect(self.Quadratic_Root)
        #pushButton_4
        self.pushButton_4.clicked.connect(self.Linear_Eq_in_2_Var)
        #pushButton_5
        self.pushButton_5.clicked.connect(self.laurenz)
        #pushButton_10
        self.pushButton_10.clicked.connect(self.time_dialation)
        #pushButton_9
        self.pushButton_9.clicked.connect(self.Linear_Eq_in_3_Var)
        #pushButton_3
        self.pushButton_3.clicked.connect(self.Two_Eq_graph)
        #pushButton_6
        self.pushButton_6.clicked.connect(self.Trigno)

        #HOME
        self.pushButton_8.clicked.connect(self.home)

    def home(self):
        print("Home Button SecondPage")
        self.home_window=FirstPage()
        widget.addWidget(self.home_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Trigno(self):
        print("Trignometry Button clicked i.e. pushButton_6")
        self.call_create_window = NinePage()
        widget.addWidget(self.call_create_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def Quadratic_Root(self):
        print("Quadratic Root Button Clicked i.e. pushButton")
        self.call_create_window = ThirdPage()
        widget.addWidget(self.call_create_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def Linear_Eq_in_2_Var(self):
        print("Linear Equation in 2 Variable Button Clicked i.e. pushButton_4")
        self.call_create_window = ForthPage()
        widget.addWidget(self.call_create_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def laurenz(self):
        print("Laurenz Button Clicked i.e. pushButton_5")
        self.call_create_window = SixthPageOne()
        widget.addWidget(self.call_create_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def time_dialation(self):
        print("Time Dialation Button Clicked i.e. pushButton_10")
        self.call_create_window = FifthPageOne()
        widget.addWidget(self.call_create_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Linear_Eq_in_3_Var(self):
        print("Linear Equation in 3 variable i.e. pushButton_9")
        self.call_create_window = SeventhPage()
        widget.addWidget(self.call_create_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Two_Eq_graph(self):
        print("2 Equation Graph i.e. pushButton_3")
        self.call_create_window=EightPage()
        widget.addWidget(self.call_create_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class ThirdPage(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("physics_p3.ui", self)


        self.lineEdit.textChanged.connect(self.lineEdit_text_changed)
        self.lineEdit_5.textChanged.connect(self.lineEdit_5_text_changed)
        self.lineEdit_3.textChanged.connect(self.lineEdit_6_text_changed)
        self.lineEdit_6.textChanged.connect(self.lineEdit_3_text_changed)
        self.lineEdit_7.textChanged.connect(self.lineEdit_4_text_changed)
        self.lineEdit_4.textChanged.connect(self.lineEdit_7_text_changed)

        self.pushButton.clicked.connect(self.push_button_clicked)

        # HOME
        self.pushButton_8.clicked.connect(self.home)

    def home(self):
        print("Home Button ThirdPage")
        self.home_window = FirstPage()
        widget.addWidget(self.home_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def lineEdit_text_changed(self):
        self.lineEdit_5.setText(self.lineEdit.text())

    def lineEdit_5_text_changed(self):
        self.lineEdit.setText(self.lineEdit_5.text())

    def lineEdit_6_text_changed(self):
        self.lineEdit_6.setText(self.lineEdit_3.text())

    def lineEdit_3_text_changed(self):
        self.lineEdit_3.setText(self.lineEdit_6.text())

    def lineEdit_7_text_changed(self):
        self.lineEdit_7.setText(self.lineEdit_4.text())

    def lineEdit_4_text_changed(self):
        self.lineEdit_4.setText(self.lineEdit_7.text())


    def push_button_clicked(self):


        # Retrieve the values from the combo boxes
        first_symbol = self.findChild(QComboBox, 'comboBox').currentText()
        second_symbol = self.findChild(QComboBox, 'comboBox_2').currentText()
        third_symbol = self.findChild(QComboBox, 'comboBox_3').currentText()

        print(f"first symbol = {first_symbol}\nsecond symbol = {second_symbol}\nthird symbol = {third_symbol}")


        a = b = c = None

        a = float(self.lineEdit.text())
        b = float(self.lineEdit_3.text())
        c = float(self.lineEdit_4.text())



        if first_symbol != '+':
            a = -1 * a
        if second_symbol != '+':
            b = -1 * b
        if third_symbol != '+':
            c = -1 * c

        print(a, b, c)

        from sympy import symbols, solve

        x = symbols("x")


        quad_eq = a * x ** 2 + b * x + c


        ans = solve(quad_eq, x)


        print(ans[0], ans[1])


        self.call_create_window = ThirdPageOutput(ans[0], ans[1],quad_eq)
        widget.addWidget(self.call_create_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class ThirdPageOutput(QMainWindow):
    def __init__(self, x1, x2, quad_eq):
        super().__init__()
        loadUi("physics_p3_ii.ui", self)

        # Set the text for the labels with the roots
        self.label_5.setText(str(round(x1, 8)))
        self.label_7.setText(str(round(x2, 8)))

        self.pushButton_2.clicked.connect(self.back)
        self.pushButton_4.clicked.connect(lambda: self.view_graph(quad_eq))

        print(quad_eq)

        # HOME
        self.pushButton_8.clicked.connect(self.home)

    def home(self):
        print("Home Button SecondPage 2")
        self.home_window = FirstPage()
        widget.addWidget(self.home_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def view_graph(self, quad_eq):
        # Pass the quadratic equation to ThirdPageGraph
        self.call_window = ThirdPageGraph(quad_eq)
        widget.addWidget(self.call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def back(self):
        # Open the previous window
        self.call_window = ThirdPage()
        widget.addWidget(self.call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)


import numpy as np
import sympy as sp
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from PyQt5.uic import loadUi

class ThirdPageGraph(QMainWindow):
    def __init__(self, quad_eq):
        super().__init__()
        loadUi("physics_p3_iii.ui", self)

        # Create the widget to hold the graph
        self.widget = QWidget(self)
        self.widget.setGeometry(110, 80, 751, 381)

        # Add canvas for graph plotting
        self.canvas = FigureCanvas(plt.figure())

        # Create layout to hold the canvas
        layout = QVBoxLayout(self.widget)
        layout.addWidget(self.canvas)

        # Plot the graph using the provided quadratic equation
        self.plot_graph(quad_eq)

        self.pushButton_2.clicked.connect(self.back)

        # HOME
        self.pushButton_8.clicked.connect(self.home)

    def home(self):
        print("Home Button SecondPage 3")
        self.home_window = FirstPage()
        widget.addWidget(self.home_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def back(self):
        self.call_window = FirstPage()
        widget.addWidget(self.call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def plot_graph(self, quad_eq):
        ax = self.canvas.figure.add_subplot(111)

        # Generate x values for plotting
        x_vals = np.linspace(-50, 50, 40)

        # Convert the sympy equation to a numerical function
        x = sp.symbols('x')
        func = sp.lambdify(x, quad_eq, modules=['numpy'])

        # Compute the y values for the quadratic function
        y_vals = func(x_vals)

        # Clear previous plots
        ax.clear()
        self.beautiful_quad_eq=quad_eq


        # Plot the quadratic function
        ax.plot(x_vals, y_vals, label=f'y = {quad_eq}', color='#c7053d')

        # Fill the area under the curve with a light shade
        ax.fill_between(x_vals, y_vals, where=(y_vals >= 0), interpolate=True, color='#FFCC00', alpha=0.3)

        # Find the intersection points (roots)
        roots = sp.solve(quad_eq, x)

        # Initialize the intersection text
        intersection_text = "Intersections:\n"

        # Plot the intersection points and add to the text box content
        for root in roots:
            if root.is_real:  # Only consider real roots
                x_root = float(root)
                y_root = float(func(x_root))
                ax.plot(x_root, y_root, 'ro')  # Plot the root as a red point
                intersection_text += f'({x_root:.2f}, {y_root:.2f})\n'  # Add to the text box content

        # Display the intersection points in a text box at the bottom-left corner
        ax.text(
            -50, min(y_vals) - 10,  # Position near bottom-left corner
            intersection_text,
            fontsize=10,
            color='black',
            bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5')  # Add a box around the text
        )

        # Add x=0 and y=0 axis lines (centralized axes)
        ax.axhline(0, color='black', linewidth=1)
        ax.axvline(0, color='black', linewidth=1)

        # Set the graph limits to zoom out
        ax.set_xlim(-50, 50)
        y_max = np.max(y_vals) + 10  # Add a buffer for y-axis limits
        ax.set_ylim(min(y_vals) - 10, y_max)

        # Add grid, labels, title, and legend
        ax.grid(True)
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.set_title('Quadratic Equation Graph with Shaded Area and Roots')
        ax.legend()

        # Refresh the canvas to display the updated plot
        self.canvas.draw()


class ForthPage(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("physics_p4.ui",self)

        self.lineEdit.setPlaceholderText("α")
        self.lineEdit_3.setPlaceholderText("β")
        self.lineEdit_2.setPlaceholderText("γ")
        self.lineEdit_6.setPlaceholderText("δ")
        self.lineEdit_4.setPlaceholderText("c1")
        self.lineEdit_5.setPlaceholderText("c2")

        self.lineEdit.textChanged.connect(self.lineEdit_text_changed)
        self.lineEdit_7.textChanged.connect(self.lineEdit_7_text_changed)

        self.lineEdit_3.textChanged.connect(self.lineEdit_3_text_changed)
        self.lineEdit_8.textChanged.connect(self.lineEdit_8_text_changed)

        self.lineEdit_4.textChanged.connect(self.lineEdit_4_text_changed)
        self.lineEdit_9.textChanged.connect(self.lineEdit_9_text_changed)

        self.lineEdit_2.textChanged.connect(self.lineEdit_2_text_changed)
        self.lineEdit_11.textChanged.connect(self.lineEdit_11_text_changed)

        self.lineEdit_6.textChanged.connect(self.lineEdit_6_text_changed)
        self.lineEdit_10.textChanged.connect(self.lineEdit_10_text_changed)

        self.lineEdit_5.textChanged.connect(self.lineEdit_5_text_changed)
        self.lineEdit_12.textChanged.connect(self.lineEdit_12_text_changed)


        self.pushButton.clicked.connect(self.button_function)

        # HOME
        self.pushButton_8.clicked.connect(self.home)

    def home(self):
        print("Home Button ForthPage")
        self.home_window = FirstPage()
        widget.addWidget(self.home_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def lineEdit_text_changed(self):
        self.lineEdit_7.setText(self.lineEdit.text())

    def lineEdit_7_text_changed(self):
        self.lineEdit.setText(self.lineEdit_7.text())

    def lineEdit_3_text_changed(self):
        self.lineEdit_8.setText(self.lineEdit_3.text())

    def lineEdit_8_text_changed(self):
        self.lineEdit_3.setText(self.lineEdit_8.text())

    def lineEdit_4_text_changed(self):
        self.lineEdit_9.setText(self.lineEdit_4.text())

    def lineEdit_9_text_changed(self):
        self.lineEdit_4.setText(self.lineEdit_9.text())

    def lineEdit_2_text_changed(self):
        self.lineEdit_11.setText(self.lineEdit_2.text())

    def lineEdit_11_text_changed(self):
        self.lineEdit_2.setText(self.lineEdit_11.text())

    def lineEdit_6_text_changed(self):
        self.lineEdit_10.setText(self.lineEdit_6.text())

    def lineEdit_10_text_changed(self):
        self.lineEdit_6.setText(self.lineEdit_10.text())

    def lineEdit_5_text_changed(self):
        self.lineEdit_12.setText(self.lineEdit_5.text())

    def lineEdit_12_text_changed(self):
        self.lineEdit_5.setText(self.lineEdit_12.text())

    def button_function(self):
        from sympy import symbols, Eq, solve  # Import necessary modules from sympy

        # Declare symbols for x and y
        x, y = symbols("x y")

        # Retrieve the symbols (+ or -) from the combo boxes
        x1_symbol = self.findChild(QComboBox, 'comboBox').currentText()  # For x in eq1
        y1_symbol = self.findChild(QComboBox, 'comboBox_2').currentText()  # For y in eq1
        c1_symbol = self.findChild(QComboBox, 'comboBox_3').currentText()  # For constant in eq1

        x2_symbol = self.findChild(QComboBox, 'comboBox_4').currentText()  # For x in eq2
        y2_symbol = self.findChild(QComboBox, 'comboBox_5').currentText()  # For y in eq2
        c2_symbol = self.findChild(QComboBox, 'comboBox_6').currentText()  # For constant in eq2

        # Get coefficients and constants from the input fields, applying correct signs
        try:
            # Apply the + or - symbol from the combo boxes
            a = float(self.lineEdit.text()) if x1_symbol == '+' else -float(self.lineEdit.text())
            b = float(self.lineEdit_3.text()) if y1_symbol == '+' else -float(self.lineEdit_3.text())
            e = float(self.lineEdit_4.text()) if c1_symbol == '+' else -float(self.lineEdit_4.text())

            c = float(self.lineEdit_2.text()) if x2_symbol == '+' else -float(self.lineEdit_2.text())
            d = float(self.lineEdit_6.text()) if y2_symbol == '+' else -float(self.lineEdit_6.text())
            f = float(self.lineEdit_5.text()) if c2_symbol == '+' else -float(self.lineEdit_5.text())
        except ValueError:
            print("Please enter valid numbers.")
            return

        # Set up the equations using sympy
        eq1 = Eq(a * x + b * y, e)
        eq2 = Eq(c * x + d * y, f)

        # Solve the system of equations
        sol = solve((eq1, eq2), (x, y))

        # Handle cases where no solutions are found
        if not sol:
            print("No solution found or infinite solutions.")
            return

        # Print the solutions
        print(f"Solution for x: {sol[x]}, Solution for y: {sol[y]}")

        # Round the solutions to 9 decimal places
        x_solution = round(float(sol[x]), 9)
        y_solution = round(float(sol[y]), 9)

        # Pass the solutions to the next window/page
        self.call_window_variable = ForthPageOutput(x_solution, y_solution,eq1,eq2)
        widget.addWidget(self.call_window_variable)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class ForthPageOutput(QMainWindow):
    def __init__(self,a,b,eq1,eq2):
        super().__init__()
        loadUi("physics_p4_ii.ui", self)
        print(a,b)
        self.label_6.setText(str(a))  # Uncomment to show the solution
        self.label_7.setText(str(b))

        self.pushButton_8.clicked.connect(self.home_button_function)
        self.pushButton_2.clicked.connect(self.back_button_clicked)
        self.pushButton_4.clicked.connect(self.graph)

        self.eq1=eq1
        self.eq2=eq2


    def home_button_function(self):
        print("Home ForthPage 2")
        # Avoid creating a new instance of FirstPage if already there
        if not hasattr(self, 'first_page_instance'):
            self.first_page_instance = FirstPage()
        widget.addWidget(self.first_page_instance)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def back_button_clicked(self):
        print("Back Button Clicked !!")
        # Avoid creating a new instance of ForthPage if already there
        if not hasattr(self, 'forth_page_instance'):
            self.forth_page_instance = ForthPage()  # Ensure ForthPage is defined
        widget.addWidget(self.forth_page_instance)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def graph(self):
        self.call_window=ForthPageGraph(self.eq1,self.eq2)
        widget.addWidget(self.call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from PyQt5.uic import loadUi
from sympy.solvers import solve

class ForthPageGraph(QMainWindow):
    def __init__(self, eq1, eq2):
        super().__init__()
        loadUi("physics_p4_iii.ui", self)

        # Create the widget to hold the graph
        self.widget = QWidget(self)
        self.widget.setGeometry(110, 100, 761, 381)

        # Add canvas for graph plotting
        self.canvas = FigureCanvas(plt.figure())

        # Create layout to hold the canvas
        layout = QVBoxLayout(self.widget)
        layout.addWidget(self.canvas)

        # Plot the graph using the provided equations
        self.plot_graph(eq1, eq2)

        self.pushButton_2.clicked.connect(self.home)

        # HOME
        self.pushButton_8.clicked.connect(self.home)

    def home(self):
        print("Home Button ForthPage 3")
        self.home_window = FirstPage()
        widget.addWidget(self.home_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)


    def home(self):
        self.call_window = FirstPage()  # Assuming FirstPage is defined elsewhere
        widget.addWidget(self.call_window)  # Assuming 'widget' is a QStackedWidget
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def plot_graph(self, eq1, eq2):
        ax = self.canvas.figure.add_subplot(111)

        # Generate x values for plotting
        x_vals = np.linspace(-50, 50, 400)

        # Extract coefficients from the equations
        a1, b1, c1 = eq1.lhs.as_coefficients_dict().get(sp.symbols('x')), eq1.lhs.as_coefficients_dict().get(
            sp.symbols('y')), eq1.rhs
        a2, b2, c2 = eq2.lhs.as_coefficients_dict().get(sp.symbols('x')), eq2.lhs.as_coefficients_dict().get(
            sp.symbols('y')), eq2.rhs

        # Create functions for y values
        func1 = lambda x: (c1 - a1 * x) / b1 if b1 != 0 else None
        func2 = lambda x: (c2 - a2 * x) / b2 if b2 != 0 else None

        # Compute the y values for each equation
        y_vals_eq1 = func1(x_vals)
        y_vals_eq2 = func2(x_vals)

        # Clear previous plots
        ax.clear()

        # Format the equation labels
        label_eq1 = self.format_equation(a1, b1, c1)
        label_eq2 = self.format_equation(a2, b2, c2)

        # Plot the equations
        ax.plot(x_vals, y_vals_eq1, label=label_eq1, color='blue')
        ax.plot(x_vals, y_vals_eq2, label=label_eq2, color='orange')

        # Find the intersection points (roots)
        sol = solve((eq1, eq2), (sp.symbols('x'), sp.symbols('y')))

        # Plot the intersection point
        if sol:
            x_sol = float(sol[sp.symbols('x')])
            y_sol = float(sol[sp.symbols('y')])
            ax.plot(x_sol, y_sol, 'ro')  # Plot the root as a red point

            # Create a text box to display the values of x and y
            textstr = f'X: {x_sol:.2f}\nY: {y_sol:.2f}'
            # Create a bounding box around the text
            ax.text(-48, -48, textstr, fontsize=10,
                    bbox=dict(facecolor='white', alpha=0.5, edgecolor='black', boxstyle='round,pad=0.5'))

        # Add x=0 and y=0 axis lines (centralized axes)
        ax.axhline(0, color='black', linewidth=1)
        ax.axvline(0, color='black', linewidth=1)

        # Set the graph limits to zoom out
        ax.set_xlim(-50, 50)
        ax.set_ylim(-50, 50)

        # Add grid, labels, title, and legend
        ax.grid(True)
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        # ax.set_title('Graph of the Equations')
        ax.legend()

        # Refresh the canvas to display the updated plot
        self.canvas.draw()

    def format_equation(self, a, b, c):
        """Formats the equation in the form of '<>x + or - <>y = c'."""
        sign_y = '+' if b >= 0 else '-'
        formatted_a = abs(a) if a != 0 else ''
        formatted_b = abs(b) if b != 0 else ''

        equation_str = ''
        if formatted_a:
            equation_str += f'{formatted_a}x '
        if formatted_b:
            equation_str += f'{sign_y} {formatted_b}y '
        equation_str += f'= {c}'

        return equation_str.strip()


class FifthPageOne(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("physics_p5_i.ui", self)
        self.pushButton_2.clicked.connect(self.next)

        # HOME
        self.pushButton_8.clicked.connect(self.home)

    def home(self):
        print("Home Button ForthPage")
        self.home_window = FirstPage()
        widget.addWidget(self.home_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def next(self):
        print("Next Button Clicked !! 5th 1st")
        self.call_window = FifthPageTwo()
        widget.addWidget(self.call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class FifthPageTwo(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("physics_p5_ii.ui", self)
        self.pushButton_2.clicked.connect(self.next)
        self.pushButton_3.clicked.connect(self.back)  # Assuming pushButton_3 is for back

        # HOME
        self.pushButton_8.clicked.connect(self.home)

    def home(self):
        print("Home Button ForthPage")
        self.home_window = FirstPage()
        widget.addWidget(self.home_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def next(self):
        print("Next Button Clicked !! 5th 2nd")
        self.call_window = FifthPageThree()
        widget.addWidget(self.call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def back(self):
        print("Back Button Clicked !! 5th 2nd")
        self.call_window = FifthPageOne()
        widget.addWidget(self.call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class FifthPageThree(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("physics_p5_iii.ui", self)
        self.pushButton_2.clicked.connect(self.next)
        self.pushButton_3.clicked.connect(self.back)  # Assuming pushButton_3 is for back

        # HOME
        self.pushButton_8.clicked.connect(self.home)

    def home(self):
        print("Home Button ForthPage")
        self.home_window = FirstPage()
        widget.addWidget(self.home_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def next(self):
        print("Next Button Clicked !! 5th 3rd")
        self.call_window = FifthPageFour()
        widget.addWidget(self.call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def back(self):
        print("Back Button Clicked !! 5th 3rd")
        self.call_window = FifthPageTwo()
        widget.addWidget(self.call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class FifthPageFour(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("physics_p5_iv.ui", self)
        self.pushButton_2.clicked.connect(self.next)
        self.pushButton_3.clicked.connect(self.back)  # Assuming pushButton_3 is for back

        # HOME
        self.pushButton_8.clicked.connect(self.home)

    def home(self):
        print("Home Button ForthPage")
        self.home_window = FirstPage()
        widget.addWidget(self.home_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def next(self):
        print("Next Button Clicked !! 5th 4th")
        self.call_window= FifthPageVideo()
        widget.addWidget(self.call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def back(self):
        print("Back Button Clicked !! 5th 4th")
        self.call_window = FifthPageThree()
        widget.addWidget(self.call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)



from PyQt5.QtWidgets import QMainWindow, QLabel, QFrame
from PyQt5.QtGui import QMovie
from PyQt5 import QtCore
import vlc



class FifthPageVideo(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("physics_p5_video.ui", self)


        self.pushButton_2.clicked.connect(self.home)
        # Set up the animation (GIF) in a specified area
        self.animation_label = QLabel(self)
        # self.animation_label.setGeometry(125, 90, 711, 400)   # FINAL for vid.mp4
        self.animation_label.setGeometry(105, 90, 749, 389)    # FINAL for vid_2.mp4
        self.movie = QMovie("vid_2.mp4")  # Provide your GIF file here
        self.animation_label.setMovie(self.movie)
        self.movie.start()

        # Create a QFrame for VLC video playback in the same area
        self.video_frame = QFrame(self)
        #self.video_frame.setGeometry(125, 90, 711, 400)  # FINAL for vid.mp4
        self.video_frame.setGeometry(105, 90, 749, 389)   # FINAL for vid_2.mp4
        self.video_frame.show()

        # Start the video directly (no delay)
        QtCore.QTimer.singleShot(0, self.start_video)

        # HOME
        self.pushButton_8.clicked.connect(self.home)

    def home(self):
        print("Home Button ForthPage")
        self.home_window = FirstPage()
        widget.addWidget(self.home_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def start_video(self):
        # Stop the animation and hide the QLabel for GIF
        self.movie.stop()
        self.animation_label.hide()

        # Set up VLC video playback within the QFrame
        self.instance = vlc.Instance()
        self.mediaPlayer = self.instance.media_player_new()

        video_path = "vid_crop.mp4"  # Replace with your video file path

        if QtCore.QFile.exists(video_path):
            # Set the video output to the QFrame's winId() to control the display
            self.mediaPlayer.set_hwnd(int(self.video_frame.winId()))  # On Windows
            media = self.instance.media_new(video_path)
            self.mediaPlayer.set_media(media)

            # Connect the end-of-media event to the loop method
            self.mediaPlayer.event_manager().event_attach(vlc.EventType.MediaPlayerEndReached, self.loop_video)

            # Set video size to fill the frame
            self.mediaPlayer.video_set_scale(0)  # Use 0 to scale to fit the QFrame
            self.mediaPlayer.play()
        else:
            print(f"Error: Video file {video_path} not found.")

    def loop_video(self, event):
        """ Loop the video when it ends """
        self.mediaPlayer.stop()  # Stop the current playback
        self.mediaPlayer.play()  # Start the video again

    def home(self):
        self.call_window=FirstPage()
        widget.addWidget(self.call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)
class SixthPageOne(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("physics_p6_i.ui",self)
        self.pushButton_2.clicked.connect(self.next)
        # HOME
        self.pushButton_8.clicked.connect(self.home)

    def home(self):
        print("Home Button ForthPage")
        self.home_window = FirstPage()
        widget.addWidget(self.home_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def next(self):
        print("Next Button Clicked !! 6th Ist")
        self.call_window=SixthPageTwo()
        widget.addWidget(self.call_window)
        widget.setCurrentIndex(widget.currentIndex()+1)

class SixthPageTwo(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("physics_p6_ii.ui", self)

        self.pushButton_2.clicked.connect(self.next)
        self.pushButton_3.clicked.connect(self.back)
        # HOME
        self.pushButton_8.clicked.connect(self.home)

    def home(self):
        print("Home Button ForthPage")
        self.home_window = FirstPage()
        widget.addWidget(self.home_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def next(self):
        print("Next Button Clicked !! 6th 2nd")
        self.call_window = SixthPageThree()
        widget.addWidget(self.call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def back(self):
        print("Back Button Clicked !! 6th 2nd")
        self.call_window = SixthPageOne()
        widget.addWidget(self.call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class SixthPageThree(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("physics_p6_iii.ui", self)
        self.pushButton_2.clicked.connect(self.next)
        self.pushButton_3.clicked.connect(self.back)

        # HOME
        self.pushButton_8.clicked.connect(self.home)

    def home(self):
        print("Home Button ForthPage")
        self.home_window = FirstPage()
        widget.addWidget(self.home_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def next(self):
        print("Next Button Clicked !! 6th 3rd")
        self.call_window = SixthPageCalculation()
        widget.addWidget(self.call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def back(self):
        print("Back Button Clicked !! 6th 3rd")
        self.call_window=SixthPageTwo()
        widget.addWidget(self.call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class SixthPageCalculation(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("physics_p6_c_i.ui", self)

        # Connect the text and combo box changes to real-time conversion
        self.lineEdit_5.textChanged.connect(self.convert_button)
        self.comboBox.currentIndexChanged.connect(self.convert_button)
        self.comboBox_2.currentIndexChanged.connect(self.convert_button)
        self.pushButton_3.clicked.connect(self.back)

        # Speed of light in m/s
        self.c = Decimal("2.998e8")  # meters per second
        self.comboBox.raise_()
        self.comboBox_2.raise_()
        self.comboBox_3.raise_()
        self.comboBox_4.raise_()
        self.label_4.raise_()
        self.lineEdit_5.raise_()
        self.lineEdit_7.raise_()
        self.lineEdit_6.raise_()
        self.label_6.raise_()

        self.label_5.raise_()
        # Connect the combo box changes to the synchronization methods
        self.comboBox_3.currentIndexChanged.connect(self.same_box)
        self.comboBox_4.currentIndexChanged.connect(self.same_box2)
        self.pushButton_2.clicked.connect(self.solve_button_function)

        # HOME
        self.pushButton_8.clicked.connect(self.home)

    def home(self):
        print("Home Button ForthPage")
        self.home_window = FirstPage()
        widget.addWidget(self.home_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

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
                self.ans = math.sqrt(1 - self.ans)

                print("Back Button Clicked !!")
                self.call_window = SixthPageCalculationSolve(self.ans)
                widget.addWidget(self.call_window)
                widget.setCurrentIndex(widget.currentIndex() + 1)

        except ValueError:
            QMessageBox.critical(self, "Error", "Please enter valid numbers.")



    def back(self):
        print("Back Button Clicked !! 5th C")
        self.call_window = SixthPageThree()
        widget.addWidget(self.call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)
class SixthPageCalculationSolve(QMainWindow):
    def __init__(self, ans):
        super().__init__()
        loadUi("physics_p6_c_ii.ui", self)
        print(ans)
        self.ans=ans
        self.label_6.setText(f"{ans:.2f}")
        self.label_8.setText(f"{(ans*100):.2f}")
        self.pushButton_3.clicked.connect(self.back)
        self.pushButton_4.clicked.connect(self.graph)

        # HOME
        self.pushButton_8.clicked.connect(self.home)

    def home(self):
        print("Home Button ForthPage")
        self.home_window = FirstPage()
        widget.addWidget(self.home_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def back(self):
        print("Back Button Clicked !! 5th CS")
        self.call_window=SixthPageCalculation()
        widget.addWidget(self.call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def graph(self):
        print("Back Button Clicked !! 5th CS")
        self.call_window=SixthGraph(self.ans)
        widget.addWidget(self.call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class SixthGraph(QMainWindow):
    def __init__(self, m, L_0=1):
        super().__init__()
        loadUi("physics_p6_c_graph.ui", self)

        # Store m and L_0
        self.m = m
        self.L_0 = L_0

        # Create the widget to hold the graph
        self.widget = QWidget(self)
        self.widget.setGeometry(110, 110, 761, 390)

        # Add canvas for graph plotting
        self.canvas = FigureCanvas(plt.figure())

        # Create layout to hold the canvas
        layout = QVBoxLayout(self.widget)
        layout.addWidget(self.canvas)

        # Plot the graph
        self.plot_graph()

        # HOME
        self.pushButton_8.clicked.connect(self.home)

    def home(self):
        print("Home Button ForthPage")
        self.home_window = FirstPage()
        widget.addWidget(self.home_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def plot_graph(self):
        ax = self.canvas.figure.add_subplot(111)

        # Define x (or m) values (for example, range of m values)
        m_values = np.linspace(-10, 10, 500)

        # Compute the corresponding L values using the formula L = m * L_0
        L_values = self.m * m_values * self.L_0

        # Clear any previous plots
        ax.clear()

        # Plot the line without subscripts in the label
        ax.plot(m_values, L_values, label=f'L = {self.m} * L0', color='#008080')

        # Add x=0 and y=0 axis lines
        ax.axhline(0, color='black', linewidth=1)
        ax.axvline(0, color='black', linewidth=1)

        # Add grid, labels, title, and legend
        ax.grid(True)
        ax.set_xlabel('m (slope)')
        ax.set_ylabel('L (Length)')
        ax.set_title('Graph of L = m * L0')  # No subscript here as well
        ax.legend()

        # Refresh the canvas to display the updated plot
        self.canvas.draw()


class SeventhPage(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("physics_p7_i.ui", self)

        # Connect signals for lineEdit and lineEdit_13
        self.lineEdit.textChanged.connect(self.text_changed_lineEdit)
        self.lineEdit_13.textChanged.connect(self.text_changed_lineEdit_13)

        # Connect signals for lineEdit_2 and lineEdit_14
        self.lineEdit_2.textChanged.connect(self.text_changed_lineEdit_2)
        self.lineEdit_14.textChanged.connect(self.text_changed_lineEdit_14)

        # Connect signals for lineEdit_3 and lineEdit_15
        self.lineEdit_3.textChanged.connect(self.text_changed_lineEdit_3)
        self.lineEdit_15.textChanged.connect(self.text_changed_lineEdit_15)

        # Connect signals for lineEdit_4 and lineEdit_16
        self.lineEdit_4.textChanged.connect(self.text_changed_lineEdit_4)
        self.lineEdit_16.textChanged.connect(self.text_changed_lineEdit_16)

        # Connect signals for lineEdit_5 and lineEdit_17
        self.lineEdit_5.textChanged.connect(self.text_changed_lineEdit_5)
        self.lineEdit_17.textChanged.connect(self.text_changed_lineEdit_17)

        # Connect signals for lineEdit_6 and lineEdit_18
        self.lineEdit_6.textChanged.connect(self.text_changed_lineEdit_6)
        self.lineEdit_18.textChanged.connect(self.text_changed_lineEdit_18)

        # Connect signals for lineEdit_7 and lineEdit_19
        self.lineEdit_7.textChanged.connect(self.text_changed_lineEdit_7)
        self.lineEdit_19.textChanged.connect(self.text_changed_lineEdit_19)

        # Connect signals for lineEdit_8 and lineEdit_20
        self.lineEdit_8.textChanged.connect(self.text_changed_lineEdit_8)
        self.lineEdit_20.textChanged.connect(self.text_changed_lineEdit_20)

        # Connect signals for lineEdit_9 and lineEdit_21
        self.lineEdit_9.textChanged.connect(self.text_changed_lineEdit_9)
        self.lineEdit_21.textChanged.connect(self.text_changed_lineEdit_21)

        # Connect signals for lineEdit_10 and lineEdit_22
        self.lineEdit_10.textChanged.connect(self.text_changed_lineEdit_10)
        self.lineEdit_22.textChanged.connect(self.text_changed_lineEdit_22)

        # Connect signals for lineEdit_11 and lineEdit_23
        self.lineEdit_11.textChanged.connect(self.text_changed_lineEdit_11)
        self.lineEdit_23.textChanged.connect(self.text_changed_lineEdit_23)

        # Connect signals for lineEdit_12 and lineEdit_24
        self.lineEdit_12.textChanged.connect(self.text_changed_lineEdit_12)
        self.lineEdit_24.textChanged.connect(self.text_changed_lineEdit_24)

        # Button connection (assuming it's part of your implementation)
        self.pushButton.clicked.connect(self.button_function)

        # HOME
        self.pushButton_8.clicked.connect(self.home)

    def home(self):
        print("Home Button ForthPage")
        self.home_window = FirstPage()
        widget.addWidget(self.home_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    # Define text changed methods for each pair
    def text_changed_lineEdit(self):
        self.lineEdit_13.setText(self.lineEdit.text())

    def text_changed_lineEdit_13(self):
        self.lineEdit.setText(self.lineEdit_13.text())

    def text_changed_lineEdit_2(self):
        self.lineEdit_14.setText(self.lineEdit_2.text())

    def text_changed_lineEdit_14(self):
        self.lineEdit_2.setText(self.lineEdit_14.text())

    def text_changed_lineEdit_3(self):
        self.lineEdit_15.setText(self.lineEdit_3.text())

    def text_changed_lineEdit_15(self):
        self.lineEdit_3.setText(self.lineEdit_15.text())

    def text_changed_lineEdit_4(self):
        self.lineEdit_16.setText(self.lineEdit_4.text())

    def text_changed_lineEdit_16(self):
        self.lineEdit_4.setText(self.lineEdit_16.text())

    def text_changed_lineEdit_5(self):
        self.lineEdit_17.setText(self.lineEdit_5.text())

    def text_changed_lineEdit_17(self):
        self.lineEdit_5.setText(self.lineEdit_17.text())

    def text_changed_lineEdit_6(self):
        self.lineEdit_18.setText(self.lineEdit_6.text())

    def text_changed_lineEdit_18(self):
        self.lineEdit_6.setText(self.lineEdit_18.text())

    def text_changed_lineEdit_7(self):
        self.lineEdit_19.setText(self.lineEdit_7.text())

    def text_changed_lineEdit_19(self):
        self.lineEdit_7.setText(self.lineEdit_19.text())

    def text_changed_lineEdit_8(self):
        self.lineEdit_20.setText(self.lineEdit_8.text())

    def text_changed_lineEdit_20(self):
        self.lineEdit_8.setText(self.lineEdit_20.text())

    def text_changed_lineEdit_9(self):
        self.lineEdit_21.setText(self.lineEdit_9.text())

    def text_changed_lineEdit_21(self):
        self.lineEdit_9.setText(self.lineEdit_21.text())

    def text_changed_lineEdit_10(self):
        self.lineEdit_22.setText(self.lineEdit_10.text())

    def text_changed_lineEdit_22(self):
        self.lineEdit_10.setText(self.lineEdit_22.text())

    def text_changed_lineEdit_11(self):
        self.lineEdit_23.setText(self.lineEdit_11.text())

    def text_changed_lineEdit_23(self):
        self.lineEdit_11.setText(self.lineEdit_23.text())

    def text_changed_lineEdit_12(self):
        self.lineEdit_24.setText(self.lineEdit_12.text())

    def text_changed_lineEdit_24(self):
        self.lineEdit_12.setText(self.lineEdit_24.text())

    def button_function(self):
        print("solve button clicked")
        #x2_symbol = self.findChild(QComboBox, 'comboBox_4').currentText()


        # ComboBox symbols
        x1_symbol = self.findChild(QComboBox, 'comboBox_2').currentText()
        y1_symbol = self.findChild(QComboBox, 'comboBox_3').currentText()
        z1_symbol = self.findChild(QComboBox, 'comboBox_4').currentText()
        c1_symbol = self.findChild(QComboBox, 'comboBox_5').currentText()

        x2_symbol = self.findChild(QComboBox, 'comboBox_6').currentText()
        y2_symbol = self.findChild(QComboBox, 'comboBox_7').currentText()
        z2_symbol = self.findChild(QComboBox, 'comboBox_8').currentText()
        c2_symbol = self.findChild(QComboBox, 'comboBox_9').currentText()

        x3_symbol = self.findChild(QComboBox, 'comboBox_10').currentText()
        y3_symbol = self.findChild(QComboBox, 'comboBox_11').currentText()
        z3_symbol = self.findChild(QComboBox, 'comboBox_12').currentText()
        c3_symbol = self.findChild(QComboBox, 'comboBox_13').currentText()

        # LineEdit inputs
        x1 = self.lineEdit.text()
        y1 = self.lineEdit_2.text()
        z1 = self.lineEdit_3.text()
        c1 = self.lineEdit_4.text()

        x2 = self.lineEdit_5.text()
        y2 = self.lineEdit_6.text()
        z2 = self.lineEdit_7.text()
        c2 = self.lineEdit_8.text()

        x3 = self.lineEdit_9.text()
        y3 = self.lineEdit_10.text()
        z3 = self.lineEdit_11.text()
        c3 = self.lineEdit_12.text()

        # Float conversion with symbol handling

        # First row
        x1_value = float(x1) if x1_symbol == '+' else -1*float(x1)
        y1_value = float(y1) if y1_symbol == '+' else -1*float(y1)
        z1_value = float(z1) if z1_symbol == '+' else -1*float(z1)
        c1_value = float(c1) if c1_symbol == '+' else -1*float(c1)

        # Second row
        x2_value = float(x2) if x2_symbol == '+' else -1*float(x2)
        y2_value = float(y2) if y2_symbol == '+' else -1*float(y2)
        z2_value = float(z2) if z2_symbol == '+' else -1*float(z2)
        c2_value = float(c2) if c2_symbol == '+' else -1*float(c2)

        # Third row
        x3_value = float(x3) if x3_symbol == '+' else -1*float(x3)
        y3_value = float(y3) if y3_symbol == '+' else -1*float(y3)
        z3_value = float(z3) if z3_symbol == '+' else -1*float(z3)
        c3_value = float(c3) if c3_symbol == '+' else -1*float(c3)

        # You can now use x1_value, y1_value, z1_value, c1_value, etc. in your further calculations
        print("Values:", x1_value, y1_value, z1_value, c1_value)
        print("Second Row:", x2_value, y2_value, z2_value, c2_value)
        print("Third Row:", x3_value, y3_value, z3_value, c3_value)

        # Define symbols for solving equations
        x, y, z = symbols('x y z')

        # Create equations using sympy
        eq1 = Eq(x1_value * x + y1_value * y + z1_value * z, c1_value)
        eq2 = Eq(x2_value * x + y2_value * y + z2_value * z, c2_value)
        eq3 = Eq(x3_value * x + y3_value * y + z3_value * z, c3_value)

        # Solve the system of equations
        solution = solve([eq1, eq2, eq3], (x, y, z))

        print(solution)
        print(type(solution))
        print(solution)

        if solution:
            print(f"Solution: x = {solution[x]}, y = {solution[y]}, z = {solution[z]}")
            self.call_window=SeventhPageSolution(solution[x],solution[y],solution[z],eq1,eq2,eq3)
            widget.addWidget(self.call_window)
            widget.setCurrentIndex(widget.currentIndex() + 1)
        else:
            print("No solution found.")
            QMessageBox.information(self, "No solution found".title(), "reenter values or try with another".title())

class SeventhPageSolution(QMainWindow):
    def __init__(self,x,y,z,eq1,eq2,eq3):
        super().__init__()
        loadUi("physics_p7_ii.ui",self)

        self.label_7.setText(str(x))
        self.label_8.setText(str(y))
        self.label_9.setText(str(z))

        print(x,y,z)

        self.eq1=eq1
        self.eq2=eq2
        self.eq3=eq3

        self.x=x
        self.y=y
        self.z=z

        self.pushButton.clicked.connect(self.back)

        self.pushButton_4.clicked.connect(self.graph)


        # HOME
        self.pushButton_8.clicked.connect(self.home)

    def home(self):
        print("Home Button ForthPage")
        self.home_window = FirstPage()
        widget.addWidget(self.home_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def back(self):
        self.call_window = SeventhPage()
        widget.addWidget(self.call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def graph(self):
        self.call_window=SeventhGraph(self.x,self.y,self.z,self.eq1,self.eq2,self.eq3)
        widget.addWidget(self.call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from PyQt5.uic import loadUi

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from PyQt5.uic import loadUi

class SeventhGraph(QMainWindow):
    def __init__(self, x, y, z, eq1, eq2, eq3):
        super().__init__()
        loadUi("physics_p7_iii.ui", self)

        # Create the widget to hold the graph
        self.widget = QWidget(self)
        self.widget.setGeometry(110, 110, 751, 381)

        # Add canvas for graph plotting
        self.canvas = FigureCanvas(plt.figure())

        # Create layout to hold the canvas
        layout = QVBoxLayout(self.widget)
        layout.addWidget(self.canvas)

        # Store the equations and values
        self.x = x
        self.y = y
        self.z = z
        self.eq1 = eq1
        self.eq2 = eq2
        self.eq3 = eq3

        print(self.x, self.y, self.z)
        print(self.eq1, self.eq2, self.eq3)
        print("--------------------------------")

        # Plot the graph using the provided equations
        self.plot_graph(self.x, self.y, self.z, self.eq1, self.eq2, self.eq3)  # Uncommented this linedx

        self.pushButton.clicked.connect(self.home)

        # HOME
        self.pushButton_8.clicked.connect(self.home)

    def home(self):
        print("Home Button ForthPage")
        self.home_window = FirstPage()
        widget.addWidget(self.home_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def home(self):
        self.call_window = FirstPage()  # Assuming FirstPage is defined elsewhere
        widget.addWidget(self.call_window)  # Assuming 'widget' is a QStackedWidget
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def plot_graph(self, X_val, Y_val, Z_val, eq1, eq2, eq3):
        try:
            ax = self.canvas.figure.add_subplot(111, projection='3d')

            # Generate x and y values for plotting
            x_vals = np.linspace(-50, 50, 100)  # Reduced the number of points from 400 to 100
            y_vals = np.linspace(-50, 50, 100)
            X, Y = np.meshgrid(x_vals, y_vals)

            # Extract coefficients from the equations
            a1, b1, c1, d1 = self.get_coefficients(eq1)
            a2, b2, c2, d2 = self.get_coefficients(eq2)
            a3, b3, c3, d3 = self.get_coefficients(eq3)

            # Create functions for z values
            func1 = lambda x, y: (d1 - a1 * x - b1 * y) / c1 if c1 != 0 else np.nan
            func2 = lambda x, y: (d2 - a2 * x - b2 * y) / c2 if c2 != 0 else np.nan
            func3 = lambda x, y: (d3 - a3 * x - b3 * y) / c3 if c3 != 0 else np.nan

            # Compute the z values for each equation
            Z_eq1 = func1(X, Y)
            Z_eq2 = func2(X, Y)
            Z_eq3 = func3(X, Y)

            # Clear previous plots
            ax.clear()

            # Format the equation labels
            label_eq1 = self.format_equation(a1, b1, c1, d1)
            label_eq2 = self.format_equation(a2, b2, c2, d2)
            label_eq3 = self.format_equation(a3, b3, c3, d3)

            # Plot the equations as surfaces
            ax.plot_surface(X, Y, Z_eq1, color='blue', alpha=0.5, label=label_eq1)
            ax.plot_surface(X, Y, Z_eq2, color='orange', alpha=0.5, label=label_eq2)
            ax.plot_surface(X, Y, Z_eq3, color='green', alpha=0.5, label=label_eq3)

            # Plot the intersection point (x, y, z)
            ax.scatter(X_val, Y_val, Z_val, color='red', s=100, label='Solution')

            # Create a text box to display the values of x, y, and z
            textstr = f'X: {self.x:.2f}\nY: {self.y:.2f}\nZ: {self.z:.2f}'
            ax.text2D(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=10,
                      bbox=dict(facecolor='white', alpha=0.5, edgecolor='black', boxstyle='round,pad=0.5'))

            # Set the graph limits
            ax.set_xlim(-50, 50)
            ax.set_ylim(-50, 50)
            ax.set_zlim(-50, 50)

            # Add grid, labels, title, and legend
            ax.grid(True)
            ax.set_xlabel('X-axis')
            ax.set_ylabel('Y-axis')
            ax.set_zlabel('Z-axis')
            # ax.set_title('Graph of the 3 Equations')

            # Refresh the canvas to display the updated plot
            self.canvas.draw()

        except Exception as e:
            print(f"An error occurred while plotting: {e}")

    def get_coefficients(self, eq):
        """Extracts coefficients of x, y, z, and the constant from the equation."""
        coeffs = eq.lhs.as_coefficients_dict()
        a = coeffs.get(sp.symbols('x'), 0)
        b = coeffs.get(sp.symbols('y'), 0)
        c = coeffs.get(sp.symbols('z'), 0)
        d = eq.rhs
        return a, b, c, d

    def format_equation(self, a, b, c, d):
        """Formats the equation in the form of '<>x + or - <>y + or - <>z = d'."""
        sign_y = '+' if b >= 0 else '-'
        sign_z = '+' if c >= 0 else '-'
        formatted_a = abs(a) if a != 0 else ''
        formatted_b = abs(b) if b != 0 else ''
        formatted_c = abs(c) if c != 0 else ''

        equation_str = ''
        if formatted_a:
            equation_str += f'{formatted_a}x '
        if formatted_b:
            equation_str += f'{sign_y} {formatted_b}y '
        if formatted_c:
            equation_str += f'{sign_z} {formatted_c}z '
        equation_str += f'= {d}'

        return equation_str.strip()


import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QStackedWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.uic import loadUi
import sympy as sp


class EightPage(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("physics_p8_i.ui", self)
        self.pushButton.clicked.connect(self.graph_button_clicked)

    def graph_button_clicked(self):
        eq1 = self.lineEdit.text()  # First equation input by the user
        eq2 = self.lineEdit_2.text()  # Second equation input by the user
        self.call_window = EightPageGraph(eq1, eq2)
        widget.addWidget(self.call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class EightPageGraph(QMainWindow):
    def __init__(self, eq1, eq2):
        super().__init__()
        loadUi("physics_p8_ii.ui", self)

        # Create the widget to hold the graph
        self.widget = QWidget(self)
        self.widget.setGeometry(110, 80, 761, 381)

        # Add canvas for graph plotting
        self.canvas = FigureCanvas(plt.figure())

        # Create layout to hold the canvas
        layout = QVBoxLayout(self.widget)
        layout.addWidget(self.canvas)

        # Plot the graph using the equations provided
        self.plot_graph(eq1, eq2)

        self.pushButton.clicked.connect(self.back)

    def back(self):
        self.call_window = EightPage()
        widget.addWidget(self.call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def parse_expression(self, expr):
        try:
            # Use SymPy to parse the expression and create a lambda function for evaluation
            x = sp.symbols('x')
            parsed_expr = sp.sympify(expr)
            func = sp.lambdify(x, parsed_expr, modules=['numpy'])
            return func
        except Exception as e:
            print(f"Error parsing expression: {e}")
            return None

    def plot_graph(self, eq1, eq2):
        ax = self.canvas.figure.add_subplot(111)
        x = np.linspace(-50, 50, 500)  # Increased range to zoom out

        try:
            func1 = self.parse_expression(eq1)
            func2 = self.parse_expression(eq2)

            if func1 is None or func2 is None:
                print("Error: Invalid expressions entered")
                return

            # Compute the y values for both equations over the x range
            y1 = func1(x)
            y2 = func2(x)

            # Clear previous plots
            ax.clear()

            # Plot the two curves
            ax.plot(x, y1, label=f'y = {eq1}', color='#008080')
            ax.plot(x, y2, label=f'y = {eq2}', color='#E30B5D')

            ax.fill_between(x, y1, y2, where=(y1 >= y2), interpolate=True, color='#FFCC00', alpha=0.7)

            ax.set_xlim(-50, 50)  # Wider range on the x-axis
            y_min = min(np.min(y1), np.min(y2)) - 10  # Larger buffer for y-axis
            y_max = max(np.max(y1), np.max(y2)) + 10
            ax.set_ylim(y_min, y_max)

            # Add x=0 and y=0 axis lines (centralized axes)
            ax.axhline(0, color='black', linewidth=1)
            ax.axvline(0, color='black', linewidth=1)

            # Find intersections/roots using SymPy
            x_sym = sp.Symbol('x')
            eq_diff = sp.sympify(eq1) - sp.sympify(eq2)
            solutions = sp.solvers.solve(eq_diff, x_sym)

            intersection_text = "Intersections:\n"

            for sol in solutions:
                if sol.is_real:  # Only consider real intersections
                    sol_float = float(sol)
                    y_sol = func1(sol_float)
                    ax.plot(sol_float, y_sol, 'ro')  # Red dot for intersection
                    intersection_text += f'({sol_float:.2f}, {y_sol:.2f})\n'

            ax.text(
                -50, y_min + 5,  # Position near bottom-left corner
                intersection_text,
                fontsize=10,
                color='black',
                bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5')  # Add a box around the text
            )

            ax.grid(True)
            ax.set_xlabel('X-axis')
            ax.set_ylabel('Y-axis')
            ax.set_title('Graph with Shaded Common Region and Intersection Points')
            ax.legend()

            self.canvas.draw()

        except Exception as e:
            print(f"Error in plot_graph: {e}")

class NinePage(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("physics_p9.ui",self)


        self.label_22.hide() #self.label.setVisible(False)  # Hides the label
        self.label_16.hide()
        self.label_17.hide()
        self.label_18.hide()

        self.label_19.hide()
        self.label_20.hide()
        self.label_21.hide()

        # self.lineEdit_3.textChanged.connect(self.calculate_missing_value)  # Hypotenuse
        # self.lineEdit_4.textChanged.connect(self.calculate_missing_value)  # Base
        # self.lineEdit_5.textChanged.connect(self.calculate_missing_value)  # Perpendicular

        # Connect signals
        self.lineEdit_14.textChanged.connect(self.calculate_sin)
        self.lineEdit_20.textChanged.connect(self.calculate_theta)

        # For Cosine
        self.lineEdit_15.textChanged.connect(self.calculate_cos)
        self.lineEdit_21.textChanged.connect(self.calculate_theta_cos)

        # For Tangent
        self.lineEdit_16.textChanged.connect(self.calculate_tan)
        self.lineEdit_22.textChanged.connect(self.calculate_theta_tan)

        # For Cosecant (csc)
        self.lineEdit_17.textChanged.connect(self.calculate_cosec)
        self.lineEdit_23.textChanged.connect(self.calculate_theta_cosec)

        # For Secant (sec)
        self.lineEdit_18.textChanged.connect(self.calculate_sec)
        self.lineEdit_24.textChanged.connect(self.calculate_theta_sec)

        # For Cotangent (cot)
        self.lineEdit_19.textChanged.connect(self.calculate_cot)
        self.lineEdit_25.textChanged.connect(self.calculate_theta_cot)


        self.pushButton.clicked.connect(self.choose_graph)

        #side convertor
        self.lineEdit.textChanged.connect(self.degree)
        self.lineEdit_2.textChanged.connect(self.radian)

        self.pushButton_2.clicked.connect(self.pytho)

        import math
        # Fetching text from QLineEdit widgets
        self.sin = self.lineEdit_14.text() if len(self.lineEdit_14.text()) != 0 else "None"
        self.cos = self.lineEdit_15.text() if len(self.lineEdit_15.text()) != 0 else "None"
        self.tan = self.lineEdit_16.text() if len(self.lineEdit_16.text()) != 0 else "None"
        self.csc = self.lineEdit_17.text() if len(self.lineEdit_17.text()) != 0 else "None"
        self.sec = self.lineEdit_18.text() if len(self.lineEdit_18.text()) != 0 else "None"
        self.cot = self.lineEdit_19.text() if len(self.lineEdit_19.text()) != 0 else "None"

        # HOME
        self.pushButton_8.clicked.connect(self.home)

    def home(self):
        print("Home Button ForthPage")
        self.home_window = FirstPage()
        widget.addWidget(self.home_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)


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

            # Show input fields and the triangle diagram
            self.label_15.show()  # triangle diagram
            self.lineEdit_3.show()  # hypotenuse input
            self.lineEdit_4.show()  # base input
            self.lineEdit_5.show()  # perpendicular input

            # Clear the input fields
            self.lineEdit_3.clear()  # Clear hypotenuse input
            self.lineEdit_4.clear()  # Clear base input
            self.lineEdit_5.clear()  # Clear perpendicular input

            # Clear the result labels
            self.label_19.setText("")
            self.label_20.setText("")
            self.label_21.setText("")

        else:
            # If not in "BACK" mode, proceed with the calculation
            self.pushButton_2.setText("BACK")

            # Show result labels
            self.label_22.show()
            self.label_16.show()
            self.label_17.show()
            self.label_18.show()
            self.label_19.show()
            self.label_20.show()
            self.label_21.show()

            # Hide input fields and the triangle diagram
            self.label_15.hide()  # triangle diagram
            self.lineEdit_3.hide()  # hypotenuse input
            self.lineEdit_4.hide()  # base input
            self.lineEdit_5.hide()  # perpendicular input

            # Get values from the lineEdits and validate them
            h = self.lineEdit_3.text()  # Hypotenuse
            b = self.lineEdit_4.text()  # Base
            p = self.lineEdit_5.text()  # Perpendicular

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

    def calculate_sin(self):
        theta_text = self.lineEdit_14.text()
        if theta_text:  # Avoid errors if input is empty
            try:
                theta = float(theta_text)
                # Convert degrees to radians for sine calculation
                sin_theta = math.sin(math.radians(theta))
                self.lineEdit_20.blockSignals(True)  # Prevent signal from triggering when setting the value
                self.lineEdit_20.setText(f'{sin_theta:.4f}')  # Format to 4 decimal places
                self.lineEdit_20.blockSignals(False)
            except ValueError:
                self.lineEdit_20.setText('Invalid input')

    def calculate_theta(self):
        sin_text = self.lineEdit_20.text()
        if sin_text:  # Avoid errors if input is empty
            try:
                sin_theta = float(sin_text)
                if -1 <= sin_theta <= 1:  # Check if value is within the valid range for sin(theta)
                    # Calculate theta using inverse sine
                    theta = math.degrees(math.asin(sin_theta))
                    self.lineEdit_14.blockSignals(True)  # Prevent signal from triggering when setting the value
                    self.lineEdit_14.setText(f'{theta:.1f}')  # Ensure formatting
                    self.lineEdit_14.blockSignals(False)
                else:
                    self.lineEdit_14.setText('Out of range')  # Handle out of range values
            except ValueError:
                self.lineEdit_14.setText('Invalid input')  # Handle invalid inputs

    def calculate_cos(self):
        theta_text = self.lineEdit_15.text()
        if theta_text:  # Avoid errors if input is empty
            try:
                theta = float(theta_text)
                # Convert degrees to radians for cosine calculation
                cos_theta = math.cos(math.radians(theta))
                self.lineEdit_21.blockSignals(True)
                self.lineEdit_21.setText(f'{cos_theta:.4f}')  # Format to 4 decimal places
                self.lineEdit_21.blockSignals(False)
            except ValueError:
                self.lineEdit_21.setText('Invalid input')

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



    # Cosecant (csc)
    def calculate_cosec(self):
        theta_text = self.lineEdit_17.text()
        if theta_text:
            try:
                theta = float(theta_text)
                if theta == 0:  # Cosecant is undefined for theta = 0
                    QMessageBox.warning(self, 'Invalid Input',
                                        'Cosecant is undefined for 0. Please enter another value.')
                    new_value, ok = QInputDialog.getDouble(self, 'New Theta', 'Enter new degree value:')
                    if ok:
                        self.lineEdit_17.setText(str(new_value))
                        theta = new_value
                csc_theta = 1 / math.sin(math.radians(theta)) if math.sin(math.radians(theta)) != 0 else float('inf')
                self.lineEdit_23.blockSignals(True)
                self.lineEdit_23.setText(f'{csc_theta:.4f}')
                self.lineEdit_23.blockSignals(False)
            except ValueError:
                self.lineEdit_23.setText('Invalid input')

    def calculate_theta_cosec(self):
        csc_text = self.lineEdit_23.text()
        if csc_text:
            try:
                csc_theta = float(csc_text)

                if csc_theta == 0:  # Cosecant cannot be zero
                    QMessageBox.warning(self, 'Invalid Input',
                                        'Cosecant cannot be zero. Please enter another value.')
                    new_value, ok = QInputDialog.getDouble(self, 'New Cosecant', 'Enter a valid cosecant value:')
                    if ok:
                        self.lineEdit_23.setText(str(new_value))
                        csc_theta = new_value

                if abs(csc_theta) < 1:  # Cosecant must be ≥ 1 or ≤ -1
                    QMessageBox.warning(self, 'Invalid Input',
                                        'Absolute value of cosecant must be greater than or equal to 1.')
                    self.lineEdit_17.setText('Out of range')
                    return

                # Calculate theta
                theta = math.degrees(math.asin(1 / csc_theta))

                self.lineEdit_17.blockSignals(True)
                self.lineEdit_17.setText(f'{theta:.1f}')
                self.lineEdit_17.blockSignals(False)

            except ValueError:
                self.lineEdit_17.setText('Invalid input')

    def calculate_sec(self):
        theta_text = self.lineEdit_18.text()
        if theta_text:
            try:
                theta = float(theta_text)
                if theta % 180 == 90:  # Secant is undefined for odd multiples of 90° (90°, 270°, etc.)
                    QMessageBox.warning(self, 'Invalid Input',
                                        'Secant is undefined for 90° and its odd multiples. Please enter another value.')
                    new_value, ok = QInputDialog.getDouble(self, 'New Theta', 'Enter new degree value:')
                    if ok:
                        self.lineEdit_18.setText(str(new_value))
                        theta = new_value
                sec_theta = 1 / math.cos(math.radians(theta)) if math.cos(math.radians(theta)) != 0 else float('inf')
                self.lineEdit_24.blockSignals(True)
                self.lineEdit_24.setText(f'{sec_theta:.4f}')
                self.lineEdit_24.blockSignals(False)
            except ValueError:
                self.lineEdit_24.setText('Invalid input')

    def calculate_theta_sec(self):
        sec_text = self.lineEdit_24.text()
        if sec_text:
            try:
                sec_theta = float(sec_text)

                if sec_theta == 0:  # Secant cannot be zero
                    QMessageBox.warning(self, 'Invalid Input',
                                        'Secant cannot be zero. Please enter another value.')
                    new_value, ok = QInputDialog.getDouble(self, 'New Secant', 'Enter a valid secant value:')
                    if ok:
                        self.lineEdit_24.setText(str(new_value))
                        sec_theta = new_value

                if sec_theta == 1:  # sec(0°) = 1
                    theta = 0
                elif sec_theta == -1:  # sec(180°) = -1
                    theta = 180
                elif abs(sec_theta) < 1:  # Secant must be ≥ 1 or ≤ -1
                    QMessageBox.warning(self, 'Invalid Input',
                                        'Absolute value of secant must be greater than or equal to 1.')
                    self.lineEdit_18.setText('Out of range')
                    return
                else:
                    theta = math.degrees(math.acos(1 / sec_theta))

                self.lineEdit_18.blockSignals(True)
                self.lineEdit_18.setText(f'{theta:.1f}')
                self.lineEdit_18.blockSignals(False)

            except ValueError:
                self.lineEdit_18.setText('Invalid input')

    def calculate_cot(self):
        theta_text = self.lineEdit_19.text()
        if theta_text:
            try:
                theta = float(theta_text)
                if theta == 0 or theta == 180:  # Cotangent is undefined for theta = 0 or 180 degrees
                    QMessageBox.warning(self, 'Invalid Input',
                                        'Cotangent is undefined for 0° and 180°. Please enter another value.')
                    new_value, ok = QInputDialog.getDouble(self, 'New Theta', 'Enter new degree value:')
                    if ok:
                        self.lineEdit_19.setText(str(new_value))
                        theta = new_value
                cot_theta = 1 / math.tan(math.radians(theta)) if math.tan(math.radians(theta)) != 0 else float('inf')
                self.lineEdit_25.blockSignals(True)
                self.lineEdit_25.setText(f'{cot_theta:.4f}')
                self.lineEdit_25.blockSignals(False)
            except ValueError:
                self.lineEdit_25.setText('Invalid input')

    def calculate_theta_cot(self):
        cot_text = self.lineEdit_25.text()
        if cot_text:
            try:
                cot_theta = float(cot_text)

                if cot_theta == 0:  # Cotangent cannot be zero
                    QMessageBox.warning(self, 'Invalid Input',
                                        'Cotangent cannot be zero. Please enter another value.')
                    new_value, ok = QInputDialog.getDouble(self, 'New Cotangent', 'Enter a valid cotangent value:')
                    if ok:
                        self.lineEdit_25.setText(str(new_value))
                        cot_theta = new_value

                theta = math.degrees(math.atan(1 / cot_theta))

                self.lineEdit_19.blockSignals(True)
                self.lineEdit_19.setText(f'{theta:.1f}')
                self.lineEdit_19.blockSignals(False)

            except ValueError:
                self.lineEdit_19.setText('Invalid input')


    def choose_graph(self):

        sin_value = self.lineEdit_20.text() or "None"
        cos_value = self.lineEdit_21.text() or "None"
        tan_value = self.lineEdit_22.text() or "None"
        csc_value = self.lineEdit_23.text() or "None"
        sec_value = self.lineEdit_24.text() or "None"
        cot_value = self.lineEdit_25.text() or "None"
        print("310")
        print(sin_value,cos_value,tan_value,csc_value,sec_value,cot_value)

        self.call_window=NineGraph(sin_value,cos_value,tan_value,csc_value,sec_value,cot_value)
        widget.addWidget(self.call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class NineGraph(QMainWindow):
    def __init__(self,sin_theta,cos_theta,tan_theta,csc_theta,sec_theta,cot_theta):
        super().__init__()
        loadUi("physics_p9_g_i.ui",self)

        self.sin_theta=sin_theta
        self.cos_theta=cos_theta
        self.tan_theta=tan_theta
        self.csc_theta=csc_theta
        self.sec_theta=sec_theta
        self.cot_theta=cot_theta

        self.pushButton_2.clicked.connect(self.sin)
        self.pushButton_3.clicked.connect(self.cos)
        self.pushButton_4.clicked.connect(self.tan)
        self.pushButton_5.clicked.connect(self.csc)
        self.pushButton_6.clicked.connect(self.sec)
        self.pushButton_7.clicked.connect(self.cot)
        self.pushButton.clicked.connect(self.back_button)


        print("---------------------")
        print(self.sin_theta,self.cos_theta,self.tan_theta,self.csc_theta,self.sec_theta,self.cot_theta)
        # HOME
        self.pushButton_8.clicked.connect(self.home)

    def home(self):
        print("Home Button ForthPage")
        self.home_window = FirstPage()
        widget.addWidget(self.home_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def back_button(self):
        self.call_window=NinePage()
        widget.addWidget(self.call_window)
        widget.setCurrentWidget(widget.currentIndex() + 1)

    def if_theta_none(self, trig_type):
        # Supported trigonometric types
        trig_types = ["sin", "cos", "tan", "csc", "sec", "cot"]

        if trig_type in trig_types:
            # Create QMessageBox
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle(f"Missing {trig_type.capitalize()} Theta")
            msg.setText(f"The {trig_type.capitalize()} value is missing. Please choose one of the following options:")

            # Add buttons for options
            theta_button = msg.addButton('Enter Theta', QMessageBox.ActionRole)
            value_button = msg.addButton('Enter Value', QMessageBox.ActionRole)
            # cancel_button = msg.addButton('Cancel', QMessageBox.RejectRole)

            # Execute the message box
            msg.exec_()

            # Handle button responses
            if msg.clickedButton() == theta_button:
                # Ask for Theta input
                theta, ok = QInputDialog.getText(self, f'Input {trig_type.capitalize()} Theta',
                                                 f'Enter the angle (theta in degrees):')
                if ok and theta:
                    try:
                        # Convert theta to radians and calculate the trig value
                        theta_radians = math.radians(float(theta))
                        trig_value = getattr(math, trig_type)(theta_radians) if trig_type in ["sin", "cos",
                                                                                              "tan"] else self.inverse_trig(
                            trig_type, theta_radians)
                        print(
                            f'{trig_type.capitalize()} Theta entered: {theta}, {trig_type.capitalize()} Value: {trig_value}')
                        return theta  # Return theta in degrees
                    except ValueError:
                        print(f"Invalid Theta value for {trig_type}.")
                        return None

            elif msg.clickedButton() == value_button:
                # Ask for Trig value input
                value, ok = QInputDialog.getText(self, f'Input {trig_type.capitalize()} Value',
                                                 f'Enter the {trig_type.capitalize()} value:')
                if ok and value:
                    try:
                        value = float(value)
                        # Calculate theta based on the inverse of the trigonometric function
                        theta = math.degrees(self.inverse_trig(trig_type, value))
                        print(f'{trig_type.capitalize()} Value entered: {value}, Theta = {theta}')
                        return theta  # Return theta in degrees
                    except ValueError:
                        print(f"Invalid {trig_type} value.")
                        return None

            # elif msg.clickedButton() == cancel_button:
            #     # Cancel the action
            #     print(f"{trig_type.capitalize()} action cancelled.")
            #     return None

    def inverse_trig(self, trig_type, value):
        """Returns the inverse of the trigonometric function (arc function) based on type."""
        if trig_type == "sin":
            return math.asin(value)
        elif trig_type == "cos":
            return math.acos(value)
        elif trig_type == "tan":
            return math.atan(value)
        elif trig_type == "csc":
            return math.asin(1 / value)
        elif trig_type == "sec":
            return math.acos(1 / value)
        elif trig_type == "cot":
            return math.atan(1 / value)

    def sin(self):
        type = "sin"
        if self.sin_theta == "None": self.sin_theta=self.if_theta_none(type)

        # Proceed with plotting the graph if sin_theta is valid
        self.call_window = NineGraphPlot(self.sin_theta, type)
        widget.addWidget(self.call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def cos(self):
        type="cos"
        if self.cos_theta == "None": self.cos_theta=self.if_theta_none(type)
        self.call_window=NineGraphPlot(self.cos_theta,type)
        widget.addWidget(self.call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def tan(self):
        type="tan"
        if self.tan_theta=="None": self.tan_theta=self.if_theta_none(type)
        self.call_window=NineGraphPlot(self.tan_theta,type)
        widget.addWidget(self.call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def csc(self):
        type="csc"
        if self.csc_theta=="None":self.csc_theta=self.if_theta_none(type)
        self.call_window=NineGraphPlot(self.csc_theta,type)
        widget.addWidget(self.call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def sec(self):
        type="sec"
        if self.sec_theta=="None":self.sec_theta=self.if_theta_none(type)
        self.call_window=NineGraphPlot(self.sec_theta,type)
        widget.addWidget(self.call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def cot(self):
        type="cot"
        if self.cot_theta=="None":self.cot_theta=self.if_theta_none(type)
        self.call_window=NineGraphPlot(self.cot_theta,type)
        widget.addWidget(self.call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import math
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from PyQt5.uic import loadUi


class NineGraphPlot(QMainWindow):
    def __init__(self, value, trig_type):
        super().__init__()
        loadUi("physics_p9_g_ii.ui", self)

        # Create a widget to hold the graph
        self.widget = QWidget(self)
        self.widget.setGeometry(110, 80, 761, 381)

        # Add a canvas for graph plotting
        self.canvas = FigureCanvas(Figure())

        # Create a layout and add the canvas to it
        layout = QVBoxLayout(self.widget)
        layout.addWidget(self.canvas)

        # Calculate the inverse trigonometric value and plot the graph
        try:
            inverse_value = self.inverse_trig(trig_type=trig_type, value=float(value))
            print(f"Inverse of {trig_type}({value}) is: {math.degrees(inverse_value)}")

            # Plot the graph
            self.plot_graph(trig_type, inverse_value)

        except ValueError as e:
            print(f"Error: {e}")
        except ZeroDivisionError as e:
            print(f"Error: Division by zero - {e}")


    def inverse_trig(self, trig_type, value):
        """Returns the inverse of the trigonometric function (arc function) based on type."""
        if trig_type == "sin":
            return math.asin(value)
        elif trig_type == "cos":
            return math.acos(value)
        elif trig_type == "tan":
            return math.atan(value)
        elif trig_type == "csc":
            if value == 0:
                raise ValueError("Value for csc cannot be zero.")
            return math.asin(1 / value)
        elif trig_type == "sec":
            if value == 0:
                raise ValueError("Value for sec cannot be zero.")
            return math.acos(1 / value)
        elif trig_type == "cot":
            if value == 0:
                raise ValueError("Value for cot cannot be zero.")
            return math.atan(1 / value)
        else:
            raise ValueError(f"Invalid trigonometric function: {trig_type}")

    def plot_graph(self, trig_type, value):
        # Set up the axes for the plot
        ax = self.canvas.figure.add_subplot(111)

        # Define the x-axis range for plotting (from -2*pi to 2*pi for better visibility)
        x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

        # Clear previous plot
        ax.clear()

        # Determine the y values and plot based on trig_type
        if trig_type == "sin":
            y = np.sin(x)
            ax.plot(x, y, label='Sine curve', color='#FF5733')
        elif trig_type == "cos":
            y = np.cos(x)
            ax.plot(x, y, label='Cosine curve', color='#33FF57')
        elif trig_type == "tan":
            y = np.tan(x)
            ax.plot(x, y, label='Tangent curve', color='#3357FF')
            ax.set_ylim(-10, 10)  # Limit y-axis for tan function
        elif trig_type == "csc":
            y = 1 / np.sin(x)
            ax.plot(x, y, label='Cosecant curve', color='#FF33A1')
            ax.set_ylim(-10, 10)  # Limit y-axis for csc function
        elif trig_type == "sec":
            y = 1 / np.cos(x)
            ax.plot(x, y, label='Secant curve', color='#FFA133')
            ax.set_ylim(-10, 10)  # Limit y-axis for sec function
        elif trig_type == "cot":
            y = 1 / np.tan(x)
            ax.plot(x, y, label='Cotangent curve', color='#A133FF')
            ax.set_ylim(-10, 10)  # Limit y-axis for cot function

        # Mark the point corresponding to the inverse value
        if trig_type in ["sin", "cos", "tan"]:
            # Convert degrees to radians for calculation
            x_value_at_value = math.radians(float(value))  # Correct conversion of degrees to radians
            if trig_type == "sin":
                y_value_at_value = np.sin(x_value_at_value)
                # quick_theta = math.degrees(math.asin(float(value)))
            elif trig_type == "cos":
                y_value_at_value = np.cos(x_value_at_value)
                # quick_theta = math.degrees(math.acos(float(value)))
            else:  # tan
                y_value_at_value = np.tan(x_value_at_value)
                # quick_theta = math.degrees(math.atan(float(value)))

            ax.plot(x_value_at_value, y_value_at_value, 'ro', label=f'{trig_type}(x) = {value:.5f}')

            # Draw a vertical line at the marked point
            ax.axvline(x=x_value_at_value, color='blue', linestyle='--')

        # Customize the graph
        ax.set_title(f'Graph of {trig_type.capitalize()} Function with Marked Value')
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.legend()
        ax.grid(True)

        # Redraw the canvas with the new plot
        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QStackedWidget()
    main_wind = FirstPage()
    widget.addWidget(main_wind)
    widget.setFixedSize(main_wind.size())
    widget.show()
    sys.exit(app.exec())

