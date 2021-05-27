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


colorsFrame = Frame(window)
for col in COLORS:
  for row in range(len(COLORS[col])):
    # Colors - create labels
    color = Label(colorsFrame, bg=COLORS[col][row], text="          ", relief=RIDGE)
    # Colors - add events
    color.bind("<Double-Button>", lambda e,col=col,row=row: colorText.set(COLORS[col][row]))
    # Colors - place elements
    color.grid(row=row+1, column=ord(col)-ord('A')+1, padx=1, pady=1)
colorsFrame.grid(row=7, column=3, rowspan=1, columnspan=10)

# Color Preview
colorPreview = Canvas(window, bg="#FFFFFF", relief=RIDGE, width=200)
previewSpacer = Label(window, text=" ")
colorPreview.grid(row=1, column=1, rowspan=7, columnspan=1)
previewSpacer.grid(row=1, column=2)

# Create an event loop
window.mainloop()
