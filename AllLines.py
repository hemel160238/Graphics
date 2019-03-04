def first_algo(x1, y1, x2, y2):

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
def second_algo(x1, y1, x2, y2):

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
        print(y2-y1)
        print(m)
        print(incForx)

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
    '''
    print("-------------")
    print(xVector)
    print(m)
    print(yVector)
    print("-------------")'''

    #print(str(len(xVector))+" and "+str(len(yVector)))

    return [xVector, yVector]
def third_algo(x1, y1, x2, y2):

    m = (y2 - y1) / (x2 - x1)
    

    print(m)
    xVector = []
    yVector = []

    x = x1
    y = y1

    dx = x2 - x1
    dy = y2 - y1
    dT = 2*(dy - dx)
    dS = 2*dy

    d = 2*dy - dx

    xVector.append(x)
    yVector.append(y)

    while x < x2:
        x = x+1

        if(d < 0):
            d = d+dS

        else:
            y = y+1
            d = d+dT

        xVector.append(x)
        yVector.append(y)

    return [xVector, yVector]
