
#INPUT
m = float(input("Введите m:\n"))
T0 = float(input("Введите T0:\n"))
dt= int(input("Введите шаг по времени:\n"))
ubound = int(input("Введите конечное время процесса:\n"))
# m = 0.0063
# T0 = 10000
# dt = 2
# ubound = 50



# Для итоговой версии программы для сдачи неважная функция(можно удалить)
#Генерирует последовательность от begin до stop c шагом step PS Нужно для генерации последовательность с округленным float последовательностями
def genRange(begin,end,step):
    rang = []
    while begin <= end:
        rang.append(round(begin,2))
        begin+=step
    return rang


#Исходная функция
def function(x,y,t=0):
    return -x*y

#Исправленный метод Эйлера
#m = Коэф. Вводит пользователь
#y0 = Начальное значение. Вводит пользователь
#method = Ссылка на функцию производной(function)
#dt = Шаг расчета
def euler1(m,y0,dt,f):
    k1 = f(m,y0)*dt
    k2 = f(m,y0+k1)*dt
    dy = (k1+k2)/2
    y1 = y0+dy
    return y1



#Функция генерации массивов с отметками времени и значением y в этот момент
#Аргументы:
#m = Коэф. Вводит пользователь
#y0 = Начальное значение. Вводит пользователь
#f = Функция производной
#method = Ссылка на метод расчета значений(в данном случае исправленный метод эйлера
#dt = Шаг расчета
#ndigits = Количество знаков после запятой
def generateValues(m,y0,f,method,dt,ndigits = 1):
    time_vals = range(0,ubound+dt,dt)
    yvals = []
    y = y0
    for t in time_vals:
        yvals.append(y)
        y = round(method(m,y,dt,f),ndigits)
    return {'time_vals':time_vals,'yvals':yvals}




values = generateValues(m,T0,function,euler1,dt)

#OUTPUT
for x,y in zip(values['time_vals'],values['yvals']):
    print("T:{},Y:{}".format(x,y))
