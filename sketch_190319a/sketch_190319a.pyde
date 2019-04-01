def setup():
    frameRate(60)
    rectMode(CENTER)
    size(300,300)
    krtokakolorow=((255,0,0),(100,100,20),(50,37,12))
    krotkakolorow=[0]
    fill(0, 100, 0)
    strokeWeight(8)
    stroke(krotkakolorow[0])
    global x
    global y
    x=0
    y=0
def draw():
    global x
    x=x+1
    global y
    y=y+1
    rect(height/2,width/2,x,y)  #tu trzeba by zmienć, by zamiast wielkości zmeiniałą się pozycja...
    if x>width:
        exit()
def mousePressed():
    #loop()
    #noLoop()
    #redraw()
    pass