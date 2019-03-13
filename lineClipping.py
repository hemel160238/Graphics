import tkinter as tk
import time
root = tk.Tk()

canvas = tk.Canvas(root, bg="white", width=600, height=400)
canvas.pack()

coords = {"x":0,"y":0,"x2":0,"y2":0}
# keep a reference to all lines by keeping them in a list
lines = []
rectangle = None

# Defining region codes
INSIDE = 0 #0000
LEFT = 1 #0001
RIGHT = 2 #0010
BOTTOM = 4 #0100
TOP = 8	 #10000

buttonLine = canvas.create_rectangle(0, 0, 100, 30, fill="grey40", outline="grey60")
buttonTXTLine = canvas.create_text(50, 15, text="Draw Line")

buttonRectangle = canvas.create_rectangle(0, 30, 100, 60, fill="grey40", outline="grey60")
buttonTXTRectangle = canvas.create_text(50, 40, text="Draw Rectangle")

buttonCrop = canvas.create_rectangle(0, 60, 100, 90, fill="grey40", outline="grey60")
buttonTXTCrop = canvas.create_text(50, 80, text="Crop Lines")


drawMode = 1


def clickedLine(e):
    print("Hello World ")
    root.title('Direct Line')

    global drawMode
    drawMode = 1


def clickedRectangle(e):
    print("Hello World ")
    root.title('Direct Line')

    global drawMode
    drawMode = 2


def computeCode(x, y, rectangle):
    x_min, y_min, x_max, y_max = canvas.coords(rectangle)

    code = INSIDE
    if x < x_min:  # to the left of rectangle
        code |= LEFT
    elif x > x_max:  # to the right of rectangle
        code |= RIGHT
    if y < y_min:  # below the rectangle
        code |= BOTTOM
    elif y > y_max:  # above the rectangle
        code |= TOP

    return code


def cohenSutherlsnd(line, rectangle):
    x1, y1, x2, y2 = canvas.coords(line)
    code1 = computeCode(x1, y1, rectangle)
    code2 = computeCode(x2,y2, rectangle)

    print("------------")
    print(bin(code1))
    print(bin(code2))
    print("------------")
    x_min, y_min, x_max, y_max = canvas.coords(rectangle)
    ok = False

    while (True):


        if (code1 == 0 and code2 == 0):

            print("inf inf inf")
            print('--')
            ok = True
            break

        elif (code1 & code2) != 0:
            break

        else:

            x = 1.0
            y = 1.0

            if code1 != 0:
                code_out = code1

            else:
                code_out = code2

                # Find intersection point
                # using formulas y = y1 + slope * (x - x1),
                # x = x1 + (1 / slope) * (y - y1)
            if code_out & TOP:
                x = x1 + (x2 - x1) * \
                         (y_max - y1) / (y2 - y1)
                y = y_max

            elif code_out & BOTTOM:

                # point is below the clip rectangle
                x = x1 + (x2 - x1) * \
                         (y_min - y1) / (y2 - y1)
                y = y_min

            elif code_out & RIGHT:

                # point is to the right of the clip rectangle
                y = y1 + (y2 - y1) * \
                         (x_max - x1) / (x2 - x1)
                x = x_max

            elif code_out & LEFT:

                # point is to the left of the clip rectangle
                y = y1 + (y2 - y1) * \
                         (x_min - x1) / (x2 - x1)
                x = x_min

            if code_out == code1:
                x1 = x
                y1 = y
                code1 = computeCode(x1, y1, rectangle)

            else:
                x2 = x
                y2 = y
                code2 = computeCode(x2, y2, rectangle)

    x1 = round(x1)
    x2 = round(x2)
    y1 = round(y1)
    y2 = round(y2)

    if ok:
        canvas.coords(line, x1, y1, x2, y2)


    else:
        canvas.delete(line)





def clickedCrop(e):
    global drawMode
    drawMode = 3
    root.title('Clipped')

    canvas.itemconfig(rectangle, fill = "white")
    for line  in lines:

        x1, y1, x2, y2 = canvas.coords(line)

        if(x1 == x2 and y1 == y2):
            pass
        else:

            #print (" Valid Line")
            cohenSutherlsnd(line, rectangle)



def click(e):
    # define start point for line
    coords["x"] = e.x
    coords["y"] = e.y


    if(drawMode == 1):
        # create a line on this point and store it in the list
        lines.append(canvas.create_line(coords["x"], coords["y"], coords["x"], coords["y"]))

    elif(drawMode == 2):

        global rectangle

        if(rectangle != None):
            canvas.delete(rectangle)
        rectangle = canvas.create_rectangle(coords["x"], coords["y"], coords["x"], coords["y"],fill = "#CCE8FF")




def drag(e):
    # update the coordinates from the event
    coords["x2"] = e.x
    coords["y2"] = e.y

    if(drawMode == 1):

        # Change the coordinates of the last created line to the new coordinates
        canvas.coords(lines[-1], coords["x"],coords["y"],coords["x2"],coords["y2"])
    elif(drawMode == 2):

        print(type(rectangle))
        canvas.coords(rectangle, coords["x"], coords["y"], coords["x2"], coords["y2"])
        canvas.tag_lower(rectangle)


canvas.bind("<ButtonPress-1>", click)
canvas.bind("<B1-Motion>", drag)

canvas.tag_bind(buttonLine, "<Button-1>", clickedLine)
canvas.tag_bind(buttonTXTLine, "<Button-1>", clickedLine)

canvas.tag_bind(buttonRectangle, "<Button-1>", clickedRectangle)
canvas.tag_bind(buttonTXTRectangle, "<Button-1>", clickedRectangle)

canvas.tag_bind(buttonCrop, "<Button-1>", clickedCrop)
canvas.tag_bind(buttonTXTCrop, "<Button-1>", clickedCrop)

root.mainloop()