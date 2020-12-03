t0=10000

m=0.0063

maxx=50

dt=2

u0=10000

file=open('text.txt', 'w')

def f(x,y, t=0,m=-0.0063):

    return (-x*y)

u1=u0+dt*(f(m,u0+dt/2*f(m,u0)))

u2=int

x1=int

x2=int

e=0.00001

print('Время: ',0,';'' ''Значение:',round(u0,3))

print('Время: ',dt,';'' ''Значение:',round(u1,3))

file.write('Время: ')

file.write(str(0)+'; ')

file.write('Значение: ')

file.write(str(round(u0,3))+'\n')

file.write('Время: ')

file.write(str(dt)+'; ')

file.write('Значение: ')

file.write(str(round(u1,3))+'\n')

u0=u1

for i in range(4, maxx+dt, 2):

    f0=f(m,u0)

    f1=f(m,u1)

    u2=u1+dt/2*(3*f1-f0)

    f2=f(m,u2)

    x1=u2

    u2=u1+dt/2*(f1+f2)

    x2=u2

    while (abs(x1-x2))>e:

        x1=x2

        f2=f(m,u2)

        u2=u1+dt/2*(f1+f2)

        x2=u2

    u0=u1

    u1=u2

    print('Время:',i,';'' ''Значение:',round(u2,3))

    file.write('Время: ')

    file.write(str(i)+'; ')

    file.write('Значение: ')

    file.write(str(round(u2,3))+'\n')

file.close()    