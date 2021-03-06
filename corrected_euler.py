
#INPUT
# m = float(input("Введите m:\n"))
# T0 = float(input("Введите T0:\n"))
# dt= int(input("Введите шаг по времени:\n"))
# ubound = int(input("Введите конечное время процесса:\n"))
m = 0.0063
T0 = 10000
dt = 2
ubound = 50



# Для итоговой версии программы для сдачи неважная функция(можно удалить)
#Генерирует последовательность от begin до stop c шагом step PS Нужно для генерации последовательность с округленным float последовательностями
def genRange(begin,end,step):
    rang = []
    while begin <= end:
        rang.append(round(begin,2))
        begin+=step
    return rang


#Исходная функция
def function(t,y,m):
    return -m*y+t*t

#Исправленный метод Эйлера
#m = Коэф. Вводит пользователь
#y0 = Начальное значение. Вводит пользователь
#method = Ссылка на функцию производной(function)
#dt = Шаг расчета
def euler1(m,y0,t,dt,f):
    k1 = f(t,y0,m)*dt
    k2 = f(t+dt,y0+k1,m)*dt
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
def generateValues(m,y0,f,method,dt):
    time_vals = range(0,ubound+dt,dt)
    yvals = []
    y = y0
    for time in time_vals:
        yvals.append(y)
        y = method(m,y,time,dt,f)
    return {'time_vals':time_vals,'y_vals':yvals}




values = generateValues(m,T0,function,euler1,dt)
ndigits = 2
#OUTPUT
for t,y in zip(values['time_vals'],values['y_vals']):
    print("time:{},T:{}".format(t,round(y,ndigits)))
    

#OUTPUT TXT FILE
with open('result.txt','w',encoding="utf-8") as file_with_results:
    file_with_results.write("Результат для введенных аргументов:\n\n")
    file_with_results.write("m={}\n".format(m))
    file_with_results.write("T0(начальное значение)={}\n".format(T0))
    file_with_results.write("Шаг по времени={}\n".format(dt))
    file_with_results.write("Конечное время процесса={}\n".format(ubound))
    file_with_results.write("\n")
    for t,y in zip(values['time_vals'],values['y_vals']):
        file_with_results.write('time:{};T:{}\n'.format(t,round(y,ndigits)))
file_with_results.close()
