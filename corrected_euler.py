import matplotlib.pyplot as plt



#INPUT
m = 0.0063
T0 = 10000
dt = 2
ubound = 50


def genRange(begin,end,step):
    rang = []
    while begin <= end:
        rang.append(round(begin,2))
        begin+=step
    return rang


def function(x,y,t=0):
    return -x*y

def euler1(m,y0,dt,method):

    k1 = method(m,y0)*dt
    k2 = method(m,y0+k1)*dt
    dy = (k1+k2)/2
    y1 = y0+dy
    #print("DT:{},K1:{},K2:{},dy:{},y1:{},Y0:{}".format(dt,k1,k2,dy,y1,y0))
    return y1




def generateValues(m,y0,f,method):
    time_vals = range(0,ubound+dt,dt)
    yvals = []
    y = y0
    for t in time_vals:
        yvals.append(y)
        y = round(method(m,y,dt,f),6)
    return {'time_vals':time_vals,'yvals':yvals}




values = generateValues(m,T0,function,euler1)

for x,y in zip(values['time_vals'],values['yvals']):
    print("T:{},Y:{}".format(x,y))






