import sys

from PyQt5.QtCore import Qt
from sympy import symbols , Eq , solve , latex
import vlc
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QApplication , QMainWindow , QStackedWidget , QComboBox , QLabel , QPushButton , QMessageBox , \
    QInputDialog
from PyQt5.uic import loadUi
from decimal import Decimal , getcontext , InvalidOperation
import math

from PyQt5.uic.properties import QtCore
from sympy import symbols , Eq , solve


#
# # Set precision to 12 decimal places
# getcontext().prec = 12
#

class FirstPage(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("physics_p1.ui" , self)
        self.pushButton.clicked.connect(self.button_clicked)

    def button_clicked(self):
        print("Button clicked successfully!")
        self.call_create_window = SecondPage()
        widget.addWidget(self.call_create_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class SecondPage(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("physics_p2.ui" , self)

        # pushButton
        self.pushButton.clicked.connect(self.Quadratic_Root)
        # pushButton_4
        self.pushButton_4.clicked.connect(self.Linear_Eq_in_2_Var)
        # pushButton_5
        self.pushButton_5.clicked.connect(self.laurenz)
        # pushButton_10
        self.pushButton_10.clicked.connect(self.time_dialation)
        # pushButton_9
        self.pushButton_9.clicked.connect(self.Linear_Eq_in_3_Var)
        # pushButton_3
        self.pushButton_3.clicked.connect(self.Two_Eq_graph)
        # pushButton_6
        self.pushButton_6.clicked.connect(self.Trigno)

        # HOME
        self.pushButton_8.clicked.connect(self.home)

    def home(self):
        print("Home Button SecondPage")
        self.home_window = FirstPage()
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
        self.call_create_window = EightPage()
        widget.addWidget(self.call_create_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class ThirdPage(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("physics_p3.ui" , self)

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

        first_symbol = self.findChild(QComboBox , 'comboBox').currentText()
        second_symbol = self.findChild(QComboBox , 'comboBox_2').currentText()
        third_symbol = self.findChild(QComboBox , 'comboBox_3').currentText()

        print(f"first symbol = {first_symbol}\nsecond symbol = {second_symbol}\nthird symbol = {third_symbol}")
        try:
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

            print(a , b , c)

            from sympy import symbols , solve

            x = symbols("x")
    
            quad_eq = a * x ** 2 + b * x + c
            ans = solve(quad_eq , x)
            print(ans[0] , ans[1])
        except Exception as e:
            QMessageBox.critical(self , "Error" , f"{e}")
            return

        self.call_create_window = ThirdPageOutput(ans[0] , ans[1] , quad_eq)
        widget.addWidget(self.call_create_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class ThirdPageOutput(QMainWindow):
    def __init__(self , x1 , x2 , quad_eq):
        super().__init__()
        loadUi("physics_p3_ii.ui" , self)

        self.label_5.setText(str(round(x1 , 8)))
        self.label_7.setText(str(round(x2 , 8)))

        self.pushButton_2.clicked.connect(self.back)
        self.pushButton_4.clicked.connect(self.view_graph)

        self.quad_eq=quad_eq

        self.pushButton_8.clicked.connect(self.home)

    def home(self):
        print("Home Button SecondPage 2")
        self.home_window = FirstPage()
        widget.addWidget(self.home_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def view_graph(self):
        self.call_window = ThirdPageGraph(self.quad_eq)
        widget.addWidget(self.call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def back(self):
        self.call_window = ThirdPage()
        widget.addWidget(self.call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)


from PyQt5.QtWidgets import QMainWindow , QWidget , QLabel
from PyQt5.QtGui import QPixmap


import sys
import numpy as np
import sympy as sp
from PyQt5.QtWidgets import QMainWindow , QWidget , QVBoxLayout , QLabel , QApplication
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi
import matplotlib.pyplot as plt

import sys
import numpy as np
import sympy as sp
from PyQt5.QtWidgets import QMainWindow , QWidget , QVBoxLayout , QLabel , QApplication
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi
import matplotlib.pyplot as plt

class ThirdPageGraph(QMainWindow):
    def __init__(self , quad_eq):
        super().__init__()
        loadUi("physics_p3_iii.ui" , self)
        self.plot_graph(quad_eq)
        self.pushButton_2.clicked.connect(self.back)
        self.pushButton_8.clicked.connect(self.home)

    def home(self):
        self.home_window = FirstPage()
        widget.addWidget(self.home_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def back(self):
        self.call_window = FirstPage()
        widget.addWidget(self.call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def plot_graph(self , quad_eq):
        fig , ax = plt.subplots()
        x_vals = np.linspace(-50 , 50 , 500)
        x = sp.symbols('x')
        print(quad_eq , type(quad_eq))


        y_vals = [float(quad_eq.subs(x , val)) for val in x_vals]


        ax.plot(x_vals , y_vals , color='#c7053d' , label=f"${latex(quad_eq)}$")

        roots = sp.solve(quad_eq , x)

        intersection_text="\n"

        for root in roots:
            if root.is_real:
                x_root = float(root)
                y_root = float(quad_eq.subs(x , x_root))
                ax.plot(x_root , y_root , 'ro')
                intersection_text += f'({x_root:.2f} , {y_root:.2f})\n'

        ax.text(-35 , -100 , intersection_text , fontsize=10 , color='black' , 
                bbox=dict(facecolor="lightyellow" , edgecolor="black" , boxstyle="round , pad=0.3"))

        ax.axhline(0 , color='black' , linewidth=1)
        ax.axvline(0 , color='black' , linewidth=1)
        ax.grid(True)

        # Add the legend to display labels
        ax.legend()

        plt.ylim(-100 , 300)
        plt.xlim(-40 , 40)

        # Save the figure with a transparent background
        plt.savefig("physics_p3_g.png" , dpi=140 , transparent=True)
        plt.close()

        pixmap = QPixmap("physics_p3_g.png")
        self.label_4.setPixmap(pixmap)
        self.label_4.setScaledContents(True)


class ForthPage(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("physics_p4.ui" , self)

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
        from sympy import symbols , Eq , solve

        x , y = symbols("x y")


        x1_symbol = self.findChild(QComboBox , 'comboBox').currentText()
        y1_symbol = self.findChild(QComboBox , 'comboBox_2').currentText()
        c1_symbol = self.findChild(QComboBox , 'comboBox_3').currentText()

        x2_symbol = self.findChild(QComboBox , 'comboBox_4').currentText()
        y2_symbol = self.findChild(QComboBox , 'comboBox_5').currentText()
        c2_symbol = self.findChild(QComboBox , 'comboBox_6').currentText()

        try:
            a = float(self.lineEdit.text()) if x1_symbol == '+' else -float(self.lineEdit.text())
            b = float(self.lineEdit_3.text()) if y1_symbol == '+' else -float(self.lineEdit_3.text())
            e = float(self.lineEdit_4.text()) if c1_symbol == '+' else -float(self.lineEdit_4.text())

            c = float(self.lineEdit_2.text()) if x2_symbol == '+' else -float(self.lineEdit_2.text())
            d = float(self.lineEdit_6.text()) if y2_symbol == '+' else -float(self.lineEdit_6.text())
            f = float(self.lineEdit_5.text()) if c2_symbol == '+' else -float(self.lineEdit_5.text())


            # Set up the equations using sympy
            eq1 = Eq(a * x + b * y , e)
            eq2 = Eq(c * x + d * y , f)

            # Solve the system of equations
            sol = solve((eq1 , eq2) , (x , y))

            if not sol:
                print("No solution found or infinite solutions.")
                return


            print(f"Solution for x: {sol[x]} , Solution for y: {sol[y]}")

            x_solution = round(float(sol[x]) , 9)
            y_solution = round(float(sol[y]) , 9)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"{e}")
            return

        self.call_window_variable = ForthPageOutput(x_solution , y_solution , eq1 , eq2)
        widget.addWidget(self.call_window_variable)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class ForthPageOutput(QMainWindow):
    def __init__(self , a , b , eq1 , eq2):
        super().__init__()
        loadUi("physics_p4_ii.ui" , self)
        print(a , b)
        self.label_6.setText(str(a))
        self.label_7.setText(str(b))

        self.pushButton_8.clicked.connect(self.home_button_function)
        self.pushButton_2.clicked.connect(self.back_button_clicked)
        self.pushButton_4.clicked.connect(self.graph)

        self.eq1 = eq1
        self.eq2 = eq2

    def home_button_function(self):
        print("Home ForthPage 2")
        if not hasattr(self , 'first_page_instance'):
            self.first_page_instance = FirstPage()
        widget.addWidget(self.first_page_instance)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def back_button_clicked(self):
        print("Back Button Clicked !!")
        self.forth_page_instance = ForthPage()
        widget.addWidget(self.forth_page_instance)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def graph(self):
        self.call_window = ForthPageGraph(self.eq1 , self.eq2)
        widget.addWidget(self.call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)


from PyQt5.QtWidgets import QMainWindow , QWidget , QVBoxLayout
from sympy.solvers import solve


class ForthPageGraph(QMainWindow):
    def __init__(self , eq1 , eq2):
        super().__init__()
        loadUi("physics_p4_iii.ui" , self)

        self.plot_graph(eq1 , eq2)
        self.pushButton_2.clicked.connect(self.home)
        self.pushButton_8.clicked.connect(self.home)


    def home(self):
        self.call_window = FirstPage()
        widget.addWidget(self.call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def plot_graph(self , eq1 , eq2):
        fig , ax = plt.subplots(figsize=(6 , 4))
        x_vals = np.linspace(-150 , 150 , 400)


        x , y = sp.symbols('x y')
        a1 , b1 , c1 = eq1.lhs.coeff(x) , eq1.lhs.coeff(y) , eq1.rhs
        a2 , b2 , c2 = eq2.lhs.coeff(x) , eq2.lhs.coeff(y) , eq2.rhs

        def func(a , b , c , x_vals):
            return [(c - a * x) / b if b != 0 else None for x in x_vals]

        y_vals_eq1 = func(a1 , b1 , c1 , x_vals)
        y_vals_eq2 = func(a2 , b2 , c2 , x_vals)

        ax.plot(x_vals , y_vals_eq1 , label=f"${latex(eq1)}$" , color='red')
        ax.plot(x_vals , y_vals_eq2 , label=f"${latex(eq2)}$" , color='#FF8C00')


        sol = sp.solve((eq1 , eq2) , (x , y))
        # if sol:
        #     x_sol , y_sol = float(sol[x]) , float(sol[y])
        #     ax.plot(x_sol , y_sol , 'ro' , label=f"({x_sol:.2f} , {y_sol:.2f})")
        plt.scatter(sol.get(x , 0) , sol.get(y , 0) , color="#7f00ff")
        intersection_text=f"intersection:\n({sol.get(x , 0):.2f}  , {sol.get(y , 0):.2f})"
        ax.text(-90 , -90 , intersection_text , fontsize=10 , color='black' , 
                bbox=dict(facecolor="lightyellow" , edgecolor="black" , boxstyle="round , pad=0.3"))

        ax.axhline(0 , color='black' , linewidth=1)
        ax.axvline(0 , color='black' , linewidth=1)
        ax.grid(True)
        ax.legend()

        ax.set_xlim(-100 , 100)
        ax.set_ylim(-100 , 100)

        fig.savefig("physics_p4_graph.png" , dpi=140 , transparent=True)
        plt.close(fig)

        # Load into label_4
        pixmap = QPixmap("physics_p4_graph.png")
        self.label_4.setPixmap(pixmap)
        self.label_4.setScaledContents(True)



class FifthPageOne(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("physics_p5_i.ui" , self)
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
        loadUi("physics_p5_ii.ui" , self)
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
        loadUi("physics_p5_iii.ui" , self)
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
        loadUi("physics_p5_iv.ui" , self)
        self.pushButton_2.clicked.connect(self.next)
        self.pushButton_3.clicked.connect(self.back)

        self.pushButton_8.clicked.connect(self.home)

    def home(self):
        print("Home Button ForthPage")
        self.home_window = FirstPage()
        widget.addWidget(self.home_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def next(self):
        print("Next Button Clicked !! 5th 4th")
        self.call_window = FifthPageVideo()
        widget.addWidget(self.call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def back(self):
        print("Back Button Clicked !! 5th 4th")
        self.call_window = FifthPageThree()
        widget.addWidget(self.call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)


from PyQt5.QtWidgets import QMainWindow , QLabel , QFrame
from PyQt5.QtGui import QMovie
from PyQt5 import QtCore
import vlc


class FifthPageVideo(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("physics_p5_video.ui" , self)

        self.pushButton_2.clicked.connect(self.home)
        # Set up the animation (GIF) in a specified area
        self.animation_label = QLabel(self)
        self.animation_label.setGeometry(125 , 90 , 711 , 400)   # FINAL for vid.mp4
        # self.animation_label.setGeometry(105 , 90 , 749 , 389)  # FINAL for vid_2.mp4
        self.movie = QMovie("vid_1.mp4")  # Provide your GIF file here
        self.animation_label.setMovie(self.movie)
        self.movie.start()

        # Create a QFrame for VLC video playback in the same area
        self.video_frame = QFrame(self)
        self.video_frame.setGeometry(125 , 90 , 711 , 400)  # FINAL for vid.mp4
        # self.video_frame.setGeometry(105 , 90 , 749 , 389)  # FINAL for vid_2.mp4
        self.video_frame.show()

        # Start the video directly (no delay)
        QtCore.QTimer.singleShot(0 , self.start_video)

        # HOME
        self.pushButton_8.clicked.connect(self.home)

    def home(self):
        print("Home Button ForthPage")
        self.home_window = FirstPage()
        widget.addWidget(self.home_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def start_video(self):
        self.movie.stop()
        self.animation_label.hide()

        self.instance = vlc.Instance()
        self.mediaPlayer = self.instance.media_player_new()

        video_path = "vid_1.mp4"

        if QtCore.QFile.exists(video_path):
            self.mediaPlayer.set_hwnd(int(self.video_frame.winId()))
            media = self.instance.media_new(video_path)
            self.mediaPlayer.set_media(media)

            self.mediaPlayer.event_manager().event_attach(vlc.EventType.MediaPlayerEndReached , self.loop_video)

            self.mediaPlayer.video_set_scale(0)
            self.mediaPlayer.play()
        else:
            print(f"Error: Video file {video_path} not found.")

    def loop_video(self , event):
        self.mediaPlayer.stop()
        self.mediaPlayer.play()



class SixthPageOne(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("physics_p6_i.ui" , self)
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
        self.call_window = SixthPageTwo()
        widget.addWidget(self.call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class SixthPageTwo(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("physics_p6_ii.ui" , self)

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
        loadUi("physics_p6_iii.ui" , self)
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
        self.call_window = SixthPageTwo()
        widget.addWidget(self.call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class SixthPageCalculation(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("physics_p6_c_i.ui" , self)


        self.lineEdit_5.textChanged.connect(self.convert_button)
        self.comboBox.currentIndexChanged.connect(self.convert_button)
        self.comboBox_2.currentIndexChanged.connect(self.convert_button)
        self.pushButton_3.clicked.connect(self.back)


        self.c = Decimal("2.998e8")
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

    def cm_to(self , convert_to):
        cms = {
            "cm/s": Decimal("1") , 
            "m/s": Decimal("1e-2") , 
            "km/s": Decimal("1e-5") , 
            "km/hr": Decimal("3.6e-2") , 
            "AU/day": Decimal("5.775e-9") , 
            "pc/Myr": Decimal("9.775e-18") , 
            "ly/yr": Decimal("3.16888e-11")
        }
        self.perform_conversion(cms , convert_to)

    def ms_to(self , convert_to):
        ms = {
            "m/s": Decimal("1") , 
            "cm/s": Decimal("1e2") , 
            "km/s": Decimal("1e-3") , 
            "km/hr": Decimal("3.6") , 
            "AU/day": Decimal("5.775e-7") , 
            "pc/Myr": Decimal("9.775e-16") , 
            "ly/yr": Decimal("3.16888e-9")
        }
        self.perform_conversion(ms , convert_to)

    def km_s_to(self , convert_to):
        km_s = {
            "km/s": Decimal("1") , 
            "cm/s": Decimal("1e5") , 
            "m/s": Decimal("1e3") , 
            "km/hr": Decimal("3.6e3") , 
            "AU/day": Decimal("5.775e-4") , 
            "pc/Myr": Decimal("9.775e-13") , 
            "ly/yr": Decimal("3.16888e-6")
        }
        self.perform_conversion(km_s , convert_to)

    def km_hr_to(self , convert_to):
        km_hr = {
            "km/hr": Decimal("1") , 
            "cm/s": Decimal("2.77778e-3") , 
            "m/s": Decimal("0.277778") , 
            "km/s": Decimal("2.77778e-4") , 
            "AU/day": Decimal("1.598e-7") , 
            "pc/Myr": Decimal("2.654e-15") , 
            "ly/yr": Decimal("9.713e-9")
        }
        self.perform_conversion(km_hr , convert_to)

    def AU_day_to(self , convert_to):
        AU_day = {
            "AU/day": Decimal("1") , 
            "cm/s": Decimal("1.5778e+8") , 
            "m/s": Decimal("1.5778e+6") , 
            "km/s": Decimal("1.5778e+3") , 
            "km/hr": Decimal("5.6788e+6") , 
            "pc/Myr": Decimal("5.915e+14") , 
            "ly/yr": Decimal("1.711e+8")
        }
        self.perform_conversion(AU_day , convert_to)

    def pc_Myr_to(self , convert_to):
        pc_Myr = {
            "pc/Myr": Decimal("1") , 
            "cm/s": Decimal("1.022e+24") , 
            "m/s": Decimal("1.022e+22") , 
            "km/s": Decimal("1.022e+19") , 
            "km/hr": Decimal("3.679e+20") , 
            "AU/day": Decimal("1.694e+14") , 
            "ly/yr": Decimal("3.262e+6")
        }
        self.perform_conversion(pc_Myr , convert_to)

    def ly_yr_to(self , convert_to):
        ly_yr = {
            "ly/yr": Decimal("1") , 
            "cm/s": Decimal("3.154e+17") , 
            "m/s": Decimal("3.154e+15") , 
            "km/s": Decimal("3.154e+12") , 
            "km/hr": Decimal("1.136e+14") , 
            "AU/day": Decimal("1.711e+8") , 
            "pc/Myr": Decimal("3.068e-7")
        }
        self.perform_conversion(ly_yr , convert_to)

    def c_to(self , convert_to):
        c = {
            "m/s": self.c , 
            "cm/s": self.c * Decimal("1e2") , 
            "km/s": self.c * Decimal("1e-3") , 
            "km/hr": self.c * Decimal("3.6e3") , 
            "AU/day": self.c * Decimal("1.5778e-9") , 
            "pc/Myr": self.c * Decimal("1.022e-17") , 
            "ly/yr": self.c * Decimal("1.057e-12")
        }
        self.perform_conversion(c , convert_to)

    def perform_conversion(self , conversion_dict , convert_to):
        try:
            value = Decimal(self.lineEdit_5.text()) * conversion_dict[convert_to]
            self.label_5.setText(self.format_scientific(value))
        except (InvalidOperation , KeyError):
            self.label_5.setText("Error")

    def format_scientific(self , value):
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
            print(self.ans , self.error)

            if self.ans > 1:
                self.error = True
                print("Error: Value exceeds 1")
                QMessageBox.critical(self , "Error" , "The value exceeds 1. Invalid input.")
            else:
                self.ans = math.sqrt(1 - self.ans)

                print("Back Button Clicked !!")
                self.call_window = SixthPageCalculationSolve(self.ans)
                widget.addWidget(self.call_window)
                widget.setCurrentIndex(widget.currentIndex() + 1)

        except Exception as e:
            QMessageBox.critical(self , "Error" , f"{e}")
            return

    def back(self):
        print("Back Button Clicked !! 5th C")
        self.call_window = SixthPageThree()
        widget.addWidget(self.call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class SixthPageCalculationSolve(QMainWindow):
    def __init__(self , ans):
        super().__init__()
        loadUi("physics_p6_c_ii.ui" , self)
        print(ans)
        self.ans = ans
        self.label_6.setText(f"{ans:.2f}")
        self.label_8.setText(f"{(ans * 100):.2f}")
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
        self.call_window = SixthPageCalculation()
        widget.addWidget(self.call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def graph(self):
        print("Back Button Clicked !! 5th CS")
        self.call_window = SixthGraph(self.ans)
        widget.addWidget(self.call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class SixthGraph(QMainWindow):
    def __init__(self , m , L_0=1):
        super().__init__()
        loadUi("physics_p6_c_graph.ui" , self)

        self.m = m
        self.L_0 = L_0

        self.plot_graph()

        self.pushButton_8.clicked.connect(self.home)

    def home(self):
        print("Home Button SixthGraph")
        self.home_window = FirstPage()
        widget.addWidget(self.home_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def plot_graph(self):
        fig , ax = plt.subplots(figsize=(6 , 4))
        m_values = np.linspace(-10 , 10 , 500)
        L_values = self.m * m_values * self.L_0

        ax.plot(m_values , L_values , label=f'L = {self.m:.4f} × L0' , color='#8B0000')

        ax.axhline(0 , color='black' , linewidth=1)
        ax.axvline(0 , color='black' , linewidth=1)
        ax.grid(True)

        ax.set_xlabel('m (slope)')
        ax.set_ylabel('L (Length)')
        ax.set_title('Graph of L = m * L0')
        ax.legend()

        fig.savefig("physics_p6_graph.png" , dpi=140 , transparent=True)
        plt.close(fig)

        pixmap = QPixmap("physics_p6_graph.png")
        self.label_4.setPixmap(pixmap)
        self.label_4.setScaledContents(True)



class SeventhPage(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("physics_p7_i.ui" , self)

        # for lineEdit and lineEdit_13
        self.lineEdit.textChanged.connect(self.text_changed_lineEdit)
        self.lineEdit_13.textChanged.connect(self.text_changed_lineEdit_13)

        # for lineEdit_2 and lineEdit_14
        self.lineEdit_2.textChanged.connect(self.text_changed_lineEdit_2)
        self.lineEdit_14.textChanged.connect(self.text_changed_lineEdit_14)

        # for lineEdit_3 and lineEdit_15
        self.lineEdit_3.textChanged.connect(self.text_changed_lineEdit_3)
        self.lineEdit_15.textChanged.connect(self.text_changed_lineEdit_15)

        # for lineEdit_4 and lineEdit_16
        self.lineEdit_4.textChanged.connect(self.text_changed_lineEdit_4)
        self.lineEdit_16.textChanged.connect(self.text_changed_lineEdit_16)

        # for lineEdit_5 and lineEdit_17
        self.lineEdit_5.textChanged.connect(self.text_changed_lineEdit_5)
        self.lineEdit_17.textChanged.connect(self.text_changed_lineEdit_17)

        # for lineEdit_6 and lineEdit_18
        self.lineEdit_6.textChanged.connect(self.text_changed_lineEdit_6)
        self.lineEdit_18.textChanged.connect(self.text_changed_lineEdit_18)

        # for lineEdit_7 and lineEdit_19
        self.lineEdit_7.textChanged.connect(self.text_changed_lineEdit_7)
        self.lineEdit_19.textChanged.connect(self.text_changed_lineEdit_19)

        # for lineEdit_8 and lineEdit_20
        self.lineEdit_8.textChanged.connect(self.text_changed_lineEdit_8)
        self.lineEdit_20.textChanged.connect(self.text_changed_lineEdit_20)

        # for lineEdit_9 and lineEdit_21
        self.lineEdit_9.textChanged.connect(self.text_changed_lineEdit_9)
        self.lineEdit_21.textChanged.connect(self.text_changed_lineEdit_21)

        # for lineEdit_10 and lineEdit_22
        self.lineEdit_10.textChanged.connect(self.text_changed_lineEdit_10)
        self.lineEdit_22.textChanged.connect(self.text_changed_lineEdit_22)

        # for lineEdit_11 and lineEdit_23
        self.lineEdit_11.textChanged.connect(self.text_changed_lineEdit_11)
        self.lineEdit_23.textChanged.connect(self.text_changed_lineEdit_23)

        # for lineEdit_12 and lineEdit_24
        self.lineEdit_12.textChanged.connect(self.text_changed_lineEdit_12)
        self.lineEdit_24.textChanged.connect(self.text_changed_lineEdit_24)

        self.pushButton.clicked.connect(self.button_function)

        # HOME
        self.pushButton_8.clicked.connect(self.home)

    def home(self):
        print("Home Button ForthPage")
        self.home_window = FirstPage()
        widget.addWidget(self.home_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)


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
        print("Solve button clicked")

        try:
            # QComboBox symbols
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


            def validate_and_convert(value, label):
                try:
                    return float(value)
                except ValueError:
                    raise ValueError(f"Invalid input in {label}: {value}")


            x1_value = validate_and_convert(x1, "x1") if x1_symbol == '+' else -validate_and_convert(x1, "x1")
            y1_value = validate_and_convert(y1, "y1") if y1_symbol == '+' else -validate_and_convert(y1, "y1")
            z1_value = validate_and_convert(z1, "z1") if z1_symbol == '+' else -validate_and_convert(z1, "z1")
            c1_value = validate_and_convert(c1, "c1") if c1_symbol == '+' else -validate_and_convert(c1, "c1")

            x2_value = validate_and_convert(x2, "x2") if x2_symbol == '+' else -validate_and_convert(x2, "x2")
            y2_value = validate_and_convert(y2, "y2") if y2_symbol == '+' else -validate_and_convert(y2, "y2")
            z2_value = validate_and_convert(z2, "z2") if z2_symbol == '+' else -validate_and_convert(z2, "z2")
            c2_value = validate_and_convert(c2, "c2") if c2_symbol == '+' else -validate_and_convert(c2, "c2")

            x3_value = validate_and_convert(x3, "x3") if x3_symbol == '+' else -validate_and_convert(x3, "x3")
            y3_value = validate_and_convert(y3, "y3") if y3_symbol == '+' else -validate_and_convert(y3, "y3")
            z3_value = validate_and_convert(z3, "z3") if z3_symbol == '+' else -validate_and_convert(z3, "z3")
            c3_value = validate_and_convert(c3, "c3") if c3_symbol == '+' else -validate_and_convert(c3, "c3")

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

            if solution:
                print(f"Solution: x = {solution[x]}, y = {solution[y]}, z = {solution[z]}")
                self.call_window = SeventhPageSolution(solution[x], solution[y], solution[z], eq1, eq2, eq3)
                widget.addWidget(self.call_window)
                widget.setCurrentIndex(widget.currentIndex() + 1)
            else:
                QMessageBox.information(self, "No Solution Found", "Re-enter values or try with different inputs.")

        except ValueError as ve:
            QMessageBox.critical(self, "Input Error", str(ve))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Unexpected error: {e}")


class SeventhPageSolution(QMainWindow):
    def __init__(self , x , y , z , eq1 , eq2 , eq3):
        super().__init__()
        loadUi("physics_p7_ii.ui" , self)

        self.label_7.setText(str(x))
        self.label_8.setText(str(y))
        self.label_9.setText(str(z))

        print(x , y , z)

        self.eq1 = eq1
        self.eq2 = eq2
        self.eq3 = eq3

        self.x = x
        self.y = y
        self.z = z

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
        self.call_window = SeventhGraph(self.x , self.y , self.z , self.eq1 , self.eq2 , self.eq3)
        widget.addWidget(self.call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)




class SeventhGraph(QMainWindow):
    def __init__(self , x , y , z , eq1 , eq2 , eq3):
        super().__init__()
        loadUi("physics_p7_iii.ui" , self)

        self.x = x
        self.y = y
        self.z = z
        self.eq1 = eq1
        self.eq2 = eq2
        self.eq3 = eq3

        self.plot_graph(self.x , self.y , self.z , self.eq1 , self.eq2 , self.eq3)

        self.pushButton.clicked.connect(self.home)
        self.pushButton_8.clicked.connect(self.home)

    def home(self):
        print("Home Button SeventhGraph")
        self.home_window = FirstPage()
        widget.addWidget(self.home_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def plot_graph(self , X_val , Y_val , Z_val , eq1 , eq2 , eq3):
        try:
            fig = plt.figure(figsize=(6 , 4))
            ax = fig.add_subplot(111 , projection='3d')

            x_vals = np.linspace(-50 , 50 , 100)
            y_vals = np.linspace(-50 , 50 , 100)
            X , Y = np.meshgrid(x_vals , y_vals)

            # Extract coefficients for each equation
            a1 , b1 , c1 , d1 = self.get_coefficients(eq1)
            a2 , b2 , c2 , d2 = self.get_coefficients(eq2)
            a3 , b3 , c3 , d3 = self.get_coefficients(eq3)

            # Define functions for Z-values
            func1 = lambda x , y: (d1 - a1 * x - b1 * y) / c1 if c1 != 0 else np.nan
            func2 = lambda x , y: (d2 - a2 * x - b2 * y) / c2 if c2 != 0 else np.nan
            func3 = lambda x , y: (d3 - a3 * x - b3 * y) / c3 if c3 != 0 else np.nan

            # Calculate Z values for the surface plots
            Z_eq1 = func1(X , Y)
            Z_eq2 = func2(X , Y)
            Z_eq3 = func3(X , Y)

            # Plot each equation with a unique contrasting color
            ax.plot_surface(X , Y , Z_eq1 , color='#8B0000' , alpha=0.3 )
            ax.plot_surface(X , Y , Z_eq2 , color='blue' , alpha=0.3)
            ax.plot_surface(X , Y , Z_eq3 , color='orange' , alpha=0.3)

            # Highlight the solution point
            ax.scatter(X_val , Y_val , Z_val , color='black' , s=100 , label='Solution')

            # Set graph limits and labels
            ax.set_xlim(-50 , 50)
            ax.set_ylim(-50 , 50)
            ax.set_zlim(-50 , 50)
            ax.grid(True)
            ax.set_xlabel('X-axis')
            ax.set_ylabel('Y-axis')
            ax.set_zlabel('Z-axis')

            # Save the plot as an image
            fig.savefig("physics_p7_graph.png" , dpi=140 , transparent=True)
            plt.close(fig)

            # Display the image in label_4
            pixmap = QPixmap("physics_p7_graph.png")
            self.label_4.setPixmap(pixmap)
            self.label_4.setScaledContents(True)

        except Exception as e:
            print(f"An error occurred while plotting: {e}")

    def get_coefficients(self , eq):
        coeffs = eq.lhs.as_coefficients_dict()
        a = coeffs.get(sp.symbols('x') , 0)
        b = coeffs.get(sp.symbols('y') , 0)
        c = coeffs.get(sp.symbols('z') , 0)
        d = eq.rhs
        return a , b , c , d

import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication , QMainWindow , QVBoxLayout , QWidget , QStackedWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.uic import loadUi
import sympy as sp


class EightPage(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("physics_p8_i.ui" , self)
        self.pushButton.clicked.connect(self.graph_button_clicked)
        self.pushButton_8.clicked.connect(self.home)

    def home(self):
        print("Home Button SecondPage")
        self.home_window = FirstPage()
        widget.addWidget(self.home_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def graph_button_clicked(self):
        eq1 = self.lineEdit.text()
        eq2 = self.lineEdit_2.text()
        self.call_window = EightPageGraph(eq1 , eq2)
        widget.addWidget(self.call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class EightPageGraph(QMainWindow):
    def __init__(self , eq1 , eq2):
        super().__init__()
        loadUi("physics_p8_ii.ui" , self)

        self.plot_graph(eq1 , eq2)
        self.pushButton.clicked.connect(self.back)
        self.pushButton_8.clicked.connect(self.home)

    def home(self):
        print("Home Button SecondPage")
        self.home_window = FirstPage()
        widget.addWidget(self.home_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def back(self):
        self.call_window = EightPage()
        widget.addWidget(self.call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def parse_expression(self , expr):
        # This method will parse the equation and return a numerical function
        try:
            x = sp.symbols('x')
            parsed_expr = sp.sympify(expr)
            return parsed_expr
        except Exception as e:
            QMessageBox.critical(self,"Error",f"{e}")
            print(f"Error parsing expression: {e}")
            return None

    def plot_graph(self , eq1 , eq2):

        x_vals = np.linspace(-500 , 500 , 5000)

        try:
            # Parse the expressions
            expr1 = self.parse_expression(eq1)
            expr2 = self.parse_expression(eq2)

            if expr1 is None or expr2 is None:
                print("Invalid expressions provided.")
                return

            # Evaluate the expressions for the x values
            y_vals_eq1 = [float(expr1.subs('x' , i)) for i in x_vals]
            y_vals_eq2 = [float(expr2.subs('x' , i)) for i in x_vals]


            plt.plot(x_vals , y_vals_eq1 , label=f"$y = {latex(expr1)}$" , color='darkred')
            plt.plot(x_vals , y_vals_eq2 , label=f"$y = {latex(expr2)}$" , color='darkblue')


            plt.axhline(0 , color='black' , linewidth=1)
            plt.axvline(0 , color='black' , linewidth=1)

            # Grid and limits
            plt.grid(True)
            plt.xlim(-60 , 60)
            plt.ylim(-400 , 500)



            plt.legend()

            # Save the figure
            plt.savefig("physics_p8_graph.png" , dpi=140 , transparent=True)
            plt.close()

            # Load into label_4
            pixmap = QPixmap("physics_p8_graph.png")
            self.label_4.setPixmap(pixmap)
            self.label_4.setScaledContents(True)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"{e}")
            print(f"Error parsing expression: {e}")
            return


class NinePage(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("physics_p9.ui" , self)

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
        self.pushButton_8.clicked.connect(self.home)

    def home(self):
        print("Home Button SecondPage")
        self.home_window = FirstPage()
        widget.addWidget(self.home_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)
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
            except Exception as e:
                print("Invalid input. Please enter valid numbers.")
                QMessageBox.information(self, "Alert", f"{e}")

                return

            # Calculate missing side using Pythagoras theorem
            if b is not None and p is not None and h is None:
                h = math.sqrt(b ** 2 + p ** 2)  # Calculate hypotenuse
                print(f"Calculated Hypotenuse (h): {h:.2f} , Base (b): {b:.2f} , Perpendicular (p): {p:.2f}")
            elif h is not None and p is not None and b is None:
                if h > p:
                    b = math.sqrt(h ** 2 - p ** 2)  # Calculate base
                    print(f"Calculated Base (b): {b:.2f} , Hypotenuse (h): {h:.2f} , Perpendicular (p): {p:.2f}")
                else:
                    print("Invalid input: Hypotenuse must be greater than the Perpendicular.")
                    return
            elif h is not None and b is not None and p is None:
                if h > b:
                    p = math.sqrt(h ** 2 - b ** 2)  # Calculate perpendicular
                    print(f"Calculated Perpendicular (p): {p:.2f} , Hypotenuse (h): {h:.2f} , Base (b): {b:.2f}")
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
            self.lineEdit_2.blockSignals(True)
            self.lineEdit_2.setText(f"{radian_value:.5f}")
            self.lineEdit_2.blockSignals(False)
        except ValueError:
            self.lineEdit_2.clear()
    def radian(self):
        try:
            radian_value = float(self.lineEdit_2.text())
            degree_value = radian_value * 180 / (math.pi)


            self.lineEdit.blockSignals(True)
            self.lineEdit.setText(f"{degree_value:.5f}")
            self.lineEdit.blockSignals(False)
        except ValueError:
            self.lineEdit.clear()

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
                # Use atan to calculate theta , converting back to degrees
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

        print(sin_value , cos_value , tan_value , csc_value , sec_value , cot_value)

        self.call_window = NineGraph(sin_value , cos_value , tan_value , csc_value , sec_value , cot_value)
        widget.addWidget(self.call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class NineGraph(QMainWindow):
    def __init__(self , sin_theta , cos_theta , tan_theta , csc_theta , sec_theta , cot_theta):
        super().__init__()
        loadUi("physics_p9_g_i.ui" , self)
        print("NG 2134" , sin_theta , cot_theta , tan_theta , csc_theta , sec_theta , cot_theta)
        for i in ("NG 2134" , sin_theta , cot_theta , tan_theta , csc_theta , sec_theta , cot_theta):
            print(f"{i} -> type -> {type(i)}")
        self.trig_values = {
            "sin": sin_theta , 
            "cos": cos_theta , 
            "tan": tan_theta , 
            "csc": csc_theta , 
            "sec": sec_theta , 
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
            self.call_window = NineGraphPlot(float(self.trig_values['sin']) , "sin")
            widget.addWidget(self.call_window)
            widget.setCurrentIndex(widget.currentIndex() + 1)
        else:
            msg = QMessageBox(self)
            msg.setWindowTitle("Choose Option")
            msg.setText("Select an option:")

            theta_btn = msg.addButton("Theta" , QMessageBox.AcceptRole)
            value_btn = msg.addButton("Value" , QMessageBox.AcceptRole)
            msg.exec_()

            option = "Theta" if msg.clickedButton() == theta_btn else "Value"

            if option == "Theta":
                data , ok = QInputDialog.getText(self , "Enter the Theta" , "Enter the Value:")
                if ok:
                    print(f"Theta: {data}")
                    self.call_window = NineGraphPlot(math.sin(math.radians(float(data))) , "sin")
                    widget.addWidget(self.call_window)
                    widget.setCurrentIndex(widget.currentIndex() + 1)

            elif option == "Value":
                while True:
                    data , ok = QInputDialog.getText(self , "Enter Value" , "Enter the Value (between -1 and 1):")
                    if ok:
                        try:
                            value = float(data)
                            if -1 <= value <= 1:
                                print(f"Value: {value}")
                                self.call_window = NineGraphPlot(value , "sin")
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
            self.call_window = NineGraphPlot(float(self.trig_values['cos'] ), "cos")
            widget.addWidget(self.call_window)
            widget.setCurrentIndex(widget.currentIndex() + 1)

        else:
            msg = QMessageBox(self)
            msg.setWindowTitle("Choose Option")
            msg.setText("Select an option:")

            theta_btn = msg.addButton("Theta" , QMessageBox.AcceptRole)
            value_btn = msg.addButton("Value" , QMessageBox.AcceptRole)
            msg.exec_()

            option = "Theta" if msg.clickedButton() == theta_btn else "Value"

            if option == "Theta":
                while True:  # Loop until a valid theta is provided
                    data , ok = QInputDialog.getText(self , "Enter the Theta" , "Enter the Value:")
                    if ok:
                        try:
                            theta = float(data)
                            print(f"Valid Theta: {theta}")
                            self.call_window = NineGraphPlot(math.cos(math.radians(theta)) , "cos")
                            widget.addWidget(self.call_window)
                            widget.setCurrentIndex(widget.currentIndex() + 1)
                            break  # Exit the loop on valid Theta
                        except Exception as e:
                            print(f"Error: {e}")
                    else:
                        break
            elif option == "Value":
                data , ok = QInputDialog.getText(self , "Enter Value" , "Enter the Value:")
                if ok:
                    try:
                        value = float(data)
                        print(f"Value: {value}")
                        self.call_window = NineGraphPlot(value , "cos")
                        widget.addWidget(self.call_window)
                        widget.setCurrentIndex(widget.currentIndex() + 1)
                    except Exception as e:
                        print(f"Error: {e}")

    def tan_btn_function(self):
        if self.trig_values['tan'] != "None":
            self.call_window = NineGraphPlot(float(self.trig_values['tan'] ), "tan")
            widget.addWidget(self.call_window)
            widget.setCurrentIndex(widget.currentIndex() + 1)
        else:
            msg = QMessageBox(self)
            msg.setWindowTitle("Choose Option")
            msg.setText("Select an option:")

            theta_btn = msg.addButton("Theta" , QMessageBox.AcceptRole)
            value_btn = msg.addButton("Value" , QMessageBox.AcceptRole)
            msg.exec_()

            option = "Theta" if msg.clickedButton() == theta_btn else "Value"

            if option == "Theta":
                while True:
                    data , ok = QInputDialog.getText(self , "Enter the Theta" , "Enter the Value:")
                    if ok:
                        try:
                            theta = float(data)
                            if theta % 90 == 0 and theta % 180 != 0:
                                print("Invalid Theta for tan function. Please enter a non-multiple of 90.")
                            else:
                                print(f"Valid Theta: {theta}")
                                self.call_window = NineGraphPlot(math.tan(math.radians(theta)) , "tan")
                                widget.addWidget(self.call_window)
                                widget.setCurrentIndex(widget.currentIndex() + 1)
                                break
                        except Exception as e:
                            print(f"Error: {e}")
                    else:
                        break
            elif option == "Value":
                data , ok = QInputDialog.getText(self , "Enter Value" , "Enter the Value:")
                if ok:
                    try:
                        value = float(data)
                        print(f"Value: {value}")
                        self.call_window = NineGraphPlot(value , "tan")
                        widget.addWidget(self.call_window)
                        widget.setCurrentIndex(widget.currentIndex() + 1)
                    except Exception as e:
                        print(f"Error: {e}")

    def csc_btn_function(self):
        if self.trig_values['csc'] != "None":
            self.call_window = NineGraphPlot(float(self.trig_values['csc']) , "csc")
            widget.addWidget(self.call_window)
            widget.setCurrentIndex(widget.currentIndex() + 1)
        else:
            msg = QMessageBox(self)
            msg.setWindowTitle("Choose Option")
            msg.setText("Select an option:")

            theta_btn = msg.addButton("Theta" , QMessageBox.AcceptRole)
            value_btn = msg.addButton("Value" , QMessageBox.AcceptRole)
            msg.exec_()

            option = "Theta" if msg.clickedButton() == theta_btn else "Value"

            if option == "Theta":
                while True:
                    data , ok = QInputDialog.getText(self , "Enter the Theta" , "Enter the Value:")
                    if ok:
                        try:
                            theta = float(data)
                            if theta % 180 == 0:
                                print("Invalid Theta for csc function. Please enter a non-multiple of 180.")
                            else:
                                print(f"Valid Theta: {theta}")
                                self.call_window = NineGraphPlot(1 / math.sin(math.radians(theta)) , "csc")
                                widget.addWidget(self.call_window)
                                widget.setCurrentIndex(widget.currentIndex() + 1)
                                break
                        except Exception as e:
                            print(f"Error: {e}")
                    else:
                        break
            elif option == "Value":
                while True:
                    data , ok = QInputDialog.getText(self , "Enter Value" , "Enter any value except 0:")
                    if ok:
                        try:
                            value = float(data)
                            if value != 0:
                                print(f"Value: {value}")
                                self.call_window = NineGraphPlot(value , "csc")
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
            self.call_window = NineGraphPlot(float(self.trig_values['sec'] ), "sec")
            widget.addWidget(self.call_window)
            widget.setCurrentIndex(widget.currentIndex() + 1)
        else:
            msg = QMessageBox(self)
            msg.setWindowTitle("Choose Option")
            msg.setText("Select an option:")

            theta_btn = msg.addButton("Theta" , QMessageBox.AcceptRole)
            value_btn = msg.addButton("Value" , QMessageBox.AcceptRole)
            msg.exec_()

            option = "Theta" if msg.clickedButton() == theta_btn else "Value"

            if option == "Theta":
                while True:
                    data , ok = QInputDialog.getText(self , "Enter the Theta" , "Enter the Value:")
                    if ok:
                        try:
                            theta = float(data)
                            if theta % 90 == 0 and theta % 180 != 0:
                                print("Invalid Theta for sec function. Please enter a non-multiple of 90.")
                            else:
                                print(f"Valid Theta: {theta}")
                                self.call_window = NineGraphPlot(1 / math.cos(math.radians(theta)) , "sec")
                                widget.addWidget(self.call_window)
                                widget.setCurrentIndex(widget.currentIndex() + 1)
                                break
                        except Exception as e:
                            print(f"Error: {e}")
                    else:
                        break
            elif option == "Value":
                data , ok = QInputDialog.getText(self , "Enter Value" , "Enter the Value:")
                if ok:
                    try:
                        value = float(data)
                        print(f"Value: {value}")
                        self.call_window = NineGraphPlot(value , "sec")
                        widget.addWidget(self.call_window)
                        widget.setCurrentIndex(widget.currentIndex() + 1)
                    except Exception as e:
                        print(f"Error: {e}")

    def cot_btn_function(self):
        if self.trig_values['cot'] != "None":
            self.call_window = NineGraphPlot(float(self.trig_values['cot']) , "cot")
            widget.addWidget(self.call_window)
            widget.setCurrentIndex(widget.currentIndex() + 1)
        else:
            msg = QMessageBox(self)
            msg.setWindowTitle("Choose Option")
            msg.setText("Select an option:")

            theta_btn = msg.addButton("Theta" , QMessageBox.AcceptRole)
            value_btn = msg.addButton("Value" , QMessageBox.AcceptRole)
            msg.exec_()

            option = "Theta" if msg.clickedButton() == theta_btn else "Value"

            if option == "Theta":
                while True:
                    data , ok = QInputDialog.getText(self , "Enter the Theta" , "Enter the Value:")
                    if ok:
                        try:
                            theta = float(data)
                            if theta % 180 == 0:
                                print("Invalid Theta for cot function. Please enter a non-multiple of 180.")
                            else:
                                print(f"Valid Theta: {theta}")
                                self.call_window = NineGraphPlot(1 / math.tan(math.radians(theta)) , "cot")
                                widget.addWidget(self.call_window)
                                widget.setCurrentIndex(widget.currentIndex() + 1)
                                break
                        except Exception as e:
                            print(f"Error: {e}")
                    else:
                        break
            elif option == "Value":
                data , ok = QInputDialog.getText(self , "Enter Value" , "Enter the Value:")
                if ok:
                    try:
                        value = float(data)
                        print(f"Value: {value}")
                        self.call_window = NineGraphPlot(value , "cot")
                        widget.addWidget(self.call_window)
                        widget.setCurrentIndex(widget.currentIndex() + 1)
                    except Exception as e:
                        print(f"Error: {e}")


from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import math
from PyQt5.QtWidgets import QMainWindow , QWidget , QVBoxLayout
from PyQt5.uic import loadUi

import matplotlib.pyplot as plt
import numpy as np
import math
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow , QLabel , QVBoxLayout , QWidget


class NineGraphPlot(QMainWindow):
    def __init__(self , value , trig_type):
        super().__init__()
        loadUi("physics_p9_g_ii.ui" , self)  # Assuming you have loaded the UI
        self.widget = QWidget(self)
        self.widget.setGeometry(110 , 80 , 761 , 381)

        self.theta = self.calculate_inverse_trig(trig_type , value)
        print(self.theta , type(self.theta))

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
            print("Invalid trigonometric function. Please use 'sin' , 'cos' , 'tan' , 'cot' , 'sec' , or 'csc'.")

        self.pushButton_8.clicked.connect(self.home)
        self.pushButton.clicked.connect(self.home)

    def home(self):
        print("Home Button SecondPage")
        self.home_window = FirstPage()
        widget.addWidget(self.home_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)



    def calculate_inverse_trig(self , trig_type , value):
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

    def display_image_in_label(self , image_path):
        pixmap = QPixmap(image_path)
        self.label_4.setPixmap(pixmap)
        self.label_4.setAlignment(Qt.AlignCenter)


    def sin_plot(self , theta):
        x = np.linspace(-2 * np.pi , 2 * np.pi , 1000)
        y_val = [math.sin(i) for i in x]
        sin_val = math.sin(math.radians(theta))

        plt.plot(x , y_val , color="red" , label=f"sin(⊖)" , linewidth=1.2)

        plt.scatter(math.radians(theta) , sin_val , color="blue" , label=f"sin(⊖)={sin_val:.2f} \n ⊖={theta:.2f}°")

        plt.axvline(math.radians(theta) , color="orange" , linestyle="--")

        plt.axhline(0 , color="black" , linewidth=0.8)
        plt.axvline(0 , color="black" , linewidth=0.8)

        plt.grid(True)

        plt.legend()


        plt.savefig(f"physics_p9_sin.png" , transparent=True)
        plt.close()
        print(f"sin(⊖) for ⊖={theta:.2f}° = {sin_val:.2f}")
        self.display_image_in_label("physics_p9_sin.png")
    def cos_plot(self , theta):
        x = np.linspace(-2 * np.pi , 2 * np.pi , 1000)
        y_val = [math.cos(i) for i in x]
        cos_val = math.cos(math.radians(theta))

        plt.plot(x , y_val , color="green" , label=f"cos(⊖)" , linewidth=1.2)
        plt.scatter(math.radians(theta) , cos_val , color="blue" , label=f"cos(⊖)={cos_val:.2f} \n ⊖={theta:.2f}°")
        plt.axvline(math.radians(theta) , color="orange" , linestyle="--")


        plt.axhline(0 , color="black" , linewidth=0.8)
        plt.axvline(0 , color="black" , linewidth=0.8)
        plt.grid(True)
        plt.legend()



        plt.savefig(f"physics_p9_cos.png" , transparent=True)
        plt.close()
        print(f"cos(⊖) for ⊖={theta:.2f}° = {cos_val:.2f}")
        self.display_image_in_label("physics_p9_cos.png")

    def tan_plot(self , theta):

        x = np.linspace(-2 * np.pi , 2 * np.pi , 1000)
        y_val = [math.tan(i) if abs(math.tan(i)) < 10 else None for i in x]
        tan_val = math.tan(math.radians(theta)) if abs(math.tan(math.radians(theta))) < 10 else None

        plt.plot(x , y_val , color="blue" , label=f"tan(⊖)" , linewidth=1.2)
        plt.scatter(math.radians(theta) , tan_val , color="red" , label=f"tan(⊖)={tan_val:.2f} \n ⊖={theta:.2f}°")

        plt.axvline(math.radians(theta) , color="orange" , linestyle="--")
        plt.axhline(0 , color="black" , linewidth=0.8)
        plt.axvline(0 , color="black" , linewidth=0.8)
        plt.grid(True)
        plt.legend()

        plt.savefig(f"physics_p9_tan.png" , transparent=True)
        plt.close()

        print(f"tan(⊖) for ⊖={theta:.2f}° = {tan_val:.2f}" if tan_val else f"tan(⊖) for ⊖={theta:.2f}° is undefined")
        self.display_image_in_label("physics_p9_tan.png")

    def csc_plot(self , theta):

        x = np.linspace(-2 * np.pi , 2 * np.pi , 1000)

        y_val = [1 / math.sin(i) if math.sin(i) != 0 and abs(1 / math.sin(i)) < 10 else None for i in x]
        csc_val = 1 / math.sin(math.radians(theta)) if math.sin(math.radians(theta)) != 0 else None

        plt.plot(x , y_val , color="cyan" , label=f"csc(⊖)" , linewidth=1.2)
        plt.scatter(math.radians(theta) , csc_val , color="blue" , label=f"csc(⊖)={csc_val:.2f} \n ⊖={theta:.2f}°")

        plt.axvline(math.radians(theta) , color="orange" , linestyle="--")

        plt.axhline(0 , color="black" , linewidth=0.8)
        plt.axvline(0 , color="black" , linewidth=0.8)
        plt.grid(True)
        plt.legend()

        plt.savefig(f"physics_p9_csc.png" , transparent=True)
        plt.close()
        print(f"csc(⊖) for ⊖={theta:.2f}° = {csc_val:.2f}" if csc_val else f"csc(⊖) for ⊖={theta:.2f}° is undefined")
        self.display_image_in_label("physics_p9_csc.png")
    def sec_plot(self , theta):

        x = np.linspace(-2 * np.pi , 2 * np.pi , 1000)

        y_val = [1 / math.cos(i) if math.cos(i) != 0 and abs(1 / math.cos(i)) < 10 else None for i in x]
        sec_val = 1 / math.cos(math.radians(theta)) if math.cos(math.radians(theta)) != 0 else None

        plt.plot(x , y_val , color="orange" , label=f"sec(⊖)" , linewidth=1.2)
        plt.scatter(math.radians(theta) , sec_val , color="blue" , label=f"sec(⊖)={sec_val:.2f} \n ⊖={theta:.2f}°")
        plt.axvline(math.radians(theta) , color="orange" , linestyle="--")

        plt.axhline(0 , color="black" , linewidth=0.8)
        plt.axvline(0 , color="black" , linewidth=0.8)
        plt.grid(True)
        plt.legend()

        plt.savefig(f"physics_p9_sec.png" , transparent=True)
        plt.close()
        print(f"sec(⊖) for ⊖={theta:.2f}° = {sec_val:.2f}" if sec_val else f"sec(⊖) for ⊖={theta:.2f}° is undefined")
        self.display_image_in_label("physics_p9_sec.png")

    def cot_plot(self , theta):
        x = np.linspace(-2 * np.pi , 2 * np.pi , 1000)
        y_val = [1 / math.tan(i) if math.tan(i) != 0 and abs(1 / math.tan(i)) < 10 else None for i in x]
        cot_val = 1 / math.tan(math.radians(theta)) if math.tan(math.radians(theta)) != 0 else None

        plt.plot(x , y_val , color="purple" , label=f"cot(⊖)" , linewidth=1.2)
        plt.scatter(math.radians(theta) , cot_val , color="blue" , label=f"cot(⊖)={cot_val:.2f} \n ⊖={theta:.2f}°")

        plt.axvline(math.radians(theta) , color="orange" , linestyle="--")

        plt.axhline(0 , color="black" , linewidth=0.8)
        plt.axvline(0 , color="black" , linewidth=0.8)
        plt.grid(True)
        plt.legend()

        plt.savefig(f"physics_p9_cot.png" , transparent=True)
        plt.close()
        print(f"cot(⊖) for ⊖={theta:.2f}° = {cot_val:.2f}" if cot_val else f"cot(⊖) for ⊖={theta:.2f}° is undefined")
        self.display_image_in_label("physics_p9_cot.png")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QStackedWidget()
    main_wind = FirstPage()
    widget.addWidget(main_wind)
    widget.setFixedSize(main_wind.size())
    widget.show()
    sys.exit(app.exec())

