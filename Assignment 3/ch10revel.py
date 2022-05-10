# Chapter10: 2, 3, 9, 10, 12, 13

# 10 - 2
from tkinter import *


class CalcWindow:
    def __init__(self, title, inputField1, inputField2, inputField3, inputField4):
        self.window = Tk()
        self.window.title(title)
        # creates the labels for the window
        self.lbl = Label(self.window, text=inputField1).grid(row=0)
        self.lbl2 = Label(self.window, text=inputField2).grid(row=1)
        self.lbl3 = Label(self.window, text=inputField3).grid(row=2)
        self.lbl4 = Label(self.window, text=inputField4).grid(row=3)
        # The label used for displaying the answer
        self.val = 0
        self.lbl4 = Label(self.window, text=self.val).grid(row=3, column=1)

        # user inputs
        self.input1 = Entry(self.window)
        self.input2 = Entry(self.window)
        self.input3 = Entry(self.window)

        # organizes user inputs
        self.input1.grid(row=0, column=1)
        self.input2.grid(row=1, column=1)
        self.input3.grid(row=2, column=1)

        # creates & organizes 'submit' button
        self.butt = Button(self.window, text="Calculate",
                           command=self.calcButton)
        self.butt.grid(row=4, column=0)

        self.window.mainloop()

    # function that is called when button clicked (callback)
    def calcButton(self):
        cal = InvestCalculator(
            self.input1.get(), self.input2.get(), self.input3.get())
        calVal = str(cal.calcFutureVal())
        labell = Label(self.window, text=calVal)
        labell.grid(row=3, column=1)

# Calculator Logic


class InvestCalculator:
    def __init__(self, investAm, years, annualInRate):
        self._investAm = float(investAm)
        self._years = float(years)
        self._annualInRate = float(annualInRate)

    def calcFutureVal(self):
        return round(self._investAm * (1 + (self._annualInRate/12)) ** (self._years * 12), 2)


# creates an instance of window
CalcWindow("Investment Calculator", "Investment Amount",
        "Years", "Annual Interest Rate", "Future Value")


# 10 - 3
class GeoWindow:
    def __init__(self):
        self.window = Tk()
        self.window.title("Canvas Geometry")
        self.radioNum = IntVar()
        self.checkNuM = IntVar()
        self.color_fill = "white"

        # Place Canvas in Window
        self.canvas = Canvas(self.window, width=500,
                             height=110, bg="white")
        self.canvas.pack()

        # places a frame in window
        self.btnPanel = Frame(self.window)
        self.btnPanel.pack()

        # creates and adds buttons to frame
        self.btnRect = Radiobutton(
            self.btnPanel, text="Rectangle", value=1, variable=self.radioNum, command=self.processRadio).grid(row=1, column=1)

        self.btnCirc = Radiobutton(
            self.btnPanel, text="Oval", value=2, variable=self.radioNum, command=self.processRadio).grid(row=1, column=2)

        self.shapeCol = Checkbutton(
            self.btnPanel, text="Filled", variable=self.checkNuM, command=self.processCheck).grid(row=1, column=3)

        # required for window to be created
        self.window.mainloop()

    def processCheck(self):
        colorArray = ["white", "red"]
        self.color_fill = colorArray[self.checkNuM.get()]
        print("Fill Set to:", self.color_fill)
        self.refresh()

    def processRadio(self):
        if str(self.radioNum.get()) == '1':
            self.canvas.delete("all")
            self.createRect()
        else:
            self.canvas.delete("all")
            self.createOval()

    def createRect(self):
        self.canvas.create_rectangle(
            200, 5, 300, 105, tags="rect", fill=self.color_fill)
        self.canvas.pack()

    def createOval(self):
        self.canvas.create_oval(
            175, 5, 325, 105, fill=self.color_fill, tags="oval")
        self.canvas.pack()

    def refresh(self):
        self.window.update()
        self.canvas.pack()


GeoWindow()


# 10 - 9
class BarChart:
    def __init__(self):
        self.window = Tk()
        self.window.title("Bar Chart")

        Label(self.window, text="Blue", bg="blue").place(x=20, y=20)

        self.window.mainloop()


BarChart()


# 10 - 10
class pieChart:
    def __init__(self):
        self._window = Tk()
        self._window.title("Pie Chart")

        self.canvas = Canvas(self._window, width=200, height=100, bg="white")
        self.canvas.pack()

        cir = 360

        self.canvas.create_arc(10, 10, 190, 100, start=0,
                               extent=cir * .20, width=2, fill="red", tags="arc")
        self.canvas.create_arc(10, 10, 190, 100, start=0,
                               extent=(cir), width=2, fill="white", tags="arc")
        self.canvas.create_arc(10, 10, 190, 100, start=(cir * .30) + cir*.20,
                               extent=(cir*.30), width=2, fill="yellow", tags="arc")
        self.canvas.create_arc(10, 10, 190, 100, start=cir * .60,
                               extent=cir * .40, width=2, fill="purple", tags="arc")

        self._window.mainloop()
        button_panel = Frame(self._window)


pieChart()
