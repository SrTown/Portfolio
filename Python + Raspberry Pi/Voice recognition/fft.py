import numpy as np
from scipy.io import wavfile
import math

print("!!!INICIANDO CALCULOS DE LA FFT¡¡¡")

# FUNCION PARA CALCULAR LA TRANSFORMADA RAPIDA DE FOURIER DE UNA GRABACION
def calculate_fft(audio):
    fs, data = wavfile.read(audio)
    fft = np.fft.fft(data)
    return fft


# FUNCION PARA DIVIDIR EL VECTOR DE LA TRANSFORMADA RAPIDA DE FOURIER EN 
# 2 PARTES IGUALES
def split(array):
    a, b, c, d, e, f, g, h, i, j = np.split(array, 10)
    return a, b, c, d, e, f, g, h, i, j


# FUNCION PARA CALCULAR LA ENERGIA DE LAS PARTES DEL VECTOR DE LA TRANSFORMADA
# RAPIDA DE FOURIER
def calculate_energy(array):
    suma = 0
    n = len(array)
    for i in range(0, n):
        suma = pow(abs(array[i]), 2) + suma
    energy = (1 / n) * suma
    
    return energy
    
def desv_estandar(datos):
    n = len(datos)
    media = sum(datos) / n
    suma_cuadrados = sum((x - media) ** 2 for x in datos)
    desviacion_estandar = math.sqrt(suma_cuadrados / n)
    return desviacion_estandar

def respuesta(a, b, c, d, e, f, g, h, i, j):
    
    cont = 0
    cont2 = 0
    
    if  uc1l <= a <= uc1h:
        print("-------------------------------------------")
        print("LIMITE INFERIROR",uc1l)
        print("a --->",a)
        print("LIMITE SUPERIOR",uc1h)
        print("-------------------------------------------")
        cont += 1
    else:
        cont = cont
    if uc2l <= b <= uc2h:
        cont += 1
    else:
        cont = cont
    if uc3l <= c <= uc3h:
        cont += 1
    else:
        cont = cont
    if uc4l <= d <= uc4h:
        cont += 1
    else:
        cont = cont
    if  uc5l <= e <= uc5h:
        cont += 1
    else:
        cont = cont
    if uc6l <= f <= uc6h:
        cont += 1
    else:
        cont = cont
    if uc7l <= g <= uc7h:
        cont += 1
    else:
        cont = cont
    if uc8l <= h <= uc8h:
        cont += 1
    else:
        cont = cont
    if uc9l <= i <= uc9h:
        cont += 1
    else:
        cont = cont
    if uc10l <= j <= uc10h:
        cont += 1
    else:
        cont = cont
    #cubo
    if  ac1l <= a <= ac1h:
        cont2 += 1
    else:
        cont2 = cont2
    if ac2l <= b <= ac2h:
        cont2 += 1
    else:
        cont2 = cont2
    if ac3l <= c <= ac3h:
        cont2 += 1
    else:
        cont2 = cont2
    if ac4l <= d <= ac4h:
        cont2 += 1
    else:
        cont2 = cont2
    if  ac5l <= e <= ac5h:
        cont2 += 1
    else:
        cont2 = cont2
    if ac6l <= f <= ac6h:
        cont2 += 1
    else:
        cont2 = cont2
    if ac7l <= g <= ac7h:
        cont2 += 1
    else:
        cont2 = cont2
    if ac8l <= h <= ac8h:
        cont2 += 1
    else:
        cont2 = cont2
    if ac9l <= i <= ac9h:
        cont2 += 1
    else:
        cont2 = cont2
    if ac10l <= j <= ac10h:
        cont2 += 1
    else:
        cont2 = cont2
        
    if 6 <= cont <= 10:
        
        print("")
        print("----------------")
        print("DIJISTE ESFERA")
        print("----------------")
        print("")
        
        palabra = "esfera"
        
        print("ACTIVANDO BRAZO ROBOTICO")
        print("")
        print("---> ACTIVANDO MOTOR <---")
        
    elif 6 <= cont2 <= 10:
       
        print("")
        print("----------------")
        print("DIJISTE CUBO")
        print("----------------")
        print("")
        
        palabra = "cubo"
        
        print("ACTIVANDO BRAZO ROBOTICO")
        print("")
        print("--->ACTIVANDO DETECTOR MAPA VENOSO<---")
    
    elif 6 <= cont <= 10 and 6 <= cont2 <= 10:
        print("error")
        palabra = "error"
        
    else:
        print("no dijiste nada")
        palabra = "nada"
        
    print("n-esfera --->",cont)
    
    print("n-cubo --->",cont2)
    if(a>=90):
        palabra="cubo"
    else:
        palabra="esfera"
    
    
        
    return palabra

   
def analisis_audios(arr_mues):
    ffts = []  # Vector para almacenar las transformadas de fourier de las 
           # grabaciones
    ffts_p1 = []  # Vector para almacenar la primera parte de las transformadas
                  # de fourier
    ffts_p2 = []  # Vector para almacenar la segunda parte de las transformadas# de fourier
    ffts_p3 = []
    ffts_p4 = []
    ffts_p5 = []
    ffts_p6 = []
    ffts_p7 = []
    ffts_p8 = []
    ffts_p9 = []
    ffts_p10 = []


    energy_p1 = []  # Vector para almacenar las energias de la primera parte de 
                    # las transformadas de fourier
    energy_p2 = []  # Vector para almacenar las energias de la segunda parte de 
                    # las transformadas de fourier
    energy_p3 = []
    energy_p4 = []
    energy_p5 = []
    energy_p6 = []
    energy_p7 = []
    energy_p8 = []
    energy_p9 = []
    energy_p10 = []

# CICLO PARA REALIZAR EL PROCESO CON CADA UNA DE LAS GRABACIONES
    for j in range(0, len(arr_mues)):
        ffts.append(calculate_fft(arr_mues[j]))  # se calcula la transformada de 
                                                # fourier de la grabacion

        p1, p2, p3, p4, p5, p6, p7, p8, p9, p10 = split(ffts[j])  # se divide el vector de la transformada de 
                                 # fourier de la grabacion en 2

        ffts_p1.append(p1)  # se guarda la parte uno del vector de la 
                            # transformada de fourier de la grabacion

        ffts_p2.append(p2)  # se guarda la parte dos del vector de la 
                            # transformada de fourier de la grabacion
                            
        ffts_p3.append(p3)
        ffts_p4.append(p4)
        ffts_p5.append(p5)
        ffts_p6.append(p6)
        ffts_p7.append(p7)
        ffts_p8.append(p8)
        ffts_p9.append(p9)
        ffts_p10.append(p10)

        energy_p1.append(calculate_energy(ffts_p1[j]))  # se calcula y guarda la 
                                             # energia de la parte uno del vector
                                  # de la transformada de fourier de la grabacion

        energy_p2.append(calculate_energy(ffts_p2[j]))  # se calcula y guarda la 
                                             # energia de la parte dos del vector
                                  # de la transformada de fourier de la grabacion
        energy_p3.append(calculate_energy(ffts_p3[j]))
        energy_p4.append(calculate_energy(ffts_p4[j]))
        energy_p5.append(calculate_energy(ffts_p5[j]))
        energy_p6.append(calculate_energy(ffts_p6[j]))
        energy_p7.append(calculate_energy(ffts_p7[j]))
        energy_p8.append(calculate_energy(ffts_p8[j]))
        energy_p9.append(calculate_energy(ffts_p9[j]))
        energy_p10.append(calculate_energy(ffts_p10[j]))
    

    dv1 = desv_estandar(energy_p1)
    dv2 = desv_estandar(energy_p2)
    dv3 = desv_estandar(energy_p3)
    dv4 = desv_estandar(energy_p4)
    dv5 = desv_estandar(energy_p5)
    dv6 = desv_estandar(energy_p6)
    dv7 = desv_estandar(energy_p7)
    dv8 = desv_estandar(energy_p8)
    dv9 = desv_estandar(energy_p9)
    dv10 = desv_estandar(energy_p10)
        

    # CALCULAR LOS PROMEDIOS DE LAS ENERGIAS DE LAS TRANSFORMADAS DE 
    # FOURIER DE LAS GRABACIONES
    mean1 = np.mean(energy_p1)
    mean2 = np.mean(energy_p2)
    mean3 = np.mean(energy_p3)
    mean4 = np.mean(energy_p4)
    mean5 = np.mean(energy_p5)
    mean6 = np.mean(energy_p6)
    mean7 = np.mean(energy_p7)
    mean8 = np.mean(energy_p8)
    mean9 = np.mean(energy_p9)
    mean10 = np.mean(energy_p10)
    
    k=[mean1,mean2,mean3,mean4,mean5,mean6,mean7,mean8,mean9,mean10]
    print("Promedio")
    print(k)

    #calcular las tolerancias maximas y minimas para los umbrales de cada energia

    error1l = mean1 - dv1
    error1h = mean1 + dv1
    error2l = mean2 - dv2
    error2h = mean2 + dv2
    error3l = mean3 - dv3
    error3h = mean3 + dv3
    error4l = mean4 - dv4
    error4h = mean4 + dv4
    error5l = mean5 - dv3
    error5h = mean5 + dv3
    error6l = mean6 - dv4
    error6h = mean6 + dv4
    error7l = mean3 - dv3
    error7h = mean3 + dv3
    error8l = mean4 - dv4
    error8h = mean4 + dv4
    error9l = mean3 - dv3
    error9h = mean3 + dv3
    error10l = mean4 - dv4
    error10h = mean4 + dv4
    energy_sequence = [mean1, mean2, mean3, mean4, mean5, mean6, mean7, mean8, mean9, mean10]
    
    
    return error1l, error1h, error2l, error2h, error3l, error3h, error4l, error4h, error5l, error5h, error6l, error6h, error7l, error7h, error8l, error8h, error9l, error9h, error10l, error10h

# VECTOR DE GRABACIONES - ESFERA
records =['muestra#0.wav','muestra#1.wav', 'muestra#2.wav', 'muestra#3.wav',
           'muestra#4.wav', 'muestra#5.wav', 'muestra#6.wav',
           'muestra#7.wav', 'muestra#8.wav', 'muestra#9.wav',
           'muestra#10.wav','muestra#11.wav', 'muestra#12.wav',
           'muestra#13.wav','muestra#14.wav', 'muestra#15.wav',
           'muestra#16.wav','muestra#17.wav', 'muestra#18.wav', 
           'muestra#19.wav','muestra#20.wav', 'muestra#21.wav',
           'muestra#22.wav', 'muestra#23.wav', 'muestra#24.wav',
           'muestra#25.wav', 'muestra#26.wav', 'muestra#27.wav',
           'muestra#28.wav', 'muestra#29.wav', 'muestra#30.wav',
           'muestra#31.wav','muestra#32.wav', 'muestra#33.wav',
           'muestra#34.wav','muestra#35.wav', 'muestra#36.wav',
           'muestra#37.wav','muestra#38.wav', 'muestra#39.wav', 
           'muestra#40.wav',
           'muestra#41.wav','muestra#42.wav', 'muestra#43.wav',
           'muestra#44.wav','muestra#45.wav', 'muestra#46.wav',
           'muestra#47.wav','muestra#48.wav', 'muestra#49.wav']
        
records2 = ['muestrac#0.wav','muestrac#1.wav', 'muestrac#2.wav', 'muestrac#3.wav',
           'muestrac#4.wav', 'muestrac#5.wav', 'muestrac#6.wav',
           'muestrac#7.wav', 'muestrac#8.wav', 'muestrac#9.wav',
           'muestrac#10.wav','muestrac#11.wav', 'muestrac#12.wav',
           'muestrac#13.wav','muestrac#14.wav', 'muestrac#15.wav',
           'muestrac#16.wav','muestrac#17.wav', 'muestrac#18.wav', 
           'muestrac#19.wav','muestrac#20.wav', 'muestrac#21.wav',
           'muestrac#22.wav', 'muestrac#23.wav', 'muestrac#24.wav',
           'muestrac#25.wav', 'muestrac#26.wav', 'muestrac#27.wav',
           'muestrac#28.wav', 'muestrac#29.wav', 'muestrac#30.wav',
           'muestrac#31.wav','muestrac#32.wav', 'muestrac#33.wav',
           'muestrac#34.wav','muestrac#35.wav', 'muestrac#36.wav',
           'muestrac#37.wav','muestrac#38.wav', 'muestrac#39.wav', 
           'muestrac#40.wav',
           'muestrac#41.wav','muestrac#42.wav', 'muestrac#43.wav',
           'muestrac#44.wav','muestrac#45.wav', 'muestrac#46.wav',
           'muestrac#47.wav','muestrac#48.wav', 'muestrac#49.wav']
#Desviaciones esfera
uc1l, uc1h, uc2l, uc2h, uc3l, uc3h, uc4l, uc4h, uc5l, uc5h, uc6l, uc6h, uc7l, uc7h, uc8l, uc8h, uc9l, uc9h, uc10l, uc10h = analisis_audios(records)
#Desviaciones cubo
ac1l, ac1h, ac2l, ac2h, ac3l, ac3h, ac4l, ac4h, ac5l, ac5h, ac6l, ac6h, ac7l, ac7h, ac8l, ac8h, ac9l, ac9h, ac10l, ac10h = analisis_audios(records2)

#Modificaciones


de=[uc1l, uc1h, uc2l, uc2h, uc3l, uc3h, uc4l, uc4h, uc5l, uc5h, uc6l, uc6h, uc7l, uc7h, uc8l, uc8h, uc9l, uc9h, uc10l, uc10h]
dc=[ac1l, ac1h, ac2l, ac2h, ac3l, ac3h, ac4l, ac4h, ac5l, ac5h, ac6l, ac6h, ac7l, ac7h, ac8l, ac8h, ac9l, ac9h, ac10l, ac10h]
print("desviaciones esfera")
print(de)
print("dessviaciones cubo")
print(dc)
print("--->FINALIZANDO PROCESO FFT<---")
