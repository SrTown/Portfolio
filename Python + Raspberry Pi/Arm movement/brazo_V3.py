import time    
from adafruit_servokit import ServoKit   

# Constants
nbPCAServo = 16 

# Parameters
MIN_IMP = [500] * nbPCAServo
MAX_IMP = [2500] * nbPCAServo
MIN_ANG = [0] * nbPCAServo
MAX_ANG = [180] * nbPCAServo

# Objects
pca = ServoKit(channels=16)

# Function to initialize pulse width range
def init():
    for i in range(nbPCAServo):
        pca.servo[i].set_pulse_width_range(MIN_IMP[i], MAX_IMP[i])

# movimiento de la garra

# Function to set initial positions
def set_initial_positions():
        
        MyServo = 4
        pca.servo[MyServo].angle = 90
        time.sleep(.3)
       
        MyServo = 3
        pca.servo[MyServo].angle = 60
        time.sleep(.3)
        
        MyServo = 0
        pca.servo[MyServo].angle = 0
        time.sleep(.3)
        

        # ---------------------------------
        angulo1y2 = 60
        MyServo = 1
        pca.servo[MyServo].angle = angulo1y2
        time.sleep(.1)
        MyServo = 2
        pca.servo[MyServo].angle = angulo1y2
        time.sleep(.1)
        # ---------------------------------

        MyServo = 5
        pca.servo[MyServo].angle = 10
        time.sleep(.3)
        
      
def set_primera_posicion():
    MyServo = 0
    pca.servo[MyServo].angle = 95
    time.sleep(.5)
    
    for i in range(45, 25, -1):  # El rango es desde 90 hasta 25 con decrementos de 1
        MyServo = 4
        pca.servo[MyServo].angle = i
        time.sleep(.1)
    
    for k in range(60, 28, -3):
        MyServo = 3
        pca.servo[MyServo].angle = k
        time.sleep(.1)
   
    for j in range(30, 180, +10):
        MyServo = 5
        pca.servo[MyServo].angle = j
        time.sleep(.1)
    
    time.sleep(.3)
    
    print("REGRESANDO A LA POSICION INICIAL")
    # POSICION INICIAL ============================================================
    set_initial_positions() 
    

def set_segunda_posicion():
    MyServo = 0
    pca.servo[MyServo].angle = 50
    time.sleep(.5)
    
    for i in range(45, 30, -1):  # El rango es desde 90 hasta 25 con decrementos de 1
        MyServo = 4
        pca.servo[MyServo].angle = i
        time.sleep(.1)
    
    for k in range(60, 28, -3):
        MyServo = 3
        pca.servo[MyServo].angle = k
        time.sleep(.1)
   
    for j in range(30, 180, +10):
        MyServo = 5
        pca.servo[MyServo].angle = j
        time.sleep(.1)
    time.sleep(.3)
    print("REGRESANDO A LA POSICION INICIAL")
    set_initial_positions()
       

# Main function
def main():
    init()
    set_initial_positions()
    set_primera_posicion()
    set_segunda_posicion()    
    

# Run main function
if __name__ == "__main__":
    main()
