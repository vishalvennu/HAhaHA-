

def widestVerticalDistance(points):
    xlist = []

    for point in points:
        xlist.append(point[0])
    
    xlist.sort()
    xlast = len(xlist)-1
    xgap = 0

    while xlast > 0:
        gap = xlist[xlast] - xlist[xlast-1]
        if gap > xgap:
            xgap = gap
        xlast -= 1

    return xgap
    


points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
print(widestVerticalDistance(points))