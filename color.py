#!/usr/bin/env python3
from tkinter import *

# Clone of mate-color-select Utility

# Color Constants
COLORS = {
  "A": ["#EF2929", "#CC0000", "#A40000", "#000000"],
  "B": ["#FCAF3E", "#F57900", "#CE5C00", "#2E3436"],
  "C": ["#FCE94F", "#EDD400", "#C4A000", "#555753"],
  "D": ["#8AE234", "#73D216", "#4E9A06", "#888A85"],
  "E": ["#729FCF", "#3465A4", "#204A87", "#BABDB6"],
  "F": ["#AD7FA8", "#75507B", "#5C3566", "#D3D7CF"],
  "G": ["#E9B96E", "#C17D11", "#8F5902", "#EEEEEC"],
  "H": ["#888A85", "#555753", "#2E3436", "#F3F3F3"],
  "I": ["#EEEEEC", "#D3D7CF", "#BABDB6", "#FFFFFF"]
}

# # Create a window
root = Tk()
root.title("MATE Color Selection")
window = Frame(root, padx=5, pady=5)
window.pack()

# Hue
hueText = StringVar()
hueLabel = Label(window, text="Hue: ")
hueValue = Entry(window, justify=CENTER, textvariable=hueText, width=4)
hueMinus = Button(window, text=" - ")
huePlus = Button(window, text="+")
hueLabel.grid(row=1, column=3, sticky=W)
hueValue.grid(row=1, column=4)
hueMinus.grid(row=1, column=5)
huePlus.grid(row=1, column=6)

# Saturation
saturationText = StringVar()
saturationLabel = Label(window, text="Saturation: ")
saturationValue = Entry(window, justify=CENTER, textvariable=saturationText, width=4)
saturationMinus = Button(window, text=" - ")
saturationPlus = Button(window, text="+")
saturationLabel.grid(row=2, column=3, sticky=W)
saturationValue.grid(row=2, column=4)
saturationMinus.grid(row=2, column=5)
saturationPlus.grid(row=2, column=6)

# Value
valueText = StringVar()
valueLabel = Label(window, text="Value: ")
valueValue = Entry(window, justify=CENTER, textvariable=valueText, width=4)
valueMinus = Button(window, text=" - ")
valuePlus = Button(window, text="+")
valueLabel.grid(row=3, column=3, sticky=W)
valueValue.grid(row=3, column=4)
valueMinus.grid(row=3, column=5)
valuePlus.grid(row=3, column=6)

# Spacer
spacer1 = Label(window, text="     ")
spacer2 = Label(window, text="   ")
spacer1.grid(row=1, column=7)
spacer2.grid(row=1, column=8)

# Red
redText = StringVar()
redLabel = Label(window, text="Red: ")
redValue = Entry(window, justify=CENTER, textvariable=redText, width=4)
redMinus = Button(window, text=" - ")
redPlus = Button(window, text="+")
redLabel.grid(row=1, column=9, sticky=W)
redValue.grid(row=1, column=10)
redMinus.grid(row=1, column=11)
redPlus.grid(row=1, column=12)

# Green
greenText = StringVar()
greenLabel = Label(window, text="Green: ")
greenValue = Entry(window, justify=CENTER, textvariable=greenText, width=4)
greenMinus = Button(window, text=" - ")
greenPlus = Button(window, text="+")
greenLabel.grid(row=2, column=9, sticky=W)
greenValue.grid(row=2, column=10)
greenMinus.grid(row=2, column=11)
greenPlus.grid(row=2, column=12)

# Blue
blueText = StringVar()
blueLabel = Label(window, text="Blue: ")
blueValue = Entry(window, justify=CENTER, textvariable=blueText, width=4)
blueMinus = Button(window, text=" - ")
bluePlus = Button(window, text="+")
blueLabel.grid(row=3, column=9, sticky=W)
blueValue.grid(row=3, column=10)
blueMinus.grid(row=3, column=11)
bluePlus.grid(row=3, column=12)

# Horizontal Line
horizontalLine = Canvas(window, height=7)
horizontalLine.create_line(0, 7, 500, 7)
horizontalLine.grid(row=4, column=3, rowspan=1, columnspan=10)

# Color Name
def callback(*args): # TODO
  print(colorText.get())

colorText = StringVar()
colorText.trace('w', callback)
colorLabel = Label(window, text="Color name: ")
colorValue = Entry(window, justify=LEFT, textvariable=colorText, width=16)
colorText.set("#FFFFFF")
colorLabel.grid(row=5, column=3, sticky=W)
colorValue.grid(row=5, column=4, rowspan=1, columnspan=4, pady=5)

# Palette
paletteLabel = Label(window, text="Palette: ")
paletteLabel.grid(row=6, column=3, sticky=W)

# Colors - create labels
colorsFrame = Frame(window)
colorsA0 = Label(colorsFrame, bg=COLORS["A"][0], text="          ", relief=RIDGE)
colorsA1 = Label(colorsFrame, bg=COLORS["A"][1], text="          ", relief=RIDGE)
colorsA2 = Label(colorsFrame, bg=COLORS["A"][2], text="          ", relief=RIDGE)
colorsA3 = Label(colorsFrame, bg=COLORS["A"][3], text="          ", relief=RIDGE)
colorsB0 = Label(colorsFrame, bg=COLORS["B"][0], text="          ", relief=RIDGE)
colorsB1 = Label(colorsFrame, bg=COLORS["B"][1], text="          ", relief=RIDGE)
colorsB2 = Label(colorsFrame, bg=COLORS["B"][2], text="          ", relief=RIDGE)
colorsB3 = Label(colorsFrame, bg=COLORS["B"][3], text="          ", relief=RIDGE)
colorsC0 = Label(colorsFrame, bg=COLORS["C"][0], text="          ", relief=RIDGE)
colorsC1 = Label(colorsFrame, bg=COLORS["C"][1], text="          ", relief=RIDGE)
colorsC2 = Label(colorsFrame, bg=COLORS["C"][2], text="          ", relief=RIDGE)
colorsC3 = Label(colorsFrame, bg=COLORS["C"][3], text="          ", relief=RIDGE)
colorsD0 = Label(colorsFrame, bg=COLORS["D"][0], text="          ", relief=RIDGE)
colorsD1 = Label(colorsFrame, bg=COLORS["D"][1], text="          ", relief=RIDGE)
colorsD2 = Label(colorsFrame, bg=COLORS["D"][2], text="          ", relief=RIDGE)
colorsD3 = Label(colorsFrame, bg=COLORS["D"][3], text="          ", relief=RIDGE)
colorsE0 = Label(colorsFrame, bg=COLORS["E"][0], text="          ", relief=RIDGE)
colorsE1 = Label(colorsFrame, bg=COLORS["E"][1], text="          ", relief=RIDGE)
colorsE2 = Label(colorsFrame, bg=COLORS["E"][2], text="          ", relief=RIDGE)
colorsE3 = Label(colorsFrame, bg=COLORS["E"][3], text="          ", relief=RIDGE)
colorsF0 = Label(colorsFrame, bg=COLORS["F"][0], text="          ", relief=RIDGE)
colorsF1 = Label(colorsFrame, bg=COLORS["F"][1], text="          ", relief=RIDGE)
colorsF2 = Label(colorsFrame, bg=COLORS["F"][2], text="          ", relief=RIDGE)
colorsF3 = Label(colorsFrame, bg=COLORS["F"][3], text="          ", relief=RIDGE)
colorsG0 = Label(colorsFrame, bg=COLORS["G"][0], text="          ", relief=RIDGE)
colorsG1 = Label(colorsFrame, bg=COLORS["G"][1], text="          ", relief=RIDGE)
colorsG2 = Label(colorsFrame, bg=COLORS["G"][2], text="          ", relief=RIDGE)
colorsG3 = Label(colorsFrame, bg=COLORS["G"][3], text="          ", relief=RIDGE)
colorsH0 = Label(colorsFrame, bg=COLORS["H"][0], text="          ", relief=RIDGE)
colorsH1 = Label(colorsFrame, bg=COLORS["H"][1], text="          ", relief=RIDGE)
colorsH2 = Label(colorsFrame, bg=COLORS["H"][2], text="          ", relief=RIDGE)
colorsH3 = Label(colorsFrame, bg=COLORS["H"][3], text="          ", relief=RIDGE)
colorsI0 = Label(colorsFrame, bg=COLORS["I"][0], text="          ", relief=RIDGE)
colorsI1 = Label(colorsFrame, bg=COLORS["I"][1], text="          ", relief=RIDGE)
colorsI2 = Label(colorsFrame, bg=COLORS["I"][2], text="          ", relief=RIDGE)
colorsI3 = Label(colorsFrame, bg=COLORS["I"][3], text="          ", relief=RIDGE)
# Colors - add events
colorsA0.bind("<Double-Button>", lambda e: colorText.set(COLORS["A"][0]))
colorsA1.bind("<Double-Button>", lambda e: colorText.set(COLORS["A"][1]))
colorsA2.bind("<Double-Button>", lambda e: colorText.set(COLORS["A"][2]))
colorsA3.bind("<Double-Button>", lambda e: colorText.set(COLORS["A"][3]))
colorsB0.bind("<Double-Button>", lambda e: colorText.set(COLORS["B"][0]))
colorsB1.bind("<Double-Button>", lambda e: colorText.set(COLORS["B"][1]))
colorsB2.bind("<Double-Button>", lambda e: colorText.set(COLORS["B"][2]))
colorsB3.bind("<Double-Button>", lambda e: colorText.set(COLORS["B"][3]))
colorsC0.bind("<Double-Button>", lambda e: colorText.set(COLORS["C"][0]))
colorsC1.bind("<Double-Button>", lambda e: colorText.set(COLORS["C"][1]))
colorsC2.bind("<Double-Button>", lambda e: colorText.set(COLORS["C"][2]))
colorsC3.bind("<Double-Button>", lambda e: colorText.set(COLORS["C"][3]))
colorsD0.bind("<Double-Button>", lambda e: colorText.set(COLORS["D"][0]))
colorsD1.bind("<Double-Button>", lambda e: colorText.set(COLORS["D"][1]))
colorsD2.bind("<Double-Button>", lambda e: colorText.set(COLORS["D"][2]))
colorsD3.bind("<Double-Button>", lambda e: colorText.set(COLORS["D"][3]))
colorsE0.bind("<Double-Button>", lambda e: colorText.set(COLORS["E"][0]))
colorsE1.bind("<Double-Button>", lambda e: colorText.set(COLORS["E"][1]))
colorsE2.bind("<Double-Button>", lambda e: colorText.set(COLORS["E"][2]))
colorsE3.bind("<Double-Button>", lambda e: colorText.set(COLORS["E"][3]))
colorsF0.bind("<Double-Button>", lambda e: colorText.set(COLORS["F"][0]))
colorsF1.bind("<Double-Button>", lambda e: colorText.set(COLORS["F"][1]))
colorsF2.bind("<Double-Button>", lambda e: colorText.set(COLORS["F"][2]))
colorsF3.bind("<Double-Button>", lambda e: colorText.set(COLORS["F"][3]))
colorsG0.bind("<Double-Button>", lambda e: colorText.set(COLORS["G"][0]))
colorsG1.bind("<Double-Button>", lambda e: colorText.set(COLORS["G"][1]))
colorsG2.bind("<Double-Button>", lambda e: colorText.set(COLORS["G"][2]))
colorsG3.bind("<Double-Button>", lambda e: colorText.set(COLORS["G"][3]))
colorsH0.bind("<Double-Button>", lambda e: colorText.set(COLORS["H"][0]))
colorsH1.bind("<Double-Button>", lambda e: colorText.set(COLORS["H"][1]))
colorsH2.bind("<Double-Button>", lambda e: colorText.set(COLORS["H"][2]))
colorsH3.bind("<Double-Button>", lambda e: colorText.set(COLORS["H"][3]))
colorsI0.bind("<Double-Button>", lambda e: colorText.set(COLORS["I"][0]))
colorsI1.bind("<Double-Button>", lambda e: colorText.set(COLORS["I"][1]))
colorsI2.bind("<Double-Button>", lambda e: colorText.set(COLORS["I"][2]))
colorsI3.bind("<Double-Button>", lambda e: colorText.set(COLORS["I"][3]))
# Colors - place elements
colorsA0.grid(row=1, column=1, padx=1, pady=1)
colorsA1.grid(row=2, column=1, padx=1, pady=1)
colorsA2.grid(row=3, column=1, padx=1, pady=1)
colorsA3.grid(row=4, column=1, padx=1, pady=1)
colorsB0.grid(row=1, column=2, padx=1, pady=1)
colorsB1.grid(row=2, column=2, padx=1, pady=1)
colorsB2.grid(row=3, column=2, padx=1, pady=1)
colorsB3.grid(row=4, column=2, padx=1, pady=1)
colorsC0.grid(row=1, column=3, padx=1, pady=1)
colorsC1.grid(row=2, column=3, padx=1, pady=1)
colorsC2.grid(row=3, column=3, padx=1, pady=1)
colorsC3.grid(row=4, column=3, padx=1, pady=1)
colorsD0.grid(row=1, column=4, padx=1, pady=1)
colorsD1.grid(row=2, column=4, padx=1, pady=1)
colorsD2.grid(row=3, column=4, padx=1, pady=1)
colorsD3.grid(row=4, column=4, padx=1, pady=1)
colorsE0.grid(row=1, column=5, padx=1, pady=1)
colorsE1.grid(row=2, column=5, padx=1, pady=1)
colorsE2.grid(row=3, column=5, padx=1, pady=1)
colorsE3.grid(row=4, column=5, padx=1, pady=1)
colorsF0.grid(row=1, column=6, padx=1, pady=1)
colorsF1.grid(row=2, column=6, padx=1, pady=1)
colorsF2.grid(row=3, column=6, padx=1, pady=1)
colorsF3.grid(row=4, column=6, padx=1, pady=1)
colorsG0.grid(row=1, column=7, padx=1, pady=1)
colorsG1.grid(row=2, column=7, padx=1, pady=1)
colorsG2.grid(row=3, column=7, padx=1, pady=1)
colorsG3.grid(row=4, column=7, padx=1, pady=1)
colorsH0.grid(row=1, column=8, padx=1, pady=1)
colorsH1.grid(row=2, column=8, padx=1, pady=1)
colorsH2.grid(row=3, column=8, padx=1, pady=1)
colorsH3.grid(row=4, column=8, padx=1, pady=1)
colorsI0.grid(row=1, column=9, padx=1, pady=1)
colorsI1.grid(row=2, column=9, padx=1, pady=1)
colorsI2.grid(row=3, column=9, padx=1, pady=1)
colorsI3.grid(row=4, column=9, padx=1, pady=1)
colorsFrame.grid(row=7, column=3, rowspan=1, columnspan=10)

# Color Preview
colorPreview = Canvas(window, bg="#FFFFFF", relief=RIDGE, width=200)
previewSpacer = Label(window, text=" ")
colorPreview.grid(row=1, column=1, rowspan=7, columnspan=1)
previewSpacer.grid(row=1, column=2)

# Create an event loop
window.mainloop()
