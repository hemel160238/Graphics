import tkinter as tk
from AllLines import *
import time

root = tk.Tk()


canvas = tk.Canvas(root, bg="white", width=600, height=400)
canvas.pack()


#mode var

drawMode = 1
coords = {"x": 0, "y": 0, "x2": 0, "y2": 0}
# keep a reference to all lines by keeping them in a list
lines = []
temp_components = []

buttonLine1 = canvas.create_rectangle(0, 0, 100, 30, fill="grey40", outline="grey60")
buttonTXTLine1 = canvas.create_text(50, 15, text="Simple Line")

buttonLine2 = canvas.create_rectangle(0, 30, 100, 60, fill="grey40", outline="grey60")
buttonTXTLine2 = canvas.create_text(50, 40, text="Second Line")

buttonLine3 = canvas.create_rectangle(0, 60, 100, 90, fill="grey40", outline="grey60")
buttonTXTLine3 = canvas.create_text(50, 80, text="Third Line")

def clickedLine1(e):
    print("Hello World ")
    root.title('First One')

    global drawMode
    drawMode = 1

def clickedLine2(e):
    print("Hello World ")
    root.title('Second One')

    global drawMode
    drawMode = 2

def clickedLine3(e):
    print("Hello World ")
    root.title('Third One')

    global drawMode
    drawMode = 3


def click(e):
    # define start point for line
    coords["x"] = e.x
    coords["y"] = e.y

    # create a line on this point and store it in the list
    #lines.append(canvas.create_line(coords["x"], coords["y"], coords["x"], coords["y"]))


def drag(e):
    # update the coordinates from the event
    coords["x2"] = e.x
    coords["y2"] = e.y

    # Change the coordinates of the last created line to the new coordinates
    # canvas.coords(lines[-1], coords["x"],coords["y"],coords["x2"],coords["y2"])
    draw()


def draw():

    #CLear Elements in Temp_Components, clearing all excepting Buttons
    for elements in temp_components:
        canvas.delete(elements)

    # canvas.create_line(store['x'],store['y'],store['x2'],store['y2'])
    y_axis = canvas.create_line(coords['x'], 0, coords['x'], 400, fill="green")
    x_axis = canvas.create_line(0, coords['y'], 600, coords['y'], fill="green")

    pointer_oval = canvas.create_oval(coords['x2'], coords['y2'], coords['x2'], coords['y2'], fill = 'green', width = '4')

    #Adding Axises and pointing oval to temp_list as they should be cleared
    temp_components.extend([y_axis, x_axis, pointer_oval])



    x1 = coords['x']
    x2 = coords['x2']

    y1 = coords['y']
    y2 = coords['y2']

    m = (y2 - y1) / (x2 - x1)
    c = y2 - m * x2

    xVector = []
    yVector = []

    if drawMode ==1:
        coordsList = first_algo(x1, y1, x2, y2)

    elif drawMode == 2:
        coordsList = second_algo(x1, y1, x2, y2)

    elif drawMode == 3:
        coordsList = third_algo(x1, y1, x2, y2)

   # coordsList = third_algo(m, c, x1, y1, x2, y2)
   #print(coordsList)

    if abs(m) < 1:

        for xi in range(x1, x2):
            yi = m * xi + c
            rounded_y = int(yi + 0.5)

            xVector.append(xi)
            yVector.append(rounded_y)

    else:

        for yi in range(y1, y2):
            xi = (yi - c) / m

    xVector = coordsList[0]
    yVector = coordsList[1]

    for i in range(0, len(xVector) - 1):

        if (i % 2 == 0):

            #adding Lines to temp component
            temp_components.append(canvas.create_line(xVector[i], yVector[i], xVector[i + 1], yVector[i + 1], fill="red"))
        else:
            temp_components.append(canvas.create_line(xVector[i], yVector[i], xVector[i + 1], yVector[i + 1], fill="blue"))
            
            


canvas.bind("<ButtonPress-1>", click)
canvas.bind("<B1-Motion>", drag)

#adding Button Click Event
canvas.tag_bind(buttonLine1, "<Button-1>", clickedLine1)
canvas.tag_bind(buttonTXTLine1, "<Button-1>", clickedLine1)

canvas.tag_bind(buttonLine2, "<Button-1>", clickedLine2)
canvas.tag_bind(buttonTXTLine2, "<Button-1>", clickedLine2)

canvas.tag_bind(buttonLine3, "<Button-1>", clickedLine3)
canvas.tag_bind(buttonTXTLine3, "<Button-1>", clickedLine3)

root.mainloop()