import cv2
import numpy as np
import time

s=""
# Función para detectar contornos y clasificar figuras entre cubo y esfera
def detect_shape(cnt, perimeter_factor=0.03, color_threshold=30):
    peri = cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, perimeter_factor * peri, True)
    vertices = len(approx)

    # Detección de figuras entre cubo y esfera basada en el número de vértices
    if vertices >= 6:
        s="esfera"
        return s
    else:
        s="cubo"
        return s
    
    
    
    
def pachon():
        
    # Captura de video desde la cámara
    cap = cv2.VideoCapture(2)

    # Coordenadas de las posiciones a vigilar
    position_1 = (107, 235)
    position_2 = (464, 289)

    # Lista para almacenar las figuras detectadas en las regiones de interés
    detected_figure_1 = None
    detected_figure_2 = None
    a=0

    while (cv2.waitKey(1)):
        a=a+1
        ret, frame = cap.read()
        if not ret:
            break
        
        # Convertir a escala de grises
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Aplicar umbral adaptativo para obtener una imagen binaria
        thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 4)

        # Encontrar contornos en la imagen umbralizada
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Iterar sobre los contornos para detectar figuras y verificar las posiciones de interés
        for cnt in contours:
            # Obtener el área del contorno
            area = cv2.contourArea(cnt)
            # Ignorar contornos pequeños
            if area < 100:
                continue
            
            # Obtener el tipo de figura
            shape = detect_shape(cnt)

            # Dibujar el tipo de figura en el contorno
            M = cv2.moments(cnt)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                cv2.putText(frame, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                
                # Verificar si la figura está cerca de la posición 1
                if abs(cX - position_1[0]) <= 40 and abs(cY - position_1[1]) <= 40:
                    detected_figure_1 = shape
                    cv2.rectangle(frame, (position_1[0] - 40, position_1[1] - 40), (position_1[0] + 40, position_1[1] + 40), (255, 0, 0), 2)
                # Verificar si la figura está cerca de la posición 2
                if abs(cX - position_2[0]) <= 40 and abs(cY - position_2[1]) <= 40:
                    detected_figure_2 = shape
                    cv2.rectangle(frame, (position_2[0] - 40, position_2[1] - 40), (position_2[0] + 40, position_2[1] + 40), (255, 0, 0), 2)

        # Mostrar el frame
#         cv2.imshow('Frame', frame)
#         print("holi")
#         print(a)
        # Salir con 'q'
        if a==10:
#             print("hhh")
            break

    # Liberar la cámara y cerrar todas las ventanas
    cap.release()
    cv2.destroyAllWindows()

    # Imprimir las figuras detectadas en las coordenadas especificadas
#     print("Figura detectada en posición 1:", detected_figure_1)
#     print("Figura detectada en posición 2:", detected_figure_2)
    if(detected_figure_1=="cubo"):
        f1=1
    if(detected_figure_1=="esfera"):
        f1=2
    if(detected_figure_2=="cubo"):
        f2=1
    if(detected_figure_2=="esfera"):
        f2=2
    return [f1,f2]

    
