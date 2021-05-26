def a(speed):
    i=75
    points=0
    while i<=speed:
        if speed>70:
            points=points+1
            i=i+5
    print("points =",points)
    if(points>12):
        print("lisence suspended")
    if (speed<70):
        print("ok")
a(80)

