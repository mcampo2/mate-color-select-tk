#!/usr/bin/env python3
from tkinter import *
import colorsys
import re

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

# Color Preview
colorText = StringVar()
colorText.set("#FFFFFF")
colorPreview = Canvas(window, bg="#FFFFFF", relief=RIDGE, width=200)
previewSpacer = Label(window, text=" ")
colorPreview.grid(row=1, column=1, rowspan=7, columnspan=1)
previewSpacer.grid(row=1, column=2)

# make sure number is in bounds
def bound(num, bound):
  num = int("".join(re.findall('\d+', "0"+str(num))))
  num = int(num)
  if num < 0: return 0
  elif num > bound: return bound
  else: return round(num)

# make sure number is in bounds
# if out of bounds, continue on the other side
def boundContinuous(num, bound):
  num = int("".join(re.findall('\d+', "0"+str(num))))
  num = int(num)
  if num < 0: return bound
  elif num > bound: return 0
  else: return round(num)

# sets the gui color using rgb
def rgb(*args):
  # first get colors
  (red, green, blue) = args
  red = red + bound(redText.get(), 255)
  green = green + bound(greenText.get(), 255)
  blue = blue + bound(blueText.get(), 255)
  (hue, saturation, value) = colorsys.rgb_to_hsv(red/255, green/255, blue/255)
  # then convert to hex
  red = format(bound(red, 255), '02X')[-2:]
  green = format(bound(green, 255), '02X')[-2:]
  blue = format(bound(blue, 255), '02X')[-2:]
  # # then set colors
  colorText.set("#"+red+green+blue)
  hueText.set(round(hue*360))
  saturationText.set(round(saturation*100))
  valueText.set(round(value*100))


# sets the gui color using hsv
def hsv(*args):
  # first get hsv
  (hue, saturation, value) = args
  hue = boundContinuous(bound(hueText.get(), 360)+hue, 360)/360
  saturation = bound(bound(saturationText.get(), 100)+saturation, 100)/100
  value = bound(bound(valueText.get(), 100)+value, 100)/100
  # then get rgb
  (red, green, blue) = colorsys.hsv_to_rgb(hue, saturation, value)
  red = format(round(red*255), '02X')
  green = format(round(green*255), '02X')
  blue = format(round(blue*255), '02X')
  # then set colors
  colorText.set("#"+red+green+blue)
  hueText.set(boundContinuous(hue*360, 360))
  saturationText.set(bound(saturation*100, 100))
  valueText.set(bound(value*100, 100))

# Hue
hueText = StringVar()
hueLabel = Label(window, text="Hue: ")
hueValue = Entry(window, justify=CENTER, textvariable=hueText, width=4)
hueMinus = Button(window, text=" - ", command=lambda: hsv(-1, 0, 0))
huePlus = Button(window, text="+", command=lambda: hsv(1, 0, 0))
hueLabel.grid(row=1, column=3, sticky=W)
hueValue.grid(row=1, column=4)
hueMinus.grid(row=1, column=5)
huePlus.grid(row=1, column=6)

# Saturation
saturationText = StringVar()
saturationLabel = Label(window, text="Saturation: ")
saturationValue = Entry(window, justify=CENTER, textvariable=saturationText, width=4)
saturationMinus = Button(window, text=" - ", command=lambda: hsv(0, -1, 0))
saturationPlus = Button(window, text="+", command=lambda: hsv(0, 1, 0))
saturationLabel.grid(row=2, column=3, sticky=W)
saturationValue.grid(row=2, column=4)
saturationMinus.grid(row=2, column=5)
saturationPlus.grid(row=2, column=6)

# Value
valueText = StringVar()
valueLabel = Label(window, text="Value: ")
valueValue = Entry(window, justify=CENTER, textvariable=valueText, width=4)
valueMinus = Button(window, text=" - ", command=lambda: hsv(0, 0, -1))
valuePlus = Button(window, text="+", command=lambda: hsv(0, 0, 1))
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
redMinus = Button(window, text=" - ", command=lambda: rgb(-1, 0, 0))
redPlus = Button(window, text="+", command=lambda: rgb(1, 0, 0))
redLabel.grid(row=1, column=9, sticky=W)
redValue.grid(row=1, column=10)
redMinus.grid(row=1, column=11)
redPlus.grid(row=1, column=12)

# Green
greenText = StringVar()
greenLabel = Label(window, text="Green: ")
greenValue = Entry(window, justify=CENTER, textvariable=greenText, width=4)
greenMinus = Button(window, text=" - ", command=lambda: rgb(0, -1, 0))
greenPlus = Button(window, text="+", command=lambda: rgb(0, 1, 0))
greenLabel.grid(row=2, column=9, sticky=W)
greenValue.grid(row=2, column=10)
greenMinus.grid(row=2, column=11)
greenPlus.grid(row=2, column=12)

# Blue
blueText = StringVar()
blueLabel = Label(window, text="Blue: ")
blueValue = Entry(window, justify=CENTER, textvariable=blueText, width=4)
blueMinus = Button(window, text=" - ", command=lambda: rgb(0, 0, -1))
bluePlus = Button(window, text="+", command=lambda: rgb(0, 0, 1))
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
  red = int(colorText.get()[1:3], 16)
  green = int(colorText.get()[3:5], 16)
  blue = int(colorText.get()[5:7], 16)
  redText.set(red)
  greenText.set(green)
  blueText.set(blue)
  rgb(0,0,0)
  colorPreview["bg"] = colorText.get()

colorText.trace('w', callback)
colorLabel = Label(window, text="Color name: ")
colorValue = Entry(window, justify=LEFT, textvariable=colorText, width=16)
colorText.set("#FFFFFF")
colorLabel.grid(row=5, column=3, sticky=W)
colorValue.grid(row=5, column=4, rowspan=1, columnspan=4, pady=5)

# Palette Label
paletteLabel = Label(window, text="Palette: ")
paletteLabel.grid(row=6, column=3, sticky=W)
# Palette Color Chart
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

# Create an event loop
window.mainloop()
