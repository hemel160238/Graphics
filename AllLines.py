import math
def direct_line(x1, y1, x2, y2):

    m = (y2 - y1) / (x2 - x1)
    c = y2 - m * x2

    if ((m > -1 and m < 0) and (x2 < x1)) or (m > 0  and x2 < x1) or (m < -1  and y2 < y1):

        tempVar = x1
        x1 = x2
        x2 = tempVar

        tempVar = y1
        y1 = y2
        y2 = tempVar

    xVector = []
    yVector = []


    if abs(m) < 1:

        for xi in range(x1, x2):
            yi = m * xi + c
            rounded_y = int(yi + 0.5)

            xVector.append(xi)
            yVector.append(rounded_y)

    else:

        for yi in range(y1, y2):
            xi = (yi - c) / m

            rounded_xi = int(xi + 0.5)

            xVector.append(rounded_xi)
            yVector.append(yi)


    return [xVector, yVector]
def dda_algo(x1, y1, x2, y2):

    m = (y2 - y1) / (x2 - x1)
    c = y2 - m * x2

    if ((m > -1 and m < 0) and (x2 < x1)) or (m > 0  and x2 < x1) or (m < -1  and y2 < y1):

        tempVar = x1
        x1 = x2
        x2 = tempVar

        tempVar = y1
        y1 = y2
        y2 = tempVar


    x = x1
    y = y1

    xVector = [x]
    yVector = [y]

    incForx = 1/m

    i = 1

    if abs(m) < 1:

        for xi in range(x1, x2):

            yi = yVector[i-1] + m

            xVector.append(xi)
            yVector.append(yi)

            i = i+1

    else:


        for yi in range(y1, y2):

            xi = xVector[i-1] + incForx

            xVector.append(xi)
            yVector.append(yi)

            i = i+1

    i = 0
    for xCoords in xVector:
        xVector[i] = round(xVector[i])
        yVector[i] = round(yVector[i])
        i = i+1

    return [xVector, yVector]
def bresenham_line(x1, y1, x2, y2):

    m = (y2 - y1) / (x2 - x1)


    if( m > 0):

        if(x1 > x2):
            tempVar = x1
            x1 = x2
            x2 = tempVar

            tempVar = y1
            y1 = y2
            y2 = tempVar
        xVector = []
        yVector = []

        x = x1
        y = y1

        dx = x2 - x1
        dy = y2 - y1

        if (abs(m) < 1):

            dT = 2 * (dy - dx)
            dS = 2 * dy

            d = 2 * dy - dx

            xVector.append(x)
            yVector.append(y)

            while x < x2:
                x = x + 1

                if (d < 0):
                    d = d + dS

                else:
                    y = y + 1
                    d = d + dT

                xVector.append(x)
                yVector.append(y)

        else:

            dT = 2 * (dx - dy)
            dS = 2 * dx

            d = 2 * dy - dx

            xVector.append(x)
            yVector.append(y)

            while y < y2:
                y = y + 1

                if (d < 0):
                    d = d + dS

                else:
                    x = x + 1
                    d = d + dT

                xVector.append(x)
                yVector.append(y)

        return [xVector, yVector]
    elif (m < 0):

        if(y1 < y2):
            tempVar = x1
            x1 = x2
            x2 = tempVar

            tempVar = y1
            y1 = y2
            y2 = tempVar
        xVector = []
        yVector = []

        x = x1
        y = y1

        dx = x2 - x1
        dy = y2 - y1

        if (abs(m) < 1):

            dT = 2 * (dy + dx)
            dS = 2 * dy

            d = 2 * dy - dx

            xVector.append(x)
            yVector.append(y)

            while x < x2:
                x = x + 1

                if (d < 0):
                    d = d - dS

                else:
                    y = y - 1
                    d = d - dT

                xVector.append(x)
                yVector.append(y)

        else:

            dT = 2 * (dx + dy)
            dS = 2 * dx

            d = (2 * dy) - dx

            xVector.append(x)
            yVector.append(y)

            while y > y2:
                y = y - 1

                if (d < 0):
                    d = d + dS

                else:
                    x = x + 1
                    d = d + dT

                xVector.append(x)
                yVector.append(y)

    return [xVector, yVector]
def bresenham_circle(x1, y1, x2, y2):
    # init vars
    r = int(math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2)))
    d = 3 - (2 * r)

    xVector = []
    yVector = []


    x = 0
    y = r



    while x <= y:



        xVector.append(x)
        yVector.append(-y)

        xVector.append(y)
        yVector.append(-x)

        # second quarter 3rd octant
        xVector.append(y)
        yVector.append(x)

        # second quarter 4.octant
        xVector.append(x)
        yVector.append(y)

        # third quarter 5.octant
        xVector.append(-x)
        yVector.append(y)

        # third quarter 6.octant
        xVector.append(-y)
        yVector.append(x)

        # fourth quarter 7.octant
        xVector.append(-y)
        yVector.append(-x)

        # fourth quarter 8.octant
        xVector.append(-x)
        yVector.append(-y)

        if d < 0:
            d = d + (4 * x) + 6
        else:
            d = d + (4 * (x - y)) + 10
            y = y - 1
        x = x + 1
    return [xVector, yVector]


def midpoint_circle(x1, y1, x2, y2):
    # init vars
    r = int(math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2)))
    p = 1-r

    xVector = []
    yVector = []


    x = 0
    y = r



    while x <= y:



        xVector.append(x)
        yVector.append(-y)

        xVector.append(y)
        yVector.append(-x)

        # second quarter 3rd octant
        xVector.append(y)
        yVector.append(x)

        # second quarter 4.octant
        xVector.append(x)
        yVector.append(y)

        # third quarter 5.octant
        xVector.append(-x)
        yVector.append(y)

        # third quarter 6.octant
        xVector.append(-y)
        yVector.append(x)

        # fourth quarter 7.octant
        xVector.append(-y)
        yVector.append(-x)

        # fourth quarter 8.octant
        xVector.append(-x)
        yVector.append(-y)

        if p < 0:
            p = p + 2*x + 3
        else:
            p = p + 2*(x - y) + 5
            y = y - 1
        x = x + 1
    return [xVector, yVector]
