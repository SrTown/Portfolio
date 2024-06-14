import cv2
import numpy as np
from scipy.signal import butter
import time
from scipy.fft import fft
import math


energias=[]
energias_totales=[]
fro=[] #Stands for FinalReOrganization
prom=[]
fde=[]
filtered_image=""

p_pachon=[11675.001953125, 19818.896484375, 15051.521484375, 18395.921875, 18755.16015625, 7014.826171875, 11115.4775390625, 16191.4833984375, 21923.056640625]
p_ludving= [13078.220703125, 20439.09375, 10610.3447265625, 20447.4609375, 18672.416015625, 5807.9990234375, 5363.58447265625, 16022.8330078125, 24098.271484375]
p_jefferson=[11404.7724609375, 18808.29296875, 16177.5185546875, 23511.916015625, 18192.056640625, 5941.51513671875, 2872.433349609375, 8118.24755859375, 20528.267578125]
p_mara=[10444.515625, 20435.81640625, 12889.08203125, 18919.77734375, 18665.48828125, 4946.70361328125, 2015.4368896484375, 22542.62109375, 20672.865234375]
p_carlos=[9722.83984375, 19784.845703125, 13268.5537109375, 18907.759765625, 17597.318359375, 5589.6337890625, 7237.80322265625, 10569.9091796875, 20452.794921875]

d_pachon=[900, 900, 900, 900, 900, 900, 900, 900, 900]
d_ludving=[900, 900, 900, 900, 900, 900, 900, 900, 900]
d_jefferson=[900, 800, 900, 900, 900, 900, 900, 900, 900]
d_mara=[900, 900, 900, 900, 900, 900, 900, 900, 900]
d_carlos=[900, 900, 900, 900, 900, 900, 900, 900, 900]



def comparacion(prom):
    n_nombre=0
    n_mara=0;
    n_pachon=0
    n_ludving=0
    n_jefferson=0
    n_carlos=0
    nombre=""
    for i in range(9):
        rango_inferior=p_mara[i]-d_mara[i]
        rango_superior=p_mara[i]+d_mara[i]
        if ((prom[i]<=rango_superior) & (prom[i]>=rango_inferior)):
            n_mara=n_mara+1
            
        rango_inferior=p_pachon[i]-d_pachon[i]
        rango_superior=p_pachon[i]+d_pachon[i]
        if ((prom[i]<=rango_superior) & (prom[i]>=rango_inferior)):
            n_pachon=n_pachon+1
            
        rango_inferior=p_ludving[i]-d_ludving[i]
        rango_superior=p_ludving[i]+d_ludving[i]
        if ((prom[i]<=rango_superior) & (prom[i]>=rango_inferior)):
            n_ludving=n_ludving+1
            
        rango_inferior=p_jefferson[i]-d_jefferson[i]
        rango_superior=p_jefferson[i]+d_jefferson[i]
        if ((prom[i]<=rango_superior) & (prom[i]>=rango_inferior)):
            n_jefferson=n_jefferson+1
            
        rango_inferior=p_carlos[i]-d_carlos[i]
        rango_superior=p_carlos[i]+d_carlos[i]
        if ((prom[i]<=rango_superior) & (prom[i]>=rango_inferior)):
            n_carlos=n_carlos+1
    print("maria", n_mara)
    print("pachon", n_pachon)
    print("jefer", n_jefferson)
    print("carlos", n_carlos)
    print("ludving", n_ludving)
    
    datoo=[n_mara, n_pachon, n_jefferson, n_carlos, n_ludving]
    mayor=0
    for d in datoo:
        if d>mayor:
            mayor=d
    if(mayor==n_mara):
        nombre="Maria Paula"
    if(mayor==n_pachon):   
        nombre="Kevin Pachon"  
    if(mayor==n_jefferson):   
        nombre="Jefferson Perez"   
    if(mayor==n_carlos):   
        nombre="Carlos Villa" 
    if(mayor==n_ludving):   
        nombre="Ludving Beltran"
#     if(prom[1]>=20000):
#         nombre="Carlos Villa" 
    
    return nombre



def reorganization():
    ro=[] #Stands for ReOrganization
    
    for i in range(9):
        for j in range(50): #en realidad 100
            ro.append(energias_totales[j][i])
        fro.append(ro)
        ro=[]
#     fft = np.fft.fft(filtered_image)
    print("FRO:\n",fro)
    prom=[sum(r)/len(r) for r in fro]
    fde=[np.std(r) for r in fro]
    print("Promedios:\n",prom)
    print("Desviaciones:\n",fde)
    nombre=comparacion(prom)
    print(f"Bienvenid@ {nombre}!")
    return nombre
    
    
 
def img_partition(img):
    energias=[]
    #Se obtienen las dimensiones de la imagen
    height, width = img.shape
    channels = 1
    
    #Se calcula la dimension de cada parte
    part_height = height // 3
    part_width = width // 3
    
    #Recorrer cada parte y guardarla
    for i in range(3):
        for j in range(3):
            # Calcular las coordenadas de la parte actual
            x = j * part_width
            y = i * part_height
            # Extraer la parte actual de la imagen
            part = img[y:y + part_height, x:x + part_width]
            # Guardar la parte en un archivo de imagen
            cv2.imwrite('part_{}_{}.jpg'.format(i, j), part)
            #Obtencion de energias de cada una de las partes de la imagen
            energias.append(calculate_energy(part))
    energias_totales.append(energias)
    
    
def calculate_energy(img):
    suma = 0
    n = len(img)
    for i in range(0, n):
        suma = pow(abs(img[i]), 2) + suma
    energy = (1 / n) * suma
    return np.mean(energy)

def butter_highpass(cutoff, fs, order=5):
    nyq = 0.5 * fs  # Nyquist frequency
    normal_cutoff = cutoff / nyq  # Normalize cutoff frequency
    b, a = butter(order, normal_cutoff, btype='highpass')
    return b, a


def apply_butterworth_filter(image, cutoff, fs, order=5):
    if len(image.shape) == 3:  # Color image
        filtered_image = image.copy()
        for channel in range(3):
            filtered_image[:, :, channel] = cv2.filter2D(
                filtered_image[:, :, channel].astype(float), -1,
                butter_highpass(cutoff, fs, order)
            )
    else:  # Grayscale image
        filtered_image = cv2.filter2D(image.astype(float), -1, np.asarray(butter_highpass(cutoff, fs, order)))

    return filtered_image.astype(np.uint8)


def tratamiento(fotico):
    img= cv2.cvtColor(fotico,cv2.COLOR_BGR2GRAY) #Transformación de RGB a escalde grises.
    Filtromediana = cv2.medianBlur(img,5) #(imagen, grado de filtrado)
    cv2.imwrite("grises.jpg",img)
    cv2.imwrite("filtromediana.jpg",Filtromediana)
    suavizado=cv2.GaussianBlur(Filtromediana, (5, 5), 0.5)
    cv2.imwrite("suavizado.jpg",suavizado)
    
    equ = cv2.equalizeHist(Filtromediana)
    cv2.imwrite("nnnn.jpg",equ)
    
    #1
    sobel_image = cv2.Sobel(Filtromediana, cv2.CV_64F, 1, 0, ksize=5)  # Adjust ksize for detail control
    cv2.imwrite("sobel_image.jpg",sobel_image)
    thresh, binary_image = cv2.threshold(Filtromediana, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cv2.imwrite("binary_image.jpg",binary_image)
    
    
    # Convert binary_image to a data type compatible with Sobel image (e.g., cv2.CV_32F)
    binary_image = cv2.convertScaleAbs(binary_image, alpha=1.0, beta=0.0)  # Convert to float32
    cv2.imwrite("binary_image22.jpg",binary_image)

    # Combine results with explicitly specified output data type (optional)
    combined_image = cv2.addWeighted(sobel_image, 0.5, binary_image, 0.5, 0, dtype=cv2.CV_32F)
    cv2.imwrite("combined_image.jpg",combined_image)


    
    kernel = np.ones((3, 3), np.uint8)
    imagen_morfologica = cv2.morphologyEx(combined_image, cv2.MORPH_CLOSE, kernel)
    cv2.imwrite("morfo.jpg",imagen_morfologica)
    normalizada=cv2.normalize(imagen_morfologica,None,0,1,cv2.NORM_MINMAX) #Normalizacion de contraste
    cv2.imwrite("normalizada.jpg",normalizada)
#     
    cutoff = 0.2
    fs=imagen_morfologica.shape[0] #o filtromediana
    filtered_image = apply_butterworth_filter(imagen_morfologica, cutoff, fs)
    cv2.imwrite("filtered_image.jpg",filtered_image)
    
    #Division de la imagen
    img_partition(imagen_morfologica)
    #img_partition(img)

def pachon():
    cv2.namedWindow("captura")
    capture = cv2.VideoCapture(0)
    photos=[]
    while True:
        ret,frame= capture.read()
        #time.sleep(2)
        if not ret:
            print("No se reconoce la camara")
            break
        cv2.imshow("captura",frame)
        if (cv2.waitKey(10)&0xFF==ord('c')):
            print("Procesando imagen...")
            for i in range(50):
                cv2.imwrite("captura_venas.jpg",frame)
                photos.append(frame)
                cv2.destroyAllWindows()
#                 print("Picture taken_{}".format(i))
                tratamiento(frame)
            
            print("Energia total:\n", energias_totales)
            h=reorganization()
            break

    return h
pachon()
